# bigMac-00018-p03 — Gaussian 截断热核顶特征值在零点的二阶正则性

对 `u>0`，在 `L^2([-1,1])` 上定义紧自伴算子

```
(S_u f)(p) = integral_{-1}^1 K_u(p,q) f(q) dq,
K_u(p,q)   = exp(-(p-q)^2/(4u)) / (2 sqrt(pi u)).
```

令 `lambda(u)` 为 `S_u` 的最大特征值，`Phi(u)=log(lambda(u))`，并连续定义
`lambda(0)=1`、`Phi(0)=0`。证明或反驳：有限右二阶导数 `Phi''(0+)` 是否存在。
若不存在，至少给出严格的非二次余项下界并确定其正确幂次；若声称精确首个非解析项，
必须给统一余项而非浮点拟合。

一手来源：Kangqiao Liu and Deyou Chen, *Maximal-velocity deficit under a finite-support
constraint in hard-wall half-line continuous-time quantum walk*, arXiv:2609.01970v1，
Eqs. (45)--(48), (59), (69) 与 Appendix A.5，pp.6--10,15--16。来源只证明
`lambda(u)=1-(pi^2/4)u+o(u)`；Eq. (69) 的高阶解释是条件式，higher-order analysis
明确留给未来工作。

本地完整 PDF：`batches/literature/bigMac-18/2609.01970v1.pdf`；SHA-256
`9c6ac07445adeea52400085a68a9432f400552d31f1d56e162986add2ed73b68`。
