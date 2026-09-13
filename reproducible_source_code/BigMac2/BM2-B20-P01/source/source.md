# bigMac-00020-p01 — 等余维理想是否必为 split

设 `k` 为任意域，`A_•=⊕_{i>=0}A_i` 为 standard graded、locally finite、
semiconnected `k`-代数。设双边理想 `J⊲A` 满足

```
dim_k(A/J) = dim_k(A_0).
```

决定自然复合 `A_0 → A → A/J` 是否必为同构；按来源 Definition 4.1，这等价于问
`J` 是否必为 split。反例必须逐项核验分次、standardness、local finiteness、
semiconnectedness、理想闭性、两边维数和自然映射的核。若声称最小反例，还须排除
所有更小总维数。

一手来源：Darius Dramburg, *Isomorphisms of graded semiconnected algebras*,
arXiv:2609.03288v1, Definitions 1.1 and 4.1, Question 6.1, pp.1,4,9；本地 PDF
`../literature/bigMac-20/2609.03288v1.pdf`，SHA-256
`f1dff9a9f6decb301ce097bd319c2085f553e5e92f7dddafff63e772db41816e`。

拟议的最便宜反例测试是 `A=k × k[ε]/(ε^2)`、`A_0=k×k`、`A_1=kε`、
`J=k×0`。这只是待独立证明的测试，不是本 source 文件中的既定结论。不得静默加入
来源没有写出的 indecomposable、faithful 或 tangent-dimension 假设。
