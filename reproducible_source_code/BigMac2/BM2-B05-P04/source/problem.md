# Precise problem statement

## Frozen original statement

The immutable source is `source.md` (SHA-256
`22a14216f9374c837488416f68108a80987295e36c90137e98e25ff0619a2105`).
Its mathematical statement is reproduced verbatim here:

> ## DM05-04 循环图的 $\operatorname{Inc}(\mathbb N)$ edge-ideal chain 猜想
>
> 令 $n\ge6,r\ge0$，$C_n$ 是顶点集 $[n]$ 上的循环图，并令
> $$
> I_{n+r}:=\operatorname{Inc}(\mathbb N)_{n,n+r}(I(C_n))\subset R_{n+r}=k[x_1,\ldots,x_{n+r}].
> $$
> 证明或反驳以下完整充要分类：
> $$
> R_{n+r}/I_{n+r}\text{ is Cohen--Macaulay}
> \iff
> r\ge\left\lfloor\frac{n-4}{2}\right\rfloor\ \text{and}\ r\ne n-4.
> $$
>
> 陈述对任意域 $k$ 的依赖必须明确处理；若结论随 characteristic 改变，应给正确分支。有限 Macaulay2 表只算证据，普遍正方向须给 shelling/Reisner 等完整证明，反方向须给 purity、link homology 或其他精确障碍。
>
> 来源与范围：Anwar--Ghayas--Javed, *Cohen--Macaulayness of $\mathrm{Inc}(\mathbb N)$-Invariant Chains of Edge Ideals*, arXiv:2609.03566v1, Theorem 3.14 and Conjecture 3.15（PDF pp. 14--15）。来源证明 $r\ge n-3$ 时该 graph 已为 complete graph，且以计算和 gap 结构明确提出上述完整分类。

No correction or weakening of this statement is being made.

## Definitions and unambiguous notation

All numerical parameters below are integers. Fix a field $k$, $n\ge 6$, and
$r\ge 0$, and put $m=n+r$ and $R_{m,k}=k[x_1,\dots,x_m]$ with its standard
grading.

- $[q]=\{1,\dots,q\}$.
- $C_n$ is the simple cycle on $[n]$ with
  $$
  E(C_n)=\{\{i,i+1\}:1\le i\le n-1\}\cup\{\{1,n\}\}.
  $$
- Its edge ideal is
  $$
  I_k(C_n)=(x_ix_j:\{i,j\}\in E(C_n))\subseteq k[x_1,\dots,x_n].
  $$
- $\operatorname{Inc}(\mathbb N)_{n,m}$ is the set of all strictly increasing
  injections $\pi:[n]\to[m]$. Such a $\pi$ acts by the $k$-algebra map
  $x_i\mapsto x_{\pi(i)}$.
- To expose the dependence on the base cycle (which the source notation
  $I_{n+r}$ suppresses), define
  $$
  J_{n,r,k}:=
  \sum_{\pi\in\operatorname{Inc}(\mathbb N)_{n,m}}
       \pi(I_k(C_n))R_{m,k}.
  $$
  Thus the source's $I_{n+r}$ means $J_{n,r,k}$ for the specified pair
  $(n,r)$; it is not being identified with an ideal obtained from a different
  base value of $n$ having the same terminal index $m$.
- A standard graded $k$-algebra $A$ is Cohen--Macaulay when
  $\operatorname{depth}A=\dim A$ (equivalently, after localization at its
  homogeneous maximal ideal).

Equivalently, $J_{n,r,k}$ is the edge ideal of the graph $G_{n,r}$ on $[m]$
whose edges have the exact gap description
$$
\{a,b\}\in E(G_{n,r}),\quad a<b
\quad\Longleftrightarrow\quad
b-a\le r+1\ \text{ or }\ b-a\ge n-1.
$$
Indeed, the first range consists of images of a consecutive edge of $C_n$,
and the second consists of images of its wrap edge $\{1,n\}$. Hence
$$
\{a,b\}\notin E(G_{n,r})
\quad\Longleftrightarrow\quad
r+2\le b-a\le n-2. \tag{1}
$$
Let $\Delta_{n,r}=\operatorname{Ind}(G_{n,r})$. Then
$$
\Delta_{n,r}
=\bigl\{S\subseteq[m]:
  r+2\le b-a\le n-2\text{ for every }a<b\text{ in }S\bigr\},
$$
with the pairwise condition vacuous for $|S|\le1$, and
$R_{m,k}/J_{n,r,k}=k[\Delta_{n,r}]$.

## Fully quantified claim to prove or disprove

The frozen classification is read as the uniform assertion
$$
\boxed{
\forall k\text{ a field}\;\forall n\in\mathbb Z,\ n\ge6\;
\forall r\in\mathbb Z,\ r\ge0:\quad
k[\Delta_{n,r}]\text{ is Cohen--Macaulay over }k
\iff
r\ge\Big\lfloor\frac{n-4}{2}\Big\rfloor
\text{ and }r\ne n-4.}
$$
Thus every asserted positive case requires a proof valid over every field.
If reduced homology (including link homology) produces characteristic-dependent
behavior, then the displayed field-independent assertion is false as written;
a resolution must state the correct branch for each possible characteristic.
Finite computations alone do not discharge either universal direction.

The scope includes the boundary $n=6$ and $r=0$ and excludes all $n<6$.
The two sides of the biconditional require both:

1. non-Cohen--Macaulayness for
   $0\le r<\lfloor(n-4)/2\rfloor$ and for $r=n-4$; and
2. Cohen--Macaulayness for
   $\lfloor(n-4)/2\rfloor\le r\le n-5$ and for $r\ge n-3$.

## Source status, nearest result, and proposed delta

Primary source checked: Anwar--Ghayas--Javed, arXiv:2609.03566v1
(submitted 2026-09-03), Definitions 2.9--2.10, Lemma 3.13, Theorem 3.14,
and Conjecture 3.15; HTML retrieved 2026-09-06 from
<https://arxiv.org/html/2609.03566v1>.

Theorem 3.14 proves the positive range $r\ge n-3$: equation (1) then has an
empty gap interval, so $G_{n,r}=K_m$, whose independence complex is
zero-dimensional and Cohen--Macaulay over every field. The source states the
full biconditional as Conjecture 3.15 and gives computations plus the gap
structure, including the exceptional $r=n-4$ case, as evidence. A narrow
exact-assertion search on 2026-09-06 returned this preprint but no separate
resolution; that search is not a proof of novelty or open status.

Target contribution: settle the frozen biconditional, with the nearest proved
result being Theorem 3.14 and the delta being all remaining parameter ranges
and explicit field dependence. The natural exact verifier is a facet/link
analysis of the interval-gap complex $\Delta_{n,r}$, followed by shellability
or Reisner's criterion in positive cases and purity or homology obstructions in
negative cases.
