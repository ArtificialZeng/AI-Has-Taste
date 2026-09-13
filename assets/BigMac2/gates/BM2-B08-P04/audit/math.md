# Fresh mathematical referee report

**Referee job:** `bigMac-00008-p04-referee-c66654553008`  
**Frozen snapshot:** `0bccbebcb4d3e33f7bd96429a92c600339dc97a318485535805a1b0769d16be7`  
**Candidate:** full resolution of the degree-at-most-four statement in `source.md`  
**Verdict:** **ACCEPT**

I reconstructed the argument from `source.md`, `problem.md`, `claim.json`, the
snapshot, and the frozen mathematical and computational evidence. In accordance
with the job instruction, I did not use `checkpoint.md`, owner state, confidence,
earlier verdicts, or job transcripts. I also performed a fresh third exact
calculation recorded in `audit/referee_independent.py` and
`audit/referee_independent.json`.

## 1. Scope and completeness of the finite class

Let (G(I)) be the unique minimal monomial generating set. Since (I) is
(mathfrak m=(x,y,z))-primary, it contains a power of each variable. A minimal
generator dividing such a power must itself be a pure power. Hence (G(I))
contains exactly one generator on each coordinate axis. With at most four
generators, the only possibilities (with variable labels retained) are

\[
(x^a,y^b,z^c),\qquad
(x^a,y^b,z^c,x^r y^s z^t).
\]

The degree hypothesis gives (1\leq a,b,c\leq4) and (r+s+t\leq4). In the
four-generator case, minimality is equivalent to

\[
0\leq r<a,\quad 0\leq s<b,\quad 0\leq t<c,
\quad |\{i:r_i>0\}|\geq2.
\]

The strict inequalities prevent a pure power from dividing the mixed
generator; support at least two prevents the mixed generator from dividing a
pure power. Conversely these conditions make all four generators incomparable.
Thus there is no omitted generator type, redundant-presentation issue, or
symmetry assumption.

There are (4^3=64) pure-power triples. I independently checked the count of
mixed cases without relying on a variable-orbit quotient. Mixed exponents with
support two contribute

\[
3\cdot4\sum_{p,q\geq1,\ p+q\leq4}(4-p)(4-q)
=12(31)=372,
\]

and those with support three contribute

\[
3^3+3(2\cdot3\cdot3)=27+54=81.
\]

Hence the four-generator count is (372+81=453), and the complete labeled
class has (64+453=517) ideals, exactly as enumerated.

For a fixed triple ((a,b,c)), every exponent outside
(B=[0,a-1]\times[0,b-1]\times[0,c-1]) is already in (I), and therefore in
(overline I). All standard monomials of both ideals lie in this box. The
expanded grid used in the evidence also contains every immediate coordinate
successor of every point of (B).

## 2. The v-number reduction

Both (I) and (overline I) have radical (mathfrak m), hence are
(mathfrak m)-primary and have the sole associated prime (mathfrak m). For
either monomial ideal (J), a homogeneous class annihilated by (mathfrak m)
decomposes into monomial classes of the same total degree, and monomial-ideal
membership is termwise. Thus a nonzero homogeneous socle class exists in degree
(d) if and only if a monomial socle class exists in degree (d). Consequently

\[
v(J)=\min\{|u|:x^u\notin J,\ x^{u+e_1},x^{u+e_2},x^{u+e_3}\in J\}.
\]

This addresses the possibility of a lower-degree nonmonomial witness. It also
shows that the calculation uses only exponent divisibility and is independent
of the field and its characteristic.

## 3. Exact integral-closure decisions

For generator exponent set (A=\{a_1,\ldots,a_m\}), the frozen proof uses the
standard exact criterion

\[
u\in\operatorname{NP}(I)
\iff
\exists\lambda_i\geq0:\ \sum_i\lambda_i=1,
\quad\sum_i\lambda_i a_i\leq u
\text{ coordinatewise}.
\]

I checked both supplied implementations.

1. `enumerate_lp.py` works over `fractions.Fraction`. A nonempty feasible
   section of the simplex is a nonempty compact polytope and has a vertex. In
   the affine hyperplane (sum\lambda_i=1), a vertex admits (m-1) linearly
   independent active inequalities. The program tries every (m-1)-subset,
   discards singular systems, and checks every original inequality after the
   exact solve. Degenerate vertices cause no omission because some independent
   active subset still exists.

2. `enumerate_facets.py` uses the separation characterization
   (w\cdot u\geq\min_{a\in A}w\cdot a) for every (w\geq0). The coordinate
   planes and generator-tie planes subdivide the nonnegative orthant into
   polyhedral cones on which the minimum is one linear form. Every extreme ray
   of such a pointed cone is cut out by at least two of those boundary planes;
   the pairwise cross products therefore include all required rays. Testing
   additional nonnegative cross-product rays is harmless because the dual
   inequality is required for every nonnegative (w). The implementation uses
   exact integers, includes coordinate-axis rays, and does not rely on floating
   point.

The two v-number routes are also genuinely distinct: successor tests for both
ideals in the first program, versus the closed-form input socle and global
maximal elements of the closure's standard down-set in the second. The stated
closed-form input socle is correct: a maximal box point failing to dominate the
mixed exponent has exactly one positive mixed coordinate lowered to one below
that coordinate of the mixed exponent, with the other two coordinates at their
box maxima.

## 4. Fresh recomputation and falsification checks

I reran both frozen enumerators into new audit outputs and reran the comparison.
The regenerated files have exactly the frozen SHA-256 values

- primal output: `e46eb758223bb08b47e69bc5a127a5db7b5f98620195e53f2d45419314c6c013`;
- dual output: `73367001db7f12b3ae1d982641e466a7b2fb1905e38e0c4204c8794330f91c9e`;
- comparison output: `67ee57a1d15bdf9c7ffbc5d715f317da921c8833389294a7c09a6a4d1f2b7c6c`.

As a separate attack, I wrote a third checker that substitutes one barycentric
variable and applies exact rational Fourier--Motzkin elimination. It shares
neither active-set vertex enumeration nor dual-cone ray generation with the two
frozen methods. It recomputed the input and closure socles by successor tests
for every labeled ideal and compared them record by record with the frozen
certificate. The check compared 1,034 complete socle lists containing 3,552
socle exponents and reproduced all 517 pairs of v-numbers. Its result is in
`audit/referee_independent.json`.

All three exact routes give the distribution

| (v(\overline I)-v(I)) | -6 | -5 | -4 | -3 | -2 | -1 | 0 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| labeled ideals | 1 | 6 | 19 | 82 | 194 | 124 | 91 |

The counts sum to 517 and there is no positive difference. Equality cases are
therefore included rather than discarded. Each route also returns
(v(I)=2) and (v(\overline I)=3) for the nearby degree-five control
((x^2,y^2,z^5,xyz)), so the machinery detects failure in the claimed direction
immediately beyond the frozen degree bound.

I specifically checked the edge cases (a,b,) or (c=1), zero coordinates in
the mixed generator, support exactly two, and all variable labels. No division
by a parameter, characteristic assumption, limiting argument, or unverified
compactness exchange occurs.

## 5. Source comparison, contribution, and gaps

The frozen source boundary records positive results for two variables and for
three-variable equigenerated ideals, and a four-generator degree-five
counterexample. The candidate neither attributes the degree-four question to
those authors nor weakens it: it proves the exact universal degree-at-most-four
statement posed in `source.md`, over every field, for all minimal generating
sets of size at most four. This is a full resolution of the original frozen
claim, not a subsidiary restriction or a search-only observation. The
degree-five computation is used only as a control, not as proof of the theorem.

No mathematical or scope gap remains in the frozen candidate. This report does
not make a broader priority claim beyond the comparison stated in the frozen
source materials.

## Verdict

**ACCEPT.** The exact scope in `claim.json` is correct, exhaustively covered,
and supported by a complete finite proof with reproducible exact certificates
and an additional fresh exact verification. `resolution-paper` with original
status `proved` is the appropriate classification.
