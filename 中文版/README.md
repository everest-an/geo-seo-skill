# geo-seo-skill（中文版）

> **一套完整的 GEO（生成式引擎优化）+ SEO 体系，作为 opencode skill 提供** —— 让你的内容既被谷歌排名，又被 ChatGPT、Perplexity、Gemini、Claude 引用。包含实战验证的**四步极速打法**（48 小时排名 #18 → #3，流量 +320%），以及开箱即用的**审计脚本**（GEO 就绪度 + 多语言 hreflang SEO）。

> 本目录为中文备份；英文主版见仓库根 `README.md` 与 `.opencode/skills/geo-seo/`。

**TL;DR —— 什么是 GEO？**
生成式引擎优化（GEO）是让内容被 AI 答案引擎选择并引用的优化方法。**SEO 竞争排名；GEO 竞争成为答案的一部分。** 本体系把两者整合为一套系统。

---

## 为什么要做 GEO（数据支撑）

AI 搜索改变了用户获取答案的方式——AI 引擎正在蚕食传统 SEO 赢得的搜索流量：

| 信号 | 数值 | 来源 |
|------|------|------|
| AI 概览吃掉自然点击率 | ~68% | 实战观察 |
| 符合 AI 标准的引用提升 | +44% | 实战观察 |
| 含引用/统计的内容 | AI 可见性 +30–40% | Princeton GEO 论文（arXiv 2311.09735） |
| ChatGPT 占 AI 推荐流量 | 85.79% | Semrush |
| AI 回答提及品牌比例 | 占查询的 26–39% | Semrush |

**一句话记住**：清晰、结构化、易提取的内容才会被引用——AI 引用的是"最清晰、最权威、最易提取的答案"，而不是"排名第一的页面"。

---

## 内容构成

覆盖全栈的六层体系，从 GEO 基础到技术执行到监测：

```
references/
├── 01-foundations.md           # GEO 基础、SEO/AEO/GEO 对比、AI 引擎版图、RAG 检索因子
├── 02-rapid-method.md          # ★ 四步极速打法（拆 → 构 → 扫 → 追）
├── 03-content-citation.md      # 信息增益、可提取性、FAST 框架
├── 04-technical-crawl.md       # AI 爬虫 robots.txt、llms.txt、Schema/SSR、实体
├── 05-authority-entities.md    # E-E-A-T、实体建设、品牌提及
├── 06-monitoring.md            # 指标、工具、GA4 AI 流量设置
├── 07-prompt-library.md        # 10 个可复制提示词
├── 08-tools-resources.md       # 论文、工具生态、案例库
└── 09-i18n-seo.md              # 多语言 SEO（hreflang、inLanguage、llms.txt i18n）
```

## 快速上手

1. **48 小时拉排名** → 打开 `references/02-rapid-method.md`，执行 `拆 → 构 → 扫 → 追`。
2. **为什么 AI 不引用我？** → 先查 `03`（可提取性 + 信息增益），再查 `04`（AI 爬虫是否被拦）。
3. **多语言站点（/en /zh-CN /ja）？** → `09-i18n-seo.md` + `i18n_audit.py` 脚本。
4. **需要现成提示词？** → `07-prompt-library.md`。

## 自动化脚本（零依赖，仅标准库）

```bash
# GEO 就绪度审计（FAST 框架 + 引用信号）—— HTML 文件、目录或 URL
py scripts/geo_audit.py <文件|目录|URL> [--json]

# 国际 SEO 审计 —— hreflang 覆盖/x-default/BCP-47/双向、
# canonical、sitemap 变体、inLanguage、og:locale、llms.txt
py scripts/i18n_audit.py <目录> --base-url https://example.com [--sitemap sitemap.xml] [--llms-txt llms.txt]

# 生成符合规范的 /llms.txt（按 locale 分组）
py scripts/llms_txt.py --name "我的品牌" --site-url https://example.com --summary "..." \
    --pages "https://example.com/zh-CN/guide | 指南" ...
```

三个脚本均为纯 Python 3 标准库——无需 pip 安装。`--json` 输出机器可读报告。

## 如何安装为 opencode skill

1. 复制（或 clone）本仓库的 `.opencode/skills/geo-seo/` 到你的项目，或在 `opencode.json` → `skills.paths` 添加路径。
2. 重启 opencode（skill 在启动时加载）。
3. 自动触发词：GEO、生成式引擎优化、AEO、AI SEO、让 AI 引用、AI Overviews、llms.txt、hreflang、多语言 SEO、内容排名。

## FAQ

**GEO 会取代 SEO 吗？**
不会——GEO 是 SEO 的补充。AI 引擎从同一张网抓取信息，扎实的 SEO 就是 GEO 成功的大部分。

**什么内容最容易获 AI 引用？**
原创数据、权威定义、步骤式指南、对比表格、FAQ 区块。引用与统计让 AI 可见性提升 30–40%。

**llms.txt 真的有用吗？**
配置了规范的 `/llms.txt` 的站点，品牌描述在 AI 回答中的准确率提升约 24%。它是新兴标准（llmstxt.org）——成本低，值得做。

**能在多语言站点上用吗？**
可以——`references/09-i18n-seo.md` 覆盖 hreflang、locale-self canonical、`inLanguage`、`og:locale`、多语言 `llms.txt`，`i18n_audit.py` 可自动校验全部项目。

**这是给人用还是给 AI 用的？**
两者皆是。技能以 AI 编码代理（opencode）为主编写，但每份参考文档对人工 SEO 团队同样可读可用。

## License

MIT —— 免费使用、修改与分发。欢迎引用、点赞（star）。

---

*源自一次真实实验：一个零外链、零 PR 的老域名，仅靠 AI 驱动的 GEO 在 48 小时内从谷歌第 18 位跃升至第 3 位——搜索流量暴涨 320%。*
