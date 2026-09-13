# 独立 Referee 首轮报告

日期：2026-08-29（Asia/Shanghai）

结论先行：在正式声明澄清 `n=2` 的群作用以前，原题按字面是 **fatal ambiguous，并且按“每块棋盘的全部几何对称”解释时，Barker 所写的 `n>9` 递推是假的**。OEIS A321614 的数值 `a(2)=23` 使用的是保持两条坐标轴方向的四元群，而 `4×4` 棋盘的全部几何对称群是八元二面体群，后者给出 `a(2)=14`。这不是措辞问题：把第 2 项改成 14 后，所列递推在 `n=10,11,12` 分别失效。

本报告不假定候选递推正确。以下状态模型、固定点数和生成函数均从棋盘定义独立重建，可作为后续 builder 与根证书的对照基准。本轮尚未看到 `agents/builder_report.md` 或根证书；出现后必须进行第二轮逐项审计。

## 1. 必须先冻结的形式化定义

对 `n≥1`，令

\[
B_n=\{1,2,3,4\}\times\{1,\dots,2n\}.
\]

placement 是子集 `K⊂B_n`；互不攻击是任意两个不同格 `(r,c),(r',c')∈K` 均满足

\[
\max(|r-r'|,|c-c'|)>1.
\]

计数对象是满足 `|K|=2n` 的 placement。这里必须写 **maximum（最大基数）**，不能写成 maximal（按包含极大）。

`n=0` 时没有通常意义的 `4×0` 几何矩形或其“全部几何对称群”。若要采用 OEIS 的 `a(0)=1`，应明确把它定义为形式空棋盘的唯一空 placement，并令所选四元群平凡作用；不能声称这是未加约定的几何结论。

有两种互不相同的合法群约定：

1. **OEIS/轴有标记版本**：对每个 `n` 都固定使用
   \[
   G=\{e,h,v,hv\}\cong C_2\times C_2,
   \]
   其中 `h(r,c)=(5-r,c)`、`v(r,c)=(r,2n+1-c)`。即使 `n=2`，也不加入对角反射和四分之一转动。这个版本给 A321614 的 `1,4,23,106,…`，候选递推应声明为 `n≥10`。
2. **字面全部几何对称版本**：使用棋盘矩形的完整几何自同构群。除 `n=2` 外群为上述四元群；`n=2` 时为 `D_4`、阶 8。这个版本第 2 项是 14 而不是 23，候选递推只能从 `n≥13` 开始成立（假设已证明 OEIS 尾序列的递推）。

正式定理必须二选一。不能一面说“all symmetry operations”，一面在正方形处静默丢掉四个对称。

## 2. 最大性与无遗漏状态约化

把棋盘分成 `2n` 个互不相交的 `2×2` 块：行带为 `{1,2}`、`{3,4}`，列带为 `{2j-1,2j}` (`1≤j≤n`)。每块是 king graph 中的 clique，所以每块至多一个 king，故总数至多 `2n`。在每个列带的奇列分别放置行 1 和行 3 的 king，得到 `2n` 个互不攻击 king，故独立数确为 `2n`。

因此任何被计数 placement 在每个上述 `2×2` 块恰有一个 king。对一个列带，用

\[
s=(r_t,b_t,r_b,b_b)
\]

编码两个 king；`r_t∈{1,2}`、`r_b∈{3,4}`，`b_t,b_b∈{0,1}` 表示该列带的左/右列。带内互不攻击等价于 `r_b-r_t>1`，所以恰有 12 个状态：

\[
S=\{(r_t,b_t,r_b,b_b):r_t\in\{1,2\},r_b\in\{3,4\},
b_t,b_b\in\{0,1\},r_b-r_t>1\}.
\]

定义 `12×12` 的 0-1 矩阵 `T`：`T_{s,t}=1` 当且仅当把 `s` 放在列 `0,1`、把 `t` 放在列 `2,3` 后，四个 king 两两互不攻击。于是最大 placement 与满足 `T_{s_j,s_{j+1}}=1` 的长度 `n` 状态词双射。这一双射和上面的上界是 transfer 证明的逻辑入口；若证书直接给矩阵却不证明此双射，则有 major gap。

独立重建的 identity 分支为

\[
E_0=1,\qquad E_n=\mathbf1^T T^{n-1}\mathbf1\quad(n≥1),
\]

首项为

\[
E_n=1,12,79,408,1847,7698,30319,\dots\quad(n=0,1,\dots).
\]

## 3. Burnside 固定点分支的独立基准

在状态上定义

\[
\eta(r_t,b_t,r_b,b_b)=(5-r_b,b_b,5-r_t,b_t),
\]

\[
\nu(r_t,b_t,r_b,b_b)=(r_t,1-b_t,r_b,1-b_b),
\qquad \rho=\eta\nu.
\]

`h` 对状态词逐项施加 `η`；`v` 先反转状态词再逐项施加 `ν`；`hv` 先反转再逐项施加 `ρ`。必须验证 `T` 在这些 involution 下不变。

令 `F_η={s:η(s)=s}`、`f_ρ(s)=1_{ρ(s)=s}`，并令

\[
d_ν(s)=T_{s,ν(s)},\qquad d_ρ(s)=T_{s,ρ(s)}.
\]

则四个固定点分支应为：

\[
H_0=1,\quad H_n=\mathbf1_{F_η}^T
T[F_η,F_η]^{n-1}\mathbf1_{F_η}=n+1\quad(n≥1),
\]

\[
V_0=1,\quad V_{2m}=\mathbf1^TT^{m-1}d_ν=3^m\ (m≥1),
\quad V_{2m+1}=0,
\]

\[
R_0=1,\quad R_{2m}=\mathbf1^TT^{m-1}d_ρ\ (m≥1),
\quad R_{2m+1}=\mathbf1^TT^m f_ρ\ (m≥0).
\]

注意 `H_n` 必须使用 induced submatrix `T[F_η,F_η]`（或在每一步投影）；仅写 `f^T T^{n-1}f` 会错误地允许中间状态不固定。

四分支的独立首项为：

| `n` | `E_n` | `H_n` | `V_n` | `R_n` | 四元群轨道数 |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 | 1 |
| 1 | 12 | 2 | 0 | 2 | 4 |
| 2 | 79 | 3 | 3 | 7 | 23 |
| 3 | 408 | 4 | 0 | 12 | 106 |
| 4 | 1847 | 5 | 9 | 31 | 473 |
| 5 | 7698 | 6 | 0 | 52 | 1939 |
| 6 | 30319 | 7 | 27 | 119 | 7618 |

这些值能抓住常见的中心轴、奇偶和负指数错误，但它们本身不是全 `n` 证明。

进一步，四分支生成函数应精确化为

\[
E(x)=\frac{1+3x-x^2}{(1-3x)^2(1-3x+x^2)},\qquad
H(x)=\frac1{(1-x)^2},
\]

\[
V(x)=\frac1{1-3x^2},\qquad
R(x)=\frac{1+x+x^2}{(1-x-x^2)(1-3x^2)}.
\]

四元群 Burnside 给

\[
A(x)=\frac{E(x)+H(x)+V(x)+R(x)}4
=\frac{(1-2x)(1-6x+17x^2-18x^3-2x^4+7x^5+6x^6-3x^7)}{Q(x)},
\]

其中

\[
Q(x)=(1-x)^2(1-3x)^2(1-3x+x^2)(1-x-x^2)(1-3x^2)
\]

\[
=1-12x+54x^2-98x^3-17x^4+346x^5-505x^6
+210x^7+120x^8-126x^9+27x^{10}.
\]

分子与 `Q` 在 `Q[x]` 中 gcd 为 1；所以这不仅证明所列递推从 `n≥10` 成立，还证明约分后的标量生成函数分母确为十次。若只证明某个大矩阵的 characteristic/minimal polynomial，而没有证明起始向量、输出向量和不可见/不可达子空间的消去，则不能推出这一“恰好”。

## 4. `n=2` 的 fatal 分叉及精确反例

对 `4×4` 上的 79 个最大 placement，完整 `D_4` 的八类具体元素固定点数（按 `e,h,v,r^2,r,r^3,d,d'` 排列）为

\[
(79,3,3,7,3,3,7,7).
\]

因此完整几何群轨道数是

\[
\frac{79+3+3+7+3+3+7+7}{8}=14,
\]

而不是 A321614 的 23。OEIS 页面当前确实同时写了 “under all symmetry operations of the rectangle” 和 `a(2)=23`；后者揭示其实际采用的是轴有标记的四元群约定。正式论文不能只引用这句自然语言来回避冲突。

若令 `b_2=14`、其余 `b_n=a_n`，把 Barker 十阶式按原声明用于 `b`，得到：

| `n` | 实际 `b_n` | 递推右端 | 右端减实际 |
|---:|---:|---:|---:|
| 10 | 1,316,944 | 1,318,024 | 1,080 |
| 11 | 4,544,124 | 4,542,990 | -1,134 |
| 12 | 15,474,559 | 15,474,802 | 243 |

故“完整几何群且 `n>9`”是精确反例，不是可忽略的初值美学。该版本的生成函数是 `A(x)-9x^2`，相同齐次递推从 `n≥13` 才恢复。

## 5. 什么才是足够的全 `n` 有限矩阵证书

以下任一路线足够；只验很多项不够。

### 路线 A：从定义重建矩阵并验证 resolvent 恒等式

独立 verifier 应从坐标攻击规则重建 `S,T,η,ν,ρ`，而不是把 discovery 生成的矩阵当作可信输入；然后用整数/有理多项式精确验证：

\[
E(x)=1+x\mathbf1^T(I-xT)^{-1}\mathbf1,
\]

\[
H(x)=1+x\mathbf1_F^T(I-xT[F,F])^{-1}\mathbf1_F,
\]

\[
V(x)=1+x^2\mathbf1^T(I-x^2T)^{-1}d_ν,
\]

\[
R(x)=1+x\mathbf1^T(I-x^2T)^{-1}f_ρ
+x^2\mathbf1^T(I-x^2T)^{-1}d_ρ.
\]

不必信任 CAS 的“化简成功”字符串；可以给每个分支一个多项式向量 `p(x)`，直接检查 `(I-xT)p(x)=D(x)v` 及相应标量内积，或由第二套精确实现重新求解。最后验证 Burnside 和分子/分母交叉相乘恒等式，以及 `gcd(P,Q)=1`。

### 路线 B：可达且可观测商空间

给出一个有理基、有效转移矩阵、初始/输出向量并检查基满秩、转移闭包、初始向量落在该空间、输出等式；再精确检查 `Q(M)=0`（或相应标量 Hankel/minimal realization）以及最小性。由于 `V,R` 使用半长度和奇偶分支，必须显式加入 parity 状态或先改用 `x^2` 的分支生成函数，不能把四个分支错误地都写成同一个 `T^n`。

### 有限项校验何时才可升级成证明

只有先给出一个已证明的有限维线性表示，才能用 Cayley--Hamilton 将“前 `r` 个差分为零”升级为全零；此时还须明确差分序列的状态维数 `r` 和闭包。Berlekamp--Massey、猜分母、验证到 5000 或一百万项，在没有这个先验维数/闭包证书时仍只是发现证据。

证书还应 fail closed：检查状态恰为 12 个、矩阵项全为 0/1、involution 确为置换且平方为恒等、`T` 的对称不变性、全部边界值、精确散列与干净环境复跑。浮点特征值或数值秩不能承担任何决定性步骤。

## 6. 当前 gap 判级

| ID | 缺口 | 严重度 | 通过条件 |
|---|---|---|---|
| R-F1 | `n=2` 到底取四元轴保持群还是完整 `D_4` 未形式化 | **fatal** | 正式定理明确二选一；若取完整群，修正 `a_2` 与递推起点 |
| R-F2 | 当前 `problem/formal_statement.md` 仍为空壳，尚无可审计全称命题 | **fatal** | 写清 `n` 域、`n=0` 约定、群、轨道、递推起点 |
| R-M1 | 必须证明 `2n` 是最大值及 12 状态双射无遗漏/无重复 | **major** | 给出 `2×2` clique 分割上界、构造和双射证明 |
| R-M2 | Burnside 四固定点分支的中心与奇偶条件可能被错误合并 | **major** | 得到本报告的分支公式或等价精确公式，并过首项表 |
| R-M3 | “矩阵算了很多项/猜到 minimal polynomial”不足以证明全 `n` | **major** | 提供第 5 节任一 exact certificate 及独立 verifier |
| R-M4 | “分母恰为十次”还需要排除分子分母消去 | **major**（若声称最小） | 精确 gcd/Bezout 或等价最小 realization 证书 |

## 7. 第二轮针对 builder/根证书的否决测试

后续材料出现后，至少逐项执行：

1. 从攻击关系而不是证书常量重新生成 12 状态与 `T`，比对散列和全部条目。
2. 检查 builder 是否在 `n=2` 静默把“rectangle”当成四元群；若是，要求标题/定理显式写“保持两轴的四元子群”。
3. 分别重算 `(E,H,V,R)` 的 `n=0,…,6`，尤其 `V_1=0,V_2=3,R_1=2,R_2=7`。
4. 检查 horizontal 分支是否错误使用 `f^TT^kf` 而不是 induced submatrix/逐步投影。
5. 检查 odd/even reflection 的中心状态与中心边；禁止负指数掩盖 `n=0,1`。
6. 精确交叉相乘验证四个分支生成函数、总生成函数、展开后的 `Q` 与递推符号。
7. 独立验证 `gcd(P,Q)=1`；若论文只需“递推成立”，应降低“minimal”声称，反之必须补齐。
8. 在干净环境运行 verifier；任何缺依赖、缓存输入、浮点秩或只比较有限项均不得判为 PROVED。

首轮科学状态：**尚未通过（fatal gaps open）**。同时，本报告给出了一个很短的可行修复路线：选择并明确 OEIS 的四元群约定后，12 状态 exact resolvent 证书足以把猜测升级为全 `n≥10` 定理。

---

## 8. 第二轮：builder 与根证书严格复审

复审日期同上。第二轮检查对象：

- `agents/builder_report.md`
- `agents/builder/certificate.json`
- `agents/builder/verify_certificate.py`
- `certificate/a321614_certificate.json`
- `code/verify_certificate.py`
- 修订后的 `problem/formal_statement.md`

### 8.1 两个 verifier 的实际运行结果

已从项目根目录实际运行用户指定的两个命令，并额外做语法编译检查：

```text
$ python3 agents/builder/verify_certificate.py agents/builder/certificate.json
VERIFIED A321614 exact transfer/Burnside certificate
states=12 denominator_degree=10 gcd=1 n2_D2=23 n2_D4=14

$ python3 code/verify_certificate.py certificate/a321614_certificate.json
{"global_dimension": 68, "minimal_denominator_degree": 10,
 "observable_zero_moments": 68, "proof_assistant": false,
 "states": 12, "status": "PASS", ...}

$ python3 -m py_compile agents/builder/verify_certificate.py code/verify_certificate.py
# exit 0
```

本次所审版本 SHA-256：

```text
7cbf65615520b672fed1530157ad510a41b7bb49170b23c4ee1c507d36bef128  agents/builder/certificate.json
c75d00e45f89c3d7f3ae82abab9e0fa7baaec38ff0e2eea3ad3e01d9f9b11a6a  agents/builder/verify_certificate.py
af61e215342a301910f4684ea124f34f99135a1a50a4ff3105e637af7c33de65  certificate/a321614_certificate.json
afef4c0886194f1d01f65a606fbc8ae3065e6fd6ea31ed81564f6e78656d3e65  code/verify_certificate.py
```

两者均只使用 Python 标准库与精确整数/`Fraction` 运算；决定性步骤没有浮点数、随机数或外部 CAS。

### 8.2 两套状态证书不是仅仅“首项碰巧相同”

我另写了一次性只读比较，从根证书的坐标状态直接转换成 builder 的两列 bitmask 状态。所得状态置换为

```text
[7, 3, 6, 0, 10, 4, 8, 1, 11, 5, 9, 2].
```

在此置换下，两个 `12×12` transfer matrix 的全部 144 个条目相等。比较程序还逐项确认：

```text
STATE_AND_TRANSFER_ISOMORPHISM PASS
FINAL_RATIONAL_FUNCTION PASS
identity   [1,12,79,408,1847,7698,30319]
horizontal [1,2,3,4,5,6,7]
vertical   [1,0,3,0,9,0,27]
half_turn  [1,2,7,12,31,52,119]
BOUNDARIES PASS n0=1 n1=4 n2_D2=23 n2_D4=14
```

因此 builder 的“列掩码/显式 resolvent”编码与根证书的“格坐标/全局 68 维表示”编码在定义层确实同构；它们不是两个互不相关的前缀拟合。证明机制又有所不同：前者直接验证四分支有理 resolvent，后者验证一个全局可观测湮灭证书。

### 8.3 Burnside 奇偶分支复审

`agents/builder_report.md` 的反转不变词公式正确：

\[
F^J_{2k}=u^TT^{k-1}d_J\quad(k\ge1),\qquad
F^J_{2k+1}=u^TT^kf_J\quad(k\ge0).
\]

偶数长度的唯一额外条件是中心边 `T_{p,Jp}=1`；奇数长度的中心状态必须满足 `Jp=p`。对纵轴反射，`sum(d_v)=3`、`f_v=0`，所以奇数项全零；对半转，`sum(d_r)=7`、`sum(f_r)=2`。两个 verifier 均从定义重建这些向量，而非信任 JSON 常量。

根证书通过 augmented block 把 `n=0` 单独状态纳入每个分支，再用

\[
M=\begin{pmatrix}0&I\\T_{\rm aug}&0\end{pmatrix}
\]

交织偶、奇子序列。直接检查矩阵乘法可得第 `2k` 次幂读取 even 分支、第 `2k+1` 次幂读取 odd 分支；没有 off-by-one 或负指数漏洞。builder 证书则只给正次数生成函数，最后显式加入常数 1。两种 `n=0` 处理得到相同结果。

horizontal 分支方面，builder verifier 先重建固定状态集和

\[
T_h=\begin{pmatrix}1&0\\1&1\end{pmatrix},
\]

但随后把其简单生成函数写成代码常量；根证书会从该 `2×2` 矩阵自动构造分支表示，独立补上了这一很小的机器检查缺口。因此它至多是 builder verifier 的 local hardening 建议，不构成合并证书的数学缺口。

### 8.4 根证书的 Cayley--Hamilton 逻辑成立

令根证书重建的 `68×68` 整数矩阵为 `B`，输入、输出向量为 `b,ell`。其标量矩为

\[
s_n=\ell^TB^nb=E_n+H_n+V_n+R_n=4a(n).
\]

令生成函数分母对应的反向多项式为

\[
q(t)=t^{10}-12t^9+54t^8-98t^7-17t^6+346t^5-505t^4
+210t^3+120t^2-126t+27
\]

并令 `w=q(B)b`。根 verifier 不信任序列化的 `w`，而是从 `B,b,q` 重算，并精确验证

\[
\ell^TB^kw=0\qquad(0\le k<68).
\]

这 68 个零不是经验外推：由 Cayley--Hamilton，任一 `68×68` 矩阵的所有高次幂均是前 68 次幂的整数/有理线性组合；故上式自动扩展到每个 `k≥0`。这正好给出 `s_n`（从而 `a(n)`）在每个 `n≥10` 的 `q`-递推。这里不要求 `w=0`；`w` 非零但完全不可观测是合法的 scalar annihilator 情形。

一旦全称递推已经由此证明，只用前 10 个系数识别 `Q(x)A(x)` 的分子就是合法的有限步骤。根 verifier 多算到 31 项只是回归保护，不承担全称证明。

### 8.5 分母十次最小性成立

两个 verifier 独立得到同一

\[
N(x)=1-8x+29x^2-52x^3+34x^4+11x^5-8x^6-15x^7+6x^8
\]

和本报告第 3 节的 `Q(x)`。builder verifier 用精确 Euclidean gcd；根证书进一步序列化有理多项式 `U,V`，根 verifier 重算并检查

\[
U(x)N(x)+V(x)Q(x)=1.
\]

所以 `N,Q` 无公共因子，约分后分母确为十次。由有理生成函数的标准唯一性，这证明的是合并后标量序列的最小 eventual 常系数递推阶数，而不是错误地声称 12 维或 68 维矩阵自身的 minimal polynomial 为十次。此项通过。

### 8.6 `n=0,1,2` 与群语义

修订后的 `problem/formal_statement.md` 已明确：对所有 `n≥1` 使用指定的 Klein 四元群，且 `n=2` 仍排除两个对角反射和两个四分之一转动；`n=0` 另定义唯一空 placement、`a(0)=1`。这解决了首轮 R-F1、R-F2。

边界固定点为：

\[
n=0:(1,1,1,1),\qquad n=1:(12,2,0,2),\qquad
n=2:(79,3,3,7).
\]

故四元群轨道数依次为 `1,4,23`。builder verifier 还从 16 格的所有四元素子集重新枚举完整 `D_4`，得到附加固定点 `(3,3,7,7)` 和全群轨道数 14。根证书无需这四个额外操作来证明已修订定理，但 builder/breaker 的独立枚举足以支持形式声明中的警告。

### 8.7 第二轮 gap 判定

对修订后的精确数学命题和当前两套证书：**没有剩余 fatal 或 major 数学缺口**。首轮的 R-F1、R-F2、R-M1、R-M2、R-M3、R-M4 均已解决：

- 群和边界由 formal statement 冻结；
- 最大性与 12 状态双射由 builder 第 1 节给出；
- 奇偶固定词由公式 (5)--(9) 给出；
- 全 `n` 性由 resolvent 恒等式及独立的 68 维可观测 Cayley--Hamilton 证书双重支持；
- gcd/Bezout 排除约分。

仍有以下项目级问题，但应与数学证书结论分开：

1. `proof/gap_ledger.md` 在本次审计时仍把 G02、G03、G04 标成 `open`，尽管它们已分别被 builder 公式、根可观测证书、Bezout 证书解决；`proof/proof_dag.md` 仍为空。按研究治理规则，在根 agent 用准确证据关闭这些条目前，**终态/发布流程仍被文档状态阻断（major governance gap）**。
2. 第二轮审计当时 `paper/main.tex` 仍是占位稿，`audit/PROOF_AUDIT.md` 仍未运行；该历史阻断现已由最终论文、证明审计和 PDF 审计关闭。它从未构成递推定理本身的反例。
3. 最大值“可达到”的构造在 formal statement/builder 报告中只称显然；建议补一句显式坐标 `{(1,2j-1),(3,2j-1):1≤j≤n}`（按一基行号）。这是 local exposition，不是 major gap。

第二轮科学终判：**PASS for the repaired four-operation theorem**。按每块棋盘完整几何群解释的原始自然语言版本仍由首轮第 4 节精确反驳；两种陈述不可混用。未使用 Lean、Coq、Isabelle 或其他证明助手。

---

## 9. Gate 5 独立 no-import 复审与 fail-closed 矩阵

本节是第三轮复审，取代第 8.1 节所列 verifier 代码版本；证书 JSON 的散列未变。根与 builder verifier 已完成 hardening，根 verifier 现会绑定 `claim/board/environment` 元数据并验证三种 involution 的 transfer 恒等式，builder verifier 也已移除会被优化模式关闭的检查并补齐边界/对称性检查。

### 9.1 新的完全独立 verifier

新增：`agents/referee/verify_no_import.py`。该程序满足：

- 只导入 `hashlib/json/math/sys/fractions/pathlib` 标准库，不 import 任何项目模块；
- Python 3.9 兼容；没有 `assert` 或 `int.bit_count()`，所有 correctness gate 都通过显式 `VerificationError` 失败；
- 对证书顶层和每个关键子对象执行 fail-closed key-set 检查；
- 从 king 的 Chebyshev 攻击定义重新生成 12 状态、144 个 transfer 条目、三个 involution、固定状态与中心边向量；
- 从这些定义重新构造四个 Burnside 分支及 `68×68` 全局整数矩阵，并逐项比对序列化矩阵、输入/输出向量与规范 JSON 散列；
- 独立展开 Barker 的 `P,Q`，验证 `w=q(B)b` 与 68 个可观测零矩；
- 从 `n=0,1,2` 起重算 Burnside 边界，并以首 10 项确定 `Q(x)A(x)` 的分子；
- 同时验证序列化 Bezout 恒等式和独立 Euclidean gcd。

决定性的全称推理仍是：`B` 的维数为 68，且

\[
\ell^TB^kq(B)b=0\qquad(0\le k<68).
\]

Cayley--Hamilton 将其推出到每个 `k≥0`。脚本虽重算 22 个序列化边界项以检查输入完整性，但**没有**用 `n≤80` 或任何有限前缀冒充全 `n` 证明。

genuine 命令及关键输出：

```text
$ /usr/bin/python3 agents/referee/verify_no_import.py certificate/a321614_certificate.json
{"all_n_basis":"68 observable zeros plus Cayley-Hamilton", ..., "status":"PASS"}

$ /opt/homebrew/bin/python3 -O -I agents/referee/verify_no_import.py certificate/a321614_certificate.json
{"all_n_basis":"68 observable zeros plus Cayley-Hamilton", ..., "status":"PASS"}
```

两种解释器分别为 Python 3.9.6 与 3.14.7；`py_compile` 在两者下均 exit 0。

### 9.2 负例构造

每轮从 genuine JSON 新建临时副本：

- `badmatrix`：把 `global_representation.matrix[0][0]` 从 0 改成 1；
- `drop-key`：删除顶层 `minimality_bezout`。

对 builder verifier 的额外交叉测试使用同类负例：改变 `transfer_matrix[0][0]`，以及删除 `identity_resolvent`。临时负例不是可信证书，也未写入项目发布树。

no-import verifier 的 12 格 fail-closed 结果：

| Python | 模式 | genuine | badmatrix | drop-key |
|---|---|---:|---:|---:|
| 3.9.6 | normal | PASS / exit 0 | FAIL / exit 1 | FAIL / exit 1 |
| 3.9.6 | `-O -I` | PASS / exit 0 | FAIL / exit 1 | FAIL / exit 1 |
| 3.14.7 | normal | PASS / exit 0 | FAIL / exit 1 | FAIL / exit 1 |
| 3.14.7 | `-O -I` | PASS / exit 0 | FAIL / exit 1 | FAIL / exit 1 |

负例首行输出稳定为：

```text
FAIL: VerificationError: serialized global matrix mismatch
FAIL: VerificationError: certificate keys mismatch: missing=['minimality_bezout'] extra=[]
```

汇总输出：

```text
MATRIX_SUMMARY unexpected=0 expected_pass=4 expected_fail=8
```

我还对 hardening 后的 root 与 builder verifier 做了同一解释器/模式/三输入交叉矩阵，共 24 次：8 个 genuine 均 exit 0，16 个篡改均 exit 1。

```text
CROSS_SUMMARY unexpected=0 expected_pass=8 expected_fail=16
```

另将两者的 genuine 精确证书在两解释器、两模式下各运行一次，8 次均通过：

```text
EXACT_SUMMARY unexpected=0
```

### 9.3 当前审计绑定的 SHA-256

```text
44f15b093e431f96095a02d7c010c51c8836b005f5f679474154c2b5a77a8ddc  agents/referee/verify_no_import.py
afef4c0886194f1d01f65a606fbc8ae3065e6fd6ea31ed81564f6e78656d3e65  code/verify_certificate.py
c75d00e45f89c3d7f3ae82abab9e0fa7baaec38ff0e2eea3ad3e01d9f9b11a6a  agents/builder/verify_certificate.py
af61e215342a301910f4684ea124f34f99135a1a50a4ff3105e637af7c33de65  certificate/a321614_certificate.json
7cbf65615520b672fed1530157ad510a41b7bb49170b23c4ee1c507d36bef128  agents/builder/certificate.json
```

注意：`audit/PROOF_AUDIT.md` 在本轮运行时仍列出一个 builder verifier 的中间散列，必须由根 agent 用上表当前值刷新后才能冻结 release manifest；该文件的旧散列不是本 referee 当前通过的版本。

### 9.4 Gate 5 终判

**PASS**。独立 no-import verifier、修复后的 root verifier 与修复后的 builder verifier 在 Python 3.9/3.14、normal/optimized-isolated 四种运行环境下均接受 genuine 且拒绝两类篡改。全 `n` 逻辑由精确有限维表示、可观测湮灭和 Cayley--Hamilton 封闭；`P/Q` 与 Bezout 最小性也由第三套实现重算。没有新增 fatal 或 major 数学缺口。唯一剩余 release 动作是刷新引用 verifier 散列的审计/manifest 文件。
