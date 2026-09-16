# win-00075-p04 — 加权 Bergman Hilbert 算子定理的端点量词审计

## 不可变来源与问题

一手来源：Li et al., *Norm of the generalized Hilbert operator on weighted Bergman spaces*, arXiv:2609.04833v1, Theorem 3.4 及 equations (3.41)--(3.42)（PDF pp.29--30），https://arxiv.org/abs/2609.04833 。摄取日期：2026-09-09。

在来源定理的参数域内，逐字核对其证明中使用的

`G_(alpha,b)(p)=[p(b+1)-alpha-2]/[p-alpha-2] * 2[1-((alpha+2)/p)^2] / [(alpha+2)/p+2(p-alpha-2)]`。

证明或反驳端点结论

`lim_(p downarrow alpha+2) G_(alpha,b)(p)=4b`。

若成立，证明精确的局部后果：当

`b > (1/4) B(1+alpha,2+alpha/2)`

时，存在 `epsilon>0`，使每个 `p in (alpha+2,alpha+2+epsilon)` 均有

`G_(alpha,b)(p) > B(1+alpha,2+alpha/2)`。

随后审计 Theorem 3.4 的完整量词，判定上述事实只使既有证明失效，还是强迫阈值从 `beta_alpha` 改为依赖 b，或需要附加条件。没有构造违反算子范数结论的对象时，不得声称反驳了定理本身。

## 证书要求

保存源 TeX 或 PDF 的精确行/页定位、符号约分、显式 epsilon 估计，并把“证明漏洞”“修正后的引理”“定理反例”严格区分。若只是排版或记号错误且不影响结论，按 proof-gap 或已知修正登记。
