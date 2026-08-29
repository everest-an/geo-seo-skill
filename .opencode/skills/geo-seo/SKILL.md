---
name: geo-seo
description: Comprehensive GEO (Generative Engine Optimization) + SEO system covering both traditional search rankings and AI answer engine citations (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews). Use when optimizing content to get cited or recommended by AI engines, raising rankings, auditing AI visibility, information gain, AI-readable structure, llms.txt, AI crawler access, GEO monitoring, running the 4-step rapid method, or international/multilingual SEO. Triggers: GEO, Generative Engine Optimization, AEO, Answer Engine Optimization, AI SEO, AI search optimization, get cited by AI, AI Overviews optimization, ChatGPT/Perplexity/Gemini/Claude citations, content ranking, information gain, topical authority, llms.txt, structured data, E-E-A-T, multilingual SEO, international SEO, i18n, hreflang, canonical, locale, inLanguage, og:locale, 生成式引擎优化, 让AI引用, AI搜索优化, 内容排名, 多语言SEO, hreflang.
metadata:
  version: 1.1.0
  category: marketing/seo
  language: en
---

# GEO + SEO Comprehensive Optimization System

> Make content both **rank in traditional search engines** and **get cited/recommended by AI answer engines**.
> Core logic: AI engines retrieve from the same web your SEO content lives on — solid SEO is half of GEO won. GEO is about "being part of the answer," not "being first in rankings."

## When to Use This System

- Content should appear in ChatGPT / Perplexity / Gemini / Claude / Google AI Overviews answers and citations
- Running traditional SEO (keywords, technical, content, links) and want to layer AI visibility on top
- Rankings stalled, CTR low, zero AI citations after publishing
- Need competitor gap analysis, AI-readable restructuring, technical crawl, or GEO monitoring
- Auditing AI crawler accessibility, llms.txt, structured data, or E-E-A-T signals

## System Panorama (Six-Layer Pyramid)

```
                ┌─────────────────────────────┐
                │  ⑥ Monitoring & Iteration    │
                │  (GSC + GEO tools)           │
                ├─────────────────────────────┤
                │  ⑤ Authority & Entities      │
                │  (E-E-A-T, brand mentions)   │
                ├─────────────────────────────┤
                │  ④ Technical Layer           │
                │  (AI crawlers, llms.txt, Schema)│
                ├─────────────────────────────┤
                │  ③ Content Citation          │
                │  (extractability, info gain) │
                ├─────────────────────────────┤
                │  ② Traditional SEO Foundation│
                │  (technical + content + links)│
                ├─────────────────────────────┤
                │  ① GEO Foundations           │
                │  (landscape, retrieval factors)│
                └─────────────────────────────┘
```

## Core Workflow (4-Step Rapid Method · Skeleton)

A battle-tested, standardized sequence that can move a page from rank ~18 to top 3 in **48 hours** (full version in `references/02-rapid-method.md`):

| Step | Action | Tools/Engines | Output |
|------|--------|---------------|--------|
| **① Disect** | Competitor gap analysis, mine information blind spots (Information Gain) | ChatGPT / Claude | Differentiators + gap list |
| **② Restructure** | Rebuild page into "AI-favorite format" | Claude / Gemini | Extractable, citable page |
| **③ Sweep** | Technical cleanup (dead links / dup meta / H1 / sitemap) | ScreamingFrog | Technical health |
| **④ Track** | 48-hour rapid monitoring + re-indexing | Google Search Console | Rank jump + traffic |

**Mnemonic**: `Dig → Design → Clean → Drive` (mine gaps, shape format, clear obstacles, then track).

## Reference Index

| File | Contents | Read It When |
|------|----------|--------------|
| `references/01-foundations.md` | GEO basics, SEO/GEO/AEO comparison, AI engine landscape, RAG retrieval factors, key data | Building understanding; answering "what is GEO / why" |
| `references/02-rapid-method.md` | Full 4-step rapid method (with ready-to-use prompts) | Executing a 48-hour ranking sprint |
| `references/03-content-citation.md` | Content & citation optimization, FAST framework, information gain, extractability | Writing/rewriting content |
| `references/04-technical-crawl.md` | AI crawler robots.txt, llms.txt, Schema/JSON-LD, SSR, technical GEO checklist | Handling technical layer, AI accessibility |
| `references/05-authority-entities.md` | E-E-A-T, entity building, brand mentions, external signals, Wikipedia/UGC | Building authority and AI brand mentions |
| `references/06-monitoring.md` | Metrics, monitoring tools, GA4 AI traffic setup, monitoring workflow | Tracking results, verifying citations |
| `references/07-prompt-library.md` | Copy-paste prompts (gap analysis / AI restructure / content optimization / GEO audit) | Needing ready-made prompts |
| `references/08-tools-resources.md` | Research papers, tool ecosystem, case studies, links | Tool selection, citing data, case studies |
| `references/09-i18n-seo.md` | International/multilingual SEO: hreflang, locale canonical, sitemap, inLanguage, og:locale, localized metadata, multilingual llms.txt | Running multilingual sites (e.g., /en /zh-CN /ja) |

## Automation (Scripts)

The system ships with dependency-free Python 3 scripts (stdlib only) under `scripts/` — run with `py scripts/<script>.py`:

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/geo_audit.py` | GEO readiness audit — FAST framework, extractability, citation signals, on-page basics | `py scripts/geo_audit.py <file\|dir\|url> [--json] [--min-cjk]` |
| `scripts/i18n_audit.py` | International SEO audit — hreflang (coverage/x-default/BCP-47/bidirectional), canonical, sitemap variants, inLanguage, og:locale, llms.txt | `py scripts/i18n_audit.py <dir> --base-url https://... [--sitemap path] [--llms-txt path] [--json]` |
| `scripts/llms_txt.py` | Generate a spec-compliant `/llms.txt` with per-locale grouping | `py scripts/llms_txt.py --name "X" --site-url https://... --summary "..." --pages "url \| desc" ...` |

Every script is idempotent and offline (raw HTML/XML files) unless you pass URLs. Use `--json` for machine-readable reports.

## Quick Decision Guide

- **"Why does AI not cite my content?"** → `03-content-citation.md` (extractability + information gain) first, then `04-technical-crawl.md` (is the AI crawler blocked?).
- **"Want to quickly lift rankings"** → Execute `02-rapid-method.md` directly.
- **"Want long-term AI brand presence"** → `05-authority-entities.md` + `06-monitoring.md`.
- **"Need ready-made prompts"** → `07-prompt-library.md`.
- **"Need data backing / tool selection"** → `08-tools-resources.md`.
- **"Multilingual site (hreflang / locale URLs / inLanguage)"** → `09-i18n-seo.md`.

## Iron Rules (Anti-Patterns)

- ❌ Optimizing only for AI at the expense of human readers (quote-stuffing, empty formatting) — it backfires long term.
- ❌ Keyword stuffing — GEO research confirms it's counterproductive.
- ❌ Blocking AI crawlers in robots.txt while expecting citations — verify access first.
- ❌ Content without dates, authors, or sources — AI cannot judge trustworthiness and won't cite.
- ✅ Be "the clearest, most authoritative, most extractable answer," not "the page ranked first."
