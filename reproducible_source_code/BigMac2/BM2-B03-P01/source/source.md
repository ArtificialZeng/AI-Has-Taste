## DM03-01 固定周期集合能否改进 `{0,1,3}` 双向仿射拷贝的区间下界

固定整数 $q\ge2$ 且 $\gcd(q,6)=1$，取非空 $R\subseteq\mathbb Z/q\mathbb Z$，并令

$$A_N=\{1\le n\le N:n\bmod q\in R\}.$$

记

$$M(A)=\#\{(x,d)\in\mathbb Z^2:d\ne0,\ x,x+d,x+3d\in A\}.$$

证明或反驳：

$$\lim_{N\to\infty}\frac{M(A_N)}{|A_N|^2}\le\frac13,$$

并且等号成立当且仅当 $R$ 是 $\mathbb Z/q\mathbb Z$ 的某个加法子群的陪集。

来源与范围：Samuel Korsky, *Affine Copies of Three-Point Patterns in Sets of Integers*, arXiv:2609.02308v1，定义 (1.1)--(1.2)、式 (1.15)--(1.20) 与 Theorem 1.4。来源证明一般有限集的 $1/3\le\gamma_{\{0,1,3\}}\le47/122$；本题只研究 fixed-modulus periodic 方法类，不声称求出完整常数。该局部命题不是来源中的已声明定理，新颖性仍须独立核查。
