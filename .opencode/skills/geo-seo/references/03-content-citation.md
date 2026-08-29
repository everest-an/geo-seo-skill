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

## 7. Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| Publish without dates | Add timestamp + dateModified |
| Vague attributions | Name your sources |
| Skip author info | Show credentials & experience |
| Thin content | Comprehensive depth |
| Keyword stuffing | Semantics + entities + information gain |
| Poetic, vague language | Direct, standalone-sentence expressions |
