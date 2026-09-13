# bigMac-00021-p05 — `H(3,3)` 的 majority `C`-chromatic number

令 `H(3,3)=K_3 square K_3 square K_3`，顶点集为 `[3]^3`，两点恰在一个坐标不同
时相邻。一个 majority `C`-coloring 是满射 `phi:V->[p]`，使每个顶点的 6 个邻点中
至少 3 个与它同色。证明或反驳

```
chi_bar_>=(H(3,3)) = 4,
```

其中左侧表示此类着色可使用的最大颜色数。

一手来源：Csilla Bujtás, Magda Dettlaff, Hanna Furmańczyk, Aleksandra Laskowska,
*Majority C-coloring in Cartesian products*, arXiv:2608.27669v1, Section 1.2、
Proposition 6(ii)、Open Problem 3；本地 PDF
`../literature/bigMac-21/2608.27669v1.pdf`，SHA-256
`fa95b1c8448e455df20f93e43cfb66b1f6e2a3855afe3c656cff424f52025c8f`。

来源只给 `3<=chi_bar_>=<=5`。外层筛选发现一个待核验短路线：每个色类诱导最小度至少
3；尝试证明 5 点色类不可能，并以一个 9 点切片和三个 6 点 `K_3 square K_2` 切片给
四色分割。此处只提供最便宜测试，不把该草图冻结为既定结论；research 与 fresh referee
必须分别重建所有邻接计数、三角形分类和满射条件。
