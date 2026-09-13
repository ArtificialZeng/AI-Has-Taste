# Referee 定向 novelty 检索日志

截止日期：2026-08-29（Asia/Shanghai）  
检索角色：Gate 5 独立 referee。搜索引擎仅用于定位原始或正式记录；
下列结论只以 arXiv、DataCite、OpenAlex、Semantic Scholar、DBLP、原论文
及作者公开 CV 为证据。

## 冻结的待核主张

| ID | 待核主张 | 类型 |
|---|---|---|
| N1 | 原论文的展示矩阵与本项目矩阵逐项相同 | exact |
| N2 | 原论文只给出实数域数值证据，并把实数解析证明列为开放问题 | exact |
| N3 | 截止日期前 arXiv 是否有后续版本、更正或替代发表记录 | exact metadata |
| N4 | 正式引文数据库是否记录了引用该论文的后续工作 | database-bounded |
| N5 | 有限检索中是否已经出现该矩阵的显式有理分解或实数域解决 | database-bounded |

“未找到”在本日志中始终只表示：在列出的数据库、查询、日期和返回结果
范围内未找到；它不是数学上的绝对 novelty 证明。

## 原论文与版本记录

### 2026-08-29 — arXiv 题录和 v1 全文

- 查询/URL：[`arXiv:2508.14901`](https://arxiv.org/abs/2508.14901)
- 结果：题名为 *Computational Resolution of Hadamard Product
  Factorization for \(4\times4\) Matrices*，作者 Igor Rivin；submission
  history 只列 `[v1] Thu, 31 Jul 2025 21:00:28 UTC`。
- 原文位置：v1 PDF 第 3 页 Example 5（PDF 文本行 87--98）给出的四行
  正是
  `1111 / 1110 / 0100 / 1000`，所以 N1 通过。
- 原文位置：摘要与 §4.3 明说对 \(\mathbb R\) 是 “strong numerical
  evidence”；§7.1(4) 要求 “Find analytical proofs for the real case”。
  因而 N2 通过；原论文没有实代数不可行证书。
- 原文的实数结论边界：[`v1 PDF`](https://arxiv.org/pdf/2508.14901v1)，
  [`v1 HTML`](https://arxiv.org/html/2508.14901v1)。

### 2026-08-29 — arXiv API 定向查询

1. 查询：
   [`all:"Hadamard product factorization" AND all:"rank-2"`](https://export.arxiv.org/api/query?search_query=all%3A%22Hadamard%20product%20factorization%22%20AND%20all%3A%22rank-2%22&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending)
   
   返回 `totalResults=1`，唯一结果为 `2508.14901v1`。

2. 查询：
   [`ti:"Hadamard Product Factorization"`](https://export.arxiv.org/api/query?search_query=ti%3A%22Hadamard%20Product%20Factorization%22&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending)
   
   返回 `totalResults=1`，唯一结果为 `2508.14901v1`。

3. 查询：
   [`all:"Hadamard factorization" AND all:"4 x 4"`](https://export.arxiv.org/api/query?search_query=all%3A%22Hadamard%20factorization%22%20AND%20all%3A%224%20x%204%22&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending)
   
   返回 `totalResults=0`。此查询对排版和术语敏感，只作辅助负结果。

API feed 的生成时间为 `2026-08-29T02:00:24Z` 至
`2026-08-29T02:00:29Z`。这些有限查询没有找到后续实数证明或显式分解，
但不能排除采用不同术语或未被 arXiv 收录的工作。

## DOI、出版与引文数据库

### 2026-08-29 — DataCite DOI

- 查询/URL：
  [`10.48550/arXiv.2508.14901`](https://api.datacite.org/dois/10.48550/arxiv.2508.14901)
- 返回：publisher=`arXiv`，publicationYear=`2025`，version=`1`，
  `Submitted=2025-07-31T21:00:28Z`，`Updated=2025-08-22T00:00:06Z`，
  `relatedIdentifiers=[]`。
- 有界推论：该 DataCite 记录没有链接第二版本或正式期刊 DOI。空的
  `relatedIdentifiers` 不能证明别处绝无发表版本。

### 2026-08-29 — OpenAlex

- 论文记录：
  [`W4416050143`](https://api.openalex.org/works/https%3A%2F%2Fdoi.org%2F10.48550%2Farxiv.2508.14901)
- 返回：type=`preprint`，publication date=`2025-07-31`，
  primary location 为 arXiv，`is_accepted=false`，`is_published=false`，
  `cited_by_count=0`；记录 `updated_date=2026-08-26T07:47:46Z`。
- 引用过滤查询：
  [`filter=cites:W4416050143`](https://api.openalex.org/works?filter=cites%3AW4416050143&per-page=100)
  返回 `meta.count=0`。
- 有界推论：截至该数据库更新时间，OpenAlex 没有索引引用者；这不等于
  全部数学文献零引用。

### 2026-08-29 — Semantic Scholar Graph API

- 引用端点：
  [`ARXIV:2508.14901/citations`](https://api.semanticscholar.org/graph/v1/paper/ARXIV%3A2508.14901/citations?fields=title%2Cauthors%2Cyear%2CpublicationDate%2CexternalIds%2Curl&limit=100)
- 成功返回 `offset=0, data=[]`。论文 metadata 端点的同轮请求返回 HTTP
  429，故没有把该失败请求当作证据。
- 有界推论：该次 Semantic Scholar 引用查询没有记录引用者。

### 2026-08-29 — DBLP

- 查询/URL：
  [`dblp record: journals/corr/abs-2508-14901`](https://dblp.org/rec/journals/corr/abs-2508-14901)
- 返回：Igor Rivin，CoRR `abs/2508.14901` (2025)，类型为 informal/other
  publication；未显示期刊或会议版本。
- DBLP 主要覆盖计算机科学，不能据此排除数学期刊或未索引手稿。

## 作者记录与最近邻后续工作

### 2026-08-29 — 作者公开 CV

- URL：[`Igor Rivin CV`](https://igorrivin.github.io/cv.pdf)
- 位置：CV 第 9 页技术报告列表将该文列作
  `2025. arXiv:2508.14901`，没有列出替代期刊版本、勘误或实数证明。
- 限制：作者 CV 可能滞后或不完备，只能作为作者记录的补充证据。

### 2026-08-29 — 2026 年最近邻 arXiv 工作

- 查询定位到：Pratik Jawanpuria, Ankish Chandresh, Bamdev Mishra,
  [*Riemannian Optimization for Hadamard Products of Low-Rank
  Matrices*, arXiv:2606.01216](https://arxiv.org/abs/2606.01216)。
- 全文与参考文献审阅结果：该文研究低秩 Hadamard 模型的商流形和数值
  优化，引用 Ciaperoni--Gionis--Mannila 与 Wertz--Vandaele--Gillis；其
  参考文献没有 Rivin 2025，也没有讨论展示矩阵或给出实数可行/不可行
  定理。
- 推论：这是术语上最近的后续工作之一，但不抢先解决本项目的矩阵特定
  结论。

## 更正、显式分解与二次检索

2026-08-29 在第一次发现有理见证后，进行了第二轮定向检索，查询短语：

```text
"Computational Resolution of Hadamard Product Factorization" correction OR erratum
"Computational Resolution of Hadamard Product Factorization" proof real
"2508.14901" correction OR erratum OR real
"1 1 1 1" "1 1 1 0" "0 1 0 0" "1 0 0 0" Hadamard
```

搜索结果用于导航回 arXiv、DataCite、OpenAlex、作者 CV 和上述 2026
相关论文；没有定位到原作者勘误、后续 arXiv 版本、正式数据库中的引用
论文，或已经发表的该矩阵有理分解。普通聚合站和搜索摘要未作为证据。

## NOVELTY_LOCK（referee 版本）

在上述有限范围内，可以安全陈述：

> 截至 2026-08-29，arXiv 仍只显示 Rivin 论文 v1；该版本只报告实数域
> 数值证据。所列 arXiv 精确查询以及 OpenAlex、Semantic Scholar、
> DataCite、DBLP 和作者 CV 检查没有发现后续的实数域严格解决或该展示
> 矩阵的显式有理分解。

不可以仅据此陈述“这是全世界第一个”或“此前绝无人知道”。若拟投稿，
还应由主项目在定稿题名、公式和作者列表后重跑 MathSciNet/zbMATH、
Google Scholar/Dimensions（若有访问权限）、Crossref 引用链接及全文
公式检索，并把仍然是数据库负结果的部分保持为限定措辞。
