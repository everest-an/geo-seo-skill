# 06 · Monitoring & Measurement

> You can't improve what you don't measure. GEO must be quantified alongside SEO.

## 1. Key Metrics

| Metric | Description | How to measure |
|--------|-------------|----------------|
| **AI citation rate** | How often your content is cited by AI | GEO monitoring tools |
| **Brand mentions** | How often your brand appears in AI answers | Brand monitoring tools |
| **Citation accuracy** | Whether AI cites your info accurately | Manual verification |
| **Visibility score** | Overall visibility in AI search results | AI ranking tools |
| **Cited pages** | Which specific pages get cited | Traffic analysis |

## 2. Monitoring Tools

| Tool | Positioning |
|------|-------------|
| **Semrush AI Visibility Toolkit / Enterprise AIO** | Brand AI visibility, mentions, citations, share of voice |
| **Profound** | Multi-language deep AI brand visibility analysis |
| **Peec AI** | Brand mention analysis in AI search |
| **Otterly.AI** | AI search engine ranking tracking |
| **OptimizeGEO** | Visibility score, share of voice, sentiment (ISO 27001) |
| **Geol.ai** | Automated monitoring + 50-factor scoring + CMS integrations |
| **Prompt Monitor** | Prompt-level AI search performance analytics |
| **Brand24 / Mention / Brandwatch** | Whole-web brand monitoring |

(Full tool ecosystem in `08-tools-resources.md`)

## 3. GA4 AI Referral Traffic Tracking

**Goal**: isolate AI-origin traffic in GA4.

**Method** (custom channel group):
1. GA4 → Admin → Data display → Channel groups
2. Add channel "AI Referral Traffic"
3. Condition: Source → matches regex → paste the regex below
4. Move the AI Traffic group **above** Referral
5. Save and apply across acquisition reports

```regex
.*(chatgpt\.com|openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|bard\.google\.com|you\.com|search\.brave\.com|copilot\.microsoft\.com|grok\.com).*
```

## 4. Citation Overlap with Google Top 10 (Prioritization Guide)

| Platform | Domain overlap (vs Google Top10) | Characteristics |
|----------|-----------------------------------|-----------------|
| Perplexity | 91% | Closest to Google Top10; most like traditional SEO |
| Google AI Overviews | 86% | Heavily relies on Google's traditional index |
| Google AI Mode | 54% | More independent retrieval |
| ChatGPT | Lowest | Leans Bing; cites pages ranked 21+ |

## 5. Monitoring Workflow

```
Publish content → AI crawler indexing → Monitor AI citations → Analyze citation quality → Optimize content → (back to publish)
```

**Practice cadence**:
- **Short-term (48h)**: GSC crawl stats, average position, CTR; manual re-index request at hour 24.
- **Mid-term (weekly/monthly)**: AI citation rate, brand mentions, AI referral traffic.
- **Long-term (quarterly)**: Share of voice vs competitors, sentiment analysis, citation accuracy.

## 6. Warning Signals

| Signal | Meaning | Action |
|--------|---------|--------|
| Crawl volume spikes | Engine "interested" | Keep content fresh; reinforce while momentum is high |
| Rank in top 10 but low CTR | Title/description underperforming | Revise Meta; use numbers + emotional words |
| Zero AI citations but OK ranking | Extractability/authority lacking | Re-check `03` + `04` + `05` |
| Inaccurate citations | Content misunderstood | Improve entity naming, clarify definitions |
