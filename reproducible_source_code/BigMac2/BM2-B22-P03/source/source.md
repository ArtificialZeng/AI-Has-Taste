# bigMac-00022-p03 — `d=4` Hypercube Inequality：16 个顶点变量的精确判定

## 冻结的一手来源与原题

一手来源：Gennadiy Averkov, Katherina von Dichter, Ivan Soprunov,
*On the Log-Submodularity for Zonoids: From Mixed Volume Inequalities to the Hypercube*,
arXiv:2608.14909v1，Hypercube Inequality (2)，§4.4 的 (16)，以及 §§5--7；本地 PDF
`../literature/bigMac-22/2608.14909v1.pdf`，SHA-256
`5880c0a7e8de2cf4e4ceef40b482eda7722fae68ca321576099c096b9a6518e5`。

令

```text
V_4 = {0,1}^4,
F_4 = { {v in V_4 : v_i = epsilon} : i in {1,2,3,4}, epsilon in {0,1} }.
```

因此 `F_4` 恰有八个立方体 facets。给每个 `v in V_4` 一个变量
`x_v in R_{>=0}`。对每个五点子集 `S={v_0,...,v_4} subset V_4`，严格采用来源的
normalized volume 规范

```text
Vol(S) = 4! vol_4(conv(S))
       = |det([v_0 v_1 v_2 v_3 v_4; 1 1 1 1 1])|.
```

若 `S` 仿射相关，则 `Vol(S)=0`。这里绝不能把 `Vol` 换成未归一化 Euclidean
volume，也不能遗漏行列式绝对值。冻结的待证或待反驳命题是：对全部 16 个非负实变量，

```text
( sum_{S in binom(V_4,5)} Vol(S) prod_{v in S} x_v )
    ( sum_{v in V_4} x_v )^3
<= prod_{F in F_4} ( sum_{v in F} x_v ).                    (HC4)
```

目标是证明 `(HC4)`，或给出一个逐项可核验的精确反例；浮点优化、数值 SDP 或随机搜索
本身都不能结案。

## 量词、参数移位与最近边界

- `(HC4)` 的量词是 `forall x in R_{>=0}^{16}`，包括所有 boundary supports；齐次总次数
  为八，可在非零情形正规化 `sum_v x_v=1`，但必须另行保留零向量和 facet-vanishing
  边界。
- 来源令 hypercube 参数 `d=n-1`。所以这里的 `d=4` 对应来源几何/混合体积问题的
  ambient dimension `n=5`。来源在 `R^4` 证明的新 zonoid 定理对应的是 `d=3`，不是
  本题；不得因标题或摘要中的“四维”字样把已证层误认成本题。
- `d=2` 的 hypercube polynomial 是一个完全平方；来源 Theorem 5.1 与 §6 证明
  `d=3`，给出 exact SOS 加非负余项，并证明等号恰在某个 facet 的全部顶点变量为零时
  出现。§7.5 明确说 `d>=4` 仍开放；`d=4` 是下一层，显式展开约有四十万项。
- 本题不是已经被反例否定的一般 zonoid log-submodularity 猜想。它是来源提出的特定
  Bézout-type replacement / Hypercube Inequality；二者不得混写。

## 拟研究范围与首轮 exact 缩减

第一研究块不生成或保存四十万项的全展开，而按以下顺序做反例优先的 exact 筛选：

1. **最小非平凡 support。** 左端的 simplex sum 非零至少需要五个仿射独立顶点。
   在 4-cube 对称群作用下枚举五点 support 的轨道，用整数行列式生成 `Vol(S)`，对每个
   轨道精确判定相应五变量次数八不等式。随后扩展到 support size 六；不得把有限 support
   层无反例外推为 `(HC4)`。
2. **对称子空间。** 至少测试 antipodal ansatz `x_v=x_{1-v}`、Hamming-layer ansatz
   `x_v=a_|v|`，以及一个 facet/two-layer ansatz。先因式分解，再用 exact CAD、Bernstein
   系数、AM--GM 或显式平方分解判定；数值最小值只用于寻找有理点或猜测因子。
3. **稀疏到一般的桥只作为候选。** 除非给出保持两边且覆盖所有非负点的严密压缩、极射线
   或 polarization 论证，不得声称稀疏/对称验证证明一般情形。

## 快速否证、证明证书与允许出口

- **最快否证。** 正规化 `sum_v x_v=1` 后，先在五点与六点 support 轨道上优化
  `RHS-LHS`。一旦浮点搜索出现严格负值，立即在邻域中寻找 `x_v in Q_{>=0}`，重新用
  整数 determinant table 和有理算术计算两边。一个列明 16 个有理坐标、所有非零
  `Vol(S)` 贡献以及严格负有理差值的记录，就是完整反例证书。
- **一般证明证书。** 必须是可逐项展开核验的 polynomial identity、带非负系数的分解、
  exact SOS/Positivstellensatz（连同正交约束或乘子）、或覆盖完整正规化 simplex 的 exact
  cell/CAD 证书。浮点 Gram matrix 必须有有理重构并符号验证。
- **有意义的局部出口。** 若一般题未结案，可接受的最小成果是：完整解决所有五点 supports、
  所有至多六点 supports，或一个明确的非平凡对称族，并给出 exact 证书及等号分类。
  “搜索若干点未见反例”不是成果。
- **审计要求。** 所有脚本须从 `V_4` 和 determinant 定义重建 coefficient table，不抄写
  浮点体积；候选反例必须保留最简有理数版本。证明与反例搜索应对称进行。

本文件冻结问题和证书标准；后续研究产物应写入另外的工作文件，不得回写或改写此
immutable source。
