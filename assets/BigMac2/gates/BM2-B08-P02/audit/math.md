# Fresh mathematical audit

## Scope and provenance

This review addresses exactly the frozen `resolution-paper` claim in
`claim.json`, bound to snapshot digest
`cf4597267e383e2f6d584b9ff7d0a39dc9e6aea0ab3436c568fe4ad6aebf1752`.
All five snapshot file hashes were recomputed and agree with
`audit/snapshot.json`.  The review job is
`bigMac-00008-p02-referee-a5213d304bcf`.

The claim has four substantive parts: the raw classification in all of
`U(2)`, the exact time-eight weights, the complete zero-return locus, and the
fixed-experiment equivalence analysis.  I reviewed all four without weakening
the frozen scope.

## Reconstruction of the decisive argument

Let the first column of a unitary coin be `(a,c)^T`.  Independent left row
phases make it `(r,s)^T` with `r,s >= 0` and `r^2+s^2=1`.  Its unit orthogonal
complement is then `z(s,-r)^T`, `|z|=1`.  Hence every coin, including the
endpoint charts, has the form

\[
 U=D V(r,z),\qquad
 V(r,z)=\begin{pmatrix}r&sz\\s&-rz\end{pmatrix},
\]

with diagonal unitary `D`.  For an eight-step return word there are four
left and four right steps.  Left multiplication by
`diag(lambda,nu)` therefore multiplies every word amplitude by the same
factor `lambda^4 nu^4`; all coherent sums and weights are unchanged up to
that common phase.  Reduction to `V(r,z)` is thus legitimate.

I recomputed the 70 return words directly from the definition of the interval
sojourn count.  They split as 14 words in each of `k=0,2,4,6,8`, with no odd
class.  The resulting five matrix sums agree entry by entry with the displayed
formulas in `evidence/time8_classification.md`.  This was checked twice: by
running the frozen exact verifier, and by the independently written
`audit/referee_recheck.py`.  The latter uses finite-field evaluation of the
path recursion on a full 9-by-9-by-9 interpolation grid rather than the
candidate's sparse symbolic implementation.  Every entry has degree at most
eight in each of `r,s,z`; the grid therefore determines it over the field.
The possible integer coefficients have absolute value below 100, so the prime
1,000,003 also distinguishes the integer coefficients.

Writing `x=r^2`, `y=1-x`, `u=rs`, and `h=Im(z)`, direct application of
`phi_*=(1,i)^T/sqrt(2)` gives

\[
 w_0=\frac{yf^2}{2}(1-2uh),\qquad
 w_8=\frac{yf^2}{2}(1+2uh),
\]

\[
 w_2=W-u^3yh(A^2+BC),\qquad
 w_6=W+u^3yh(A^2+BC),
\]

and `w_4=u^4 M^2+u^2y^2N^2`, with the candidate's real polynomials.
The cross-term sign follows from
`|X+i z Y|^2=X^2+Y^2-2XY Im(z)`.  Independent dense rational-polynomial
expansion confirms

\[
 f=(1-2x)(1-7x+7x^2),\quad
 A^2+BC=2(2x-1)f,
\]

\[
 W-w_4=x^2y^3(2x-1)^2.
\]

These identities solve every branch without dividing by a potentially zero
quantity.  Since `w_0+w_8=yf^2`, vanishing of both forbidden endpoint weights
implies `y=0` or `f=0`.  If `y=0`, then `s=0` and every return amplitude is
zero, so the conditional distribution is undefined and this face is excluded.
If `y>0` and `f=0`, then also `x>0`, the `z`-dependent terms in `w_2,w_6`
vanish, and equality of `w_2,w_4,w_6` is equivalent to
`x^2y^3(2x-1)^2=0`.  Thus `x=y=1/2`.  Conversely, substitution at this point
gives exactly

\[
 w_2=w_4=w_6=1/128,\qquad R_8=3/128,
\]

for every unit-modulus `z`, while all other weights vanish.  The other two
roots of `1-7x+7x^2` fail equality by the strictly positive square gap.

The zero-return classification is also exhaustive.  When `y>0` and `f` is
nonzero, `w_0+w_8>0`.  When `y>0` and `f=0`, `w_4` could vanish only if
`M=N=0`; but `M-N=2x-1`, and at `x=1/2` both equal `1/4`.  Therefore
`R_8=0` exactly on `s=0`, which is exactly the diagonal-coin locus.

It follows that the raw solution set is precisely

\[
 \mathcal S=\left\{D\,\frac1{\sqrt2}
 \begin{pmatrix}1&z\\1&-z\end{pmatrix}:
 D\text{ diagonal unitary},\ |z|=1\right\}.
\]

## Equivalence checks

On the balanced locus, `z=b/a`; left row phases do not change it, and
`H_left` is exactly `z=1`.  A unitary internal-basis map preserving both
ordered chirality projectors must be diagonal.  Requiring it also to preserve
the ray of `(1,i)^T` forces its two phases to coincide, so its conjugation is
trivial.  Thus the entire circle remains under ordinary unitary basis changes.

Right diagonal multiplication is not a symmetry of the fixed experiment.
The candidate's test at `x=1/4` checks out: the right-diagonally related coins
with `z=1` and `z=i` have respectively
`w_0=75/8192` and
`w_0=(75/8192)(1-sqrt(3)/2)`.  Coincidental equality of the target law on the
balanced solution locus does not promote this operation to a setup symmetry.

For the optional antiunitary enlargement, any antiunitary preserving each
ordered chirality projector is, up to phase, `diag(1,-1) K` once the fixed
initial ray is imposed.  It sends `U` to
`J conjugate(U) J`, sends every path sum to
`J conjugate(Gamma) J`, and preserves its norm on the fixed initial vector.
After left-row gauge it induces `z -> -conjugate(z)`.  Hence the optional
quotient is exactly the stated circle involution, not a point.

## Boundary comparison and adversarial checks

The authorized frozen source comparison states that the cited theorem covers
only the real rotation family.  Substituting that family means `z=1` and
`x=cos^2(theta)`; the classification recovers exactly `theta=pi/4` on its
open parameter interval.  The new argument covers the remaining phase and
endpoint charts, so the contribution is the claimed exact all-`U(2)` delta.
It makes no broader priority claim.

I specifically checked the empty/undefined conditional face, both normal-form
endpoints, all three roots of the endpoint factor, positivity of the target
weight, the fixed initial ray, ordered chirality projectors, and the distinction
between a global setup symmetry and an accidental equality on the solution
locus.  There is no division by zero, limiting argument, numerical inference,
or cited theorem doing hidden mathematical work.

## Verdict

**ACCEPT.**  The frozen scope, correctness/evidence, and contribution all
pass.  The original claim is proved as stated.  No unresolved mathematical
gap remains within the frozen scope; the only literature limitation is the
explicitly disclosed absence of any priority claim beyond the cited boundary.
