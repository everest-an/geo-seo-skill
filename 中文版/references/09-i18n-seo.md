# 09 · 国际 SEO（多语言 / i18n）

> 针对多语言站点（如 `/en`、`/zh-CN`、`/ja`）：每个语言版本必须**独立可索引**、正确映射到自己的 locale，并对谷歌和 AI 引擎都机器可读。本模块覆盖三语言内容站点的完整审计清单。

## 1. URL 结构

**原则**：一语言一 URL，自我索引，带清晰 locale 前缀。

- 使用 locale 前缀路径：`/en/...`、`/zh-CN/...`、`/ja/...`
- 各 locale 保持相同路径形态，使每个页面恰好有 N 个语言版本、全部可索引
- 避免域/子域混用（如 `example.com/zh` 与 `zh.example.com` 混排）——选定一种方案
- 保持关键词/意图对等：各 locale 同名 URL 指向同一意图

## 2. hreflang

### layout 级（全站）
在每个页面模板上声明语言关系，使全站三语言**双向 + x-default**：

```html
<link rel="alternate" hreflang="en" href="https://example.com/en/page" />
<link rel="alternate" hreflang="zh-CN" href="https://example.com/zh-CN/page" />
<link rel="alternate" hreflang="ja" href="https://example.com/ja/page" />
<link rel="alternate" hreflang="x-default" href="https://example.com/en/page" />
```

### 详情页级
每个内容页（如 719 篇 × 4 标签）：输出**全部 4 标签（3 语言 + x-default）**，**双向**（含自引用：每页列出所有语言，包括自己）。

**必须成立的规则：**
- 双向：A 声明 B，B 必须反向声明 A
- 自引用：页面始终声明自己
- x-default 指向最合理的回退版本（通常是全局 `/en` 版）
- hreflang 必须合法 BCP-47（如 `zh-CN`，而非 `zh_cn`）
- hreflang URL 必须无重定向可访问；使用直接 canonical URL

## 3. canonical

- **locale-self canonical**：每个 locale 页面 canonical 指向**自己的 URL**（`/en/page` → `/en/page`，`/zh-CN/page` → `/zh-CN/page`）。
- 绝不要把 UI locale 变体统一 canonical 到单一全局 URL——那会合并掉独立语言索引。
- canonical 与 hreflang 保持一致：canonical 是"语言无关的自身"，hreflang 是跨语言映射。

## 4. sitemap

- **每个 locale 变体**单独条目（例如含 `/en` 前缀的 776 条 URL）。
- 每条使用最终 canonical locale URL。
- 可选：sitemap 条目内加 `xhtml:link` alternates 佐证；基本要求是全部变体可被发现。
- locale 扩展后在 GSC 重新提交。

## 5. Schema `inLanguage`

每个内容页声明语言，防止 AI 引擎混淆 locale：

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "…",
  "inLanguage": "en",
  ...
}
```

- 全部 719 篇内容加 `inLanguage`（Article、FAQPage、HowTo、Product 等）
- `inLanguage` 与 URL locale 完全一致（`en` / `zh-CN` / `ja`）
- FAQPage/HowTo 顶层同样设置 `inLanguage`

## 6. Open Graph locale

```html
<meta property="og:locale" content="zh_CN" />
<meta property="og:locale:alternate" content="en_US" />
<meta property="og:locale:alternate" content="ja_JP" />
```

- `og:locale` 与页面语言一致；alternates 列出其他语言
- 与 hreflang、inLanguage 保持一致，避免混合信号

## 7. 本地化 metadata（原生关键词）

- 每语言用**原生关键词**写标题/Meta 描述——绝不机翻英文文案
- 每语言关键词研究不同（如日式查询风格、中文变体表达）
- 使用符合 locale 习惯的术语（不只是翻译词）
- 本地化元数据现在也叠加 AI 优化：前 40 字符内前置问题、数字与明确答案

## 8. llms.txt 多语言段

提供多语言感知的 `/llms.txt`，让 AI 引擎找到各语言内容：

```markdown
# 品牌名

> 1–3 句业务简介。

## Contact
- Website: https://example.com
- Email: hello@example.com

## English
- [About](https://example.com/en/about): 摘要 …
- [Docs](https://example.com/en/docs): …

## 中文 (zh-CN)
- [关于我们](https://example.com/zh-CN/about): …
- [文档](https://example.com/zh-CN/docs): …

## 日本語 (ja)
- [概要](https://example.com/ja/about): …
- [ドキュメント](https://example.com/ja/docs): …
```

- 按 locale 分组链接；摘要用各语言撰写
- 仅当能保持各 locale 更新时才提供 `/llms-full.txt`

## 9. GEO 视角：AI 引擎与多语言内容

- AI 引擎按**查询语言**匹配内容语言；各 locale 内容 + 一致 metadata 会在各自语言池内被引用。
- **跨语言实体一致性**：品牌/实体名称、描述、关系在各 locale 完全一致——AI 视其为同一实体（见 `05-authority-entities.md`）。
- UGC 与权威信号是语言敏感的：在各自语言市场赢得提及（英文 Reddit/Quora、中文知乎、日文note 等）。
- AI 爬虫（GPTBot、ClaudeBot、PerplexityBot）按 locale 遵循 robots.txt；任何 locale 都不要拦截，否则放弃引用。
- 各 locale 也应有自己的 AI 就绪结构（`03-content-citation.md` 的 FAST 框架）——结构在所有语言都有效。

## 10. 完整 i18n SEO 审计清单

- [ ] locale 前缀 URL：`/en`、`/zh-CN`、`/ja` 独立可索引
- [ ] layout 级 hreflang：三语言双向 + x-default
- [ ] 详情页级 hreflang：每页 × 4 标签（3 语言 + x-default）
- [ ] canonical：每页 locale-self
- [ ] sitemap：全部 locale 变体列入（如 `/en` 前缀条目）
- [ ] 每篇内容 Schema `inLanguage`
- [ ] 每页 `og:locale` + `og:locale:alternate`
- [ ] 原生本地化 metadata：per-locale 关键词（拒绝机翻）
- [ ] llms.txt 多语言段（per-locale 分段）
- [ ] 跨语言实体一致性（名称、描述）
- [ ] 每个 locale 放行 AI 爬虫
- [ ] per-locale AI 可读结构（FAST）已验证
