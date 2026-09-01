# 05 · Authority & Entity Building

> Long-term AI visibility comes not from short-term tricks but from being **recognized across the web as an authority on a topic**.
> AI systems retrieve from the same web your content lives on — the more your brand is mentioned and trusted, the more likely it gets cited.

## 1. E-E-A-T Optimization

| Element | Strategy |
|---------|----------|
| **Experience** | First-hand experience, case studies, practical screenshots |
| **Expertise** | Showcase qualifications, professional background, industry recognition |
| **Authoritativeness** | Industry citations, media coverage, expert endorsements |
| **Trustworthiness** | Transparent information sources, accurate facts, secure website |

**Implementation**: author pages with real credentials and history; name expert names/titles; cite credible research; label sources and dates.

## 2. Entity Building

| Action | Purpose |
|--------|---------|
| Google Knowledge Panel | Recognized as an entity by Google |
| Wikipedia (if notable) | Authority source + significant training-data share |
| Consistent info across the web | Entity information unified (names/descriptions/relationships) |
| Industry mentions | Authority signals |

> Key: AI engines understand entities from consistent information across the web. **Names, descriptions, and relationship graphs must be consistent across platforms** (and across locales — see `09-i18n-seo.md`).

## 3. Brand Mentions (AI Brand Mentions)

- LLMs mention brands in **26–39%** of non-branded query responses.
- **Unlinked brand mentions** may carry more weight in AI contexts — being mentioned, even casually, can boost AI visibility.

**Getting more AI mentions:**
- Publish in-depth content about your brand, products, and specific use cases
- Get brand mentions in context-rich third-party content (blogs, news, Reddit, Quora)
- Run affiliate/influencer campaigns to generate buzz
- List your brand on high-quality directories
- Create "you vs. competitors" comparison content

**Improving mention sentiment:**
- Gather and act on customer feedback
- Publish data-backed case studies proving success
- Proactively manage online reviews
- Consistently communicate unique value propositions (UVPs)
- Plan a crisis strategy for negative mentions

**Challenges for emerging brands**: AI favors brands with extensive digital presence; lesser-known brands may get hedging language ("might be worth considering"). Breakthrough requires aggressively building a digital footprint.

## 4. External Signals

- Guest posts on authoritative sites
- Participation in industry research and reports
- News media coverage
- Social media authority
- Participation in knowledge platforms (Wikipedia)
- Expert answers on Q&A platforms (Quora, Stack Overflow) — and per-market equivalents

## 5. UGC & Platform Signals

| Platform | Why it matters |
|----------|----------------|
| Reddit | Appears in 68%+ of AI Mode results |
| YouTube | High exposure in AI Mode |
| Quora | Most cited site in Google AI Overviews |
| Facebook | High exposure in AI Mode |
| Wikipedia | Significant share of AI training data |

> Brand **presence on these platforms directly transfers into generative-engine visibility.**
> Locale matters: each language market has its own UGC hubs (Reddit/Quora in EN, Zhihu in CN, etc.).

## 6. Case Insights (Authority Models AI Cites)

- **Investopedia**: authoritative financial definitions → primary source for financial answers
- **WebMD / Healthline**: E-E-A-T health content → frequent citations (Healthline: 3x AI visibility via E-E-A-T strategy)
- **Stack Overflow**: developer Q&A → knowledge source for AI coding assistants
- **NerdWallet**: financial comparison content → 78% AI citation rate on personal finance queries
- **HubSpot**: comprehensive marketing guides → preferred source for marketing topics
- **Zapier**: integration guides → high-frequency citations for automation queries

## 7. Brand Fact Card (the Knowledge Base for Everything Else)

> From the GeoLook skill (MIT, github.com/aigclink/geolook). Build this first, before writing any content.
> It is the single input that generates llms.txt, JSON-LD, definition blocks and content outlines — and the #1 cause
> of AI "brand drift" is the official site, the fact card and the JSON-LD description disagreeing.

```markdown
## Entity
- Canonical name: <full name>
- Aliases / abbreviations: <all of them, incl. English name, old name, common misspellings>
- One-sentence definition: <X is a … for …>   ← this exact sentence is what AI will extract
- Company / founded / HQ:
- Website:

## Product & capability
| Product | Positioning | Core capability | Who it's for |

## Key numbers (each with source + verification date)
| Fact | Value | Source | Verified | Evidence grade |

## Applicable & not applicable
- Suitable: <3, specific to people and scenarios>
- Not suitable: <2>          ← explicit boundaries significantly raise credibility and citation rate

## Forbidden phrasing
- Don't say: <absolutist/unverified claims>
- Say instead: <verifiable version>
```

**Evidence grades**: `A officially confirmed` / `B third-party corroborated` / `C internal, pending authorization` /
`D needs verification` / `E prohibited`. D and E require a follow-up action — never leave them sitting.

**Consistency rule**: the JSON-LD `description`, the fact card's one-sentence definition, and the homepage's above-the-fold
definition line must match **verbatim**. Inconsistency is the top cause of AI misdescribing your brand.
