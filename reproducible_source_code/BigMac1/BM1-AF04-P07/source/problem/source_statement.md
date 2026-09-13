# Source statement

# 7. Tournament 中 arc-disjoint transitive triples：确定 \(\nu_3(11)\)

## 定义

对 tournament \(T\)，令：

\[
\nu_3(T)
\]

为最大 pairwise arc-disjoint transitive triples \(TT_3\) 数。

定义：

\[
\nu_3(n)
=
\min_{|T|=n}\nu_3(T).
\]

Yuster 猜测：

\[
\boxed{
\nu_3(n)
=
\left\lceil
\frac{n(n-1)}6-\frac n3
\right\rceil.
}
\]

## 当前边界

早期工作验证到 \(n\le8\)。

2026 年最新公开计算 note 给出 certified：

\[
\nu_3(9)=9,
\qquad
\nu_3(10)=12.
\]

所以下一目标：

\[
\boxed{\nu_3(11)\stackrel{?}=15.}
\]

一个简单三部 blow-up 给出：

\[
\nu_3(11)\le15.
\]

真正要做的是证明每个 11-vertex tournament 都至少能 pack 15 个 arc-disjoint \(TT_3\)。

## AI 路线

- `gentourng` / canonical tournament generation；
- score-sequence pruning；
- modular decomposition；
- exact bit-mask packing；
- packing witnesses；
- 若做不完 9 亿同构类，寻找结构归约定理。

## 注意

2026 的 \(n=9,10\) 结果非常新，因此必须对 \(n=11\) 做额外最新查重。

## 来源

- Yuster / Kabiya–Yuster 关于 tournament packing
- 2026 certified note  
  https://github.com/05oz/certify/blob/main/tt3-paper/note.md
