# win-00085-p10 — 允许零腿的 caterpillar domination polynomial

## 不可变来源与问题

一手来源：Du–Heilman–Panova, *Trees and Graphs with Non Log-concave Dominating Set Sequence via AI Tools*, arXiv:2605.02193v1，定义见 PDF p.1，caterpillar 与 Theorem 3.3 见 p.6，Remark 3.4 见 p.7。摄取批次为 `batches/inbox/bigWin-85.raw.md`，规范化审计见 `batches/normalized/bigWin-85.md`。

对整数 `k>=1` 与 `a_1,...,a_k>=0`，令 `T(a_1,...,a_k)` 为脊柱 `v_1...v_k`，并在 `v_i` 上接 `a_i` 个叶的树。若

`D_T(x)=sum_{j=0}^N d_j x^j`

中的 `d_j` 是大小为 `j` 的 dominating sets 数，证明或反驳

`d_j^2 >= d_{j-1} d_{j+1}` 对所有 `1<=j<=N-1`

及所有上述参数成立。

端点零腿按图同构可精确消去：`T(0,a_2,...,a_k)` 同构于 `T(a_2+1,a_3,...,a_k)`，右端类似。因此真正的新核心可限制为 `k>=3`、`a_1,a_k>=1` 且至少一个内部 `a_i=0`，但不得把这一约化误写成弱化原量词。

## 已知边界与证书要求

来源 Theorem 3.3 已证明所有 `a_i>=1` 时系数 log-concave；Remark 3.4 只说作者相信允许零腿时仍成立，并非正式编号猜想。当前开放性与新颖性仍须核验。

先按总顶点数递增，用精确大整数树 DP 搜索反例。反例必须给出参数向量、完整整数系数表和某个严格负的 `d_j^2-d_{j-1}d_{j+1}`。若走正向路线，须给三状态转移或等价结构证明，并严格覆盖任意内部零段；有限检验不得写成全称证明。
