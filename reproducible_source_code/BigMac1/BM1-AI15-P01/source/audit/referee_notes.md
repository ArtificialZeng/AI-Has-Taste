# Gate 5 独立 referee 审计

日期：2026-08-29（Asia/Shanghai）  
角色：从定义重建，不以原论文的数值结论或 discovery 输出为前提。

## 最终裁决

展示矩阵“在 \(\mathbb R\) 上不存在 rank-\((2,2)\) Hadamard
分解”这一矩阵特定命题是 **假的**。存在手算可验的有理分解，因此任何仍将该矩阵称为实反例、或仍尝试给出逐零模式不可行证书的结论，都有一个不可修补的 fatal error。

这只推翻矩阵特定的不存在性断言；它既不证明、也不推翻下面的全称命题：

\[
 \forall M\in\mathbb R^{4\times4},\quad
 \det M\ne0\Longrightarrow
 \exists A,B\in\mathbb R^{4\times4}:\ 
 M=A\circ B,\quad \operatorname{rank}A,\operatorname{rank}B\le2.
\]

若项目采用终态 `DISPROVED`，标题和结论必须明确说被推翻的是“所展示候选的不可分解性”，而不是上述全称问题。

## 1. 从定义独立重建

目标矩阵是

\[
M=\begin{pmatrix}
1&1&1&1\\
1&1&1&0\\
0&1&0&0\\
1&0&0&0
\end{pmatrix},\qquad \det M=1.
\]

因此它确为满秩。一般秩不等式

\[
\operatorname{rank}(A\circ B)
 \le \operatorname{rank}(A)\operatorname{rank}(B)
\]

说明：若它有秩至多二的两因子，则两个因子的秩必都恰为二。满秩条件对排除 rank-0/rank-1 边界有用，但不是下述显式分解成立的前提。

referee 独立得到的一个有理见证（与项目中两个序列化见证均不同）为

\[
A=\begin{pmatrix}
1&1&1&1\\
1&2&3&3\\
2&1&0&0\\
1&\tfrac12&0&0
\end{pmatrix},\qquad
B=\begin{pmatrix}
1&1&1&1\\
1&\tfrac12&\tfrac13&0\\
0&1&\tfrac43&2\\
1&0&-\tfrac13&-1
\end{pmatrix}.
\]

逐行相乘立即得到 \(A\circ B=M\)。写 \(A_i,B_i\) 为第
\(i\) 行，则

\[
A_3=3A_1-A_2,\qquad
A_4=\tfrac12(3A_1-A_2),
\]

以及

\[
B_3=2B_1-2B_2,\qquad
B_4=-B_1+2B_2.
\]

故两因子秩至多二。它们左上 \(2\times2\) 子式分别为
\(1\) 和 \(-\tfrac12\)，故秩又至少二。所有等式均在
\(\mathbb Q\) 中成立，无浮点、极限或紧致性步骤。

独立 SymPy 1.13.3 精确复算还给出：\(\det M=1\)，三矩阵秩依次为
\(4,2,2\)，两个因子的全部 16 个 \(3\times3\) 子式均为零，且
Hadamard 差为零矩阵。手算行关系已经足够；该 CAS 计算只是交叉核对。

## 2. 三参数族及所有除法条件

项目 proof-builder 给出的族是正确的。令 \(x,y,z\in\mathbb R\)
两两不同且均非零，并置

\[
\mathbf1=(1,1,1,1),\quad
a=(x,y,z,z),\quad
b=(x^{-1},y^{-1},z^{-1},0).
\]

定义

\[
\begin{aligned}
&A_1=B_1=\mathbf1,\quad A_2=a,\quad B_2=b,\\
&A_3=A_4=a-z\mathbf1,\\
&B_3=\frac{xy}{(y-z)(x-y)}(b-x^{-1}\mathbf1),\\
&B_4=\frac{xy}{(x-z)(y-x)}(b-y^{-1}\mathbf1).
\end{aligned}
\]

逐项所需分母只有
\(x,y,z,x-y,y-z,x-z\)。假设“两两不同且均非零”恰好保证它们
全非零；没有遗漏 \(z=1\) 一类额外条件。取 \((x,y,z)=(1,2,3)\)
给出 `certificates/builder_counterexample.json` 中的见证。此时
\(\mathbf1\) 与 \(a\)、\(\mathbf1\) 与 \(b\) 分别线性无关，故
两因子都恰为 rank 2，而不是只证明了 rank \(\le2\)。

## 3. support、零模式与尺度约化审计

目标的 1 位共有 9 个，零位恰为

\[
(2,4),(3,1),(3,3),(3,4),(4,2),(4,3),(4,4).
\]

在 1 位上必有 \(a_{ij}\ne0\ne b_{ij}\)，且
\(b_{ij}=a_{ij}^{-1}\)。在每个零位上，条件是
\(a_{ij}=0\) **或** \(b_{ij}=0\)。所以 7 个零位的 \(2^7\) 个
二叉选择确实覆盖解集，但仅在每个分支“只强制所选一侧为零、另一侧
保持任意”时才完备。若分支代码强制 exactly one zero、或把未选一侧
强制为非零，就会漏掉双零交叉层。

该候选的 support 二部图有 8 个顶点、9 条边且连通。可以用成对行列
尺度

\[
a'_{ij}=r_i c_j a_{ij},\qquad
b'_{ij}=r_i^{-1}c_j^{-1}b_{ij}
\]

沿一棵 7 边生成树正规化 7 个 \(A\) 的 support 条目。这些条目由
\(M_{ij}=1\) 保证非零，所以除法安全；不能用目标零位上的条目做同样
的除法。生成树外留下两个 cycle 参数。交换 \(A,B\) 可以配对部分
分支，但若用它减少枚举，必须显式给出分支轨道与固定点；任意行列置换
只有在同时保持目标矩阵或把目标送到明确等价问题时才可商掉。

本见证落在合法分支

\[
B_{24}=B_{31}=B_{42}=0,\qquad
A_{33}=A_{34}=A_{43}=A_{44}=0.
\]

任何 support obstruction 若排除此分支，必然使用了错误的 exactly-one
假设、错误的尺度除法或错误的 genericity 假设。

## 4. rank 条件与边界退化

对 \(4\times4\) 矩阵，rank \(\le2\) 当且仅当全部 16 个
\(3\times3\) 子式为零；这是一组闭的多项式条件，不需要额外不等式。
rank 恰为二可由一个非零 \(2\times2\) 子式认证。

因此：

- 直接 minor 建模不会漏掉 rank-0/rank-1 边界；
- 用 \(GH^\mathsf T\) 参数化 rank \(\le2\) 也是满射，但不得预先假定
  \(G,H\) 满列秩来“证明”不存在低秩边界；
- 在本见证中，非零 \(2\times2\) 子式已独立排除边界；
- 从 \(\det M\ne0\) 和秩不等式也可反推任何可行因子必须恰为 rank 2。

## 5. 矩阵转录与来源范围

arXiv:2508.14901v1 的 Example 5 确实显示与本项目逐项相同的矩阵；其
摘要和第 4.3 节只声称对 \(\mathbb R\) 有强数值证据，第 7.1 节把实数
解析证明列为开放问题。故这里不是转录错误，也不能把论文中的
“optimizer 未找到”提升为不可行性。

论文 Theorem 6 关于 \(\mathbb Z\) 的文字证明只说枚举 1 位上的
\(2^k\) 个符号。按文面，这没有处理零位选择，也没有处理零乘积中未被
置零一侧的任意整数填充值；若无另一个可复核程序或补充引理，这段文字
本身不足以认证整数不可分解。当前有理见证并不直接否定整数结论，但也
不能替原论文补上这个缺口。

## 6. 两个序列化 verifier 的复核与信任边界

实际运行：

```text
python verifier/verify_rational_decomposition.py certificates/rational_decomposition.json
PASS; det(M)=1; rank(A)=rank(B)=2

python certificates/builder_verify_counterexample.py certificates/builder_counterexample.json
PASS; det(M)=1; A/B 的全部 16 个 3x3 minors 为零，并找到非零 2x2 minors
```

另外用未导入这两个 verifier 的短 `fractions.Fraction` 高斯消元程序从
两份 JSON 重新读入，得到两份证书均满足
\(A\circ B=M\) 且秩为 \((4,2,2)\)。两份见证彼此不同；上文又给出
第三个手算见证。

信任边界如下：

1. 两个 verifier 都信任同一 CPython 标准库、`Fraction`、JSON 解析器
   和本地文件系统；它们不是两个不同证明助手或两个不同 CAS。
2. 两者的 determinant/minor 代码结构相近，因此“两个程序”不能自动
   解释为完全独立的软件栈。主 verifier 另用高斯消元及显式
   \(A=UV,B=XY\) 给出第二种秩计算；手算行关系则给出不依赖 determinant
   实现的数学复核。
3. SHA-256 输出把某次运行绑定到输入与代码字节，但不会认证 Python
   解释器、操作系统，也不会自行形成供应链证明；发布时仍需 release
   manifest 和洁净环境日志。
4. 对如此短的有理证书，人工逐项检查已经是决定性的；未使用证明助手
   不是数学缺口，但必须如实披露。

## 7. gap 裁决

| ID | 断言或步骤 | 裁决 | 严重度 | 理由/修复 |
|---|---|---|---|---|
| R-F1 | 展示矩阵在 \(\mathbb R\) 不可分解 | **false** | fatal | 上述有理见证直接反驳；必须删除不可行性结论。 |
| R-F2 | 从该见证推出“所有满秩 \(4\times4\) 实矩阵都可分解” | **未证明** | fatal（若声称） | 一个正例不解决全称命题；严格限制结论范围。 |
| R-M1 | 三参数族对所有所述参数有定义 | **通过** | resolved | 两两不同且非零覆盖全部分母；\((1,2,3)\) 非退化。 |
| R-M2 | 目标矩阵满秩且转录正确 | **通过** | resolved | \(\det M=1\)，并与 arXiv v1 Example 5 逐项一致。 |
| R-M3 | 两因子 rank \(\le2\) / rank \(=2\) | **通过** | resolved | 行关系、非零 2x2 子式、全 3x3 minors 三重核对。 |
| R-M4 | 零模式分支完备 | **条件通过** | major（对不存在性枚举） | 只有“所选侧=0、另一侧任意”的 128 分支完备；当前正例已使不可行性枚举失去必要性。 |
| R-M5 | 原论文的整数不可分解证明可直接复用 | **未通过** | major | 论文文字未覆盖零位另一因子的任意整数完成；需独立证书。 |
| R-L1 | 两个 Python verifier 完全软件独立 | **不成立但不致命** | local | 共享 CPython/Fraction；短证书另有人工行关系和不同见证。 |
| R-L2 | 全部 2026-08-29 前文献均未包含此分解 | **只能有界陈述** | major（若声称绝对 novelty） | 有限数据库检索不是全局无发现证明；采用 `literature/referee_search_log.md` 的限定措辞。 |

在结论严格限定为“该候选不可分解性被一个显式有理分解推翻”时，数学
端点通过 referee 审计；若结论扩大到全称问题或“首个绝对已知”而没有
进一步证据，则不通过。
