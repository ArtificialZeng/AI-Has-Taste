# Source statement

# 14. 中心超立方体截面：先完整解决 \(Q_5\) 的局部极值分类

令
\[
Q_n=[-\tfrac12,\tfrac12]^n,
\]
对 unit normal \(v\in S^{n-1}\) 定义
\[
\sigma(v)=\operatorname{Vol}_{n-1}(Q_n\cap v^\perp).
\]

若 \(v\) 的非零坐标绝对值相等，对应 section 称 diagonal。

Ambrus–Gárgyán Conjecture 1.3：
\[
\boxed{
Q_n\text{ 的所有 locally extremal central sections 都是 diagonal。}
}
\]

他们证明：
- 对所有 \(n\ge4\) 存在 non-diagonal critical sections；
- 但其构造都是 saddle points；
- 尚无 non-diagonal local extrema。

\(n=4\) 的 critical directions 已完整分类：除 diagonal 外，唯一非对角类型是
\[
(1,1,2,2)/\sqrt{10},
\]
并且 Hessian indefinite。因此
\[
\boxed{n=5}
\]
是自然的第一个完整未知局部极值分类。

## AI 路线

利用 sign changes 与 \(S_5\) symmetry 约化到
\[
a_1\ge a_2\ge\cdots\ge a_5\ge0.
\]

按 subset-sum hyperplanes 分 chamber。在每个 chamber：
1. 写出 section volume 的显式分片表达；
2. 解 critical equations；
3. exact Hessian signature；
4. 分类所有 critical points。

反例：一个 non-diagonal algebraic \(v\) 且 Hessian definite。  
正面：证明每个 non-diagonal critical point 都 Hessian indefinite。

## 来源

Gergely Ambrus, Barnabás Gárgyán, *Non-diagonal critical central sections of the cube*, Advances in Mathematics 441 (2024), 109524.  
https://arxiv.org/abs/2307.03792

---
