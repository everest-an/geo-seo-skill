# 12 · Engine Citation Audit: "Why Does AI Not Cite Us?"

> The most direct GEO effectiveness check: **ask the engine a buyer-intent question, watch who it cites,
> and diagnose why your brand is absent.** This is the audit workflow behind the classic finding:
> "Doubao cited our competitors but not us — because our Chinese content ecosystem has zero mentions of us."

## 1. The Two-Gate Model (retrieval ≠ selection)

Before anything else, decide which gate you failed. These require different fixes and confusing them wastes months:

```
Gate 1: RETRIEVAL  — did the engine even find you as a candidate?
Gate 2: SELECTION  — you're in the candidate pool, why didn't it pick you?
```

| Gate | Question | Failure symptom | What actually fixes it |
|---|---|---|---|
| **1. Retrieval** | Is your brand/page in the engine's candidate set? | The answer never mentions you at all | Content-ecosystem presence: third-party mentions, tutorials, reviews, discussions (NOT your website) |
| **2. Selection** | You're retrievable — why not cited? | You appear, but citations go to competitors | Page-level citability: quotable passages, authority signals, structured data, on-topicness |

> **The single most common mistake**: a brand with a great website that no engine cites assumes the website is broken.
> Usually the website is *fine* — the brand simply isn't in the retrieval candidate set, because **nobody on the
> open web writes about it.** (See `11-cn-geo-playbook.md` §1: official sites are only 1.37% of CN AI citations —
> official sites are fact sources, not citation sources.)

## 2. The 5-Step Audit

### Step 1 · Define the question set

Pick 5–10 **buyer-intent** questions (recommendation / comparison / alternative / price). These are closest to
conversion and the ones that matter. Real user phrasings, no translationese:

- CN: "AI 记忆产品有哪些好用的？" "Mem0 和 Mem.ai 哪个好？" "给 AI 加记忆的工具"
- EN: "What's the best AI memory tool in 2026?" "Mem0 vs Mem.ai comparison"

Mark each question `market` (cn / global) — Chinese questions route to Chinese engines, English to overseas ones.

### Step 2 · Run the engine (record the environment)

Record the environment or the sample is worthless (evidence grading, see `11-cn-geo-playbook.md` §7):

| Environment | Meaning |
|---|---|
| API, online (grounding on) | Real retrieval, reproducible |
| API, offline (no grounding) | Parametric knowledge only — measures brand cognition, NOT visibility |
| Web / App, fresh conversation | Real UX sample, grade A if recorded (sandbox/incognito/clean profile) |

Rules: one fresh conversation per question (no follow-ups — context biases later answers); copy the FULL answer
verbatim including citation links; **record "brand not mentioned" too — that is the most important data point.**

### Step 3 · Record what happened

For each answer, log:

1. **Which sources were cited** (domains + titles) — this is the current distribution map
2. **Where your brand appears**: mentioned + cited / mentioned only / not mentioned at all
3. **If mentioned, is the description accurate?** (right industry, right facts, right wording)
4. **Citation position** — are you first, middle, or absent

### Step 4 · Diagnose with the decision tree

```
Is your brand in the answer at all?
├─ NO → you failed GATE 1 (retrieval)
│   └─ Why? Your content ecosystem has zero mentions.
│       → Check: does "brand + category" return anything on the platforms that engine reads
│         (CN: Zhihu / CSDN / Juejin / WeChat articles / web; overseas: Reddit / YouTube / blogs)?
│       → Fix: content-ecosystem building (§4), NOT website work.
├─ YES, mentioned but all citations go to competitors → you passed Gate 1, failed Gate 2 (selection)
│   └─ Why? You're retrievable but the cited pages win on passage quality/authority.
│       → Check: does your page have quotable passages (≥60 words + hard info, see `03` §8.5)?
│         Authority signals (dates, author, external refs)? Structured data? On-topic H1/H2?
│       → Fix: page-level citability (`03` evidence-page skeleton), authority (`05`).
└─ YES, mentioned but described WRONG (wrong industry / wrong facts / wrong wording)
    └─ You're retrievable but your entity representation is inconsistent.
        → Fix: brand fact card + JSON-LD verbatim consistency (`05` §7) — AI "brand drift" #1 cause.
```

### Step 5 · Act + re-test

Priorities (merge with `11-cn-geo-playbook.md` §6 ordering):

1. **P0 — retrieval blockers** on your own site: robots/WAF blocking, SPA empty shell, no sitemap, no structured data (see `04`)
2. **P1 — content ecosystem**: the exact gaps the audit surfaced — tutorials, reviews, community discussions, ranking-site entries
3. **P1 — page citability** for pages that ARE retrievable (evidence-page skeleton, `03` §8.6)
4. **P2 — long-tail expansion**

Re-run the same 5–10 questions after changes (weekly for ecosystem building, at least one full cycle per month).
Track: mention rate, first-appearance position, citation-share delta.

## 3. The Competitor "Cited, We're Not" Post-Mortem

When the engine cites competitors but never you, read the cited sources and reverse-engineer why they won:

| What competitors have | Where it lives | What it proves |
|---|---|---|
| Product page + reviews (EN+CN content ecosystem) | Third-party review sites, blogs | They are IN the retrieval pool on both markets |
| Open-source standard + many tutorials (GitHub stars + CN tutorials) | CSDN / Juejin / GitHub / docs | Tutorial content = brand-mention density = retrieval wins |
| Chinese community / open-source projects | Zhihu / community sites | Native-language presence beats website language |
| Hardware reviews (e-commerce + review articles) | E-commerce sites, review blogs | Reviews are citations in disguise |

**The pattern**: every cited competitor has a **third-party content trail**. An engine doing live RAG can only cite
what its candidate pool contains — and the pool is built from the open web's mentions, not from your own site.
The website is the *fact anchor*; the ecosystem is the *citation source*. (1.37% rule, `11` §1.)

## 4. Content-Ecosystem Building Checklist (the Gate-1 fix)

| Channel | Content to create | Engine that reads it |
|---|---|---|
| **Tutorials** (CN: CSDN / Juejin; EN: Dev.to / Medium) | "How to add memory to your AI app" — the exact tutorial the audit shows competitors winning with | Doubao (ByteDance ecosystem), Tongyi, DeepSeek, ChatGPT |
| **Community discussions** (CN: Zhihu; EN: Reddit / HN) | Answer real questions, name your product naturally, no astroturfing | Perplexity (Reddit 46.7%), Doubao, Kimi |
| **Third-party reviews / comparisons** | Pitch reviewers; comparison articles ("A vs B") with same-dimension tables | All engines — comparison pages are the highest-value GEO asset |
| **Ranking / directory sites** (CN: maigoo / chinapp / cnpp; EN: G2 / Capterra) | Get listed — AI loves copying existing rankings | Cross-platform (see `11` §5) |
| **Official site** | Fact anchor only: definitions, facts, structured data, consistent wording | Nobody cites it directly, but it's where every mention links to |

**Discipline**:
- Every piece of ecosystem content must link back to the official site (the fact anchor) with consistent brand name/spelling.
- No duplicate identical posts across channels — same facts, different form per platform (`content-patterns` 一稿多投 rules).
- Never pay for or fake mentions; build real tutorials and reviews. Detection and penalties are the risk.
- If you have NO official site (e-commerce product, mini-program, offline brand): ecosystem building still works —
  `--no-site` mode; AI visibility mainly comes from external placements anyway (`11` §1).

## 5. Doubao (豆包) Specific Notes

Doubao = ByteDance ecosystem. Retrieval pool is heavily ByteDance content:

- **抖音图文/视频 is the main entry** (iesdouyin.com = 28.1% of Doubao App citations — see `11` §2)
- Toutiao (头条号) secondary; WeChat OA mainly serves Tencent Yuanbao, not Doubao
- Doubao App and Doubao web have different source pools — sample separately (Jaccard ~47% overlap)
- API note: Doubao's `/responses` + web_search requires the content plugin enabled in the Volcengine console;
  offline API measures parametric knowledge only (evidence grade B-offline, not A)

**The user-side fix is content-ecosystem building; the tech-side fix is maximizing "once retrieved, it gets cited" —
but you must enter the candidate set first.**

---

*Distilled from a real audit: "AI memory products" query on Doubao cited Noumi / Mem.ai / Supermemory / Mem0 /
OpenHuman / Obsidian+Engram — our brand absent because the Chinese content pool had zero mentions of it.*
