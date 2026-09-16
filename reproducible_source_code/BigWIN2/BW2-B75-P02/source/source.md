# win-00075-p02 — Example 8.7 的全部 n-Lie deformation maps

## 不可变来源与问题

一手来源：*Extending Structures for n-Lie Algebras*, arXiv:2609.05051v1, Definition 7.1（PDF p.30）、Example 8.7（pp.36--37）与 Corollary 8.8，https://arxiv.org/abs/2609.05051 。摄取日期：2026-09-09。

在来源 Example 8.7 的特征零底域与 n-Lie 结构中，把线性映射 `r:V->g` 在所给基下写作

`R=[[A,v],[w^T,alpha]]`,

其中 `A in M_(n-1)(K)`，`v,w in K^(n-1)`，`alpha in K`。证明或反驳：`r` 是 deformation map 当且仅当

`det(A)*v=0` 且 `det(R)=alpha*det(A)`。

等价地，完整解集应分为：

1. `det(A)!=0`：必须 `v=0`，而 `w,alpha` 任意；
2. `det(A)=0`：必须 `det(R)=0`。

## 已知边界与证书要求

来源只展示 `r(u_i)=x_i (i<n), r(u_n)=0` 的一个例子；Corollary 8.8 只给补空间的两个同构类，并未显式分类全部 deformation maps。先按 Definition 7.1 在 `n=4` 符号展开，确认没有遗漏因排列符号或基约定产生的条件；再给一般 n 的多线性证明。若该分类是既有 ternary deformation-map 定理的直接推论，必须如实登记而不得主张新颖性。
