# Mathematical audit: accept

Job: `win-00060-p02-referee-f2ea9b0224bc`  
Frozen snapshot: `7f73e26f61f0bec41577a20ec5776d6c794c8616fb5f1344d69f7e609da0748d`

## Frozen scope and source comparison

I checked the SHA-256 digest of every file in `audit/snapshot.json`; all eight
entries agree with the frozen mapping.  In particular, the supplied PDF has
SHA-256
`cbe004fd2b861aa6342b9b2d8d2ba065319ae039be5cb2cda4721780e534fac3`.
Its Appendix B, equation (60), is exactly the univariate form stated in
`problem.md`, including the factors `(k!)^{-2}` in the ghost terms.  The PDF's
Proposition 5 proves only the vanishing-cut threshold
`1/(gamma_D-p^2)` and the resulting cut-uniform lower bound, and explicitly
leaves equality with the full-cut threshold open.  Thus the candidate addresses
the precise unresolved step in the frozen source rather than a weakened or
subsidiary statement.

The claim has full frozen scope: all five degrees, exact values, absence of
interior maximizers, and both one-sided endpoint classifications.  The primary
source is the nearest result actually used.  No non-elementary external theorem
is needed by the proof; the endpoint evaluation identity is reconstructed from
shifted Legendre polynomials.  The literature statement remains appropriately
bounded: this audit confirms the delta from the supplied primary source, not a
general priority claim beyond the documented search limits in `problem.md`.

## Reconstruction of the decisive argument

Write the nonconstant monomial coefficient vectors of `u` and `q` as
`alpha,beta`, put `D=5p(p+1)`, and replace the constant coefficient of `q` by
the independent coordinate `y=q(kappa)`.  Direct integration gives

\[
 U_{ij}=\frac{ij(-1)^{i+j-2}}{i+j-1},\qquad
 K_{ij}=\frac{ij\kappa^{i+j-1}}{i+j-1},\qquad
 v_i=i\kappa^{i-1}.
\]

Completing the Nitsche boundary square reconstructs the exact identity

\[
 a^{(2)}_{\kappa,\gamma}
 =D\left(y-\frac{v^T\beta}{D}\right)^2
  +\alpha^TU\alpha+\gamma\|\beta-\alpha\|^2
  +\beta^T\left(K-\frac{vv^T}{D}\right)\beta .
\]

There is no constraint lost here: the change from the constant coefficient of
`q` to `y` is invertible for every `kappa`, and the unused constant coefficient
of `u` is exactly a null direction.  Also, `U` is the Gram matrix of the
derivative monomials on `(-1,0)`, hence is positive definite.

At

\[
 g_* = \frac1{D-p^2}=\frac1{p(4p+5)},\qquad P=U+g_*I,
\]

the second completion of squares leaves the Schur matrix

\[
 S_p(\kappa)=K-\frac{vv^T}{D}+g_*I-g_*^2P^{-1}.
\]

For `p=1`, the separate two-square calculation gives exactly

\[
 \tau_1(\kappa)=
 \begin{cases}
 (1-10\kappa)/(9+10\kappa),&0<\kappa<1/10,\\
 0,&1/10\leq\kappa<1,
 \end{cases}
\]

so the claimed degree-one result follows directly.

For `p=2`, I checked the displayed direct matrix and its congruence to the two
completed squares.  At `g_*=1/26`, the first leading minor of `S_2` is
`(2870 kappa+1)/2870`, while

\[
 \det S_2=\frac{\kappa(4305\kappa^3+6\kappa^2+32\kappa+444)}{12915}.
\]

Both have the required signs on `kappa>=0`, and both are strictly positive for
`kappa>0`.  I also recomputed, for symbolic `gamma`,

\[
 \det S_{2,\gamma}(0)
 =\frac{\gamma(26\gamma-1)}{30(3\gamma^2+7\gamma+1)},
\]

which independently confirms the endpoint transition at `1/26`.

For `p=3,4,5`, the frozen evidence gives every coefficient of every leading
principal minor of `S_p`.  The denominators are positive; for orders below `p`
all coefficients are positive, and at order `p` the constant coefficient is
zero while every positive-degree coefficient is positive.  Consequently
Sylvester elimination has positive first `p-1` pivots and a nonnegative last
pivot on `kappa>=0`, with the last pivot zero exactly at `kappa=0`.  Hence
`S_p(0)` is positive semidefinite and `S_p(kappa)` is positive definite for
every `kappa>0`.  Together with the two positive square blocks, this proves
the global upper bound at `g_*`, and strict positive definiteness on all
effective coordinates whenever `kappa>0`.

The endpoint necessity is also exact.  At `kappa=0` and arbitrary positive
`gamma`, the remaining Schur matrix is

\[
 A_\gamma-\frac{e_1e_1^T}{D},\qquad
 A_\gamma=\gamma I-\gamma^2(U+\gamma I)^{-1}\succ0.
\]

Since

\[
 A_\gamma^{-1}=\gamma^{-1}I+U^{-1},\qquad
 (U^{-1})_{11}=p^2,
\]

the rank-one downdate is positive semidefinite exactly when
`1/gamma+p^2<=D`, equivalently `gamma>=g_*`.  The identity
`(U^{-1})_{11}=p^2` follows from the endpoint reproducing kernel on
`P_{p-1}`: the squared norm is `sum_{m=0}^{p-1}(2m+1)=p^2`.  If
`gamma<g_*`, choosing `beta=A_gamma^{-1}e_1` and the square-minimizing
`alpha,y` gives the strictly negative exact value `t-t^2/D`, where
`t=1/gamma+p^2>D`.  Continuity in `kappa` carries this negative direction to
all sufficiently small positive cuts.  This establishes the matching lower
bound for the open cut interval and proves `tau_p(kappa)->g_*` as
`kappa->0+`.

Finally, strict positive definiteness at `g_*` for every fixed
`kappa>0` is an open condition in `gamma`, so `gamma` can be decreased
slightly at each interior cut.  Thus no interior cut is a maximizer.  At
`kappa=1` the same strictness and joint continuity give one smaller fixed
weight on a full one-sided neighbourhood, so `limsup_{kappa->1-} tau_p(kappa)
<g_*`.  Therefore the only limiting maximizer is `kappa->0+`.

## Exact checks performed

- Recomputed every frozen SHA-256 entry and inspected the relevant primary
  source pages containing Proposition 4, equation (60), and Proposition 5.
- Ran `evidence/verify_p3_p5.py` with Python 3/SymPy; it completed with
  `exact p=3,4,5 certificates verified`.
- Separately constructed the original monomial-coordinate matrix for every
  `p=1,...,5`, applied the invertible `q_0 -> y=q(kappa)` change, and compared
  it entrywise with the claimed block matrix.  All five symbolic identities
  were exact.
- Independently recomputed all Schur leading minors.  Their denominators,
  degrees, and sign patterns agree with the frozen certificates; the supplied
  verifier additionally matches every displayed coefficient.  I separately
  recomputed the symbolic `p=2` endpoint determinant above.
- Checked the open-domain quantifiers, positivity of `D-p^2`, the sole unused
  constant null direction, the semidefinite endpoint pivot, monotonicity in
  the ghost weight, and the continuity steps used to classify maximizers.

## Gaps and verdict

I found no mathematical or scope gap in the frozen candidate.  The proof is an
exact PSD certificate, not a determinant-only or floating-point argument, and
it proves the full original classification.  Verdict: **accept**.
