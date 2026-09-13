# Strict positive square energy for every 2-connected noncycle

This note uses the notation of Akbari--Hu--Liu, arXiv:2609.04069v1.
For a graph with adjacency matrix \(A\), write

\[
A=P-N,\qquad P=A_+\succeq0,\quad N=A_-\succeq0,\quad PN=0,
\]

and

\[
\mu_v(P)=P_{vv}^2+2\sum_{u\ne v}P_{vu}^2.
\]

## Strict triangle lemma

**Lemma.**  If \(S\subseteq V(G)\) is the vertex set of a triangle, then
some \(v\in S\) satisfies \(\mu_v(P)>2\).  No connectedness assumption is
needed.

**Proof.**  Put \(X=P[S]\), and for \(v\in S\) put

\[
\tau_v=P_{vv}^2+2\sum_{u\in S\setminus\{v\}}P_{vu}^2.
\]

Because \(P-A=N\succeq0\), its principal submatrix on \(S\) is
positive semidefinite.  Since \(G[S]=K_3\),

\[
\mathbf1^T X\mathbf1\geq \mathbf1^TA[S]\mathbf1=6. \tag{1}
\]

Apply Cauchy--Schwarz to the six real numbers

\[
P_{vv}\quad(v\in S),\qquad 2P_{uv}\quad(\{u,v\}\in {S\choose2}).
\]

Their sum is \(\mathbf1^TX\mathbf1\), and their squared sum is
\(\sum_{v\in S}\tau_v\).  Hence

\[
36\leq (\mathbf1^TX\mathbf1)^2
   \leq 6\sum_{v\in S}\tau_v. \tag{2}
\]

Suppose, for a contradiction, that \(\mu_v(P)\leq2\) for every
\(v\in S\).  Since \(\tau_v\leq\mu_v(P)\), (2) forces equality throughout:
\(\tau_v=\mu_v(P)=2\) for each \(v\in S\).  Equality in Cauchy--Schwarz,
together with (1), forces all six displayed numbers to equal \(1\).  Thus

\[
X=\begin{pmatrix}
1&1/2&1/2\\
1/2&1&1/2\\
1/2&1/2&1
\end{pmatrix}. \tag{3}
\]

Moreover,

\[
0=\mu_v(P)-\tau_v
 =2\sum_{u\notin S}P_{vu}^2
\]

for every \(v\in S\), so \(P[S,V(G)\setminus S]=0\).  The matrix in
(3) has eigenvalues \(2,1/2,1/2\), hence is invertible.  Taking the
\(S\)-by-\(S\) block of \(PN=0\) now gives

\[
0=(PN)[S,S]=X\,N[S,S],
\]

where the omitted block-product term vanishes because
\(P[S,V(G)\setminus S]=0\).  Consequently \(N[S,S]=0\).  But
\(N=P-A\), while (3) gives \(P_{vv}=1\) and a simple graph has
\(A_{vv}=0\).  Thus \(N_{vv}=1\) for \(v\in S\), a contradiction.
Therefore some \(v\in S\) has \(\mu_v(P)>2\). \(\square\)

## Classification theorem

**Theorem.**  If \(G\) is a finite simple 2-connected graph of order
\(n\) and \(G\) is not a cycle, then

\[
s^+(G)>n.
\]

In particular, the class requested in `source.md` is empty: there is no
2-connected noncycle satisfying \(s^+(G)=|V(G)|\).

**Proof.**  A 2-connected noncycle has \(n\geq4\) and
\(\Delta(G)\geq3\).  If \(G\) is triangle-free, the strict clause of
Akbari--Hu--Liu, Theorem 3.4 (proved from their Lemma 3.3), gives
\(s^+(G)>n\).

Otherwise, choose a triangle with vertex set \(S\).  The strict triangle
lemma supplies \(v\in S\) with
\(\mu_v(P)>2\).  Since \(G\) is 2-connected, \(G-v\) is connected.
The Liu--Tang--Zhang bound (Akbari--Hu--Liu, Theorem 2.1) and the deletion
inequality (their Lemma 2.4) yield

\[
s^+(G)\geq s^+(G-v)+\mu_v(P)
       \geq (n-2)+\mu_v(P)>n.
\]

This covers both cases. \(\square\)

## Dependency and gap audit

- The strict triangle lemma is proved above directly from the spectral-part
  identities \(A=P-N\), \(P,N\succeq0\), and \(PN=0\); it does not assume
  the desired classification; in fact it needs neither connectedness nor a
  proper triangle.
- The classification theorem additionally uses exactly three cited inputs:
  the connected-graph lower bound \(s^+(F)\geq |V(F)|-1\), the vertex-deletion
  inequality, and the source paper's strict triangle-free case.
- All hypotheses are checked: a noncycle in the 2-connected domain has
  \(n\geq4\) and \(\Delta\geq3\), and 2-connectivity makes \(G-v\)
  connected.
- Known proof gaps: none.
