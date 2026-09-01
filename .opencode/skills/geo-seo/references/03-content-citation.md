# 03 · Content & Citation Optimization

> Core question: why does an AI engine **cite** A and not B?
> Answer: **extractability + information gain + trust.**

## 1. Content Types Most Likely to Be Cited by AI

| Content type | Why it gets cited |
|--------------|-------------------|
| **Original research/data** | Provides unique evidence to back specific claims |
| **Case studies** | Supports AI's specific recommendations |
| **Authoritative definitions** | Easy to extract and quote directly |
| **Step-by-step guides** | Actionable value |
| **Comparison tables** | Structured info AI can use directly |
| **FAQ / Q&A** | Direct answers, naturally extractable |
| **Thought-leadership opinions** | AI wants unique, diverse perspectives |
| **News/time-sensitive content** | Pre-trained data can't cover recent events |
| **Brand-owned content** | AI trusts brands on their own information |

**Not suitable for GEO**: thin content, duplicate content, pure sales copy, unsourced opinions, outdated info.

## 2. Information Gain — Key to Ranking Uplift

**Definition**: how much **new, unique** information your page adds beyond the AI engine's already-indexed top results.

**Method (Step 1 of the rapid method)**:
1. Pull the target keyword's Top 5–10 competitors.
2. Extract consensus info + differentiators + blind spots (see `02-rapid-method.md` prompts).
3. Fill only the blind spots — unique data, exclusive cases, uncovered angles.
4. Result: the semantic system judges your page as higher "information gain" → ranking boost signal.

**Anti-warning**: only replicating consensus info = zero gain = no ranking momentum.

## 3. Extractability — The "AI-Favorite Format"

Make it one-line-extractable by AI:

- **Question-style heading hierarchy**: H2/H3 written as real user queries ("What is X", "How much does X cost").
- **2–3 sentences per paragraph**: avoid long blocks; easier for NLP parsing.
- **Lists/tables for key conclusions**: definitions, data, comparisons.
- **Top "quick navigation zone"**: TL;DR + direct answers to the 5 most likely follow-ups.
- **Independent "quotation-worthy" sentences**: one sentence that can be lifted into a citation.
- **Explicit sources and dates**: AI must judge credibility and freshness.

## 4. Semantics & Entities (LSI / Synonyms)

- Naturally embed synonym variants (LSI keywords) at **2–3%** density (not stuffing).
- **Entity coverage**: cover related entities (persons, organizations, concepts, products) around the topic — semantic relevance is the highest-weight RAG factor (~40%).
- Keyword stuffing is counterproductive — confirmed by GEO research.

## 5. FAST Framework (AI Fetchability Check)

> Source: Semrush — "Why Site Health Is Vital For AI Search Visibility"

| Dimension | Question | Key actions |
|-----------|----------|-------------|
| **F - Fetchable** | Can AI read the HTML without rendering JS? | Test with JS off; core info in initial HTML; SSR |
| **A - Accessible** | Is content understandable without executing scripts? | Alt text, H1–H6 hierarchy, semantic HTML5 |
| **S - Structured** | Schema, semantic tags, clear hierarchies in place? | Definition boxes, Product/Article/Organization Schema, FAQ Schema |
| **T - Trim** | Sending only what's needed, no bloat/noise? | Clean tracking scripts, compress assets, minimize JS deps |

> **Quick test**: open your top 20 pages with JavaScript disabled. What you see is approximately what AI crawlers see.

## 6. GEO Content Checklist

**Content elements**
- [ ] Question-style title
- [ ] Summary/TL;DR at top
- [ ] Original data (with sources)
- [ ] Expert quotes (name + title)
- [ ] FAQ block (3–5 Q&A)
- [ ] Clear definitions
- [ ] "Last updated" timestamp
- [ ] Author + credentials

**Structure elements**
- [ ] Article Schema with dates
- [ ] Person Schema for author
- [ ] FAQPage Schema
- [ ] Load < 2.5s
- [ ] Clean semantic HTML

## 7. Citability Scoring Framework (borrowed from claude-seo)

> A weighted audit model — score any page 0–100 on why an AI engine would pick it.

| Dimension | Weight | What to check |
|-----------|--------|---------------|
| **Citability** | 25% | 134–167 word self-contained answer blocks; direct answer in the first 40–60 words; specific facts/statistics; attributed claims; "X is…" definition patterns |
| **Structural readability** | 20% | Clean H1→H2→H3 hierarchy; question-based headings; 2–4 sentence paragraphs; tables and lists; FAQ Q&A blocks |
| **Multi-modal** | 15% | Text + images, video, charts, interactive tools; structured data for media (multi-modal content is selected **156% more often**) |
| **Authority & brand** | 20% | Author byline + credentials; published/updated dates; primary-source citations; entity presence in Wikipedia/Wikidata; Reddit/YouTube/LinkedIn mentions |
| **Technical accessibility** | 20% | SSR (AI crawlers don't run JS); AI-crawler allow rules in robots.txt; llms.txt presence; structured data |

**Highest-leverage numbers:**

- Optimal citable passage: **134–167 words**
- **~44%** of AI citations come from the **first 30%** of the page → front-load the answer, don't bury it below the fold
- **92%** of Google AI Overviews citations come from top-10 pages, but **47%** come from pages below position 5 → classic ranking ≠ citation selection
- Freshness: content under 3 months old is **~3x more likely** to be cited; pages stale 6+ months lose citation eligibility → schedule refreshes
- **Brand mentions correlate ~3x more strongly with AI visibility than backlinks** (Ahrefs study, 75k brands): YouTube mentions r≈0.737 (strongest), Reddit high, Wikipedia high, LinkedIn moderate; Domain Rating only r≈0.266

## 8. Platform-Specific Citation Sources

AI engines cite **different source pools** — optimize per platform:

| Platform | Primary citation sources | Optimization focus |
|----------|--------------------------|--------------------|
| **Google AI Overviews** | Strongly ranking-correlated (cites pages that already rank) | Classic SEO + passage optimization |
| **Google AI Mode** (Gemini 2.5-based) | Weakly ranking-correlated; ~9 domains cited per query | Freshness, entity authority, citable passages beyond position 5 |
| **ChatGPT** | Wikipedia (47.9%), Reddit (11.3%) | Entity presence, authoritative sources |
| **Perplexity** | Reddit (46.7%), Wikipedia | Community validation, discussion presence |
| **Bing Copilot** | Bing index, authoritative sites | Bing SEO, IndexNow |

> **Two Google citation engines, not one.** AI Mode and AI Overviews reach the same conclusion ~86% of the time but cite the same URLs only **13.7%** of the time (Ahrefs study, 540k query pairs). Treat them as separate surfaces.
>
> **Only 11% of domains** are cited by both ChatGPT and Google AI Overviews for the same query — don't expect one page to win everywhere.

## 9. Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| Publish without dates | Add timestamp + dateModified |
| Vague attributions | Name your sources |
| Skip author info | Show credentials & experience |
| Thin content | Comprehensive depth |
| Keyword stuffing | Semantics + entities + information gain |
| Poetic, vague language | Direct, standalone-sentence expressions |
