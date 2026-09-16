# Mathematical referee report

## Frozen scope

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: for every
fixed odd integer (m\geq 3), the colored (m)-cycle with one vertex-color
class and pairwise distinct edge-color classes has
(\operatorname{mlt}(G_m)=2). This includes the full original case (m=5)
and therefore disproves the immutable assertion
(\operatorname{mlt}(G_5)=1). I did not reduce the reviewed scope to the
five-cycle corollary.

All files named by `audit/snapshot.json` matched their recorded SHA-256
digests. In particular, the primary PDF matched digest
`29727f7143ce6a7a92cf15dc80882e74590b7a3de66c42b50c31a4d94737e48d`.

## Reconstruction of the decisive argument

For a fixed odd (m\geq3), fix the common diagonal parameter at (a=2).
Writing (K(2,b)x=0) in the independent edge parameters gives

\[
x_{i-1}b_{i-1}+x_{i+1}b_i=-2x_i .
\]

The coefficient matrix (B_m(x)) has, in row (i), supported columns
(i-1) and (i). A supported determinant permutation is forced cyclically
to choose either all columns (i-1) or all columns (i). Thus the only two
Leibniz terms have the same monomial (\prod_i x_i), and their relative sign
is the sign of an (m)-cycle. Hence

\[
\det B_m(x)=\bigl(1+(-1)^{m-1}\bigr)\prod_i x_i
           =2\prod_i x_i
\]

for odd (m). There is therefore a unique rational solution
(b(x)=-2B_m(x)^{-1}x) whenever every coordinate is nonzero. At
(x=\mathbf 1), uniqueness and the equations give (b_i=-1) for every
(i). Continuity on the positive orthant then supplies a nonempty open
neighborhood (U_m) of (\mathbf1) on which all (b_i(x)<0). This is an
open subset of (\mathbb R^m), so it has positive Lebesgue measure; no
uniform choice of neighborhood as (m) varies is required by the claim.

For (x\in U_m), define (D=\operatorname{diag}(x_i)) and
(w_i=-b_i x_i x_{i+1}>0). Multiplying the kernel equation by (x_i) gives
(2x_i^2=w_{i-1}+w_i). Entrywise this is exactly

\[
D K(2,b(x))D=L_w,
\]

where (L_w) is the positive-weight Laplacian of the connected cycle.
Because (D) is invertible, this congruence proves
(K(2,b(x))\succeq0), (\ker K(2,b(x))=\mathbb R x), and
(\operatorname{rank}K(2,b(x))=m-1). The matrix is in the claimed colored
concentration space: distinct edge colors make the (b_i) independent
parameters and do not require their numerical values to differ.

Consequently a positive-measure set of one-observation vectors has a
nonzero PSD annihilator. This directly defeats the almost-everywhere
condition for threshold one, so (\operatorname{mlt}(G_m)>1). The supplied
primary source's Proposition 3.26 states
(\operatorname{gcr}(G_m)=2) for this all-distinct-edge family, while
Corollary 3.7 states (\operatorname{mlt}(G)\leq\operatorname{gcr}(G)).
Thus (\operatorname{mlt}(G_m)\leq2), and the two bounds yield equality.

## Adversarial and source checks

- There is no division by zero in the construction: the proof deliberately
  works inside the positive orthant. Empty and measure-zero coordinate
  strata play no role.
- The PSD conclusion is an exact congruence to a weighted Laplacian, not an
  inference from sampled eigenvalues or a limiting exchange. Connectivity
  also establishes the equality case and exact rank.
- The parity calculation was checked at the boundary (m=3) and on both odd
  and even dimensions. For even (m), the displayed determinant vanishes as
  it should; the proof makes no claim that this construction establishes the
  even case.
- I ran `evidence/research_all_odd.py` and
  `evidence/research_disproof.py`. Both completed successfully. They checked
  exact symbolic determinant identities, rational kernel equations, the
  Laplacian congruence, rank certificates, and the explicit five-dimensional
  open-box inequalities. The infinite theorem rests on the reconstructed
  argument above, not on these finite tests.
- In the supplied PDF, Definition 2.13 defines MLT through almost-sure MLE
  existence; Theorem 3.4(2) gives the PSD-kernel characterization;
  Corollary 3.7 gives the needed upper bound; and Proposition 3.26 gives
  `gcr=2` and the even result. Conjecture 3.27 asserts the contrary odd-cycle
  value (1), so the candidate is a direct exact resolution relative to that
  source. Appendix Table 2 already records the (m=3) instance with MLT 2,
  consistently with the theorem.
- The immutable `source.md` has incorrect title/author metadata for the local
  PDF, but `problem.md` identifies the PDF correctly. This bibliographic
  defect does not alter the frozen mathematical statement or the proof.

## Contribution and remaining limits

The five-cycle construction alone is a complete positive-measure disproof of
the original assertion. The same argument valid for every fixed odd (m)
is a substantive and coherent strengthening, and combining it with the
source's even theorem gives the advertised parity classification. The
literature comparison is expressly bounded to the supplied v1 primary source
and the recorded searches; no exhaustive priority claim is being accepted.
I found no unresolved mathematical gap in the exact frozen scope.

## Verdict

**Accept.** The full frozen claim is correct, it disproves the original
five-cycle assertion in its almost-everywhere scope, and the strengthened
all-odd theorem has a complete exact proof with the cited upper-bound
hypotheses verified.
