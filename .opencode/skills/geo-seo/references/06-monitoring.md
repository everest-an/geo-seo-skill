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
.*(chatgpt\.com|openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|bard\.google\.com|you\.com|search\.brave\.com|copilot\.microsoft\.com|grok\.com|doubao\.com|kimi\.moonshot\.cn|kimi\.com|chat\.deepseek\.com|chatglm\.cn|yuanbao\.tencent\.com|tongyi\.aliyun\.com|tongyi\.com|yiyan\.baidu\.com|metaso\.cn|n\.cn|quark\.cn|sm\.cn).*
```

## 4. Attribution Chain: From "Cited" to "Business Result"

> Visibility metrics (mention rate / citation share) tell you you're *in* the AI answer. Attribution answers the next
> question: **did AI traffic actually land on your site, and did those visitors convert?**
> From the GeoLook skill (MIT, github.com/aigclink/geolook).

```
User asks AI → answer cites you → user clicks the citation → landing page → signup / inquiry / purchase
              (sampling measures)      (referrer/UTM measures)        (events + source snapshot measures)
```

The three stages each measure something different, each leaks, and **none substitutes for another**:

1. **Sampling** measures "are you in the answer" — upstream supply
2. **Referrer/UTM** measures "how many sessions did AI bring"
3. **Conversion events + source snapshot** measures "what those sessions are worth" — lives in your business system

### AI engine referrer domain list

> Verify against your OWN server logs / GA4 first — each app's referrer policy changes over time, and in-app opens
> often carry no referrer at all (see "lower bound" discipline below).

| Engine | Common referrer domains | Note |
|---|---|---|
| ChatGPT | `chatgpt.com`, `chat.openai.com` | web carries referrer |
| Perplexity | `perplexity.ai` | relatively high citation click rate |
| Gemini | `gemini.google.com` | |
| Copilot | `copilot.microsoft.com`, `bing.com` | bing.com mixes traditional search |
| Claude | `claude.ai` | |
| Grok | `grok.com` | |
| 豆包 | `doubao.com` | most App traffic has no referrer |
| Kimi | `kimi.moonshot.cn`, `kimi.com` | |
| DeepSeek | `chat.deepseek.com` | |
| 智谱清言 | `chatglm.cn` | |
| 腾讯元宝 | `yuanbao.tencent.com` | |
| 通义 | `tongyi.aliyun.com`, `tongyi.com` | |
| 文心一言 | `yiyan.baidu.com` | most Baidu-AI clicks still come via `baidu.com` — hard to separate from traditional search |
| 秘塔 | `metaso.cn` | |
| 纳米AI | `n.cn` | |
| 夸克 | `quark.cn`, `sm.cn` | sm.cn mixes traditional search |

> Not listed ≠ doesn't exist. For any new engine, grab a slice of your logs, grep the `Referer` header, add it.

### Three configuration actions

1. **GA4 / analytics**: create a custom "AI Sources" channel group with a source (referrer) regex — the upgraded regex above covers global + CN engines.
2. **Server logs**: grep is more reliable than GA4 — immune to front-end blocking and ad blockers, and you can see the AI
   crawlers' own fetch behavior (UA contains GPTBot / ClaudeBot / PerplexityBot — more crawling usually *precedes* more citations, a leading signal):
   ```bash
   grep -iE "chatgpt\.com|perplexity\.ai|gemini\.google|claude\.ai|doubao\.com|kimi\.|deepseek|chatglm|yuanbao\.tencent|metaso" access.log | wc -l
   ```
3. **Conversion events save a source snapshot**: attribution priority **click ID > UTM > referrer > direct/unknown**.
   Store first-touch + last-touch source in your business DB at signup/inquiry/purchase — otherwise you can only see aggregates later.

### Discipline: you measure a lower bound, don't extrapolate

- In-app opens, privacy policy, cross-device all eat referrers — **measured AI traffic is a lower bound**.
  Report "attributable AI sessions ≥ N", never "AI brought N".
- AI-source sessions are usually small in volume but deep in intent — look at conversion RATE first, not session count;
  don't conclude on samples under three digits.
- Don't stack UTM params on public content for attribution: a parameterized URL, once cited, dilutes the canonical URL's
  citation share. **UTM only where you fully control and engines won't index it** (email, private channels); public placements rely on referrer attribution.

## 5. Citation Overlap with Google Top 10 (Prioritization Guide)

| Platform | Domain overlap (vs Google Top10) | Characteristics |
|----------|-----------------------------------|-----------------|
| Perplexity | 91% | Closest to Google Top10; most like traditional SEO |
| Google AI Overviews | 86% | Heavily relies on Google's traditional index |
| Google AI Mode | 54% | More independent retrieval |
| ChatGPT | Lowest | Leans Bing; cites pages ranked 21+ |

## 6. Monitoring Workflow

```
Publish content → AI crawler indexing → Monitor AI citations → Analyze citation quality → Optimize content → (back to publish)
```

**Practice cadence**:
- **Short-term (48h)**: GSC crawl stats, average position, CTR; manual re-index request at hour 24.
- **Mid-term (weekly/monthly)**: AI citation rate, brand mentions, AI referral traffic.
- **Long-term (quarterly)**: Share of voice vs competitors, sentiment analysis, citation accuracy.

## 7. Warning Signals

| Signal | Meaning | Action |
|--------|---------|--------|
| Crawl volume spikes | Engine "interested" | Keep content fresh; reinforce while momentum is high |
| Rank in top 10 but low CTR | Title/description underperforming | Revise Meta; use numbers + emotional words |
| Zero AI citations but OK ranking | Extractability/authority lacking | Re-check `03` + `04` + `05` |
| Inaccurate citations | Content misunderstood | Improve entity naming, clarify definitions |
