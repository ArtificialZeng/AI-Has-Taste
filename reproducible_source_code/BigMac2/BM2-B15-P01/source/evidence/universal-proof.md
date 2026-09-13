# Universal cyclic-prefix proof

Status: research proof candidate, not yet independently refereed.  The theorem
below has exactly the frozen scope in `source.md` and `problem.md`; in particular,
all singular matrices are included and the basis is the polynomial basis for an
arbitrary monic irreducible modulus.

## Theorem

For every integer \(n\geq 2\) and every monic irreducible
\(p\in\mathbb F_2[t]\) of degree \(n\), the joint Boolean ANF of

\[
  G(P,u)=\operatorname{adj}(P)J_{n,p}(Pu)
\]

has ordering leap \(L(G)=n\).

## Proof

Index rows, columns, and vector coordinates by \(0,\ldots,n-1\).  For a set
\(A\) of input variables, let \(1_A\) denote its indicator assignment and let

\[
  c_A=\bigoplus_{C\subseteq A}G(1_C)
\]

be its vector ANF coefficient.

First, \(G(P,u)=0\) at every input of Hamming weight less than \(n\).  Indeed,
if \(u=0\), then \(J_{n,p}(Pu)=J_{n,p}(0)=0\).  If \(u\ne0\), fewer than
\(n\) total ones leave at most \(n-2\) nonzero entries in \(P\).  Hence
\(\operatorname{rank}P\le n-2\), every \((n-1)\)-minor of \(P\) vanishes,
and \(\operatorname{adj}(P)=0\).  It follows from the displayed subset-XOR
formula that

\[
  c_A=0\qquad\text{whenever }|A|<n. \tag{1}
\]

Consequently every supported monomial has degree at least \(n\).  In every
ordering of the nonempty support, the first monomial therefore introduces at
least \(n\) variables, so

\[
  L(G)\ge n. \tag{2}
\]

We now construct a supported prefix proving the reverse inequality.  Put
\(\alpha=t\bmod p\), and fix \(i=1\).  Since irreducibility and \(n\ge2\)
give \(p(0)=1\), write

\[
 p(t)=t^n+a_{n-1}t^{n-1}+\cdots+a_1t+1.
\]

In the polynomial basis, division of \(p(\alpha)=0\) by \(\alpha\) gives

\[
 \alpha^{-1}=\alpha^{n-1}+a_{n-1}\alpha^{n-2}
               +\cdots+a_2\alpha+a_1. \tag{3}
\]

Let \(v=J_{n,p}(e_i)\), the coordinate vector of \(\alpha^{-1}\).  If
\(n\ge3\), choose \(r=n-1\); then (3) gives \(v_r=1\), and \(r\ne i\).
If \(n=2\), irreducibility of \(t^2+a_1t+1\) implies
\(a_1=p(1)=1\); choose \(r=0\), so again \(v_r=1\) and \(r\ne i\).

For each \(k\in\{0,\ldots,n-1\}\), define the cyclic permutation
\(\sigma_k(h)=h+k\pmod n\), put \(c_k=\sigma_k(r)\), and set

\[
 A_k=\{p_{h,\sigma_k(h)}:h\ne r\}\ \cup\
     \{u_{\sigma_k(i)}\}. \tag{4}
\]

Each \(A_k\) has exactly \(n\) variables.  At the assignment \(1_{A_k}\),
the matrix \(P^{(k)}\) has a single 1 in position
\((h,\sigma_k(h))\) for every \(h\ne r\), and has zero row \(r\).  Its
missing column is \(c_k\).  Since \(r\ne i\), multiplication by the operand
\(u=e_{\sigma_k(i)}\) gives

\[
 P^{(k)}u=e_i. \tag{5}
\]

The adjugate convention in `problem.md` is
\(\operatorname{adj}(P)_{ab}=\det(P\text{ with row }b\text{ and column }a
\text{ deleted})\).  For \(P^{(k)}\), deleting row \(r\) and column \(c_k\)
leaves a permutation matrix, whose determinant is 1 over \(\mathbb F_2\).
Every other such minor retains the zero row (if its deleted row is not \(r\))
or deletes the unique 1 from one retained row (if its deleted column is not
\(c_k\)).  Therefore, with the transpose orientation explicitly accounted for,

\[
 \operatorname{adj}(P^{(k)})=e_{c_k}e_r^{\mathsf T}. \tag{6}
\]

By (1), all proper-subset evaluations in the coefficient formula for
\(A_k\) vanish.  Equations (3), (5), and (6) now give the exact coefficient

\[
 c_{A_k}=G(1_{A_k})
 =e_{c_k}e_r^{\mathsf T}J_{n,p}(e_i)
 =e_{c_k}v_r=e_{c_k}\ne0. \tag{7}
\]

Thus all \(A_0,\ldots,A_{n-1}\) belong to the joint support.  They are
pairwise disjoint: as \(k\) varies, each matrix variable outside row \(r\)
occurs exactly once in (4), and each operand variable occurs exactly once.
Their union is precisely

\[
 \{p_{hj}:h\ne r,\ 0\le j<n\}\ \cup\ \{u_j:0\le j<n\}. \tag{8}
\]

Order these \(n\) supported monomials first, in any order.  Each introduces
exactly \(n\) variables.  After this prefix, (8) shows that the only unseen
input variables are the \(n\) entries \(p_{r0},\ldots,p_{r,n-1}\).  Append
all remaining supported monomials in any order; each can introduce at most
those \(n\) variables.  Hence this ordering has maximum leap at most \(n\),
so \(L(G)\le n\).  Together with (2), this proves \(L(G)=n\).  \(\square\)

## Scope and checks

- The proof uses no invertibility assumption on \(P\); its witnesses are
  rank-\((n-1)\) singular partial permutation matrices.
- The only modulus-dependent step is (3), which holds for every allowed
  irreducible \(p\); the special quadratic boundary is handled explicitly.
- `evidence/exact_triage.py` independently evaluates the coefficient
  subset sums and the adjugate identities with exact binary arithmetic for
  every irreducible modulus in degrees 2 through 6.  This finite computation
  is corroboration, not a premise of the proof.
- Researcher gap list: none identified.  Independent mathematical review is
  still required by the workflow.
