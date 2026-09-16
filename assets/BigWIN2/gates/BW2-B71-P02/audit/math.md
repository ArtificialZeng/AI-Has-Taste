# Fresh mathematical referee report

## Frozen scope and integrity

This review concerns exactly the `resolution-paper` statement in `claim.json`:
the particular complex Motakis realisation (X) over (S^4), the fixed space
(E=X\oplus X), and the fixed operators (S,T\in\mathcal B(E)) constructed in
Theorem 5.1 of Horvath--Kania. It does not assert the same conclusion for other
realisations, lifts, Banach spaces, or scalar fields.

I checked every file listed in `audit/snapshot.json` against its recorded
SHA-256 digest. All six hashes match. I also recomputed the canonical hash of
the snapshot's `files` mapping and obtained
`06fb35fe7f658b5644a6f3ca4214484a53e95cf9b59866912acc6128e29efc33`.
The immutable `source.md` has SHA-256
`1f45293be7a70747265ec3e6814e177c7ef256f3caa5f0af205904754ad57bee`,
as recorded in the snapshot.

## Reconstruction of the component-injectivity lemma

Let (Y) be an infinite-dimensional complex Banach space with a Schauder
basis, let (q:\mathcal B(Y)\to\mathcal Q(Y)) be the Calkin quotient, and
suppose (v\in\operatorname{Inv}(\mathcal B(Y))) has
(q(v)\in\operatorname{Inv}_0(\mathcal Q(Y))). The proof that

\[
q_*:\mathfrak I(\mathcal B(Y))\longrightarrow
\mathfrak I(\mathcal Q(Y))
\]

is injective has the following three independently checked steps.

1. If (P_n) are the basis partial-sum projections, then
   (P_n\to I) strongly and (sup_n\|P_n\|<\infty). Uniform convergence on
   the compact set \(\overline{K(B_Y)}\) gives
   \(\|(I-P_n)K\|\to0\) for every compact (K). Thus compact operators are
   approximated in norm by the finite-rank operators (P_nK). The finite-net
   estimate in `evidence/proof.md` correctly supplies this uniformity; it does
   not assume norm convergence (P_n\to I) on all of (Y).

2. If (a=I+K) is invertible, choose finite-rank (F) with
   \(\|a^{-1}\|\,\|F-K\|<1\). The path
   \(a+t(F-K)=a(I+t a^{-1}(F-K))\) stays invertible by the strict Neumann
   bound. For (M=F(Y)) and a closed complement (N), the endpoint has block
   form
   \[
   I+F=\begin{pmatrix}C&B\\0&I_N\end{pmatrix}.
   \]
   Its invertibility forces (C\in GL(M)). Removing (B) preserves
   invertibility, and (GL(M)) is path connected because (M) is a
   finite-dimensional complex space. Consequently every invertible (I+K)
   is joined to (I). This avoids the invalid general shortcut
   (t\mapsto I+tK).

3. Choose a path \(\gamma\) in
   \(\operatorname{Inv}(\mathcal Q(Y))\) from (q(v)) to (1), and put
   \(L=\max_t\|\gamma(t)^{-1}\|\). On a sufficiently fine finite partition,
   \(\delta_i=\gamma(t_i)^{-1}\gamma(t_{i+1})\) satisfies
   \(\|\delta_i-1\|<1/2\). The quotient-norm definition then gives a lift
   (h_i) of \(\delta_i-1\) with the strict bound \(\|h_i\|<1\). Hence each
   path (s\mapsto v_i(I+s h_i)) consists of invertibles, and the endpoint
   (v_m) satisfies (q(v_m)=1). It is therefore (I+K) for compact (K)
   and contracts by step 2. No global path-lifting property or surjectivity on
   invertible groups is assumed.

These steps prove precisely that the kernel of (q_*) is trivial. The uses of
the Schauder basis, complex scalars, compactness, and strict norm bounds are all
explicit and valid. The argument is applied only to (E=X^2) and
(E\oplus E=X^4), both of which inherit Schauder bases from (X).

## Check of the source-to-claim deductions

I inspected the archived primary-source PDF at the cited locations rather than
relying on the dossier's paraphrase.

- Theorem 4.1 gives this (X) a Schauder basis and a unital Banach-algebra
  isomorphism \(\mathcal Q(X)\cong C(S^4)\). The discussion preceding Lemma
  4.5 gives \(\mathcal Q(X^n)\cong M_n(\mathcal Q(X))\).
- Theorem 5.1 constructs the fixed (S,T), proves
  (u=I_E-2ST) invertible, and shows that its Calkin image is the
  Klaja--Ransford function (c), which is outside the identity component.
- The calculation on printed page 23 identifies
  \(\mathfrak I(C(S^4,M_2(\mathbb C)))\) with
  \(\pi_4(GL_2(\mathbb C))\cong\mathbb Z/2\), including the justification
  that based and free homotopy classes agree here. The image of (u) is the
  nonzero class.
- The stable-range calculation on printed page 2 gives
  \(\pi_4(GL_3(\mathbb C))=0\); the displayed isomorphism
  \(\pi_j(U(m))\to\pi_j(U(m+1))\) for (j<2m), with (m=3,j=4), gives
  \(\pi_4(GL_4(\mathbb C))=0\).

Apply the proved injectivity lemma to (Y=E). Its target component group has
two elements, and the nonzero one has the invertible lift (u). Thus

\[
\mathfrak I(\mathcal B(E))\cong\mathbb Z/2,
\]

with nonidentity element ([u]). This conclusion uses surjectivity only for
the two target components: the identity lifts to (I_E), and the unique
nonidentity component lifts to (u).

Next use the block-operator identification
\(M_2(\mathcal B(E))\cong\mathcal B(E\oplus E)\). Its Calkin algebra is

\[
\mathcal Q(E\oplus E)\cong C(S^4,M_4(\mathbb C)).
\]

Since (GL_4(\mathbb C)) is path connected and its fourth homotopy group is
zero, every map (S^4\to GL_4(\mathbb C)) is null-homotopic (one may first
normalize its value at a base point). Lemma 2.3 of the source therefore makes
the target Calkin component group trivial. Injectivity of the Calkin map on
components forces

\[
\mathfrak I(M_2(\mathcal B(E)))=1.
\]

It follows that the first stabilization has all of
\(\mathfrak I(\mathcal B(E))\) as kernel. Hence

\[
\ker s_{\mathcal B(E)}=\{[I_E],[I_E-2ST]\}\cong\mathbb Z/2,
\qquad
\operatorname{ord}[I_E-2ST]=2.
\]

This answers both parts of the frozen Question 9.1 with equality and does not
silently weaken or enlarge its quantifiers.

## Source comparison, contribution, and remaining limits

Printed page 26 of the archived source explicitly asks for this kernel and the
upstairs order and states that the Calkin order alone did not determine the
upstairs order. The component-injectivity argument supplies exactly the missing
implication, so the candidate is a complete resolution of the frozen original
question rather than a subsidiary result or a toy restriction.

The frozen literature screen reports a bounded search through 2026-09-08 and
no located later primary resolution. Its wording correctly disclaims exhaustive
priority, and I do not treat it as proof of priority or as part of the
mathematical proof. Whether the general injectivity lemma is standard does not
alter the correctness or full-scope resolution of the specific published
question. No unresolved mathematical gap remains in the claimed result.

## Verdict

**Accept.** The exact frozen scope, mathematical proof, source deductions, and
claimed contribution pass review.
