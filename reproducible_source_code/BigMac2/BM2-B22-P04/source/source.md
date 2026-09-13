# bigMac-00022-p04 — cograph anchored configuration spaces 的整数挠存在性

## 冻结的一手来源与原题

一手来源：Adityo Mamun, Jonathan Nalikka, Eric Ramos,
*Universality in the Algebra and Topology of Cographs*, arXiv:2609.04554v1，
Definition 4.13、Corollary 4.18 及其后关于 integral torsion 的未编号问题，pp. 25--28；
本地 PDF `../literature/bigMac-22/2609.04554v1.pdf`，SHA-256
`f73a5cf3fa71f1c5f387de7cf1d881214831d557a2b46ba43e2e2518bac37480`。

把有限图 `G` 看成一维 simplicial complex。对有限锚点集 `K subset V(G)`，来源定义

```text
Sigma(G,K,n) = { (x_1,...,x_n) in G^n :
                   every vertex k in K occurs among the coordinates x_j }.
```

这是 `G^n` 的 cubical subcomplex；粒子有序，并且允许碰撞。来源的原始存在性问题是：

```text
是否存在有限图 G、K subset V(G)、n>=|K|、i>=0 和素数 p，
使 Tor H_i(Sigma(G,K,n); Z) 非零（等价地含 p-torsion）？       (AT)
```

本项目冻结其中紧贴论文新定理的 cograph 子问题：在 `(AT)` 中额外要求 `G` 是 cograph
（即没有 induced `P_4`）。一个 cograph 反例同时回答原始存在性问题；cograph 全部无挠
则只是原题的一个子类定理。

## 精确量词、最近定理与首个非平凡层

- 反例量词是存在有限 pointed cograph `(G,K)`、整数 `n>=|K|, i>=0` 和素数 `p`。
  若要证明 cograph 子类无挠，则须覆盖所有这些量词，而不是有限顶点 census。
- 来源回顾：anchored configuration spaces 对所有树均无整数挠，对 cycle 也无挠。
  Corollary 4.18 证明：固定 `(i,r,n)` 后，`G -> H_i(Sigma(G,K,n);Z)` 在 pointed
  cographs 上有限生成；特别地，其可能 torsion 的指数有只依赖 `(i,r,n)` 的统一界。
  这限制挠的类型，但不证明挠不存在，也不给出挠例。
- 本轮固定首层 `n=3, |K|=1`。`n=1` 平凡；当 `n=2`、`K={k}` 时，
  `Sigma(G,{k},2)=(G x {k}) union ({k} x G)`，其整数同调无挠。因此 `n=3` 是单锚点下
  第一个能形成二维 cells、从而值得搜索的层。
- 首个指定图为 diamond `K_4-e`。它是 connected cograph，既不是树也不是 cycle；
  自同构群在顶点上有两个轨道（度二端点与度三端点），两个锚点轨道都必须分别计算。

## 拟研究范围

1. 先对 `G=K_4-e`、`n=3` 和两个单锚点轨道建立完整 cubical chain complex并求整数
   homology。
2. 随后按 canonical cotree / pointed isomorphism class 枚举全部至多六顶点 cographs，
   包括 disconnected cases；对每个单锚点轨道计算 `Sigma(G,K,3)` 的 Smith normal form。
3. 在此固定层，complex 的维数至多二。因此 `H_0` 无挠，`H_2` 作为自由链群的子群也
   无挠，唯一需要检验的群是 `H_1`。实现仍须计算并核验 `partial_1 partial_2=0`，不能只对
   单个 boundary matrix 读 SNF。
4. 若六顶点以内无挠，允许从 cotree 形状中提炼并证明一个 exact、无限且有意义的无挠
   子类，例如由实际计算支持的 bounded-height cotree family；未经证明不得预先指定该
   子类，也不得把 census 写成全体 cograph 定理。

## 证书规范与最快否证

- **最快否证。** 从 `K_4-e` 的两个锚点轨道开始，固定顶点、定向边和 product-cell 的
  canonical ordering，生成 `C_2 -> C_1 -> C_0` 的整数矩阵并计算 `H_1` 的 SNF。任一
  大于一的 invariant factor 即给出整数挠候选，随后独立重算。
- **挠反例证书。** 必须给图的 adjacency list 或 canonical cotree、锚点、`n`、有向 cell
  bases、两个 boundary matrices，以及可核验的 unimodular row/column transformations
  或等价 Smith certificate；同时给一个显式 torsion cycle 和其阶数验证。只报告软件输出
  或模 `p` Betti jump 不够。
- **有限 census 证书。** 必须说明 cograph 与 pointed-orbit 枚举完备、去同构方法、cell
  选择和符号约定，并保留每例的 SNF/invariant factors。六顶点以内没有挠只能表述为该
  有限 census。
- **无挠子类证书。** 需要对所声明无限子类给 chain contraction、unimodular reduction、
  cotree induction 或其他 exact proof；不得从有限样本归纳。
- **允许出口。** 最优出口是首个 anchored torsion 例。若没有，允许出口是一个精确、
  非平凡、无限的无挠 cograph 子类；完整且可复现的六顶点 census 可作为数据性中间成果，
  但不是原题的总定理。

## 与同源邻题的严格区别

neighbor `bigMac-00012-p13` 研究的是 connected cographs 上的普通、未锚定、collision-free
ordered configuration space `Conf_3(G)`，并做至多七顶点 census。本题研究允许碰撞但强制
锚点出现的 `Sigma(G,{k},3)`，枚举至多六顶点的 pointed cographs，且同一底图的不同锚点
轨道是不同输入。两者虽来自同一篇论文，却不是同一空间、同一 chain complex 或等价问题；
任一 census 或无挠结论均不得直接转移到另一题。

本文件冻结问题和证书标准；后续研究产物应写入另外的工作文件，不得回写或改写此
immutable source。
