# Source statement

# 6. 105 次单位根 minimal vanishing sums：把分类从 weight 19 推到 20

## 问题

令：

\[
\zeta=e^{2\pi i/105}.
\]

寻找：

\[
S\subseteq\mathbb Z/105\mathbb Z
\]

满足：

\[
\sum_{s\in S}\zeta^s=0,
\]

且没有非空 proper subset 也满足零和。

按 affine-Galois equivalence：

\[
S\sim a+uS,
\qquad
a\in\mathbb Z_{105},
\quad
u\in(\mathbb Z_{105})^\times.
\]

## 当前边界

现有 exact cyclotomic + Boolean solving 已完整分类：

\[
\boxed{\text{weight}\le19}.
\]

得到有限个 affine-Galois orbits。

自然下一步：

\[
\boxed{\text{weight }20}.
\]

## 为什么非常适合 AI

把：

\[
X^s\bmod\Phi_{105}(X)
\]

表示为有理向量，得到：

\[
A x=0,
\qquad
x_s\in\{0,1\},
\qquad
\sum_sx_s=20.
\]

再：

- 固定 \(x_0=1\) quotient translation；
- 用 units quotient Galois action；
- 阻止已知 proper zero-sum subsets；
- Z3/SAT enumerate；
- exact minimality check。

## 可能结果

### A. 无解

严格证明不存在 weight-20 minimal vanishing sum。

### B. 有解

完整输出新的 affine-Galois orbit representatives。

两种都是论文级的精确推进。

## 来源

https://theoremdb.org/statements/minimal-vanishing-105th-root-sums
