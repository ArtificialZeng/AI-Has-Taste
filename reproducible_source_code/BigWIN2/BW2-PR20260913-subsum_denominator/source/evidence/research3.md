# Research pass 3: a sharp-start Newton-positivity conjecture

Job: `primary-20260913-subsum-denominator-research-077128f18f2f`.
Date: 2026-09-13. Proposed handoff: **candidate / conjecture-note**.
Original status: **unresolved**. This is an evidence dossier for a fresh
referee, not an accepted result, manuscript, or publication.

## Original and subsidiary statements

The immutable original is the coefficient log-concavity of

\[
D_n(x)=\prod_{i=1}^n(1+x^i)^{\#\{q\ge0:2^q i\le n\}}
\]

for every positive n outside {3,5,6,7}, at every internal integer degree.
Its exact interpretation is in `problem.md`. No upper bound on n or
restriction on the original indices has been substituted.

For positive s and integer t>=0 with n=s*2^t>=9, define the actual old stage

\[
a_{s,t}(x)=D_{s2^t-1}(x)
 \prod_{\ell=1}^{v_2(s)}(1+x^{s/2^\ell}).
\]

The extra factors are exactly those preceding the factor (1+x^s) in the
ascending dyadic recurrence. For any coefficient sequence a, extended by
zero outside its support, let T_j(a)=a_j^2-a_(j-1)a_(j+1), and put

\[
F_{s,j}(t)=2T_j(a_{s,t}(1+x^s))-T_j(a_{s,t})-T_{j-s}(a_{s,t}).
\]

**Conjecture K_sharp_v1 (unproved; unchanged from pass 2).** For every
integer j>=0 and 1<=s<=j+1, let tau be the least integer t>=0 such that
s*2^t>=9 and 2*s*2^t>j+1. Then

\[
c_{s,j,h}:=\Delta^hF_{s,j}(\tau)\ge0
\qquad(0\le h\le2j).
\tag{K_sharp_v1}
\]

Here Delta acts on t with step one, not on n with step one. A falsifier is
one admissible integer tuple (s,j,h) with its uniquely specified tau and a
negative exact signed binomial sum. A negative c need not make F negative.
No equivalence with the original conjecture is claimed.

The conjecture concerns actual intermediate stages and every forward
difference of a quadratic minor margin, whereas the source conjecture
concerns the final D_n and only its individual minors. Its payoff is a
uniform nonnegative Newton certificate for all affected stages s<=j+1 in
the affine region 2n>j+1. It also implies the later-start kernel K by
translating the Newton expansion forward. It leaves the unbounded region
j>=2n-1. For unaffected shifts s>=j+2, H reduces to an old minor; its
nonnegativity needs an induction or separate information. Thus K_sharp
alone is not presented as a proof of original log-concavity on a moving
linear edge, let alone on the full support.

## Exact polynomial reduction

Let m=j+1, A=a_(s,tau), and P_m(x)=product_(i=1)^m(1+x^i). The exponent
e_i(n)=#{q>=0:2^q i<n} obeys

\[
e_i(2n)-e_i(n)=\mathbf1_{i<2n}.
\]

Because 2*s*2^tau>m, every exponent through m increases by one at each
subsequent doubling. The earlier-stage factors are fixed. Consequently

\[
a_{s,\tau+u}(x)\equiv A(x)P_m(x)^u\pmod{x^{m+1}}
\quad(u\in\mathbb Z_{\ge0}).
\]

The coefficient of x^r is polynomial in u of degree at most r: expand each
(1+x^i)^(E_i+u) using binomial polynomials. Hence F_(s,j)(tau+u) is a
polynomial of degree at most 2j and has the exact expansion

\[
F_{s,j}(\tau+u)=\sum_{h=0}^{2j}c_{s,j,h}\binom uh.
\tag{3}
\]

The integer binomial factors are nonnegative for u>=0. This is a proved
degree bound, not numerical interpolation used as a substitute for one.

Define L_j(W)=[x^j y^j]W-[x^(j-1)y^(j+1)]W for symmetric W. Expanding the
quadratic margin gives the additional identity

\[
c_{s,j,h}=\mathcal L_j\left(
A(x)A(y)(1+2x^s+2y^s+(xy)^s)
(P_m(x)P_m(y)-1)^h\right).
\tag{4}
\]

Indeed twice the new product minus the old product and its (xy)^s shift
has multiplier 2(1+x^s)(1+y^s)-1-(xy)^s. Each forward difference multiplies
the remaining product by P_m(x)P_m(y)-1. The signed functional in (4)
explains why ordinary nonnegative coefficients do not prove the conjecture.

## Complete edge certificate and its proof

The saved pass-2 sharp-start design certificate covers 0<=j<=64.
`research3_design_verify.py/.json` now independently recomputes all its
185,185 coefficients in 2,145 templates, using logarithmic derivatives
and signed binomial sums. It also checks all 1,112 earlier admissible
triples below the sharp start and recomputes the bases D_1,D_2,D_4,D_8.
This is verification of inherited data, not new held-out evidence.

The assigned held-out range 65<=j<=96 is in
`research3_sharp_probe.py/.json`: 2,608 templates, all 427,952 coefficients
strictly positive, and all 2,014 earlier finite margins nonnegative.
The producer uses sparse shift/add products and the exact doubling identity.
`research3_verify.py/.json` uses independently constructed logarithmic
derivatives, expands the quadratic margin directly, and reproduces every
coefficient by a signed binomial sum. It checks 5,216 further evaluations
outside the interpolation grids and both highest-order formulas per template.

Thus all 4,753 pairs (s,j), j<=96 and 1<=s<=j+1, have all their 613,137
Newton coefficients nonnegative. All 3,126 earlier admissible triples are
checked separately. There is no symmetry sampling in these domains.

**Restricted computer-assisted theorem.** For every n>=9, every actual
stage obeys H (that is, F>=0) at 0<=j<=96 and at the reflected indices in
the degree of the new stage. For every positive n outside the four
exceptions, T_j(D_n)>=0 whenever 1<=j<deg D_n and
min(j,deg D_n-j)<=96.

**Proof.** For an affected shift s<=j+1, the certificates and (3) cover all
t>=tau; the enumerated earlier triples cover n>=9 with t<tau. For an
unaffected shift s>=j+2, the coefficient triple at j is unchanged,
T_(j-s)=0, and F=T_j(old). Induct over every ascending stage starting
from D_8, whose full coefficient sequence is checked. The old minor
indices on the right of H are j and j-s, both at most 96; negative
indices have zero minors. If they are nonnegative then H implies that
the new minor is nonnegative. This simultaneously supplies the old
minor needed in unaffected stages. The bases n=1,2,4 are separately
checked, and the four known exceptions remain excluded.

Every stage polynomial is a product of palindromic factors. If the old
degree is L, then F_j=F_(L+s-j); the old minors interchange under this
reflection. Reflection therefore supplies the other edge. No unbounded
interior claim is inferred from the fixed cutoff. This proof relies on
the actual finite certificate checks, not merely their summary flags.

## Uniform supporting lemmas

`research2_band.md` supplies a complete algebraic proof that, for every
j,k>=0, h=2j-k>=0 and j>=2k^2+k-1, the expression (4) is nonnegative.
The proof even permits arbitrary symmetric nonnegative B and R with
R's linear part x+y: expand R=(x+y)+S and smooth each homogeneous
component by a binomial power. A symmetric monomial pair of residual
degree d is nonnegative after multiplication by (x+y)^N if N+2>=d^2.
In the relevant expansion d<=2k and N=2j-d, giving the stated bound.
This applies at the sharp start because A has nonnegative coefficients.
The top two rows, with C_j=binom(2j,j)/(j+1), are

\[
c_{s,j,2j}=C_j,\qquad
c_{s,j,2j-1}=(a_1+2\mathbf1_{s=1})C_j
 +(2j-1)(C_j-C_{j-1})\quad(j\ge1).
\]

These provide a genuine infinite supporting band, but leave the low and
middle orders unproved. No novelty is claimed for Newton interpolation
or for binomial smoothing as general techniques.

The new `research3_boundary_lemma.md` proves, for every n>=9 and every
actual shift s at n, that at j=2n-1 the polynomial tail extrapolation P
satisfies F(t)-P(0)=-a_(2n-2)-2a_(2n-s-2)<0. Every even forward difference
of order at least 4n is therefore negative. The all-order polynomial/
Newton method cannot extend unchanged through this boundary. This
universal result does not refute K_sharp, H, or the original conjecture;
it does not even assert negativity at orders h<=2j at that excluded start.
The independent verifier directly checks all 48 stages in 9<=n<=32,
including actual differences of order 4n and the tail extrapolations.

## Adversarial evidence, limitations, and next falsifier

After the conjecture was frozen, a second attack selected the degrees
{126,127,128,129,190,191,192,193,254,255,256,257,510,511,512,513} and
the shifts {1,2,3,floor((j+1)/2),floor((j+1)/2)+1,j-1,j,j+1} at each degree.
This includes the last admissible index before a dyadic start changes,
small shifts, threshold shifts, and first-overlap shifts. All 69,632 Newton
coefficients at these 128 pairs are nonnegative in
`research3_boundary_probe.py/.json`.
The arithmetic uses exact FLINT integer polynomials, with Python integer
differences; no floating-point signs are used.

`research3_boundary_verify.py/.json` independently checks the first five
Newton orders, both top formulas, and two outside-grid evaluations for
every listed pair. It does not separately recompute every middle Newton
coefficient in this sparse larger range. The complete second-implementation
coverage ends at j=96. The listed larger degrees are not exhaustive
coverage through 513. Untested shifts at those degrees, other j>96, and
the uniform low/middle-order assertion remain open.

The candidate is the explicit unproved K_sharp_v1, supported by the
restricted theorem, infinite high-order band, and precise boundary
obstruction. These together pass the research screen for scrutiny; they
are not asserted to meet a journal's novelty or interest threshold before
a fresh referee. There is no known gap in the supplied arguments for the
supporting lemmas and the finite-certificate reduction, but K_sharp itself
has no uniform proof. The original all-n, all-index problem is unresolved.

**One next test:** independently attack K_sharp_v1 for
j in {1022,1023,1024}, s in {1,2,3,511,512,513,j,j+1}, and every 0<=h<=2j
at the prescribed tau. A negative coefficient must be reproduced by the
signed binomial formula and distinguished from a negative H margin.

## Sources and reproduction

The current primary comparison and search limits are recorded in
`research3_literature.md`. The decisive BBFM journal PDF and Chen--Ono--Zhang
v2 PDF are copied unchanged into `evidence/external/` and included in the
candidate evidence. Source.md is preserved byte for byte. No literal
literature/*handoff*.md was present; the semantic outer-intake.md lead was
reread and its recurrence and source-status assertions checked.

From the project root, run these as separate foreground commands:

```
python3 evidence/research3_design_verify.py
python3 evidence/research3_sharp_probe.py
python3 evidence/research3_verify.py
python3 evidence/research3_boundary_probe.py
python3 evidence/research3_boundary_verify.py
python3 evidence/research3_integrity.py
```

Only the boundary producer needs python-flint (version 0.9.0 here); the
other scripts use Python 3 arbitrary-precision integers and the standard
library. Computational assistance covers the exact finite checks and
separate implementations described above. No random sampling, floats,
formal checker, additional agents, or fresh mathematical referee was used.
The runner must freeze the claim and obtain that referee before any
publication drafting.
