# 04 · 技术层：AI 爬虫可访问性

> 内容再好，AI 爬虫进不来、读不懂，就永远不会被引用。
> 技术层是 GEO 的"地基中的地基"，对应 `AEO Foundations Architect` 的职责域。

## 1. AI 爬虫访问管理（robots.txt）

**完整 AI 爬虫矩阵**（14 个 User-Agent，2026 年最新）：

| 爬虫 | 归属 | 用途 | 遵守 robots.txt？ |
|------|------|------|-------------------|
| GPTBot | OpenAI | ChatGPT 网页搜索 | 是 |
| OAI-SearchBot | OpenAI | OpenAI 搜索功能 | 是 |
| ChatGPT-User | OpenAI | ChatGPT 浏览（用户触发） | **否**（用户触发） |
| ClaudeBot | Anthropic | Claude 网页功能 | 是 |
| anthropic-ai | Anthropic | Claude 训练 | 是 |
| PerplexityBot | Perplexity | Perplexity AI 搜索 | 是 |
| CCBot | Common Crawl | 训练数据（常被拦截） | 是 |
| Bytespider | ByteDance | TikTok/抖音 AI | 是 |
| cohere-ai | Cohere | Cohere 模型 | 是 |
| Google-Extended | Google | Gemini/Vertex 训练与 grounding 退出机制 | 是 |
| Google-CloudVertexBot | Google | 站点主请求的 Vertex AI Agent 抓取 | 是 |
| Google-Agent | Google | 代理式浏览（Project Mariner），替用户行动 | **否**（用户触发） |
| Google-NotebookLM | Google | 抓取用户添加的来源 URL | **否**（用户触发） |
| Google Messages | Google | 用户触发抓取 | **否**（用户触发） |

**推荐配置（想被 AI 引用就放行）：**

```robots.txt
# 允许主流 AI 搜索爬虫（影响实时 AI 回答/引用）
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /

# 允许 AI 训练爬虫（影响未来模型训练语料）
User-agent: CCBot
Allow: /
User-agent: anthropic-ai
Allow: /
User-agent: Bytespider
Allow: /
```

**策略决策：**

| 策略 | 适用 |
|------|------|
| 全放行 | 想被 AI 引用 + 进入训练语料 |
| 只拦训练爬虫（如 GPTBot） | 想被实时引用，但不想被训练 |
| 选择性 | 按平台策略分别配置 |

> **用户触发的抓取器天然无视 robots.txt**（Google-Agent、Google-NotebookLM、Google Messages、ChatGPT-User）。robots.txt 拦不住它们——需用服务端访问控制。新动向：**Web Bot Auth**（RFC 9421）让机器人通过 `Signature-Agent` 头 + 密钥目录认证（Google-Agent 已采用）；反向 DNS 验证仍是兜底手段。

### robots.txt 必须按 RFC 9309 语义判，不是逐行正则

逐行正则会漏三种真实封禁（GeoLook 方法层）：

1. **`User-agent: * / Disallow: /` 会封掉所有没有专属组的 AI 爬虫**——最常见的"无意封禁"
2. **多个 `User-agent` 行共享一组规则**——逐行正则会把第一个 UA 判成空规则
3. **specificity 不看顺序**：专属组存在时通配符组整组失效——`User-agent: GPTBot / Allow: /`
   会让 GPTBot 无视通配符组里的任何 `Disallow`

**robots 放行 ≠ 真放行。** WAF/CDN（Cloudflare Bot Fight、阿里云 WAF 等）可能对 AI 爬虫 UA 单独返回 403，
浏览器里一切正常，站长自己看不出来。用 GPTBot / ClaudeBot / PerplexityBot / Bytespider 的真实 UA
抓一次首页做差异探测（GeoLook crawl.py 的 `ai_ua_probe`）。

**llms.txt 只有指向可抓取的有效页面才有意义。** 指向 404 或被 robots 封禁的路径等于递给 AI 一份坏地图，
抽样验证其中链接。

## 2. llms.txt（AI 友好的站点索引）

`llms.txt` 是新兴标准（类 robots.txt，见 https://llmstxt.org/），给 AI 一份结构化、机器可读的站点说明。

> **证据核查（2026 年更新）：** 谷歌官方 AI 优化指南明确表示谷歌搜索**忽略** `llms.txt`——对排名或 AI 可见性既无帮助也无损害。John Mueller 称其发现场景是"死胡同"；Gary Illyes 确认谷歌无支持计划。SE Ranking 30 万域名研究发现 AI 引用 Top 50 域名中**只有 1 个**有 llms.txt；OtterlyAI 服务器日志显示仅 **0.1%** 的 AI 机器人请求指向它。**但仍建议发布**：Cursor、Claude Code 等 AI 编码代理越来越多地消费它（对文档站是净收益），对非谷歌系统是零成本的选择权。绝不要把它宣传为谷歌排名或引用杠杆。

- 放在站点根路径 `/llms.txt`（生产域名）。
- 精简列出高价值稳定页面，而非堆 URL。
- 可选的 `llms-full.txt` 提供全量内容（仅在能保持更新时使用）。

```markdown
# 品牌名

> 1–3 句话的品牌/业务简介。

## Contact
- Website: https://example.com
- Email: hello@example.com

## Services
- [服务1](https://example.com/service-1): 简述
- [服务2](https://example.com/service-2): 简述

## Key Information
- [关于我们](https://example.com/about)
- [文档](https://example.com/docs)
```

> 注意：`llms.txt` **不替代** `robots.txt` 的抓取控制；两者各司其职。

## 3. 结构化数据（Schema / JSON-LD）

Schema 帮助 AI 精确理解内容类型与实体。Google 推荐 JSON-LD 格式。

**推荐类型**：Article、FAQPage、HowTo、Product、Organization、Person、BreadcrumbList、Speakable（语音）。

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "标题",
  "author": { "@type": "Person", "name": "作者名", "url": "作者主页" },
  "datePublished": "2026-01-01",
  "dateModified": "2026-08-01",
  "publisher": { "@type": "Organization", "name": "机构名" }
}
```

## 4. 服务端渲染（SSR）与 AI 爬虫

- AI 爬虫大多**不执行 JavaScript**。
- 依赖客户端渲染（CSR）的内容对 AI 可能**不可见**。
- 核心信息必须落在**初始 HTML**；必要时上 SSR / SSG / 预渲染。

## 5. 实体解析与语义信任

| 技术 | 说明 |
|------|------|
| **实体解析** | 内容中一致命名、消歧、链到权威来源，让 AI 精确识别实体 |
| **语义信任机制** | 强事实背书、引用可信研究、展示专业度（超越传统外链，靠内容内在可信） |
| **RAG 适配** | 模块化内容、清晰标题与摘要，让关键信息易被检索与合成 |

## 6. 产品信息源（Product Feed）

结构化产品数据能提升 AI 商品引用：

| 平台 | 提交方式 |
|------|----------|
| Google | Google Merchant Center |
| Microsoft | Microsoft Merchant Center（驱动 Copilot 商品结果） |
| ChatGPT | 产品发现注册（待开放） |

## 7. 技术 GEO 清单

- [ ] 实现 Schema.org 结构化数据（JSON-LD）
- [ ] 优化加载速度（< 2.5s）
- [ ] 移动端友好
- [ ] 语义化 HTML（H1–H6 正确层级、每个页面仅 1 个 H1）
- [ ] XML sitemap 生成并提交
- [ ] robots.txt 放行 AI 爬虫
- [ ] 创建 `/llms.txt`
- [ ] 全站 HTTPS
- [ ] 图片 alt 文本
- [ ] 关键内容 SSR / 初始 HTML
- [ ] 修复 4xx/5xx 死链（> 5 条即拉低质量分）
- [ ] 消除重复 Meta 描述（> 10 页共享即触发低质量惩罚）
