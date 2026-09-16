# win-00085-p11 — 三等长区间在 lambda=5/2 的精确 Turán 常数

## 不可变来源与问题

一手来源：Fu–Li–Wang–Wang, *Turán problem on the union of three intervals of equal length*, arXiv:2608.15643v1。定义与式 (1.1)–(1.2) 见 PDF p.1，Theorem 1.2 见 p.2，有限 SDP 见 p.9，Proposition 4.2 见 pp.9–11，Lemma 5.1 见 pp.11–12，Discussion 见 p.13。摄取批次为 `batches/inbox/bigWin-85.raw.md`，规范化审计见 `batches/normalized/bigWin-85.md`。

令

`Omega_lambda=(-1,1) union (lambda-1,lambda+1) union (-lambda-1,-lambda+1)`，

且 `T_R(Omega_lambda)` 是所有连续正定函数 `f:R->C` 中，在 `f(0)=1` 与 `supp(f) subset Omega_lambda` 条件下 `integral f` 的上确界。固定 `lambda=5/2`，精确求 `T_R(Omega_{5/2})`。极值元分类为第二层目标，不得阻碍先冻结精确最优值。

按来源的有限约化，等价地最大化

`1+2(c_1+c_4+c_5+c_6)`

于所有实数 `c_1,c_4,c_5,c_6`，满足对每个实数 `t`：

`1+2c_1 cos(t)+2c_4 cos(4t)+2c_5 cos(5t)+2c_6 cos(6t)>=0`，

再将最优值除以 `2`。

## 已知边界与证书要求

来源已证明

`(559+80 sqrt(42))/506 <= T_R(Omega_{5/2}) <= 9/4`，

并明确不声称 Proposition 4.2 的可行多项式最优。该固定精确值未被单列为正式问题，开放性与新颖性仍须独立核验。

浮点 SDP 只能发现候选。严格下界须给 Fejér–Riesz 分解、精确 PSD Gram 矩阵或等价代数证书；严格上界须给精确 dual/moment 证书。两者目标相等方可宣称精确值。任何严格改进已知任一端的精确证书可作为独立候选，但必须明确未解决原精确值时的范围。
