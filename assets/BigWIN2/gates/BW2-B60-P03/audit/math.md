# Fresh mathematical referee report

## Scope and evidence binding

I reviewed the exact frozen `resolution-paper` claim against `source.md`,
`problem.md`, `claim.json`, snapshot digest
`952ec68c27a7713fe1e32162ff743686ae874ef4d2b152c9b97f31d8681fc6f6`,
and every evidence file listed in that snapshot.  The recomputed SHA-256
digest of each listed file agrees with `audit/snapshot.json`.

The primary-source PDF defines \(\mathcal S_4\) by the lifted PSD constraint
and formulates (9) by representing the first and off-diagonal second moments
as a convex combination of the sixteen Boolean vertices.  Thus the finite
conic program in `problem.md` is an accurate, label-explicit reading of (9).
The source proves only feasibility at value \(-1/100\) (Proposition 3 and
Appendix A) and reports an uncertified numerical optimum near \(-0.0108\); it
does not contain the exact algebraic value, the dual certificate, or the
optimal-face classification asserted here.  The candidate makes no broader
priority claim, so the bounded source comparison is adequate for its stated
contribution.

## Reconstruction of the certificate

Let \(P(A)=32A^3+48A^2+26A+1\).  Direct rational evaluation gives opposite
signs at \(-1/24\) and \(-1/25\), while \(P'\) is positive throughout that
interval.  Hence the specified \(\alpha\) exists and is unique there.  All
following calculations were reduced exactly in
\(\mathbb Q[A]/(P)\); signs were checked by rational root isolation, not by
floating-point rounding.

After eliminating \(x\) and the six off-diagonal entries, write

\[
Y=E_{00}+\sum_z p_zF_z+\sum_{i=1}^4 d_iE_{ii},\qquad
L=\sum_iQ_{ii}d_i+\sum_zp_zh_z,
\]

where
\(h_z=c^Tz+2\sum_{i<j}Q_{ij}z_iz_j\).  For the displayed matrix \(S\), I
checked exactly that \(S_{ii}=Q_{ii}\) for \(i=1,\ldots,4\), and that the
sixteen reduced slacks

\[
r_z=h_z-\langle S,F_z\rangle
\]

vanish precisely for
\(0000,0001,0011,0111,1010,1111\).  Each of the other ten slacks is strictly
positive at \(\alpha\).

As an independent PSD check, I reconstructed \(S\), the proposed weights,
and \(Y\) from the formulas and enumerated all principal minors.  Using the
tighter rational isolating interval
\([-415623/10^7,-415622/10^7]\), exact Sturm checks gave:

- for \(S\), all five order-one and all ten order-two principal minors are
  positive, and every principal minor of order at least three is zero;
- for \(Y\), every principal minor of orders one, two, and three is positive,
  and every principal minor of orders four and five is zero.

Thus \(S\succeq0\) with rank two and \(Y\succeq0\) with rank three.  All six
listed probabilities are strictly positive and reduce to a sum of one.  The
moment equations defining \(x\) and the off-diagonal entries hold by their
construction.  Exact multiplication gives \(SY=0\), and exact objective
reduction gives

\[
L=-t,\qquad t=(32\alpha^2+16\alpha+1)/36.
\]

For every feasible point, the identity

\[
L=\langle S,Y\rangle-S_{00}+\sum_zp_zr_z
\]

has only nonnegative terms apart from \(-S_{00}=-t\).  This proves the global
lower bound, while the reconstructed point attains it.  Eliminating \(\alpha\)
also reproduces
\(576v^3-16v^2+92v+1=0\) for \(v=-t\), with the claimed numerical root.
The certificate is therefore a dual certificate for an exactly equivalent
elimination of the frozen finite conic formulation, and the displayed
identity directly certifies the uneliminated variables as well.

## Complete-face check

At any optimum the ten positive unused-atom slacks force their probabilities
to zero.  Equality in \(\langle S,Y\rangle\geq0\) for PSD \(S,Y\) forces
\(SY=0\).  I independently formed these equations in the six remaining
probabilities and four diagonal variables.  A square subsystem consisting of
the normalization equation, all five entries of row zero of \(SY\), and
columns \(0,1,2,4\) of row one has determinant, modulo \(P\),

\[
\frac{5775280\alpha^2+8296838\alpha+334859}{331776}.
\]

Its numerator is coprime to \(P\), so this determinant is nonzero at
\(\alpha\).  The proposed six weights and four diagonal entries have zero
residual in this subsystem.  Consequently they are the unique possible
optimal variables; the moment equations then uniquely determine \(x\) and
all off-diagonal entries.  This proves uniqueness in the full
\((x,X,p)\)-space, not merely in a symmetric slice.  Direct substitution also
shows that the probability vector, \(x\), and \(X\) are fixed by the stated
reverse-complement involution.

## Verdict

**Accept.**  The exact value, a feasible exact primal point, a matching exact
dual lower-bound certificate, and the entire optimal face including the
auxiliary distribution are all established at the frozen scope.  I found no
unresolved mathematical gap or scope mismatch.
