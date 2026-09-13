# Source statement

# 15. 有限整数字母表上是否存在 infinite additive-square-free word？

## 定义

取有限：

\[
A\subset\mathbb Z.
\]

寻找 infinite word：

\[
a_0a_1a_2\cdots,
\qquad
a_i\in A,
\]

使不存在任何 \(i,\ell\ge1\) 满足：

\[
\sum_{r=0}^{\ell-1}a_{i+r}
=
\sum_{r=0}^{\ell-1}a_{i+\ell+r}.
\]

也就是说，任何相邻等长 blocks 的元素和都不相等。

## 当前状态

这是仍开放的 combinatorics-on-words 问题。

对某些固定 alphabet，最大 finite length 已可精确求出；例如：

\[
\{0,1,2,4\}
\]

上已知最大 finite additive-square-free word 长度为：

\[
62.
\]

但仍未知：

\[
\boxed{
\text{是否存在某个有限整数 alphabet 支持无限 additive-square-free word？}
}
\]

## 为什么适合 AI 发现结构

设 prefix sums：

\[
S_n=\sum_{j<n}a_j.
\]

additive square 等价于：

\[
S_i+S_{i+2\ell}=2S_{i+\ell}.
\]

因此问题等价于：

> 找 bounded-increment infinite integer walk，使其 prefix-sum sequence 不出现等间距 index 上的 3-term arithmetic progression。

这提供了：

- morphism search；
- automatic sequence search；
- substitution invariants；
- finite-state verification；
- SAT-guided grammar search。

## 两条成果路线

### 正面

找到：

- finite alphabet \(A\)；
- substitution / automaton；
- 严格证明其无限 fixed point 无 additive square。

### 负面子结果

证明某个 alphabet size 或某类 substitutions 不可能。

## 来源

https://theoremdb.org/statements/additive-square-finite-alphabet
