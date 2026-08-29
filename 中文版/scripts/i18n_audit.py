#!/usr/bin/env python3
"""
i18n_audit.py — International SEO audit for multilingual sites.

Validates the i18n checklist from references/09-i18n-seo.md:
  - locale-prefixed URLs (independent & indexable)
  - hreflang: per-page 4 tags (all locales + x-default), BCP-47, self-reference
  - hreflang cross-bidirectionality across pages
  - canonical: locale-self
  - sitemap: all locale variants of every logical page
  - Schema inLanguage matches the URL locale
  - og:locale + og:locale:alternate
  - llms.txt multilingual sections

Usage:
  py i18n_audit.py <file-or-dir> [more...] --base-url https://example.com
                  [--locales en,zh-CN,ja] [--sitemap sitemap.xml] [--llms-txt llms.txt] [--json]

Notes:
  - Pure Python 3 standard library.
  - --base-url maps local files to public URLs (e.g. files under "site/" with
    base "https://example.com" become https://example.com/<relative path>).
  - Works on raw HTML files (no network needed unless URLs are passed).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit

BCP47 = re.compile(r"^(x-default|[a-z]{2,3}(-[A-Z]{2,4})?(-[a-z]{4})?(-[0-9]{3})?(-[A-Z0-9]{2,8})?)$", re.I)
LOCALE_SEG_RE = re.compile(r"/(en|zh-CN|zh-cn|ja)(/|$)")
LOCALE_NORM = {"zh-cn": "zh-CN", "zh_cn": "zh-CN", "en": "en", "ja": "ja"}


def norm_locale(x: str) -> str:
    return LOCALE_NORM.get(x.lower(), x)


class I18nParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hreflangs: list[tuple[str, str]] = []
        self.canonical = ""
        self.og_locale = ""
        self.og_locale_alts: list[str] = []
        self.in_languages: list[str] = []
        self._ld = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        a = {k.lower(): v for k, v in attrs}
        if tag == "link":
            rel = (a.get("rel") or "").lower().split()
            if "canonical" in rel:
                self.canonical = a.get("href", "")
            if "alternate" in rel and a.get("hreflang"):
                self.hreflangs.append((a["hreflang"], a.get("href", "")))
        elif tag == "meta":
            prop = (a.get("property") or "").lower()
            if prop == "og:locale":
                self.og_locale = a.get("content", "")
            elif prop == "og:locale:alternate":
                self.og_locale_alts.append(a.get("content", ""))
        elif tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self._ld = True

    def handle_endtag(self, tag):
        if tag.lower() == "script":
            self._ld = False

    def handle_data(self, data):
        if self._ld and data.strip():
            try:
                blob = json.loads(data)
            except Exception:
                return
            items = blob if isinstance(blob, list) else [blob]
            for it in items:
                if isinstance(it, dict) and it.get("inLanguage"):
                    self.in_languages.append(str(it["inLanguage"]))


class Check:
    def __init__(self, name: str, status: str, detail: str = ""):
        self.name, self.status, self.detail = name, status, detail

    def __repr__(self):
        return f"{self.status}: {self.name} — {self.detail}"


def infer_locale(url_or_path: str) -> str | None:
    seg = LOCALE_SEG_RE.search(url_or_path.replace("\\", "/"))
    if not seg:
        return None
    return norm_locale(seg.group(1))


def page_checks(url: str, html: str, locales: list[str]) -> list[Check]:
    p = I18nParser()
    try:
        p.feed(html)
        p.close()
    except Exception:
        pass
    checks: list[Check] = []
    expected = infer_locale(url)

    # --- URL locale ----------------------------------------------------------
    if not expected:
        checks.append(Check("url_locale", "FAIL", f"No locale prefix found in {url} — use /{''.join(locales)}/ style"))
    else:
        checks.append(Check("url_locale", "PASS", f"locale={expected}"))

    # --- hreflang: presence of all locales + x-default + self ----------------
    declared = {norm_locale(l): h for l, h in p.hreflangs if l.lower() != "x-default"}
    has_xdefault = any(l.lower() == "x-default" for l, _ in p.hreflangs)
    missing = [l for l in locales if l not in declared]
    if missing:
        checks.append(Check("hreflang_coverage", "FAIL",
                            f"missing hreflang: {', '.join(missing)} (expected {', '.join(locales)}+x-default)"))
    else:
        checks.append(Check("hreflang_coverage", "PASS", f"{len(declared)} locales declared"))
    if not has_xdefault:
        checks.append(Check("hreflang_xdefault", "FAIL", "no hreflang=x-default"))
    else:
        checks.append(Check("hreflang_xdefault", "PASS", "x-default present"))

    if expected:
        self_same = declared.get(expected)
        if self_same is None:
            checks.append(Check("hreflang_self", "FAIL", f"no hreflang entry for own locale {expected}"))
        else:
            same = norm_url(self_same) == norm_url(url) or self_same.endswith(url) or url.endswith(self_same.split("//")[-1] if "//" in self_same else self_same)
            checks.append(Check("hreflang_self", "PASS" if same else "WARN",
                                f"self entry {self_same}" + ("" if same else " points to different URL")))

    bad = [(l, h) for l, h in p.hreflangs if not BCP47.match(l)]
    checks.append(Check("hreflang_bcp47", "PASS" if not bad else "FAIL",
                        "all tags valid" if not bad else f"invalid: {bad[:3]}"))
    dups = len(p.hreflangs) - len({(norm_locale(l), h) for l, h in p.hreflangs})
    if dups > 0:
        checks.append(Check("hreflang_duplicates", "WARN", f"{dups} duplicate hreflang entries"))

    # --- canonical ------------------------------------------------------------
    if not p.canonical:
        checks.append(Check("canonical", "FAIL", "missing canonical"))
    else:
        if expected and f"/{expected}" in p.canonical.replace("zh-cn", "zh-CN", 1) or (expected and LOCALE_SEG_RE.search(p.canonical) and expected in norm_locale(LOCALE_SEG_RE.search(p.canonical).group(1))):
            checks.append(Check("canonical", "PASS", f"locale-self: {p.canonical}"))
        else:
            checks.append(Check("canonical", "FAIL" if expected else "WARN",
                                f"{p.canonical} does not match locale {expected}"))

    # --- og:locale ------------------------------------------------------------
    og_ok = expected is None or (p.og_locale and p.og_locale.lower().split("_")[0] == expected.lower().split("-")[0])
    checks.append(Check("og_locale", "PASS" if og_ok else "FAIL",
                        f"og:locale={p.og_locale or 'MISSING'}" + ("" if og_ok else f" (expected {expected})")))
    alt_needed = {loc for loc in locales if loc != expected} if expected else set()
    alt_have = {norm_locale(a.lower().split("_")[0]) for a in p.og_locale_alts}
    alt_missing = {"en" if l == "en" else ("zh" if l.startswith("zh") else l) for l in alt_needed} - alt_have
    checks.append(Check("og_locale_alternate", "PASS" if not alt_missing else "WARN",
                        f"alternates: {', '.join(p.og_locale_alts) or 'none'}"
                        + (f"; missing {', '.join(sorted(alt_missing))}" if alt_missing else "")))

    # --- inLanguage -----------------------------------------------------------
    if not p.in_languages:
        checks.append(Check("schema_inLanguage", "WARN", "no inLanguage in JSON-LD"))
    else:
        il = p.in_languages[0]
        ok = norm_locale(il) == expected
        checks.append(Check("schema_inLanguage", "PASS" if ok else "FAIL",
                            f"inLanguage={il}" + ("" if ok else f" (URL locale {expected})")))
    return checks


def norm_url(u: str) -> str:
    u = u.rstrip("/").lower()
    for ext in (".html", ".htm"):
        if u.endswith(ext):
            u = u[: -len(ext)]
    return u


# ---------------------------------------------------------------------------
# sitemap & llms.txt checks
# ---------------------------------------------------------------------------

def sitemap_checks(path: str, locales: list[str]) -> list[Check]:
    checks: list[Check] = []
    try:
        import xml.etree.ElementTree as ET
        tree = ET.parse(path)
    except Exception as e:
        return [Check("sitemap_parse", "FAIL", f"cannot parse sitemap: {e}")]
    locs = [el.text.strip() for el in tree.iter() if el.tag.endswith("loc") and el.text]
    if not locs:
        return [Check("sitemap_entries", "FAIL", "no <loc> entries")]
    bases: dict[str, set[str]] = {}
    for loc in locs:
        loc = norm_url(loc)
        m = LOCALE_SEG_RE.search(loc)
        if not m:
            bases.setdefault(loc, set()).add("")
            continue
        base = loc[: m.start()] + "/" + loc[m.end():]
        bases.setdefault(base, set()).add(norm_locale(m.group(1)))
    incomplete = {b: sorted(set(locales) - vs) for b, vs in bases.items() if len(vs) < len(locales)}
    if incomplete:
        checks.append(Check("sitemap_variants", "FAIL",
                            f"{len(incomplete)} logical pages missing locale variants, e.g. {list(incomplete.items())[:2]}"))
    else:
        checks.append(Check("sitemap_variants", "PASS", f"{len(bases)} logical pages x {len(locales)} locales"))
    prefix_ok = all(any(f"/{l}" in loc for l in locales) for loc in locs[:200])
    checks.append(Check("sitemap_locale_urls", "PASS" if not locs or prefix_ok else "WARN",
                        f"{len(locs)} URLs" + ("" if prefix_ok else "; some lack locale prefix")))
    return checks


def llmstxt_checks(path: str, locales: list[str]) -> list[Check]:
    checks: list[Check] = []
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return [Check("llms_txt", "FAIL", f"cannot read: {e}")]
    sections = [ln for ln in text.splitlines() if ln.startswith("#")]
    miss = []
    for l in locales:
        l_low = l.lower()
        if not any(l_low in s.lower() or f"/{l_low}" in s.lower() for s in sections):
            miss.append(l)
    if miss:
        checks.append(Check("llms_txt_multilingual", "FAIL",
                            f"no per-locale section for: {', '.join(miss)} (group links per locale)"))
    else:
        checks.append(Check("llms_txt_multilingual", "PASS", "per-locale sections present"))
    return checks


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="International SEO audit (hreflang/canonical/sitemap/inLanguage/og:locale/llms.txt)")
    ap.add_argument("paths", nargs="+", help="HTML file(s), directory(ies) — or .xml/.txt for sitemap/llms.txt")
    ap.add_argument("--base-url", default="", help="site base URL to map local files (e.g. https://example.com)")
    ap.add_argument("--locales", default="en,zh-CN,ja", help="comma-separated locales")
    ap.add_argument("--sitemap", default="", help="path to sitemap.xml for variant check")
    ap.add_argument("--llms-txt", default="", help="path to llms.txt for multilingual section check")
    ap.add_argument("--json", action="store_true", help="emit JSON report")
    args = ap.parse_args()
    locales = [norm_locale(x.strip()) for x in args.locales.split(",") if x.strip()]

    reports: list[dict] = []

    # sitemap / llms.txt direct args
    if args.sitemap:
        reports.append({"source": args.sitemap, "checks": [c.__dict__ for c in sitemap_checks(args.sitemap, locales)]})
    if args.llms_txt:
        reports.append({"source": args.llms_txt, "checks": [c.__dict__ for c in llmstxt_checks(args.llms_txt, locales)]})

    # HTML pages
    html_files: list[tuple[str, str]] = []  # (abs path, rel posix path)
    for p in args.paths:
        path = Path(p)
        if path.is_dir():
            for f in sorted(path.rglob("*.html")) + sorted(path.rglob("*.htm")):
                html_files.append((str(f), f.relative_to(path).as_posix()))
        elif path.suffix.lower() in (".html", ".htm"):
            html_files.append((str(path), Path(p).name))

    cross: dict[str, tuple[str, set]] = {}  # norm_url -> (file, declared locales)
    for f, rel in html_files:
        html = Path(f).read_text(encoding="utf-8", errors="replace")
        url = urljoin(args.base_url.rstrip("/") + "/", rel) if args.base_url else rel
        checks = page_checks(url, html, locales)
        reports.append({"source": f, "url": url, "checks": [c.__dict__ for c in checks]})
        p2 = I18nParser()
        try:
            p2.feed(html)
            p2.close()
        except Exception:
            pass
        cross[norm_url(url)] = (f, {norm_locale(l) for l, h in p2.hreflangs})

    # cross-bidirectionality
    if len(cross) > 1:
        bad: list[str] = []
        for ua, (fa, langs_a) in cross.items():
            pl = I18nParser()
            try:
                pl.feed(Path(fa).read_text(encoding="utf-8", errors="replace"))
            except Exception:
                pass
            for l, h in pl.hreflangs:
                if l.lower() == "x-default":
                    continue
                tgt = norm_url(h)
                if tgt not in cross:
                    continue  # external/not scanned
                fb, _ = cross[tgt]
                # b should declare our url with our locale
                p3 = I18nParser()
                try:
                    p3.feed(Path(fb).read_text(encoding="utf-8", errors="replace"))
                except Exception:
                    pass
                back = {(norm_locale(ll), norm_url(hh)) for ll, hh in p3.hreflangs}
                my_loc = infer_locale(ua)
                if my_loc and (my_loc, ua) not in back:
                    bad.append(f"{fa} -> {h} (missing backlink)")
        if bad:
            reports.insert(0, {"source": "cross-bidirectional hreflang", "checks": [
                {"name": "hreflang_bidirectional", "status": "FAIL", "detail": "; ".join(bad[:5]) + (f" (+{len(bad)-5} more)" if len(bad) > 5 else "")}]})
        else:
            reports.insert(0, {"source": "cross-bidirectional hreflang", "checks": [
                {"name": "hreflang_bidirectional", "status": "PASS", "detail": "all scanned pages declare backlinks"}]})

    if args.json:
        print(json.dumps(reports, ensure_ascii=False, indent=2))
        return 0
    for rep in reports:
        print(f"===== {rep['source']} =====")
        for c in rep["checks"]:
            print(f"  [{c['status']:4}] {c['name']}: {c['detail']}")
        fails = sum(1 for c in rep["checks"] if c["status"] == "FAIL")
        print(f"  --> {fails} FAIL\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
