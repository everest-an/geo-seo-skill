# 11 · China GEO Playbook: Winning the Domestic AI-Search Market

> Data-backed playbook for Chinese AI search (百度 AI, 文心, 豆包, 千问, 元宝, Kimi, DeepSeek).
> Every number here is computed from the public **CN-GEO citation dataset** (187,818 deduplicated citations,
> 19,190 domain×platform rows, 12 platform endpoints; data v2.0.1, 2026-07-14).
> Upstream data: github.com/yaojingang/geo-citation-lab · Playbook distilled from the MIT-licensed GeoLook skill (github.com/aigclink/geolook).

## 1. The Number That Changes Resource Allocation: Official Sites = 1.37%

| Source category | Share of all CN citations | Domains |
|---|---:|---:|
| Content platforms (qq / toutiao / baidu / iesdouyin) | **16.4%** | 4 |
| General news media | **13.6%** | 68 |
| **Ranking / recommendation sites** | **9.1%** | **28** |
| **Brand official site / corporate site** | **1.37%** | 52 |

**Read**: in China's AI citation ecosystem, your official site is a **fact source, not a citation source**.
"Build a great website and AI will cite you" is a strategic misjudgment. 28 ranking-site domains alone eat 9.1%
of all citations — and occupy the most front-of-answer positions (see §4).

- Official site's real job: keep AI's *description of you* accurate (right industry, right facts, right wording), and give external sites a trustworthy landing page to link.
- Resource allocation: get the site to "crawlable + has definitions + has structured data + consistent wording", then **spend the remaining effort on external sources**.

## 2. Platform Ecosystem Bifurcation (CN-GEO computed, not anecdotal)

| Platform | Top-8 concentration | Own-ecosystem top source | What you must prepare |
|---|---:|---|---|
| **百度 AI** | **66.2%** | baidu.com **37.7%** | Baidu Baike / Baijiahao / Baidu Knows — skip them, you're basically out |
| **文心 (Ernie)** | **66.8%** | baidu.com **29.0%** | Same as above |
| **千问 (Tongyi)** | 61.0% | **sm.cn (Quark/Shenma) 19.2%** | **Optimizing Quark search coverage ≈ optimizing Tongyi** — most people miss this |
| **豆包 App** | 54.3% | iesdouyin.com **28.1%** | **Douyin image/text + video is the main entry** |
| **Kimi** | 47.9% | no own ecosystem (sohu 15.8%, cnblogs 9.1%) | Long reports, whitepapers, structured long-form; tech-community content |
| **豆包 web** | 46.0% | iesdouyin.com 12.0% | Same as App but more external-content opportunity |
| **腾讯元宝 (Yuanbao)** | 43.8% | qq.com **20.5%** | **WeChat Official Accounts, Tencent News** — Yuanbao's moat |
| **DeepSeek** | **21.8%** | **no own ecosystem, most neutral** | Full argumentation, traceable numbers, explicit boundaries; **content quality pays off most here** |
| **抖音 AI** | 100% | cites iesdouyin.com only | External content can't get in — **not worth investing in** |

Rule of thumb: the higher the concentration, the more closed the platform — you must play inside its ecosystem.
Low concentration (DeepSeek) competes on general content quality.

**Practical consequence**: publish each piece of content in at least three versions — official-site authoritative page
(long, complete, with schema), WeChat-article version (for Yuanbao / WeChat Search), vertical-community version (for 豆包 / 千问).

## 3. Web ≠ App: Measured, Not Fastidious

Same product, different endpoint, different source pool:

| Product | web domains | App domains | **Jaccard similarity** |
|---|---:|---:|---:|
| 千问 (Tongyi) | 1,036 | 677 | **24.5%** |
| 元宝 (Yuanbao) | 2,989 | 3,206 | **31.4%** |
| 豆包 (Doubao) | 2,701 | 2,283 | 47.3% |
| DeepSeek | 2,666 | 2,337 | 51.6% |

Tongyi web and App share only **24.5%** of their source domains — using web results to infer App performance is ~75% wrong.
Every platform+endpoint must be sampled and scored **separately**. Never merge them into one "mention rate".

## 4. Citation Position: Who Sits at the Front of the Answer

`average_quote_position` smaller = appears earlier = higher weight. Top of the list (sample ≥300):

| Domain | Avg position | Citations | Type |
|---|---:|---:|---|
| sm.cn | 5.31 | 6,501 | Search proxy (Alibaba) |
| **cnpp.cn** | 6.10 | 3,429 | **Ranking site** |
| **maigoo.com (买购网)** | 6.36 | 6,741 | **Ranking site** |
| **phb123.com (排行榜123)** | 7.12 | 437 | **Ranking site** |
| iimedia.cn (艾媒) | 7.27 | 379 | Industry research |
| **cnpp100.com** | 7.35 | 783 | **Ranking site** |

**Ranking sites dominate.** When AI answers "which is best / how to choose", the laziest move is to copy an existing ranking list.

## 5. External Source Priority (replaces all subjective ordering)

1. **Cross-platform layer** (covers all 11 platform endpoints; one investment, all platforms benefit)
   - Ranking/brand-directory sites: `maigoo.com`, `chinapp.com`, `cnpp.cn`, `phb123.com`, `cnpp100.com` — **highest ROI, most teams skip it**
   - Content platforms: `qq.com` (WeChat OA / Tencent News), `toutiao.com` (Toutiao account)
   - News media: `sohu.com`, `163.com`, `sina.cn`; consumer decisions: `smzdm.com`
2. **Platform-ecosystem layer** (pick by the platform you care about)
   - 百度 AI / 文心 → Baidu Baike, Baijiahao, Baidu Knows
   - 豆包 → Douyin posts & video, Toutiao
   - 元宝 → WeChat OA, Tencent News
   - 千问 → **Quark/Shenma search coverage**, Alibaba-family content
3. **Professional content layer** (tech / B2B products): `cnblogs.com`, `csdn.net`, `zhihu.com`, `zol.com.cn`, `36kr.com`; industry research `askci.com`, `iimedia.cn` (cited very early)
4. **Official site** — must-do, but don't expect citations from it (1.37%)

**Discipline**: the table above is the industry-wide picture; your industry may differ. After sampling, always read the report's
"Top AI-cited source domains" — **that is your industry's actual distribution map right now. Use it as truth.**

## 6. Content Engineering for CN (from the CN-GEO method layer)

**Write evidence pages, not opinion pages.** Every question you target, the page must have:

1. One directly-extractable definition sentence
2. 2–5 numbers with units and sources
3. One comparison block (table preferred)
4. One step block
5. Applicable + NOT-applicable scenarios ("who this isn't for" raises credibility)

Page skeleton:

```
Title: <the target question verbatim>
1. What is X (one-sentence definition + expansion)
2. Key numbers (3–5, each with source and date)
3. X vs Y (table, same dimensions)
4. How to (5 steps)
5. Applicable and not-applicable scenarios
6. FAQ (3–5)
7. Reference sources (real clickable links)
```

**Pure Q&A formatting gives no lift (measured −5.7%)** — the format isn't the point; definitions, numbers,
structure and on-topicness are. FAQ's only value is query recall: use real user phrasings, answer in the first sentence.

## 7. Sampling Discipline (evidence grades)

**Without raw answers / screenshots / sampling-environment records, it is not "real sampling".**

| Grade | Meaning |
|---|---|
| A | Manual/browser real sample, with answer text + source links |
| B | Reproducible API sample (note whether online) |
| C | Synthetic demo / inference |
| D | Pending review |

Rules:
- **API ≠ web.** DeepSeek's official API is offline — it tests parametric knowledge, not retrieval. Record separately, never merge.
- **Web ≠ App.** Each platform+endpoint is its own line.
- Minimum four metric layers: mention rate, first-position/Top-3 rate, description accuracy, citation quality (recall + precision). Mention rate alone severely overstates results.
- Default attribution: **"observed correlation"**. Higher confidence requires a baseline window + observation window + control prompt + competitor control + external-event log.
- Manual web sampling: fresh conversation per question, record environment (sandbox/incognito/clean profile = grade A; personal account = auto-downgraded to D), record "brand not mentioned" too — that's the most important data point.

## 8. Language & Region

- CN market: Simplified Chinese, real user phrasings ("XX 好用吗" "XX 和 YY 哪个好" "XX 多少钱") — no translationese.
- **Chinese prompts trigger weaker retrieval than English** (cross-platform: EN avg 11.68 citations vs CN 10.41; Google shows the biggest gap, 11.57 vs 7.53). For overseas, write native English content — don't expect Chinese pages to be translated and cited.
- US domain + English is still the dominant overseas arena (US = 82.70–86.76% of identifiable countries; EN = 82.90–95.07% of identifiable languages).

---

**Source notes**: CN-GEO dataset (github.com/yaojingang/geo-citation-lab, `03-cn-geo-citation-dataset`) — a static snapshot, not live monitoring; trends/sentiment/brand-recommendation rates are NOT usable, only source coverage and cross-platform consensus. Papers: arXiv 2607.15771 (CN generative search citations, Web/App differences), arXiv 2604.25707 (citation selection → absorption). Playbook distilled from the MIT-licensed **GeoLook** skill (github.com/aigclink/geolook).
