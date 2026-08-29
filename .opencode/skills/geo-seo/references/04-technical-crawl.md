# 04 · Technical Layer: AI Crawler Accessibility

> No matter how good the content, if AI crawlers can't reach or read it, it will never be cited.
> The technical layer is the "foundation beneath the foundation" of GEO — the domain of the `AEO Foundations Architect`.

## 1. AI Crawler Access Management (robots.txt)

**Key AI user-agents:**

| Crawler | Owner |
|---------|-------|
| GPTBot / OAI-SearchBot / ChatGPT-User | OpenAI (ChatGPT) |
| ClaudeBot / anthropic-ai / Claude-Web | Anthropic (Claude) |
| PerplexityBot | Perplexity |
| Google-Extended | Google (AI training; AI Overviews uses Googlebot) |
| Applebot-Extended | Apple |
| CCBot | Common Crawl |
| Bytespider | ByteDance |

**Recommended config (allow if you want AI citations):**

```robots.txt
# Allow major AI search crawlers (affect real-time AI answers/citations)
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /

# Allow AI training crawlers (affect future model training)
User-agent: CCBot
Allow: /
User-agent: anthropic-ai
Allow: /
User-agent: Bytespider
Allow: /
```

**Strategy decision:**

| Strategy | When |
|----------|------|
| Allow all | Want AI citations + training corpus inclusion |
| Block training crawlers only (e.g., GPTBot) | Want real-time citations, but no training |
| Selective | Per-platform policy |

> For multilingual sites: apply the same allowance to **every locale** (`/en`, `/zh-CN`, `/ja`).

## 2. llms.txt (AI-Friendly Site Index)

`llms.txt` is an emerging standard (like robots.txt; see https://llmstxt.org/) that gives AI a structured, machine-readable site overview. **Brand description accuracy improves ~24%** when configured.

- Serve at the exact root `/llms.txt` on the production domain.
- Curate a short list of high-value, stable pages — not every URL.
- Optional `llms-full.txt` for full content (only if kept current).
- For multilingual sites: group links **per locale** (see `09-i18n-seo.md`).

```markdown
# Brand Name

> 1–3 sentence business summary.

## Contact
- Website: https://example.com
- Email: hello@example.com

## Services
- [Service 1](https://example.com/service-1): Brief description
- [Service 2](https://example.com/service-2): Brief description

## Key Information
- [About Us](https://example.com/about)
- [Documentation](https://example.com/docs)
```

> Note: `llms.txt` does **not** replace `robots.txt` crawl control; they serve different purposes.

## 3. Structured Data (Schema / JSON-LD)

Schema helps AI precisely understand content type and entities. Google recommends JSON-LD.

**Recommended types**: Article, FAQPage, HowTo, Product, Organization, Person, BreadcrumbList, Speakable (voice). **Multilingual**: add `inLanguage` (see `09-i18n-seo.md`).

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Title",
  "inLanguage": "en",
  "author": { "@type": "Person", "name": "Author Name", "url": "Author page" },
  "datePublished": "2026-01-01",
  "dateModified": "2026-08-01",
  "publisher": { "@type": "Organization", "name": "Org Name" }
}
```

## 4. Server-Side Rendering (SSR) & AI Crawlers

- AI crawlers **largely don't execute JavaScript**.
- Content depending on client-side rendering (CSR) may be **invisible** to AI.
- Core information must be in the **initial HTML**; use SSR / SSG / pre-rendering where needed.

## 5. Entity Resolution & Semantic Trust

| Technique | Explanation |
|-----------|-------------|
| **Entity resolution** | Consistent naming, disambiguation, links to authoritative sources so AI identifies entities precisely |
| **Semantic trust mechanisms** | Strong factual backing, credible research citations, demonstrated expertise — trust intrinsic to content itself (beyond traditional backlinks) |
| **RAG adaptation** | Modular content, clear headings and summaries, key info easily extractable for synthesis |

## 6. Product Feeds

Structured product data boosts AI product citations:

| Platform | Submission |
|----------|-----------|
| Google | Google Merchant Center |
| Microsoft | Microsoft Merchant Center (drives Copilot product results) |
| ChatGPT | Product discovery registration (not yet open) |

## 7. Technical GEO Checklist

- [ ] Schema.org structured data (JSON-LD)
- [ ] Load speed < 2.5s
- [ ] Mobile-friendly
- [ ] Semantic HTML (correct H1–H6 hierarchy; exactly 1 H1 per page)
- [ ] XML sitemap generated and submitted
- [ ] robots.txt allows AI crawlers
- [ ] `/llms.txt` created
- [ ] HTTPS everywhere
- [ ] Image alt text
- [ ] Critical content SSR / in initial HTML
- [ ] 4xx/5xx dead links fixed (> 5 drags down quality score)
- [ ] Duplicate Meta descriptions eliminated (> 10 pages sharing one triggers low-quality penalty)
