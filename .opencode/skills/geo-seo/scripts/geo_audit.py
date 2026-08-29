#!/usr/bin/env python3
"""
geo_audit.py — GEO readiness audit for a page or site (single-language).

Audits content against the GEO + SEO system's citation-readiness criteria:
  - FAST framework (Fetchable / Accessible / Structured / Trim)
  - Extractability & citation-worthiness (TL;DR, FAQ, lists/tables, short paragraphs)
  - Scope/trust signals (date, author, sources, schema, question-style headings)
  - On-page SEO basics (H1, title/meta length)

Usage:
  py geo_audit.py <file-or-dir-or-url> [more paths...] [--json] [--min-cjk]

Notes:
  - Pure Python 3 standard library, no dependencies.
  - For directories, scans *.html /*.htm recursively.
  - For URLs, fetches via urllib (requires network).
  - --min-cjk lowers token-count heuristics for CJK content (short paragraphs OK).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

# ---------------------------------------------------------------------------
# HTML parsing
# ---------------------------------------------------------------------------

class PageParser(HTMLParser):
    """Collect structural facts from a rendered-or-raw HTML document."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.h1 = 0
        self.h2 = 0
        self.h3 = 0
        self.h1_texts: list[str] = []
        self.h2_texts: list[str] = []
        self.h3_texts: list[str] = []
        self.tables = 0
        self.lists = 0          # <ul>/<ol>
        self.imgs = 0
        self.imgs_no_alt = 0
        self.scripts = 0
        self.inline_script_bytes = 0
        self.stylesheets = 0
        self.link_rels: set[str] = set()
        self.ld_json: list[str] = []
        self.paragraphs: list[str] = []
        self.text_len = 0
        self.title = ""
        self.meta_description = ""
        self.semantic_tags: set[str] = set()
        self.current_tag_stack: list[str] = []
        self._alt_in_footer_guard = False
        self._iframes = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        a = dict(attrs)
        tag = tag.lower()
        self.current_tag_stack.append(tag)
        if tag in ("article", "section", "nav", "main", "header", "footer"):
            self.semantic_tags.add(tag)
        if tag == "h1":
            self.h1 += 1
        elif tag == "h2":
            self.h2 += 1
        elif tag == "h3":
            self.h3 += 1
        elif tag == "table":
            self.tables += 1
        elif tag in ("ul", "ol"):
            self.lists += 1
        elif tag == "img":
            self.imgs += 1
            if not a.get("alt"):
                self.imgs_no_alt += 1
        elif tag == "script":
            self.scripts += 1
            src = a.get("src")
            if not src:
                # count inline script chars roughly later via data
                self._capture_script = True
            if a.get("type", "").lower() == "application/ld+json":
                self._capture_ld = True
        elif tag == "link":
            rel = (a.get("rel") or "").lower().split()
            self.link_rels.update(rel)
            if "stylesheet" in rel:
                self.stylesheets += 1
            if "canonical" in rel:
                self.canonical_href = a.get("href", "")
            if "alternate" in rel and a.get("hreflang"):
                self.hreflangs = getattr(self, "hreflangs", [])
                self.hreflangs.append((a.get("hreflang"), a.get("href", "")))
        elif tag == "meta":
            if a.get("property", "").lower() == "og:locale":
                self.og_locale = a.get("content", "")
            if a.get("property", "").lower() == "og:locale:alternate":
                self.og_locale_alts = getattr(self, "og_locale_alts", [])
                self.og_locale_alts.append(a.get("content", ""))
            if a.get("name", "").lower() == "description":
                self.meta_description = a.get("content", "")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "script":
            self._capture_script = False
            self._capture_ld = False
        if self.current_tag_stack and self.current_tag_stack[-1] == tag:
            self.current_tag_stack.pop()

    def handle_data(self, data: str) -> None:
        if not data.strip():
            return
        if getattr(self, "_capture_ld", False):
            self.ld_json.append(data.strip())
            return
        if getattr(self, "_capture_script", False):
            self.inline_script_bytes += len(data)
            return
        self.text_len += len(data.strip())
        # grab heading text
        if self.current_tag_stack:
            for t in ("h1", "h2", "h3"):
                if self.current_tag_stack[-1] == t:
                    getattr(self, f"{t}_texts").append(data.strip())

    # shortcut accessors -----------------------------------------------------
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, v: str) -> None:
        self._title = v


# ---------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------

class Check:
    def __init__(self, name: str, status: str, detail: str = ""):
        self.name = name
        self.status = status  # PASS | FAIL | WARN
        self.detail = detail

    def as_dict(self):
        return {"name": self.name, "status": self.status, "detail": self.detail}


QUESTION_WORDS = re.compile(r"^(what|how|why|when|where|which|who|is|are|do|does|can|should|vs|vs\.)", re.I)
SUMMARY_KEYS = re.compile(r"(tl;?dr|quick answer|key takeaways|summary|executive summary|结论|总结|速读|快速回答)", re.I)
FAQ_KEYS = re.compile(r"(faq|frequently asked|常见问题|疑问)", re.I)
DATE_KEYS = re.compile(r"(datePublished|dateModified|last.*updated|更新于|发布于|last updated|\b20\d{2}[-/]\d{1,2}[-/]\d{1,2}\b)", re.I)
AUTHOR_KEYS = re.compile(r"(author|by\s+[A-Z][a-z]+|作者|撰写|edited by)", re.I)
NUMERIC_STAT = re.compile(r"\d+(\.\d+)?%?|\d+\s*(元|万元|亿|k|m|万|%|×|x)?")


def audit(html: str, path_label: str, min_cjk: bool = False) -> list[Check]:
    p = PageParser()
    p.current_tag_stack = []
    p._capture_script = False
    p._capture_ld = False
    try:
        p.feed(html)
        p.close()
    except Exception:
        pass

    checks: list[Check] = []
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()

    # --- Standard SEO -------------------------------------------------------
    title = ""
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    if m:
        title = m.group(1).strip()
    if not title:
        checks.append(Check("title", "FAIL", "missing <title>"))
    elif len(title) > 60:
        checks.append(Check("title", "WARN", f"title length {len(title)} > 60 chars"))
    else:
        checks.append(Check("title", "PASS", f"length {len(title)}"))

    md = getattr(p, "meta_description", "")
    if not md:
        checks.append(Check("meta_description", "FAIL", "missing description"))
    elif not (50 <= len(md) <= 165):
        checks.append(Check("meta_description", "WARN", f"length {len(md)}, recommended 50-165"))
    else:
        checks.append(Check("meta_description", "PASS", f"length {len(md)}"))

    # --- H1 / heading hierarchy --------------------------------------------
    if p.h1 == 0:
        checks.append(Check("h1_count", "FAIL", "no H1"))
    elif p.h1 > 1:
        checks.append(Check("h1_count", "FAIL", f"{p.h1} H1s (exactly 1 required)"))
    else:
        h1txt = " ".join(p.h1_texts).strip()
        if not h1txt:
            checks.append(Check("h1_count", "FAIL", "H1 is empty"))
        else:
            checks.append(Check("h1_count", "PASS", f'"{h1txt[:60]}"'))

    if not p.h2_texts:
        checks.append(Check("h2_levels", "WARN", "no H2 (add question-style H2 sections)"))
    else:
        q_h2 = sum(1 for t in p.h2_texts if QUESTION_WORDS.search(t.strip()))
        ratio = q_h2 / max(1, len(p.h2_texts))
        if ratio >= 0.5:
            checks.append(Check("h2_levels", "PASS", f"{q_h2}/{len(p.h2_texts)} question-style H2"))
        else:
            checks.append(Check("h2_levels", "WARN", f"only {q_h2}/{len(p.h2_texts)} question-style H2"))

    # --- Extractability -----------------------------------------------------
    has_summary = bool(SUMMARY_KEYS.search(text[:4000]))
    checks.append(Check("tldr_summary", "PASS" if has_summary else "WARN",
                        "summary/TL;DR block present" if has_summary else "no TL;DR/quick-answer near top"))

    faq_like = FAQ_KEYS.search(text)
    has_faq_h2 = any(FAQ_KEYS.search(h) or "?" in h for h in (p.h2_texts + p.h3_texts))
    checks.append(Check("faq_block", "PASS" if (faq_like or has_faq_h2) else "WARN",
                        "FAQ/Q&A section present" if (faq_like or has_faq_h2) else "no FAQ section (3-5 Q&A improves citations)"))

    lists_tables = p.lists + p.tables
    checks.append(Check("lists_tables", "PASS" if lists_tables >= 2 else "WARN",
                        f"{p.lists} lists + {p.tables} tables" if lists_tables else "no lists/tables for key data"))

    # paragraph length (non-tag text split by sentence)
    sentences = [s for s in re.split(r"[.!?。！？]\s+", text) if s.strip()]
    if min_cjk or any("\u4e00" <= c <= "\u9fff" for c in text):
        checks.append(Check("paragraph_length", "PASS", "CJK content: short-paragraph rule relaxed"))
    else:
        avg_sents = len(sentences) / max(1, min(50, len(text) // 200))
        if avg_sents <= 3.5:
            checks.append(Check("paragraph_length", "PASS", f"~{avg_sents:.1f} sentences/block"))
        else:
            checks.append(Check("paragraph_length", "WARN", f"~{avg_sents:.1f} sentences/block (>3 = long blocks)"))

    # --- Citation/trust signals ---------------------------------------------
    has_date = bool(DATE_KEYS.search(text) or any("datePublished" in s for s in p.ld_json))
    checks.append(Check("freshness_date", "PASS" if has_date else "FAIL",
                        "date/last-updated present" if has_date else "no visible date (AI can't judge freshness)"))

    has_author = bool(AUTHOR_KEYS.search(text))
    checks.append(Check("author_signal", "PASS" if has_author else "WARN",
                        "author/person signal present" if has_author else "no author signal (add name + credentials)"))

    stat_count = len(NUMERIC_STAT.findall(text))
    checks.append(Check("quotable_data", "PASS" if stat_count >= 3 else "WARN",
                        f"{stat_count} numeric data points (quotes/stats +30-40% AI visibility)"
                        if stat_count else "no statistics — add citable numbers"))

    # --- Schema (S) -----------------------------------------------------------
    types: set[str] = set()
    inlang = None
    for block in p.ld_json:
        try:
            data = json.loads(block)
        except Exception:
            continue
        items = data if isinstance(data, list) else [data]
        for it in items:
            if not isinstance(it, dict):
                continue
            t = it.get("@type")
            if isinstance(t, list):
                types.update(str(x) for x in t)
            elif t:
                types.add(str(t))
            if it.get("inLanguage"):
                inlang = it["inLanguage"]
    needed = {"Article", "FAQPage", "Person", "Organization", "Product", "HowTo"}
    found = types & needed
    if not types:
        checks.append(Check("schema", "FAIL", "no JSON-LD found (add Article/FAQPage/Person schema)"))
    else:
        missing = needed - found - {"Product", "HowTo"}
        status = "PASS" if missing - {"Product", "HowTo"} else "WARN"
        checks.append(Check("schema", status,
                            f"types: {', '.join(sorted(types)) or 'none'}"
                            + (f"; inLanguage={inlang}" if inlang else "")))
        if inlang:
            checks.append(Check("schema_inLanguage", "PASS", f"inLanguage={inlang}"))
        else:
            checks.append(Check("schema_inLanguage", "WARN", "no inLanguage in schema (needed for multilingual)"))

    # --- FAST: Fetchable / Accessible / Trim --------------------------------
    # F: text present without JS (best-effort: content text length)
    body_text_len = p.text_len
    if body_text_len < 400:
        checks.append(Check("FAST_F_fetchable", "WARN",
                            f"only ~{body_text_len} chars of text — core content may not be in initial HTML; verify SSR"))
    else:
        checks.append(Check("FAST_F_fetchable", "PASS", f"~{body_text_len} chars in HTML text"))

    # A: alt text & semantics
    if p.imgs_no_alt:
        checks.append(Check("FAST_A_alt_text", "WARN", f"{p.imgs_no_alt}/{p.imgs} images missing alt"))
    else:
        checks.append(Check("FAST_A_alt_text", "PASS", "all images have alt (or no images)"))
    semantic = {"article", "section", "nav", "main", "header", "footer"} & p.semantic_tags
    checks.append(Check("FAST_A_semantic_html", "PASS" if semantic else "WARN",
                        "semantic tags used" if semantic else "no <article>/<section> semantic tags"))

    # T: trim
    if p.scripts > 25 or p.inline_script_bytes > 200_000:
        checks.append(Check("FAST_T_trim", "WARN",
                            f"{p.scripts} scripts (~{p.inline_script_bytes//1024}KB inline) — trim tracking/JS"))
    else:
        checks.append(Check("FAST_T_trim", "PASS", f"{p.scripts} scripts, {p.inline_script_bytes//1024}KB inline"))

    return checks


# ---------------------------------------------------------------------------
# source loading
# ---------------------------------------------------------------------------

def load_source(path: str) -> str:
    if path.startswith(("http://", "https://")):
        import urllib.request
        req = urllib.request.Request(path, headers={"User-Agent": "Mozilla/5.0 geo-audit"})
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.read().decode("utf-8", errors="replace")
    return Path(path).read_text(encoding="utf-8", errors="replace")


def iter_sources(paths: list[str]):
    for p in paths:
        path = Path(p)
        if path.is_dir():
            for f in sorted(path.rglob("*.htm")):
                yield str(f), load_source(str(f))
            for f in sorted(path.rglob("*.html")):
                yield str(f), load_source(str(f))
        else:
            yield p, load_source(p)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="GEO readiness audit (citation-readiness of a page/site)")
    ap.add_argument("paths", nargs="+", help="HTML file(s), directory(ies), or URL(s)")
    ap.add_argument("--json", action="store_true", help="emit JSON report")
    ap.add_argument("--min-cjk", action="store_true", help="relax paragraph heuristic for CJK content")
    args = ap.parse_args()

    reports = []
    for label, html in iter_sources(args.paths):
        checks = audit(html, label, args.min_cjk)
        reports.append({"source": label, "checks": checks})

    if args.json:
        print(json.dumps(reports, ensure_ascii=False, indent=2, default=lambda o: o.__dict__))
        return 0

    for rep in reports:
        print(f"===== {rep['source']} =====")
        for c in rep["checks"]:
            icon = {"PASS": "PASS", "FAIL": "FAIL", "WARN": "warn"}[c.status]
            print(f"  [{icon:4}] {c.name}: {c.detail}")
        fails = sum(1 for c in rep["checks"] if c.status == "FAIL")
        warns = sum(1 for c in rep["checks"] if c.status == "WARN")
        print(f"  --> {fails} FAIL, {warns} WARN\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
