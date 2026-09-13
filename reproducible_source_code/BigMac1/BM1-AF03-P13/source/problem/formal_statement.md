# Formal statement

## 1. Objects and notation

Let \(m\in\mathbb Z_{\ge 0}\).  A generalized snake word of **length**
\(m\) is
\[
  \mathbf w=\varepsilon w_1\cdots w_m,\qquad w_i\in\{L,R\}.
\]
The initial symbol \(\varepsilon\) is not counted in the length.  The
associated poset \(P(\mathbf w)\) is the \((2m+4)\)-element poset defined
recursively as in Definition 2.2 of Lee--Vindas-Mel\'endez--Wang:

* \(P(\varepsilon)\) has elements \(\{0,1,2,3\}\) and cover relations
  \(1\prec0,2\prec0,3\prec1,3\prec2\).
* On appending \(w_m\), add \(2m+2,2m+3\), the covers
  \(2m+3\prec2m+1\), \(2m+3\prec2m+2\), and
  \[
  2m+2\prec
  \begin{cases}
  2m-1,&m=1,\ w_m=L,\text{ or }m\ge2,\ w_{m-1}w_m\in\{RL,LR\},\\
  2m,&m=1,\ w_m=R,\text{ or }m\ge2,\ w_{m-1}w_m\in\{LL,RR\}.
  \end{cases}
  \]

For a finite poset \(P\), use the order-polytope convention
\[
 \mathcal O(P)=\{x\in[0,1]^P:x_i\le x_j\text{ whenever }i<_Pj\}.
\]
Its Ehrhart polynomial \(L_{\mathcal O(P)}(t)\in\mathbb Q[t]\) is the
unique polynomial satisfying
\(L_{\mathcal O(P)}(q)=|q\mathcal O(P)\cap\mathbb Z^P|\) for every
\(q\in\mathbb Z_{\ge0}\).  A root is always a complex root counted with
algebraic multiplicity.

For a word of length \(m\), put \(d=2m+4\).  If
\(h^*(\mathbf w;z)=\sum_i h_i^*z^i\), then the normalization used here is
\[
 L(\mathbf w;t)=\sum_{i=0}^{d}h_i^*\binom{t+d-i}{d}.
\]

## 2. Corrected general conjecture

For every \(m\in\mathbb Z_{\ge0}\), every word
\(\mathbf w\in\{\varepsilon\}\times\{L,R\}^m\), and every
\(\rho\in\mathbb C\) such that \(L(\mathbf w;\rho)=0\),
\[
 \boxed{\left|\rho+\frac{m+4}{2}\right|\le \frac{m+2}{2}}. \tag{D_m}
\]
The disk is closed.  Thus equality is allowed and must be certified, not
discarded as a numerical tolerance event.  Theorem 2.9 gives
\(L(\mathbf w;t)=L(\mathbf w;-m-4-t)\), so the disk center agrees with the
proved symmetry center \(-(m+4)/2\).

The published arXiv-v1 display is internally inconsistent: it says that the
word has length \(n+1\), writes a positive center inside the modulus, and in
the same sentence gives the negative symmetry axis.  Statement \((D_m)\) is
the correction explicitly adopted by the user and consistent with Definition
2.1 and Theorem 2.9.  No result below is to be interpreted as proving the
literal inconsistent v1 display.

## 3. Finite endpoint required in this project

The target is the finite universal statement \((D_{10})\):
\[
 \forall\mathbf w\in\{\varepsilon\}\times\{L,R\}^{10},\quad
 \forall\rho\in\mathbb C,\quad
 L(\mathbf w;\rho)=0\Longrightarrow |\rho+7|\le6. \tag{F10}
\]
There are exactly \(2^{10}=1024\) literal words before any symmetry
quotient.  A symmetry quotient is admissible only after an exact proof that
it preserves \(L\); otherwise all 1024 cases remain in the certificate.

For \(m=10\), \(d=24\).  The already-proved factorization and symmetry give
\[
 \prod_{j=1}^{13}(t+j)\mid L(\mathbf w;t),\qquad
 L(\mathbf w;t)=L(\mathbf w;-14-t).
\]
The fixed roots \(-1,\ldots,-13\) lie in the target disk, with \(-1\) and
\(-13\) on its boundary.  Any remaining roots, repeated roots, and the
central root \(-7\) must still be included with their full multiplicities.

## 4. Degenerate and endpoint conventions

* The empty word \(m=0\) is part of the general conjecture but not part of
  the finite endpoint \((F10)\).
* Complementing every \(L/R\) is a proved poset/Ehrhart symmetry in Remark
  2.8 of the source.  Reversal is not assumed here until independently
  proved.
* A numerical root approximation, a modular identity, or a count of tested
  words is not a proof of \((F10)\).  Certification must use exact serialized
  integer/rational data and a verifier that reconstructs the polynomials from
  definitions and fails closed.
