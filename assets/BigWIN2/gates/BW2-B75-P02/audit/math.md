# Fresh mathematical referee report

Referee job: `win-00075-p02-referee-d82f71566a68`  
Frozen snapshot: `2abd722cebd0f37ea9e4a65b6b334a4e718a4612c1df8b4dacd8b14a605cc700`

## Scope and integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`, with
original status `proved`. I compared every file enumerated by
`audit/snapshot.json` with its recorded SHA-256 value; all seven hashes match.
I also independently recomputed the canonical digest of the snapshot's `files`
mapping, obtaining the digest displayed above. The assessed scope is therefore
the unchanged claim for every integer \(n\geq 4\) and every characteristic-zero
field \(K\), with the column convention specified in `problem.md`.

## Reconstruction of the decisive argument

Let \(q_1,\ldots,q_n\in V\), and let \(Q\) be the matrix whose \(j\)-th column
is the coordinate vector of \(q_j\) in the ordered \(u\)-basis. Since the
columns of the matrix of \(r(q_1),\ldots,r(q_n)\) are those of \(RQ\), the sole
bracket value in \(\mathfrak g\) gives

\[
G_r(q_1,\ldots,q_n)=\det(RQ)x_n
                  =\det(R)\det(Q)x_n. \tag{1}
\]

Write \(\varepsilon=u_n^*\). The alternating action fixed in the problem is

\[
\rho_{\mathfrak g}(y_1,\ldots,y_{n-1})q
=\det\!\bigl(p_a(y_b)\bigr)_{a,b<n}\,\varepsilon(q)u_n.
\]

Substituting this into the signed sum defining \(H_r\), its scalar coefficient
is the Laplace expansion along the last row of

\[
B=\begin{pmatrix}
p_1(r(q_1))&\cdots&p_1(r(q_n))\\
\vdots&&\vdots\\
p_{n-1}(r(q_1))&\cdots&p_{n-1}(r(q_n))\\
\varepsilon(q_1)&\cdots&\varepsilon(q_n)
\end{pmatrix}.
\]

Indeed the action's sign \((-1)^{n-i}\) equals the last-row cofactor sign
\((-1)^{n+i}\). With

\[
D=\begin{pmatrix}A&v\\0&1\end{pmatrix},
\]

one has \(B=DQ\), hence

\[
H_r(q_1,\ldots,q_n)=\det(B)u_n
=\det(A)\det(Q)u_n. \tag{2}
\]

Equations (1)--(2) show, without assuming that \(Q\) is invertible, that the
deformation-map residual on an arbitrary tuple is \(\det(Q)\) times its value
on \((u_1,\ldots,u_n)\). Thus (DM) holds for all tuples if and only if

\[
\det(R)x_n=\det(A)r(u_n).
\]

Since \(r(u_n)=\sum_{j<n}v_jx_j+\alpha x_n\), coordinate comparison is exactly

\[
\det(A)v=0,\qquad \det(R)=\alpha\det(A). \tag{3}
\]

This proves necessity. Conversely, (3) makes the basis-tuple residual zero, and
the displayed factorization by \(\det(Q)\) makes it zero on every tuple, proving
sufficiency.

For \(\det(A)\ne0\), the first equation in (3) gives \(v=0\); the resulting
block-triangular determinant is automatically \(\alpha\det(A)\), independently
of \(w\), so \(w,\alpha\) are arbitrary. For \(\det(A)=0\), the first equation
is automatic and the second is precisely \(\det(R)=0\). These two field-valued
cases are exhaustive.

## Adversarial checks

- **Signs and conventions.** The cofactor parity was recomputed above. The
  column convention gives \(RQ\), not \(QR\), and therefore gives \(\det R\)
  on the ordered basis as claimed.
- **Degenerate inputs.** No cancellation by \(\det(Q)\) or \(\det(A)\) is used.
  Consequently dependent tuples and singular \(A\) are included, rather than
  being recovered by an invalid density argument over an arbitrary field.
- **Quantifiers and edge cases.** All steps are determinant identities over
  \(K\); they apply uniformly to every stated \(n\ge4\) and every stated
  characteristic-zero field. There is no division, limiting argument, or hidden
  algebraic-closure assumption. The proof in fact uses less than the stated
  characteristic hypothesis, which does not weaken the submitted result.
- **Exact computation.** I reran `evidence/n4_symbolic_check.py`; its polynomial
  assertion passed. As a separate diagnostic, I checked the factorizations
  \(\det(RQ)=\det(R)\det(Q)\), \(\det(DQ)=\det(A)\det(Q)\), and the full residual
  identity on 100 deterministic exact-integer instances for
  \(n=4,5,6,7\); all passed. These checks support but are not used in place of
  the general derivation.

## Source comparison and contribution

Within the frozen evidence, `literature/triage_sources.md` reports that the
inspected 2026 source states the general deformation criterion, exhibits one
map in Example 8.7, and classifies complement isomorphism types in Corollary
8.8, but does not state this all-matrices classification. Full-text comparison
with the 2022 ternary predecessor was unavailable. The candidate explicitly
makes no novelty or priority claim, and the frozen theorem concerns \(n\ge4\),
not the ternary case. This literature limitation therefore does not create a
mathematical gap in a full-scope resolution of the frozen problem, and it is
disclosed accurately rather than converted into a novelty assertion.

## Verdict

**Accept.** The exact frozen claim is proved in both directions over its full
quantified scope, the two advertised cases are exhaustive, and I found no
unresolved mathematical or scope gap.
