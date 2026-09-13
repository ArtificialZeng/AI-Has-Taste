# bigMac-00020-p03 — `Q_3` 的 directional localization number

使用 Jones--Kinnersley 的 partial-feedback directional localization game：每轮 `c` 个
cops 同时 probe 顶点；若 probe 正好是 robber 所在点，robber 回答该点，否则回答一个
位于某条从 probe 到 robber 的最短路上的邻点。若未被唯一定位，robber 随后可留在原地
或沿一条边移动。`ζ_d(G)` 是保证有限时间内唯一定位 robber 所需的最少 cops 数。

精确决定三维超立方体 `Q_3` 的值：

```
ζ_d(Q_3) = 3  or  4?
```

值 3 需要完整 winning strategy（可先给 belief-state action table，再压缩成证明）；值 4
需要对所有三-probe 动作闭合的 robber strategy/trap。有限程序输出必须由独立 replay
检查，不能只报告搜索结果。

一手来源：John Jones and William B. Kinnersley, *The Directional Localization Game on
Graphs*, arXiv:2609.01745v1, Corollary 3.9 and Question 6.1, pp.14,29；本地 PDF
`../literature/bigMac-20/2609.01745v1.pdf`，SHA-256
`1f1ac4c3c0a1313003b326c5c98cad06253482beaecfdbd14f7f0fd6c2a67d58`。
来源证明 `ζ_d(Q_n)∈{n,n+1}` 并猜测恒为 `n`；本题只冻结首个未知切片，不声称解决
全部超立方体。
