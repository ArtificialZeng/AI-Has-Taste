# Builder/Reduction reconstruction for \(R_n^{(1,2)}\)

## 1. Primary-source reconstruction and version control

The primary source used here is John Lentfer, *A conjectural basis for the
\((1,2)\)-bosonic-fermionic coinvariant ring*, **Algebraic Combinatorics** 8
(2025), no. 3, 711--743, DOI 10.5802/alco.424. The publisher records receipt
on 2024-08-09, revision on 2025-02-19, acceptance on 2025-02-24, and online
publication on 2025-06-26. The exact source locations relevant to this branch
are:

| Item | Published location |
|---|---|
| General \(R_n^{(k,j)}\), diagonal action, and supercommutation | p. 712, equation (1) and the paragraph immediately following it |
| Specialization to \(R_n^{(1,2)}\) | p. 713, paragraph beginning “The ring \(R_n^{(1,2)}\)” |
| Modified Motzkin paths and their weights | p. 715, opening of Section 2 and Definition 2.1 |
| Super-Artin set | p. 716, Definition 2.3 |
| Generalized \(\alpha\)-sequence and candidate set | p. 717, Definition 3.1 |
| Basis conjecture and verified range | p. 717, Conjecture 3.2 and Remark 3.3 |
| Candidate Hilbert series and cardinality | p. 719, Proposition 3.6 and Theorem 3.7 |

The latest arXiv source as of 2026-08-29 is arXiv:2406.19715v3, dated
2026-04-07, later than the journal publication. In the v3 TeX source the same
items occur at lines 393--396 (general ring), 429--430 (the \((1,2)\) ring),
473--493 (modified Motzkin paths), 614--620 (generalized \(\alpha\) and candidate),
706--711 (Conjecture 3.2 and the \(n\leq4\) report), and 727--768 (candidate
Hilbert series and cardinality). Comparing v3 with the v2/journal source shows
no change to these definitions or to the reported range \(n\leq4\). The v3
archive consists only of a TeX file, a BBL file, and arXiv's README metadata; it
does not contain verification code.

The paper does **not** state a term order, a Gröbner basis for the
\((1,2)\)-ideal, or the algorithm/certificate used for Remark 3.3. Therefore
“the 1920 candidates are exactly the standard monomials” is not a claim made in
the source and has no source-defined term order. It is a possible additional
route, not a faithful restatement of Conjecture 3.2.

## 2. Exact algebra and sign convention

Work first over \(\mathbb Q\); scalar extension to \(\mathbb C\) preserves every
rank below. Put

\[
A_n=\mathbb Q[x_1,\ldots,x_n]\otimes
\bigwedge_{\mathbb Q}\langle\theta_1,\ldots,\theta_n,
\xi_1,\ldots,\xi_n\rangle .
\]

The \(x_i\) are even and commute with every generator. All \(\theta_i,\xi_i\)
are odd, so any two odd generators anticommute and every odd generator squares
to zero. The action of \(\sigma\in S_n\) is the even algebra automorphism

\[
\sigma(x_i)=x_{\sigma(i)},\qquad
\sigma(\theta_i)=\theta_{\sigma(i)},\qquad
\sigma(\xi_i)=\xi_{\sigma(i)}.
\]

Let \(A_n^{S_n,+}\) be the direct sum of all positive total multidegrees in the
invariant algebra. The Hilbert ideal and ring are

\[
I_n=A_n A_n^{S_n,+},\qquad R_n^{(1,2)}=A_n/I_n.
\]

The implementation uses canonical monomials

\[
x^a\theta_T\xi_S
=x_1^{a_1}\cdots x_n^{a_n}
  \theta_{t_1}\cdots\theta_{t_r}
  \xi_{s_1}\cdots\xi_{s_q},
\]

with both sets increasing. If \(T\cap U=S\cap V=\varnothing\), multiplication
has sign

\[
(\theta_T\xi_S)(\theta_U\xi_V)
=(-1)^{|S||U|+\operatorname{inv}(T,U)+\operatorname{inv}(S,V)}
 \theta_{T\cup U}\xi_{S\cup V},
\]

where
\(\operatorname{inv}(T,U)=|\{(t,u)\in T\times U:t>u\}|\); it is zero if either
same-species intersection is nonempty.

There is a minor source-level sign ambiguity worth exposing. The path weight
on p. 715 is multiplied in increasing step order, while Definition 3.1 writes
\(\theta_T\xi_S\), with each species ordered separately. For example the
published Figure 1 contains \(\xi_2\theta_3=-\theta_3\xi_2\). Canonicalizing a
candidate therefore may rescale it by \(-1\). This cannot affect whether the
set is a basis, but it must be fixed in executable data and in any literal
“standard monomial” claim.

## 3. Exact closed form of the candidate

For \(T,S\subseteq\{2,\ldots,n\}\), Lentfer defines

\[
\alpha_1(T,S)=0,\qquad
\alpha_i(T,S)=\alpha_{i-1}(T,S)-1+
\mathbf 1_{i\notin T}+\mathbf 1_{i\notin S}.
\]

Equivalently,

\[
\alpha_i(T,S)=i-1-|T\cap\{2,\ldots,i\}|-
|S\cap\{2,\ldots,i\}|. \tag{3.1'}
\]

The first Motzkin step is forced up. At step \(i\ge2\), membership in neither,
exactly one, or both of \(T,S\) gives respectively an up, horizontal, or down
step. The height after step \(i\) is \(\alpha_i(T,S)+1\). Consequently
\(\theta_T\xi_S\in B_n^{(0,2)}\) is equivalent to

\[
T,S\subseteq\{2,\ldots,n\},\qquad
\alpha_i(T,S)\ge0\quad(1\le i\le n). \tag{3.2'}
\]

Thus, up to the harmless individual signs just discussed,

\[
B_n^{(1,2)}=
\{x^a\theta_T\xi_S:
\text{(3.2') holds and }0\le a_i\le\alpha_i(T,S)\}.
\]

In particular \(0\le a_i\le i-1\), so every candidate already lies in the
Artin coordinate basis used below. The source's Theorem 3.7 proves
\(|B_n^{(1,2)}|=2^{n-1}n!\), hence \(|B_5^{(1,2)}|=1920\).

## 4. Finite exact reduction

Let \(e_i=e_i(x_1,\ldots,x_n)\) and

\[
E_n=(e_1,\ldots,e_n)A_n,\qquad C_n=A_n/E_n.
\]

Since each \(e_i\) is a positive-degree invariant, \(E_n\subseteq I_n\). The
following is the key reduction.

**Finite reduction lemma.** In characteristic zero,

\[
R_n^{(1,2)}\cong C_n/\langle(C_n^{S_n})_+\rangle . \tag{4.1}
\]

**Proof.** The quotient map \(q:A_n\to C_n\) is \(S_n\)-equivariant. The
Reynolds operator
\(\rho=\frac1{n!}\sum_{\sigma\in S_n}\sigma\) shows that \(q\) is surjective on
invariants: if \(c\in C_n^{S_n}\) and \(q(a)=c\), then
\(q(\rho(a))=\rho(c)=c\). The multigrading shows likewise that
\(q(A_n^{S_n,+})=(C_n^{S_n})_+\). Therefore
\(I_n/E_n=\langle(C_n^{S_n})_+\rangle\), and the third isomorphism theorem gives
(4.1). \(\square\)

Computationally, the unnormalized operator
\(\mathcal R=\sum_{\sigma\in S_n}\sigma=n!\rho\) is applied to **every**
coordinate monomial and its image is row-reduced. No assertion is made that
each orbit sum is nonzero or that one unsigned orbit representative suffices.
Indeed a stabilizer may act with Koszul sign \(-1\), causing exact cancellation:
for \(n=2\),
\(\mathcal R(\theta_1\theta_2)=\theta_1\theta_2+
\theta_2\theta_1=0\). Nevertheless
\(\operatorname{im}\mathcal R=C_n^{S_n}\) in characteristic zero, so scanning
all coordinate vectors spans the full invariant subspace; zero averages are
included harmlessly.

For lexicographic order \(x_1>\cdots>x_n\), the classical Gröbner basis

\[
h_i(x_i,\ldots,x_n),\qquad 1\le i\le n,
\]

of \((e_1,\ldots,e_n)\) has leading monomials \(x_i^i\). Hence \(C_n\) has the
explicit basis

\[
\mathcal C_n=\{x^a\theta_T\xi_S:0\le a_i<i,
T,S\subseteq[n]\}. \tag{4.2}
\]

It follows without any conjectural degree bound that

\[
\dim C_n=n!4^n,\quad
0\le d_x\le\binom n2,\quad0\le d_\theta,d_\xi\le n. \tag{4.3}
\]

This is stronger computationally than invoking a Noether bound in the infinite
ambient algebra: **all** needed invariants are obtained by exact Reynolds
projection inside the finite space (4.2).

For \(n=5\), the ambient dimension is \(120\cdot4^5=122880\). If
\(M_5(d)=[q^d][5]_q!\), the \((d,t,s)\)-block has dimension

\[
M_5(d)\binom5t\binom5s.
\]

The Mahonian coefficients are

\[
(M_5(0),\ldots,M_5(10))=(1,4,9,15,20,22,20,15,9,4,1),
\]

so the largest block has dimension \(22\binom52^2=2200\).

## 5. Block recurrence for the Hilbert ideal

Write \(C_{d,t,s}\) for a trihomogeneous block and
\(J=\langle(C_n^{S_n})_+\rangle\subset C_n\). Starting with
\(J_{0,0,0}=0\), total-degree induction gives the exact recurrence

\[
\begin{aligned}
J_{d,t,s}={}&(C_{d,t,s}^{S_n})_+
+\sum_{i=1}^n x_iJ_{d-1,t,s}\\
&+\sum_{i=1}^n\theta_iJ_{d,t-1,s}
+\sum_{i=1}^n\xi_iJ_{d,t,s-1}. \tag{5.1}
\end{aligned}
\]

Terms with negative indices are zero. Inclusion from right to left is the ideal
property. Conversely, every positive-degree multiplier of an invariant is a
linear combination of products by the algebra generators; induction on the
multiplier's total degree proves the other inclusion. Thus (5.1) neither omits
higher-degree invariants nor assumes a conjectural generating family.

Let \(W_{d,t,s}\) be the coordinate span of the candidate monomials in that
block. Conjecture 3.2 at fixed \(n\) is equivalent to the finite family of exact
direct-sum identities

\[
C_{d,t,s}=J_{d,t,s}\oplus W_{d,t,s}. \tag{5.2}
\]

Over \(\mathbb Q\), (5.2) is checked by exact sparse row reduction: the relation
rank must be
\(\dim C_{d,t,s}-|B_{d,t,s}|\), every candidate coordinate vector must increase
the rank, and adjoining all candidates must give full ambient rank.

## 6. What this reduction does and does not prove

- It is an exact equivalence and a finite algorithm for every fixed \(n\).
- It supplies rigorous degree bounds and blocks of size at most 2200 for \(n=5\).
- It tests the actual basis statement; it does not assume the dimension
  conjecture \(2^{n-1}n!\).
- It does not by itself make the candidates “standard monomials” for a
  super-Gröbner term order. A separate term order and initial-ideal certificate
  would be required for that stronger assertion.
- A completed run of the Builder program is still discovery output until a
  no-import verifier reconstructs (4.1)--(5.2) from serialized exact data.
