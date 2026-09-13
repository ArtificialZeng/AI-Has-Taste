# Formal statement

## Basic objects

Let \(\mathbb N=\{1,2,\ldots\}\), with matrix coordinates: row numbers
increase downward and column numbers increase to the right. A **straight
shape** is a finite order ideal \(\lambda\subset \mathbb N^2\) for the
coordinatewise order. Equivalently it is a partition
\(\lambda=(\lambda_1\geq\cdots\geq\lambda_r>0)\). The empty partition is
allowed. We identify a partition with its set of boxes.

For partitions \(\lambda,\nu\), write \(\lambda\subseteq\nu\) when
\(\lambda_i\leq\nu_i\) for every \(i\), after appending zero parts. If
\(\lambda\subseteq\nu\), the closed Young-lattice interval is

\[
  [\lambda,\nu]
  :=\{\mu:\mu\text{ is a partition and }
            \lambda\subseteq\mu\subseteq\nu\}.
\]

An **increasing tableau** is a map \(T:\lambda\to\mathbb N\) whose entries
strictly increase from left to right in each row and from top to bottom in each
column. Its shape is \(\operatorname{sh}(T)=\lambda\). Its alphabet is the
finite set \(\operatorname{im}(T)\). It is **initial on \([n]\)** when
\(\operatorname{im}(T)=[n]=\{1,\ldots,n\}\). The unique empty tableau is
initial on \([0]=\varnothing\).

The row word \(\operatorname{row}(T)\) reads each row from left to right,
starting with the bottom row and proceeding upward. K-Knuth equivalence
\(\equiv_K\) is the least equivalence relation on finite words in
\(\mathbb N\) that is a monoid congruence and contains

\[
\begin{aligned}
 xzy&\equiv_K zxy &&(x<y<z),\\
 yxz&\equiv_K yzx &&(x<y<z),\\
 x&\equiv_K xx,\\
 xyx&\equiv_K yxy &&(x,y\in\mathbb N).
\end{aligned}
\]

The last rule includes \(x=y\), where it is redundant; the primitive-pair
algorithm may therefore restrict it to \(x\ne y\). Tableaux are K-Knuth
equivalent when their row words are:
\(S\equiv_K T\iff\operatorname{row}(S)\equiv_K\operatorname{row}(T)\).
Each word move preserves the set of distinct letters, so each tableau class has
a fixed alphabet.

## Original conjecture (all finite alphabets)

For every finite K-Knuth equivalence class \(\mathcal C\) of straight
increasing tableaux, define

\[
  \Sigma(\mathcal C)=
  \{\operatorname{sh}(T):T\in\mathcal C\}.
\]

Conjecture 7.6 asserts that, for every \(\mathcal C\) and every comparable pair
\(\lambda,\nu\in\Sigma(\mathcal C)\) with \(\lambda\subseteq\nu\),

\[
  [\lambda,\nu]\subseteq\Sigma(\mathcal C).
\]

No condition is imposed by an incomparable pair. Repeated endpoint shapes and
the degenerate interval \([\lambda,\lambda]=\{\lambda\}\) are included and are
automatic. For the empty endpoint \(n=0\), the only tableau has empty shape,
so the assertion is also automatic.

## Finite endpoint investigated here

Let \(\mathcal T_n^{\rm init}\) be the set of all initial straight increasing
tableaux on \([n]\). The exact \(n=8\) endpoint is:

> For every K-Knuth component \(\mathcal C\) of
> \(\mathcal T_8^{\rm init}\), every comparable
> \(\lambda,\nu\in\Sigma(\mathcal C)\), and every partition \(\mu\),
> if \(\lambda\subseteq\mu\subseteq\nu\), then there exists
> \(U\in\mathcal C\) with \(\operatorname{sh}(U)=\mu\).

This is a finite statement. Every tableau on any eight-element ordered
alphabet standardizes order-preservingly to an initial tableau on \([8]\);
standardization preserves shape and commutes with all four K-Knuth relations.
Thus the displayed endpoint covers arbitrary alphabets of cardinality eight.
Tableaux on a proper subset of \([8]\) standardize to a smaller endpoint and
are covered by the reproduced \(n\leq7\) baseline.

Every \(T\in\mathcal T_n\) has shape contained in the staircase
\((n,n-1,\ldots,1)\), since the entry in box \((i,j)\) is at least
\(i+j-1\). Hence all sets in the finite endpoint are genuinely finite.

## What constitutes a certificate

A positive \(n=8\) result requires a complete canonical enumeration of
\(\mathcal T_8\), the exact connected components given by the proven finite
Algorithm 1 of Gaetz et al., and an exact interval check, all reconstructed by
an independent fail-closed verifier from serialized data. A negative result
requires two tableaux in one certified component with comparable endpoint
shapes and a proof that no tableau of a specified intermediate shape lies in
that component. Merely exhibiting K-Knuth paths to the endpoints does not
certify the global absence claim.
