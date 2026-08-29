# 07 · Prompt Library (Copy-Paste Ready)

> Ready-to-use prompts for each stage of the system. Replace `{{ }}` placeholders with your actual content.

## 1. Competitor Dissection (Mine Blind Spots · Rapid Method Step 1)

```
Analyze these 5 competitor articles. Output:
1. The consensus information they all cover;
2. Each article's unique differentiators;
3. Information blind spots: what NO article mentions but users might care about;
4. Frequent reader complaints / unmet needs.

Competitor content:
{{paste top-5 competitor pages}}
```

**Advanced version (with coverage matrix)**:

```
Compare the following competitor pages. Output a Markdown table "content coverage comparison matrix":
- Rows = all subtopics/entities/questions covered by any competitor
- Columns = each competitor (mark "covered" or not)
Then list the 10 information blind spots that the current Top 10 ALL miss,
ordered by search-intent value (highest first).
```

## 2. AI-Readability Restructure (Rapid Method Step 2)

```
Restructure the following content into the format AI crawlers love to parse:
1. Clear question-style H2/H3 heading hierarchy;
2. Every paragraph 2–3 sentences max, avoid long text blocks;
3. Key data and conclusions in lists/tables;
4. Naturally embed synonym variants (LSI keywords) throughout, density 2–3%;
5. Add a "quick navigation zone" near the top that directly answers the
   user's 5 most likely follow-up questions.

Content:
{{paste original text}}
```

## 3. Content GEO Optimization (General)

```
You are a GEO (Generative Engine Optimization) expert. Optimize the content below so
ChatGPT/Perplexity/Gemini/Claude are more likely to cite it:
1. Give a directly quotable core conclusion in the first 40 characters;
2. Add source and date to every key data point;
3. Split any paragraph longer than 3 sentences;
4. Add an FAQ block (5 questions, answered directly);
5. Generate Article Schema (JSON-LD) with dates and author;
6. Note author credentials (or flag that I need to supply them).
```

## 4. GEO Audit (Diagnose "Why Doesn't AI Cite Me")

```
Audit the following page/site using the FAST framework; output issues + priority (high/medium/low):
- F Fetchable: can AI read core info without executing JS?
- A Accessible: semantic HTML, H1-H6 hierarchy, alt text in place?
- S Structured: missing Article/FAQPage/Person/Organization Schema?
- T Trim: redundant scripts, uncompressed assets, excessive JS deps?

Then check: does robots.txt block GPTBot/ClaudeBot/PerplexityBot/Google-Extended?
Is llms.txt configured? Does the content have clear dates, author, and sources?

Page/site:
{{URL or paste HTML}}
```

## 5. Information-Gain Copy (Fill Blind Spots)

```
Below are the "consensus info" all Top-5 competitors cover, and the "blind spots" they all miss.
Write ~200 words of unique content based on the blind spots, designed to be cited by AI.
Requirements: at least 1 concrete data point, 1 clear conclusion, direct language
(no poetic or vague expressions).

Consensus info: {{...}}
Blind spots: {{...}}
```

## 6. Meta Title/Description Optimization (Boost CTR)

```
Generate 5 candidate Meta titles and 5 Meta descriptions for the page below.
Requirements: specific numbers, emotional words, clear value promise;
titles ≤ 60 chars, descriptions ≤ 155 chars;
each naturally includes the core keyword "{{keyword}}".

Page topic: {{...}}
```

## 7. Brand Mention Strategy (Increase AI Mentions)

```
Based on my brand info, output an "AI brand mention growth checklist":
1. 10 own-content topics to create/optimize (easy for AI to cite);
2. 5 types of third-party contextual mentions to earn (blogs/news/Reddit/Quora/directories);
3. 3 angles for "brand vs competitor" comparison content;
4. Platforms where my brand info may be inconsistent (entity unification needed).

Brand info: {{...}}
```

## 8. Entity & Schema Generation

```
Generate complete Schema.org JSON-LD for the following content:
- Type: {{Article / FAQPage / HowTo / Product / Organization}}
- Include author (Person + url), datePublished, dateModified, publisher (Organization).
- If FAQPage: extract 5 real Q&A pairs from the content.
- For multilingual: set inLanguage per locale.
```

## 9. llms.txt Generation

```
Based on the site info below, generate a /llms.txt file following the llmstxt.org spec:
- 1–3 sentence brand summary
- Contact details
- 5–10 highest-value pages (with one-line descriptions)
- For multilingual sites: group links per locale (/en, /zh-CN, /ja)

Site info: {{...}}
```

## 10. GEO Competitor Verification Queries (Manual Citation Check)

Ask each major AI engine directly to verify mentions:

```
Templates (replace {{your brand}} and {{industry}}):
"What are the best 3 {{products/services}} in {{industry}}?"
"Compare {{your brand}} vs {{competitor}}: pros and cons of each?"
"Recommend a {{product}} for {{use case}}"
```

> Record: which engines mention you? Is the wording recommending / neutral / hedging? Which of your pages got cited?
