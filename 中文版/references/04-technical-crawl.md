# 04 · 技术层：AI 爬虫可访问性

> 内容再好，AI 爬虫进不来、读不懂，就永远不会被引用。
> 技术层是 GEO 的"地基中的地基"，对应 `AEO Foundations Architect` 的职责域。

## 1. AI 爬虫访问管理（robots.txt）

**关键 AI User-Agent：**

| 爬虫 | 归属 |
|------|------|
| GPTBot / OAI-SearchBot / ChatGPT-User | OpenAI（ChatGPT） |
| ClaudeBot / anthropic-ai / Claude-Web | Anthropic（Claude） |
| PerplexityBot | Perplexity |
| Google-Extended | Google（AI 训练；AI Overviews 走 Googlebot） |
| Applebot-Extended | Apple |
| CCBot | Common Crawl（通用语料） |
| Bytespider | ByteDance |

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

## 2. llms.txt（AI 友好的站点索引）

`llms.txt` 是新兴标准（类 robots.txt，见 https://llmstxt.org/），给 AI 一份结构化、机器可读的站点说明。**配置后品牌描述准确率约提升 24%**。

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
