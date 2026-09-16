# Locked formal statement

Locked at 2026-08-30T04:30:22Z after checking arXiv:2603.12462v1,
Definitions (1.1)--(1.2) and Conjecture 5. No convention below is inferred
from the short source statement alone.

## Definitions

For an integer \(n\ge 1\), let
\[
 V_n=\{1,\ldots,n\},\qquad
 E_n=\{\{i,i+1\}:1\le i<n\}
\]
be the undirected path graph \(P_n\), with graph distance
\(d(i,j)=|i-j|\). For \(i\in V_n\) and real \(r\ge0\), put
\[
 B_n(i,r)=\{j\in V_n:|i-j|\le r\}.
\]
For every real-valued \(f:V_n\to\mathbb R\), define the centered graph
Hardy--Littlewood maximal operator by
\[
 (M_{P_n}f)(i)=
 \max_{r\ge0}\frac1{|B_n(i,r)|}
 \sum_{j\in B_n(i,r)}|f(j)|.
\]
The maximum is finite and may equivalently be taken over the integer radii
\(0\le r\le\max\{i-1,n-i\}\). For any \(g:V_n\to\mathbb R\), define
\[
 \operatorname{Var}_{P_n}g=
 \sum_{i=1}^{n-1}|g(i+1)-g(i)|,
\]
so every undirected edge is counted exactly once.

The sharp constant is
\[
 \mathbf C_{P_n}=
 \sup_{\operatorname{Var}_{P_n}f>0}
 \frac{\operatorname{Var}_{P_n}(M_{P_n}f)}
      {\operatorname{Var}_{P_n}f}.
\]
Equivalently it is the least \(C\ge0\) for which the inequality holds for
all real-valued \(f\). Constant inputs have zero variation and map to
constant outputs, so the excluded zero-denominator case imposes no extra
condition.

## Full conjecture under study

For every integer \(n\ge3\),
\[
 \boxed{\mathbf C_{P_n}=1-\frac1n}.
\]

The user-designated first new finite target is the exact assertion
\[
 \boxed{\mathbf C_{P_{11}}=\frac{10}{11}}.
\]
A result about \(P_{11}\) alone is a certified finite result, not a proof of
the full conjecture.

## Exact reductions allowed in the research

1. Since \(M_{P_n}f=M_{P_n}|f|\) and
   \(\operatorname{Var}|f|\le\operatorname{Var}f\), the supremum may be
   restricted to nonnegative inputs \(x\).
2. Let
   \[
   (\mathcal A_n z)(i)=\max_{r\ge0}|B_n(i,r)|^{-1}
   \sum_{j\in B_n(i,r)}z(j)
   \]
   for arbitrary real \(z\). If \(x\ge0\), then
   \(\mathcal A_nx=M_{P_n}x\). Also
   \(\mathcal A_n(z+c\mathbf1)=\mathcal A_nz+c\mathbf1\). Hence every
   nonnegative \(x\) can be replaced by \(z=x-x(1)\mathbf1\), and every
   real \(z\) with \(z(1)=0\) can be shifted upward to a nonnegative input,
   without changing either variation. Thus
   \[
   \mathbf C_{P_n}=
   \max_{\substack{z(1)=0\\\operatorname{Var}z=1}}
   \operatorname{Var}(\mathcal A_nz).
   \]
   This normalized feasible set is compact, since \(|z(i)|\le1\).
3. Positive scaling is removed by \(\operatorname{Var}z=1\). Path reversal
   is the only nontrivial graph relabeling used.

## Sharp lower bound

For the endpoint point mass \(e_1\),
\(\operatorname{Var}e_1=1\) and \(M_{P_n}e_1\) is nonincreasing from
\(1\) to \(1/n\). Consequently
\[
 \operatorname{Var}(M_{P_n}e_1)=1-\frac1n,
\]
so \(\mathbf C_{P_n}\ge1-1/n\) for every \(n\ge2\). Only the matching
upper bound is open in the stated range.

## Statement-repair record

The source wording omitted the definitions of graph balls, the absolute
value inside the averages, the edge-counting convention, the zero case, and
the meaning of “smallest constant.” They are fixed above exactly as in the
cited source. The phrase “interval averages” means graph balls (centered
intervals clipped by the two endpoints), not all uncentered subintervals.
