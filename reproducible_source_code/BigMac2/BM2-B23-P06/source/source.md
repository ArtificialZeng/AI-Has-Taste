# bigMac-00023-p06 — immutable source

> 冻结日期：2026-09-09。此文件保存不可变的问题入口；后续研究不得把有限软件输出改写为普遍分类。

## 一手来源与本地证据

- Milan Basic, *On uniquely colorable Cayley graphs*，arXiv:2609.03184v1，
  §2 的 integral circulant 定义及 §5 Conclusion（PDF pp. 2, 7）。
- 本地 PDF：`batches/literature/bigMac-23/2609.03184v1.pdf`。
- SHA-256：`eec197e27fcab9602c1cd8b033dd84a45d4401abcbdbe225db3de9d6afb9acf2`。

## 来源中的对象与开放边界

对整数 `n>=1`，令 `D_n` 为 `n` 的所有严格真因子。对 `D subseteq D_n`，
`ICG_n(D)` 是顶点集 `Z/nZ` 上的简单无向 Cayley 图，其中不同顶点 `i,j` 相邻当且仅当

```text
gcd(i-j,n) is in D.
```

来源指出 perfect unitary Cayley graphs（`D={1}`）已有分类，而全部 perfect integral
circulant graphs 的分类仍是开放方向。来源没有宣称下面的 `n<=64` 有限表是新定理。

## 冻结的拟研究命题

对每个 `1<=n<=64` 和每个 `D subseteq D_n`，精确判定 `ICG_n(D)` 是否 perfect，并将
全部正例压缩为可人工复查的因子格条件、有限参数族或无歧义表格。`D=emptyset`、不连通图、
完全图及其补图均包含在量词内，不得静默删除退化边界。

按 Strong Perfect Graph Theorem，图 perfect 当且仅当它不含长度至少 5 的 induced odd cycle，
且其补图也不含。因此计算判定必须落实为 exact combinatorial certificate，而非浮点谱测试。

## 贡献边界与语义差异

- 普遍分类仍未解决；本题只冻结 `n<=64` 的完整有限层。
- 若完整结果只是已公开数据库或经典定理的直接查表，则应停放，不包装为新贡献。
- 若得到可证明的 divisor-lattice 条件覆盖该层、首个反例到自然猜想、或显著压缩的独立证书，
  才可能成为 result note。
- registry 中既有 Cayley SDP、着色和谱常数对象，不与本有限 perfectness 分类等价。

## 证书标准

- 每个 imperfect 类必须给一个顶点序列，精确验证其在图或补图中诱导长度至少 5 的奇圈。
- 每个 perfect 类必须给可独立重放的 Berge/perfectness 证书、完整的可证明结构分解，或一个
  审计过的穷尽算法及覆盖证明；软件只返回 `true` 不充分。
- 应按乘法单位作用对 `D`/witness 去冗余并记录算法、版本、输入域和输出哈希。
- 有限层不推出 `n>64`，也不推出来源的普遍分类。

## 最便宜决定性测试与快速否证

先枚举 `n<=32` 的全部 divisor sets，用 exact adjacency 检查并提取最短 odd hole/antihole；
观察 perfect 正例能否由二分、complete multipartite、chordal、补图以及已知 unitary 分类覆盖。
若到 32 已出现大量没有短结构证书的正例，或总证书规模失控，立即停放而不是扩到 64。

一个漏掉的 `D`、错误的 induced-cycle witness 或与公开分类冲突的实例即可否证拟议表；
triage 还须先查有限 census 是否已有一手来源。

## 原题状态

来源的全部 integral circulant perfectness 分类未解；本题是新拟议的有限层，开放性与新颖性均为
`status-uncertain`。
