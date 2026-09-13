# bigMac-00019-p02 — 24 顶点图的 4/8/16 圈有限层

证明或反驳：每个恰有 24 个顶点且最小度至少 3 的有限简单图，都含有长度为
`4`、`8` 或 `16` 的简单圈。

反例须给完整 adjacency list 或 graph6，并独立复核简单性、顶点数、最小度与三种圈
的缺失；正向结果须给可独立检查的完备 UNSAT 证书。

一手来源：Daniel Garcia, *Small graphs without power-of-two cycles: a lower bound of 24,
a correction to a construction of Exoo, and explicit bounds for f(k)*,
arXiv:2609.04686v1，Theorem 2.1、Corollary 2.2、Remark 2.3、Section 8，
pp.2--3,8。来源以 SAT+DRAT 证明一般图到 23 点，三正则子类已覆盖 24 点，但完整
24 点 `{4,8,16}` 决定尚未完成。本地 PDF：
`batches/literature/bigMac-19/2609.04686v1.pdf`；SHA-256
`0ab4267dc8b9de8abb3c3868385a2afad9fb8f08614836297581a4ee03ab77f8`。
