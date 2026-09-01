# 06 · 监测与度量

> 你无法改进你看不见的东西。GEO 必须与 SEO 一样被量化追踪。

## 1. 关键指标

| 指标 | 说明 | 测量方式 |
|------|------|----------|
| **AI 引用率** | 内容被 AI 引用的频率 | GEO 监测工具 |
| **品牌提及** | AI 回答中的品牌出现次数 | 品牌监测工具 |
| **引用准确度** | AI 引用你的信息是否准确 | 人工核验 |
| **可见性分数** | AI 搜索结果中的整体可见性 | AI 排名工具 |
| **引用来源页** | 具体被引用的页面 | 流量分析 |

## 2. 监测工具

| 工具 | 定位 |
|------|------|
| **Semrush AI Visibility Toolkit / Enterprise AIO** | 品牌 AI 可见性、提及、引用、声量份额 |
| **Profound** | 多语言 AI 品牌可见性深度分析 |
| **Peec AI** | 品牌在 AI 搜索中的提及分析 |
| **Otterly.AI** | AI 搜索引擎排名追踪 |
| **OptimizeGEO** | AI 可见性分数、声量份额、情感（ISO 27001） |
| **Geol.ai** | 自动化监测 + 50 因子评分引擎 + CMS 集成 |
| **Prompt Monitor** | 提示词级 AI 搜索性能分析 |
| **Brand24 / Mention / Brandwatch** | 全网品牌监测 |

（完整工具生态见 `08-tools-resources.md`）

## 3. GA4 追踪 AI 推荐流量

**目标**：在 GA4 中单独识别 AI 来源的推荐流量。

**做法**（自定义渠道分组）：

1. GA4 → 管理 → 数据显示 → 渠道分组
2. 新增渠道"AI 推荐流量"
3. 条件：来源 → 匹配正则 → 粘贴下方正则
4. 将 AI 流量组移到 Referral 组**上方**
5. 保存并应用到所有获取报告

```regex
.*(chatgpt\.com|openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|bard\.google\.com|you\.com|search\.brave\.com|copilot\.microsoft\.com|grok\.com|doubao\.com|kimi\.moonshot\.cn|kimi\.com|chat\.deepseek\.com|chatglm\.cn|yuanbao\.tencent\.com|tongyi\.aliyun\.com|tongyi\.com|yiyan\.baidu\.com|metaso\.cn|n\.cn|quark\.cn|sm\.cn).*
```

## 4. 归因链路：从「被引用」到「带来业务结果」

> 可见性指标（提及率/引用份额）说明你进了 AI 的答案；归因层回答下一个问题：
> **AI 的答案有没有把人送到你的站上、这些人有没有转化。**
> 来自 GeoLook skill（MIT，github.com/aigclink/geolook）。

```
用户问 AI → 答案引用你 → 用户点击引用链接 → 落地页 → 注册/咨询/下单
            （采样可测）      （referrer/UTM 可测）    （事件 + 来源快照可测）
```

三段各自能测、各自会漏，**不能互相替代**：

1. **采样**测「答案里有没有你」——上游供给
2. **Referrer/UTM** 测「AI 带来了多少会话」
3. **转化事件 + 来源快照**测「这些会话值多少钱」——落在你的业务系统里

### AI 引擎来源域名清单

> 配置前先在**自己的服务器日志/GA4 里核对**——各家 App 的 referrer 策略随时会变，
> 且 App 内打开经常不带 referrer（见下方「测的是下界」）。

| 引擎 | 常见 referrer 域名 | 备注 |
|---|---|---|
| ChatGPT | `chatgpt.com`、`chat.openai.com` | 网页版带 referrer |
| Perplexity | `perplexity.ai` | 引用点击率相对高 |
| Gemini | `gemini.google.com` | |
| Copilot | `copilot.microsoft.com`、`bing.com` | bing.com 混杂传统搜索 |
| Claude | `claude.ai` | |
| Grok | `grok.com` | |
| 豆包 | `doubao.com` | App 流量大部分无 referrer |
| Kimi | `kimi.moonshot.cn`、`kimi.com` | |
| DeepSeek | `chat.deepseek.com` | |
| 智谱清言 | `chatglm.cn` | |
| 腾讯元宝 | `yuanbao.tencent.com` | |
| 通义 | `tongyi.aliyun.com`、`tongyi.com` | |
| 文心一言 | `yiyan.baidu.com` | 百度AI搜索的点击多数仍从 `baidu.com` 来，难与传统搜索区分 |
| 秘塔 | `metaso.cn` | |
| 纳米AI | `n.cn` | |
| 夸克 | `quark.cn`、`sm.cn` | sm.cn 混杂传统搜索 |

> 未列出 ≠ 不存在。任何新引擎先抓一段自己的日志看 `Referer` 头再加进清单。

### 三条配置动作

1. **GA4 / 分析工具**：建「AI 来源」自定义渠道组，用上面的升级正则（已含国内引擎）。
2. **服务器日志**：grep 比 GA4 可靠——不受前端拦截、广告屏蔽影响，还能看到 AI 爬虫自己的抓取行为
   （UA 含 GPTBot / ClaudeBot / PerplexityBot——抓取变多通常先于引用变多，是个前置信号）：
   ```bash
   grep -iE "chatgpt\.com|perplexity\.ai|gemini\.google|claude\.ai|doubao\.com|kimi\.|deepseek|chatglm|yuanbao\.tencent|metaso" access.log | wc -l
   ```
3. **转化事件保存来源快照**：归因优先级 **点击 ID > UTM > referrer > 直接/未知**。
   在注册/留资/下单事件里把「首次触点 + 末次触点」的来源存进业务库。

### 纪律：测的是下界，不许外推

- App 内打开、隐私策略、跨设备都会吃掉 referrer——**测到的 AI 流量是下界**，
  报告里写「可归因的 AI 会话 ≥ N」，不写「AI 带来了 N」
- AI 来源会话通常绝对量小、意图深——先看转化率而不是会话数，样本小于三位数时不下结论
- 不要为了归因给公开内容链接堆 UTM 参数：带参 URL 被 AI 引用后会稀释规范 URL 的引用份额。
  **UTM 只用在你完全可控且不会被引擎收录的位置**（邮件、私域）；公开阵地靠 referrer 归因

## 5. 各引擎 AI 引用与谷歌重叠度（定位优先级）

| 平台 | 域名重叠（vs Google Top10） | 特点 |
|------|------------------------------|------|
| Perplexity | 91% | 最贴近谷歌 Top10，最像传统 SEO |
| Google AI Overviews | 86% | 深度依赖谷歌传统索引 |
| Google AI Mode | 54% | 更独立检索 |
| ChatGPT | 最低 | 偏 Bing 排序，引用 21 位之后的页面 |

## 6. 监测工作流

```
内容发布 → AI 爬虫索引 → 监测 AI 引用 → 分析引用质量 → 优化内容 → (回到发布)
```

**实践节奏**：
- **短期（48h）**：GSC 盯抓取频率、平均排名、CTR；第 24h 手动请求重索引。
- **中期（周/月）**：追踪 AI 引用率、品牌提及、AI 推荐流量。
- **长期（季度）**：声量份额（Share of Voice）对比竞品、情感分析、引用准确度。

## 7. 预警信号

| 信号 | 含义 | 动作 |
|------|------|------|
| 抓取量突升 | 引擎"感兴趣" | 保持内容新鲜，趁热补强 |
| 排名进前 10 但 CTR 低 | 标题/描述吸引力不足 | 改 Meta，用数字 + 情绪词 |
| AI 引用为零但排名尚可 | 可提取性/权威不足 | 回查 `03` + `04` + `05` |
| 引用不准确 | 内容被误解 | 优化实体命名、定义清晰化 |
