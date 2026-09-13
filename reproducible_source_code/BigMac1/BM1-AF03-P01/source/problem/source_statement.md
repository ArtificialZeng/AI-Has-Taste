# Source statement

# 1. \(d\)-degree Erdős–Ko–Rado：只剩 \(n=9,10\) 即可解决整个 \((k,d)=(4,3)\) 参数族

设
\[
\mathcal F\subseteq\binom{[n]}k
\]
是 intersecting family，即任意 \(A,B\in\mathcal F\) 满足 \(A\cap B\ne\varnothing\)。对 \(d\)-subset \(S\) 定义
\[
d_{\mathcal F}(S)=|\{F\in\mathcal F:S\subseteq F\}|,
\qquad
\delta_d(\mathcal F)=\min_{|S|=d}d_{\mathcal F}(S).
\]

Huang–Zhang 的 Conjecture 4.1 预测，对 \(k>d\ge0,\ n\ge2k+1\)，
\[
\boxed{
\delta_d(\mathcal F)\le
\binom{n-d-1}{k-d-1}.
}
\]

2026 年他们证明了 \(d\ge2\) 且
\[
n\ge2k+2d-3
\]
时成立；母猜想对 \(d=0,1,2\) 也已有结果。

固定
\[
(k,d)=(4,3),
\]
右侧为
\[
\binom{n-4}{0}=1.
\]
因此需要证明：任意 intersecting \(\mathcal F\subseteq\binom{[n]}4\)，都有某个三元组只被至多一个成员包含。

一般定理已经覆盖
\[
n\ge 2(4)+2(3)-3=11,
\]
而母猜想从 \(n\ge9\) 开始。因此：
\[
\boxed{\text{只剩 }n=9,10.}
\]

## AI 攻击方式

对每个 \(E\in\binom{[n]}4\) 设 Boolean variable \(x_E\)。

若 \(E\cap E'=\varnothing\)，加约束
\[
\neg x_E\lor\neg x_{E'}.
\]

若要寻找反例，则要求每个 triple \(S\) 满足
\[
\sum_{E\supset S}x_E\ge2.
\]

- SAT：输出反例 family，几行代码即可独立验证。
- UNSAT：必须输出 LRAT/VeriPB 或等价严格证书。

若 \(n=9,10\) 都 UNSAT，就得到
\[
\boxed{
\delta_3(\mathcal F)\le1
\quad\forall n\ge9,
}
\]
即完整关闭 \((k,d)=(4,3)\) 参数族。

## 来源

Hao Huang, Yi Zhang, *On a \(d\)-degree Erdős–Ko–Rado Theorem*  
https://arxiv.org/abs/2407.14091

正式发表于 *Journal of Combinatorial Theory, Series A* 221 (2026), 106163.

---
