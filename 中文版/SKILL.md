---
name: geo-seo
description: 全面的 GEO（生成式引擎优化）+ SEO 体系。Use when 优化内容让 AI 搜索引擎引用/推荐、提升搜索排名、做 AI 可见性、信息增益、结构化内容、llms.txt、AI 爬虫配置、GEO 审计或监测、多语言/国际 SEO、hreflang、canonical、inLanguage、og:locale。触发词：GEO、生成式引擎优化、Generative Engine Optimization、AEO、答案引擎优化、AI 搜索优化、AI SEO、让 AI 引用、AI Overviews 优化、ChatGPT/Perplexity/Gemini/Claude 引用、内容排名、信息增益、topical authority、llms.txt、多语言 SEO、hreflang。
metadata:
  version: 1.0.0
  category: marketing/seo
  language: zh-CN
---

# GEO + SEO 全面优化体系

> 让内容既被**传统搜索引擎收录排名**，又被 **AI 答案引擎引用推荐**。
> 核心逻辑：AI 引擎从互联网的同一张网抓取信息，你做扎实的 SEO 就是 GEO 成功的一半；GEO 是"成为答案的一部分"，而非"抢占排名第一位"。

## 何时使用本体系

- 想让内容出现在 ChatGPT / Perplexity / Gemini / Claude / Google AI Overviews 的回答与引用中
- 做传统 SEO（关键词、技术、内容、外链）并希望叠加 AI 可见性
- 内容上线后排名停滞、点击率低、AI 引用为零
- 需要竞品拆解、AI 可读性重构、技术扫障、GEO 监测
- 审计站点的 AI 爬虫可访问性、llms.txt、结构化数据

## 体系全景（六层金字塔）

```
                ┌─────────────────────────────┐
                │  ⑥ 监测与迭代（GSC + GEO工具）│
                ├─────────────────────────────┤
                │  ⑤ 权威与实体（E-E-A-T、品牌提及）│
                ├─────────────────────────────┤
                │  ④ 技术层（AI爬虫、llms.txt、Schema）│
                ├─────────────────────────────┤
                │  ③ 内容引用优化（可提取、信息增益）│
                ├─────────────────────────────┤
                │  ② 传统 SEO 地基（技术+内容+外链）│
                ├─────────────────────────────┤
                │  ① GEO 认知基础（版图、检索因子）│
                └─────────────────────────────┘
```

## 核心工作流（四步极速打法 · 骨架）

这是从实战沉淀出的、可在 **48 小时**内把页面排名大幅拉升的标准化动作（完整版见 `references/02-rapid-method.md`）：

| 步骤 | 动作 | 工具/引擎 | 产出 |
|------|------|-----------|------|
| **① 拆** | 竞品拆解，挖信息盲区（Information Gain） | ChatGPT / Claude | 差异点 + 盲区清单 |
| **② 构** | 重构页面为"AI 最爱格式" | Claude / Gemini | 可提取、易引用的页面 |
| **③ 扫** | 技术扫障（死链/重复Meta/H1/sitemap） | ScreamingFrog | 技术健康 |
| **④ 追** | 48 小时极速追踪与重索引 | Google Search Console | 排名跃升 + 流量 |

**记忆口诀**：`拆 → 构 → 扫 → 追`（先挖盲区，再塑格式，后清障碍，终做追踪）。

## 引用文档索引

| 文件 | 内容 | 何时查阅 |
|------|------|----------|
| `references/01-foundations.md` | GEO 基础、SEO/GEO/AEO 对比、AI 引擎版图、RAG 检索因子、核心数据 | 建立认知、回答"GEO 是什么/为什么" |
| `references/02-rapid-method.md` | 四步极速打法全文（含每步的具体指令） | 执行 48 小时快速拉排名 |
| `references/03-content-citation.md` | 内容与引用优化、FAST 框架、信息增益、可提取结构、易引用内容类型 | 写/改内容时 |
| `references/04-technical-crawl.md` | AI 爬虫 robots.txt、llms.txt、Schema/JSON-LD、SSR、技术 GEO 清单 | 处理技术层、AI 可访问性 |
| `references/05-authority-entities.md` | E-E-A-T、实体建设、品牌提及、外部信号、Wikipedia/UGC | 建立权威与品牌 AI 提及 |
| `references/06-monitoring.md` | 指标、监测工具、GA4 AI 流量设置、监测工作流 | 追踪效果、验证是否被引用 |
| `references/07-prompt-library.md` | 可直接复制的提示词（竞品拆解/AI重构/内容优化/GEO审计） | 需要现成 prompt 时 |
| `references/08-tools-resources.md` | 研究论文、工具清单、案例库、参考链接 | 找工具、引用数据、看案例 |
| `references/09-i18n-seo.md` | 多语言/国际 SEO：hreflang、locale canonical、sitemap、inLanguage、og:locale、本地化 metadata、多语言 llms.txt | 运营多语言站点（如 /en /zh-CN /ja） |
| `references/11-cn-geo-playbook.md` | 国内 GEO 实战：官网仅占引用 1.37%、平台生态割据、Web≠App 采样、外部信源优先级、国内证据等级 | 做国内 AI 搜索 GEO（百度/豆包/千问/元宝/Kimi/DeepSeek） |

## 自动化工具（Scripts）

纯 Python 3 标准库、零依赖的校验脚本（位于 `scripts/`，用 `py scripts/<脚本>.py` 运行）：

| 脚本 | 用途 | 用法 |
|------|------|------|
| `scripts/geo_audit.py` | GEO 就绪度审计 — FAST 框架、可提取性、引用信号、基础 SEO | `py scripts/geo_audit.py <文件\|目录\|URL> [--json] [--min-cjk]` |
| `scripts/i18n_audit.py` | 多语言 SEO 审计 — hreflang（覆盖/x-default/BCP-47/双向）、canonical、sitemap 变体、inLanguage、og:locale、llms.txt | `py scripts/i18n_audit.py <目录> --base-url https://... [--sitemap 路径] [--llms-txt 路径]` |
| `scripts/llms_txt.py` | 生成符合 llmstxt.org 规范的 `/llms.txt`（按 locale 分组） | `py scripts/llms_txt.py --name "X" --site-url https://... --summary "..." --pages "URL \| 描述" ...` |

全部脚本离线可用（本地 HTML/XML 文件），传 URL 才走网络；`--json` 输出机器可读报告。

## 快速决策指南

- **"为什么我的内容 AI 不引用？"** → 先看 `03-content-citation.md`（可提取性 + 信息增益），再看 `04-technical-crawl.md`（AI 爬虫是否被拦）。
- **"想快速拉排名"** → 直接走 `02-rapid-method.md` 四步法。
- **"想建立长期 AI 品牌声量"** → `05-authority-entities.md` + `06-monitoring.md`。
- **"要现成提示词"** → `07-prompt-library.md`。
- **"要数据支撑/工具选型"** → `08-tools-resources.md`。
- **"多语言站点（hreflang / locale URL / inLanguage）"** → `09-i18n-seo.md` + `i18n_audit.py`。
- **"国内市场 / 中文 AI 搜索（百度/豆包/千问/元宝/Kimi/DeepSeek）"** → `11-cn-geo-playbook.md`。

## 铁律（Anti-Patterns）

- ❌ 只为 AI 优化而牺牲人类阅读体验（引文堆砌、无实义的空格式）——长期必反噬。
- ❌ 堆砌关键词 / 关键词填充——GEO 论文明确反效果。
- ❌ 让 AI 爬虫被 robots.txt 拦截却指望被引用——先确认访问权。
- ❌ 内容无日期、无作者、无来源——AI 无法判断可信度，拒绝引用。
- ✅ 做"最清晰、最权威、最易提取"的那个答案，而非"排名第一的那个页面"。
