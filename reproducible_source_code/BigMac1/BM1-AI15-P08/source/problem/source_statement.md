# Source statement

# 8. Sheil-Small 自反多项式 covering problem

## 问题

设

\[
P(z)=\sum_{k=0}^n a_kz^k
\]

是 self-inversive polynomial，即零点关于

\[
\zeta\mapsto\frac1{\bar\zeta}
\]

不变。令

\[
A=\max_k|a_k|.
\]

是否总有：

\[
P(\mathbb D)
\]

包含某个半径为 \(A\) 的开圆盘？

这是 Hayman–Lingham *Research Problems in Function Theory* 中长期未解决的 Problem 4.24。

## 为什么 AI 有机会

不是一上来证明所有次数。先做真正有发表价值的最低阶分界：

1. 完全解决 \(n=2,3,4,5\)；
2. 直接搜索最低次数反例；
3. 如果低次全部成立，从 extremal polynomial 猜一般不等式。

self-inversive 条件把自由系数约减半，边界像

\[
P(e^{it})
\]

又是强对称三角多项式。

## 证书

若找到反例，应给：
- exact algebraic coefficients；
- 自反条件精确验证；
- 用 interval arithmetic / algebraic curve geometry 证明其 image 的 inradius \(<A\)。

## 来源

- 当前问题页  
  https://api.scinet.pub/p/11ff995d-348a-4fda-93d6-a23c6cee26aa
- Hayman & Lingham, Problem 4.24.

---
