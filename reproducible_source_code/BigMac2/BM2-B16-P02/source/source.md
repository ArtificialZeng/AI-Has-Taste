# bigMac-00016-p02 — 扫帚图三次幂闭邻域理想的精确同调不变量

对整数 `n,m>=2`，令扫帚图 `B(n,m)` 的顶点为
`x_1,...,x_n,y_1,...,y_m`，边为全部 `{x_i,y_1}` 及
`{y_j,y_(j+1)}`。令 `B(n,m)^3` 连接原图距离至多3的不同顶点。
在 `S=K[x_1,...,x_n,y_1,...,y_m]` 中令

`NI(B(n,m)^3)=(product_{w in N[v]} w:v in V(B(n,m)^3))`，

并取其最小单项式生成集。对全部 `n,m>=2` 给出并证明
`pd(S/NI)`、`reg(S/NI)`、`ht(NI)` 的完整分段闭式公式，
列全小 `m` 例外，并精确分类 `S/NI` 何时 Cohen--Macaulay。

一手来源：Anda Olteanu and Oana Olteanu,
*On the closed neighborhood ideal of the square of broom and double broom graphs*,
arXiv:2609.04831v1, https://arxiv.org/html/2609.04831 。
定位 Section 2 定义；Theorem 2.3；Theorems 3.7--3.8；Corollary 3.9。
来源处理平方；三次幂是 source-derived adjacent family，开放性/新颖性 status-uncertain。
有限 Betti 表只能发现递推；普遍公式必须证明 mapping-cone 极小性及所有端点。
