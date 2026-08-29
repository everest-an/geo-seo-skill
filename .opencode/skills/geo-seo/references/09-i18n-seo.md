# 09 · International SEO (Multilingual / i18n)

> For multilingual sites (e.g., `/en`, `/zh-CN`, `/ja`): each language variant must be **independently indexable**, correctly mapped to its locale, and machine-readable for both Google and AI engines. This module covers the full audit checklist for a three-locale content site.

## 1. URL Structure

**Principle**: one URL per language, self-indexable, with a clear locale prefix.

- Use locale-prefixed paths: `/en/...`, `/zh-CN/...`, `/ja/...`
- Keep the same path shape across locales so every page has exactly N language variants, all indexable
- Avoid locale confusion via domain/subdomain mixing (e.g., a mix of `example.com/zh` and `zh.example.com`) — pick one scheme
- Preserve query/keyword parity: the same URL in each locale targets the same intent

## 2. hreflang

### Layout-level (site-wide) hreflang
Declare language relationships on every page template so the whole site maps three locales **bidirectionally + x-default**:

```html
<link rel="alternate" hreflang="en" href="https://example.com/en/page" />
<link rel="alternate" hreflang="zh-CN" href="https://example.com/zh-CN/page" />
<link rel="alternate" hreflang="ja" href="https://example.com/ja/page" />
<link rel="alternate" hreflang="x-default" href="https://example.com/en/page" />
```

### Detail-page level
For each content page (e.g., 719 articles × 4 tags): emit **all 4 tags (3 locales + x-default)**, bidirectional (self-referencing included: every page lists every language, including itself).

**Rules that must hold:**
- Bidirectional: if A links to B, B must link back to A
- Self-referencing: page always lists itself
- x-default points to the most sensible fallback (usually the global `/en` version)
- hreflang pairs must be valid BCP-47 (e.g., `zh-CN`, not `zh_cn`)
- hreflang URLs must be accessible without redirects; use the direct canonical URL

## 3. canonical

- **Locale-self canonical**: each locale page canonicalizes to **its own URL** (`/en/page` → `/en/page`, `/zh-CN/page` → `/zh-CN/page`).
- Never canonicalize UI locale variants to a single global URL — that collapses independent language indexes.
- Keep canonical and hreflang consistent: the canonical is the language-agnostic "self", hreflang is the cross-language map.

## 4. sitemap

- Include **every locale variant** as its own entry (e.g., 776 URLs across locales with `/en` prefix etc.).
- Each entry uses its final canonical locale URL.
- Optionally add `xhtml:link` alternates inside sitemap entries for completeness; the essential requirement is that all variants are discoverable.
- Submit and re-submit in GSC after any locale expansion.

## 5. Schema `inLanguage`

Every content page declaring language prevents AI engines from mixing locales:

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "…",
  "inLanguage": "en",
  ...
}
```

- Add `inLanguage` to all 719 content items (Article, FAQPage, HowTo, Product, etc.)
- Match `inLanguage` exactly with the URL locale (`en` / `zh-CN` / `ja`)
- For FAQPage/HowTo, also set `inLanguage` at the top level

## 6. Open Graph locale

```html
<meta property="og:locale" content="zh_CN" />
<meta property="og:locale:alternate" content="en_US" />
<meta property="og:locale:alternate" content="ja_JP" />
```

- `og:locale` must match the page language; alternates list the other locales
- Keep og:locale consistent with hreflang and inLanguage to avoid mixed signals

## 7. Localized metadata (native keywords)

- Write title/meta descriptions in **native keywords per locale** — never machine-translate English copy
- Keyword research per locale differs (e.g., Japanese query styles, Chinese variant terms)
- Use locale-appropriate terminology (not just translated words)
- Localized metadata now includes AI-relevant optimization (front-load questions, numbers, and a clear answer in the first ~40 chars)

## 8. llms.txt multilingual section

Serve a multilingual-aware `/llms.txt` so AI engines find each language's content:

```markdown
# Brand Name

> 1–3 sentence business summary.

## Contact
- Website: https://example.com
- Email: hello@example.com

## English
- [About](https://example.com/en/about): Summary …
- [Docs](https://example.com/en/docs): …

## 中文 (zh-CN)
- [关于我们](https://example.com/zh-CN/about): …
- [文档](https://example.com/zh-CN/docs): …

## 日本語 (ja)
- [概要](https://example.com/ja/about): …
- [ドキュメント](https://example.com/ja/docs): …
```

- Group links by locale; keep summaries in each locale's language
- Consider `/llms-full.txt` only if you can keep per-locale updates current

## 9. GEO angle: AI engines and multilingual content

- AI engines match **query language** to content language; per-locale content with consistent metadata gets cited within its language pool.
- **Cross-language entity consistency**: keep brand/entity names, descriptions, and relationships identical across locales — AI treats them as one entity (see `05-authority-entities.md`).
- UGC and authority signals are locale-sensitive: earn mentions within each language market (Reddit/Quora in English, Zhihu in Chinese, note in Japanese, etc.).
- AI crawlers (GPTBot, ClaudeBot, PerplexityBot) respect robots.txt per locale; do not block them on any locale if you want citations.
- Each locale should also have its own AI-ready structure (FAST framework from `03-content-citation.md`) — structure wins across all languages.

## 10. Full i18n SEO Audit Checklist

- [ ] Locale-prefixed URLs: `/en`, `/zh-CN`, `/ja` independent and indexable
- [ ] Layout-level hreflang: all 3 locales bidirectional + x-default
- [ ] Detail-page hreflang: every page × 4 tags (3 locales + x-default)
- [ ] canonical: locale-self on every page
- [ ] sitemap: all locale variants listed (e.g., `/en` prefix entries)
- [ ] Schema `inLanguage` on every content item
- [ ] `og:locale` + `og:locale:alternate` on every page
- [ ] Native localized metadata: per-locale keywords (no machine translation)
- [ ] llms.txt with multilingual (per-locale) sections
- [ ] Cross-locale entity consistency (names, descriptions)
- [ ] AI crawlers allowed on every locale
- [ ] Per-locale AI-readable structure (FAST) verified
