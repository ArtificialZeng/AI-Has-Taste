## DM05-04 循环图的 $\operatorname{Inc}(\mathbb N)$ edge-ideal chain 猜想

令 $n\ge6,r\ge0$，$C_n$ 是顶点集 $[n]$ 上的循环图，并令
$$
I_{n+r}:=\operatorname{Inc}(\mathbb N)_{n,n+r}(I(C_n))\subset R_{n+r}=k[x_1,\ldots,x_{n+r}].
$$
证明或反驳以下完整充要分类：
$$
R_{n+r}/I_{n+r}\text{ is Cohen--Macaulay}
\iff
r\ge\left\lfloor\frac{n-4}{2}\right\rfloor\ \text{and}\ r\ne n-4.
$$

陈述对任意域 $k$ 的依赖必须明确处理；若结论随 characteristic 改变，应给正确分支。有限 Macaulay2 表只算证据，普遍正方向须给 shelling/Reisner 等完整证明，反方向须给 purity、link homology 或其他精确障碍。

来源与范围：Anwar--Ghayas--Javed, *Cohen--Macaulayness of $\mathrm{Inc}(\mathbb N)$-Invariant Chains of Edge Ideals*, arXiv:2609.03566v1, Theorem 3.14 and Conjecture 3.15（PDF pp. 14--15）。来源证明 $r\ge n-3$ 时该 graph 已为 complete graph，且以计算和 gap 结构明确提出上述完整分类。
