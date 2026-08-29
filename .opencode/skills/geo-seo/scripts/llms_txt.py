#!/usr/bin/env python3
"""
llms_txt.py — Generate a spec-compliant /llms.txt for your site (see llmstxt.org).

Usage:
  py llms_txt.py --name "Brand" --site-url https://example.com \
      --summary "1-3 sentence business summary" \
      --pages "https://example.com/en/about | About us: what we do" \
      --pages "https://example.com/zh-CN/about | 关于我们：介绍" \
      --out llms.txt

Options:
  --name       brand/site name
  --site-url   production base URL (also required to resolve relative pages)
  --summary    1-3 sentence business summary
  --pages      "url | description" (repeatable). URLs may include /en /zh-CN /ja
               prefixes -> they get grouped into per-locale sections
  --contact    optional "Label: value" extra line (repeatable)
  --out        output file (default: stdout)

Notes:
  - Pure Python 3 standard library.
  - Per-locale grouping: groups pages by locale segment in the URL; pages
    without a locale prefix go into a general "Services/Key Information"
    section. AI engines match query language to content language, so listing
    every locale explicitly helps citations across languages.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlsplit

LOCALE_RE = re.compile(r"/(en|zh-CN|zh-cn|ja)(/|$)")
LOCALE_LABELS = {"en": "English", "zh-CN": "中文 (zh-CN)", "ja": "日本語 (ja)"}


def norm_l(l: str) -> str:
    return {"zh-cn": "zh-CN"}.get(l.lower(), l)


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate /llms.txt (llmstxt.org spec)")
    ap.add_argument("--name", required=True)
    ap.add_argument("--site-url", required=True, help="base URL, e.g. https://example.com")
    ap.add_argument("--summary", required=True, help="1-3 sentence business summary")
    ap.add_argument("--pages", action="append", default=[], help='"url | description" (repeatable)')
    ap.add_argument("--contact", action="append", default=[], help='"Label: value" (repeatable)')
    ap.add_argument("--out", default="", help="write to file instead of stdout")
    args = ap.parse_args()

    base = args.site_url.rstrip("/")

    groups: dict[str, list[tuple[str, str]]] = {}
    plain: list[tuple[str, str]] = []
    for item in args.pages:
        if "|" in item:
            url, desc = item.split("|", 1)
            url, desc = url.strip(), desc.strip()
        else:
            url, desc = item.strip(), ""
        if url.startswith("/"):
            url = urljoin(base + "/", url.lstrip("/"))
        m = LOCALE_RE.search(url)
        if m:
            groups.setdefault(norm_l(m.group(1)), []).append((url, desc))
        else:
            plain.append((url, desc))

    lines: list[str] = []
    lines.append(f"# {args.name}")
    lines.append("")
    lines.append(f"> {args.summary}")
    if args.contact:
        lines.append("")
        lines.append("## Contact")
        for c in args.contact:
            lines.append(f"- {c}")
    if plain:
        lines.append("")
        lines.append("## Key Information")
        for url, desc in plain:
            lines.append(f"- [{desc or url}]({url})" if desc else f"- [{url}]({url})")

    for loc in sorted(groups):
        lines.append("")
        lines.append(f"## {LOCALE_LABELS.get(loc, loc)} ({loc})")
        for url, desc in groups[loc]:
            lines.append(f"- [{desc or url}]({url})" if desc else f"- [{url}]({url})")

    out = "\n".join(lines) + "\n"
    if args.out:
        Path(args.out).write_text(out, encoding="utf-8")
        print(f"Wrote {args.out} ({len(out)} bytes)")
    else:
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
