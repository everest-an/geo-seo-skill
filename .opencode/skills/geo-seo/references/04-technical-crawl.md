# 04 · Technical Layer: AI Crawler Accessibility

> No matter how good the content, if AI crawlers can't reach or read it, it will never be cited.
> The technical layer is the "foundation beneath the foundation" of GEO — the domain of the `AEO Foundations Architect`.

## 1. AI Crawler Access Management (robots.txt)

**Full AI crawler matrix** (14 user-agents, current as of 2026):

| Crawler | Owner | Purpose | Obeys robots.txt? |
|---------|-------|---------|-------------------|
| GPTBot | OpenAI | ChatGPT web search | Yes |
| OAI-SearchBot | OpenAI | OpenAI search features | Yes |
| ChatGPT-User | OpenAI | ChatGPT browsing (user-triggered) | **No** (user-triggered) |
| ClaudeBot | Anthropic | Claude web features | Yes |
| anthropic-ai | Anthropic | Claude training | Yes |
| PerplexityBot | Perplexity | Perplexity AI search | Yes |
| CCBot | Common Crawl | Training data (often blocked) | Yes |
| Bytespider | ByteDance | TikTok/Douyin AI | Yes |
| cohere-ai | Cohere | Cohere models | Yes |
| Google-Extended | Google | Gemini/Vertex training & grounding opt-out | Yes |
| Google-CloudVertexBot | Google | Site-owner-requested Vertex AI Agent crawls | Yes |
| Google-Agent | Google | Agentic browsing (Project Mariner), acts for a user | **No** (user-triggered) |
| Google-NotebookLM | Google | Fetches user-added source URLs | **No** (user-triggered) |
| Google Messages | Google | User-triggered fetch | **No** (user-triggered) |

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

> **User-triggered fetchers ignore robots.txt by design** (Google-Agent, Google-NotebookLM, Google Messages, ChatGPT-User). robots.txt cannot block them — use server-side access controls. Emerging: **Web Bot Auth** (RFC 9421) lets bots authenticate via a `Signature-Agent` header + key directory (used by Google-Agent); reverse-DNS verification remains the fallback.

> For multilingual sites: apply the same allowance to **every locale** (`/en`, `/zh-CN`, `/ja`).

### robots.txt must be judged by RFC 9309 semantics, not line-by-line regex

Three real-world block types that naive per-line parsing misses (GeoLook method layer):

1. **`User-agent: * / Disallow: /` blocks every AI crawler without its own group** — the most common "unintentional block"
2. **Multiple `User-agent` lines sharing one rule set** — per-line regex misreads the first UA as an empty rule
3. **Specificity ignores order**: when a dedicated group exists, the wildcard group is entirely void — `User-agent: GPTBot / Allow: /` makes GPTBot ignore any `Disallow` in the wildcard group

**robots allowing ≠ actually allowing.** WAF/CDN (Cloudflare Bot Fight, Aliyun WAF, …) may return 403 specifically for AI
crawler UAs while everything looks fine in a browser. Probe it: fetch the homepage with the real UAs of GPTBot / ClaudeBot /
PerplexityBot / Bytespider and diff the responses (`ai_ua_probe` in GeoLook's crawl.py).

**llms.txt only matters if it points to crawlable pages.** Links to 404s or robots-blocked paths hand AI a broken map.
Sample-verify the links inside it.

## 2. llms.txt (AI-Friendly Site Index)

`llms.txt` is an emerging standard (like robots.txt; see https://llmstxt.org/) that gives AI a structured, machine-readable site overview.

> **Evidence check (updated 2026):** Google's official AI optimization guide states Google Search **ignores** `llms.txt` — it does not help or hurt rankings or AI visibility. John Mueller called the discovery use case "a dead end"; Gary Illyes confirmed Google has no support plans. SE Ranking's 300k-domain study found only **1 of the top 50 AI-cited domains** had one, and OtterlyAI server logs show only **0.1%** of AI-bot requests target it. **Ship it anyway**: AI coding agents (Cursor, Claude Code) increasingly consume it for docs sites, and it's zero-cost optionality for non-Google systems. Never present it as a Google ranking or citation lever.

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
