# Fresh mathematical referee report

**Verdict: accept the exact frozen result-note scope.** The proof establishes
the stated four-edge theorem, including the stronger algebraic assertion for
all real m,n >= 4 and the closed-disk exclusion for the reduced rational
numerator at integer parameters. The unrestricted original conjecture remains
unresolved. No substantive revision or restriction of the candidate was made
in this review.

Referee job: `primary-20260914-matching-mgf-zero-free-referee-868ff24221f8`.
Review date: 2026-09-14.
Snapshot: `d80a6dbdfd612bd1bf2471a72897466bbe4e48864aa0ee5a6b08702e91645e11`.
Frozen kind: `result-note`. Frozen original status: `unresolved`.

## Inputs and independent checks

I read the original statement, precise interpretation, claim, snapshot, and
the listed proof, programs, exact data, and source comparison. I inspected the
decisive sections of the listed Wästlund primary text, independently extracted
PDF pages 8 and 23, and visually checked the rendered page 8 containing the
recurrence and its exceptional-case instructions. That rendering is retained
as `audit/referee-source-page-8.png`. I also checked the actual Holtz theorem
and the primary bibliographic sources described below. Unlisted project
history, checkpoint/state files, previous audit verdicts, and job transcripts
were not consulted. Proposer assertions of completeness were not evidence.

All 13 input file digests, including `source.md`, match the frozen snapshot;
its canonical mapping digest also matches. These checks were repeated after
the independent computation. No frozen input was modified.

The new program `audit/referee_verify.py` imports neither proposer program and
does not execute either one. It uses Python exact integers and SymPy 1.14.0,
with original ghost indices for the recurrence and fraction-free Bareiss
elimination for the determinants. The proposer's two determinant algorithms
were permutation expansion and recursive Laplace expansion. Thus this review
adds a distinct determinant calculation and separately checks the translation
of the primary recurrence, although one computer algebra library is shared.
This is a fresh review pass, not formal proof-assistant certification or a
claim of statistical independence.

Reproduction command:

```sh
python3 audit/referee_verify.py
```

The successful run recorded 82 passing checks in
`audit/referee-verification.json`. All seven displayed coefficient matrices,
112 transformed-polynomial coefficients, and 951 Hurwitz-determinant
coefficients were compared exactly. The support rectangles were checked in
full, including their positive constant terms. Exact additional parameter
checks were (4,4), (4,17), (17,4), (5,6), and (9/2,17/3); these are diagnostics,
not the reason for the universal conclusion.

## Reconstruction of the decisive argument

The probabilistic input is Wästlund's Theorem 8, equivalently equation (9)
with its explicitly separate d=0 rule. It concerns minimum total cost of a
cardinality-k matching with independent rate-one exponential edge costs;
only the d=0 ghost function is the normalized MGF. For d>=1, the source gives

\[
F^{(d)}_{k,m,n}=
\frac{F^{(d-1)}_{k-1,m,n-1}/(m-k+d)
 +(d+1)tF^{(d+1)}_{k,m,n}/n+F^{(d)}_{k-1,m,n-1}}
 {1-dt/((m-k+d)n)}.
\]

At d=k the last two numerator terms vanish. At d=0 the rule is
\(F^{(0)}_{k,m,n}=tF^{(1)}_{k,m,n}/n+F^{(0)}_{k-1,m,n-1}\), and the base
value is one. These are the actual instructions on the inspected PDF page,
not an inference from a generic formula at a zero denominator. The listed
source is [Wästlund, arXiv:2602.07563v1](https://arxiv.org/pdf/2602.07563v1),
printed pages 7–8 and 23.

Substituting k=i, d=i-j and n replaced by n-4+i gives precisely the dossier's
triangular recurrence. When i>0 its column count n-4+i is at least one, and
m-j is at least one for j<i. The separate diagonal rule never divides by
m-i. Thus m=4 or n=4 causes no invalid recurrence step.

I independently evaluated the source recurrence in QQ(m,n,t), transcribed
the displayed sextic in the variables s=m+n and r=mn, and verified

\[
F^{(0)}_{4,m,n}=\frac{AP(t)}{Q(t)},\quad
A=\prod_{j=0}^{3}(m-j)(n-j),\quad
Q(t)=\prod_{i,j\ge0,\ i+j<4}
       \bigl((m-i)(n-j)-(4-i-j)t\bigr).
\]

The transcribed P agrees coefficient by coefficient with the frozen expanded
data, has degree six and leading coefficient 12, and satisfies AP(0)=Q(0).
Transpose symmetry and the independently printed 3-by-3 formula (10) also
hold exactly. Agreement with the older frozen generic rational data was
checked by rational-function equality, not by textual comparison.

With R=mn/4, direct substitution and exact cancellation reconstruct

\[
H(z)=\frac{4^6}{(mn)^3}(1+z)^6
       P\left(R\frac{1-z}{1+z}\right)
     =h_0z^6+\cdots+h_6.
\]

All seven coefficients match the frozen expressions. After m=4+x,n=4+y,
the seven 4-by-4 matrices printed in the proof agree with the resulting
polynomials. This checks the displayed proof, not only its auxiliary JSON.

For the stated Hurwitz matrix, the independent Bareiss calculation replaces
each trailing entry by
\((b_{kk}b_{ij}-b_{ik}b_{kj})/p_{\rm previous}\), starting with previous
pivot one. Every polynomial division is exact; pivots are nonzero
polynomials. Its final entries give the leading determinants. All six
results match every serialized coefficient. The reproduced minima are:

| Determinant | Full support | Coefficients | Minimum coefficient |
|---|---|---:|---:|
| Delta1 | 0<=a,b<=3 | 16 | 82200 |
| Delta2 | 0<=a,b<=6 | 49 | 5637588000 |
| Delta3 | 0<=a,b<=9 | 100 | 176698647552000 |
| Delta4 | 0<=a,b<=12 | 169 | 1539481522876416000 |
| Delta5 | 0<=a,b<=15 | 256 | 2195347272420556800000 |
| Delta6 | 0<=a,b<=18 | 361 | 237097505421420134400000 |

Each h_i also has the complete support 0<=a,b<=3 and only positive integer
coefficients. Consequently h0>0 and all six determinants are strictly
positive throughout x,y>=0, including both axes and their intersection.
The identity Delta6=h6 Delta5 is verified separately. Positivity of h_i
alone would not suffice; the determinant checks are essential.

The real Routh–Hurwitz criterion therefore makes H strictly stable. I
checked the ascending-coefficient convention in the proof of Theorem 3 of
[Holtz, *Hermite-Biehler, Routh-Hurwitz, and total positivity*](https://arxiv.org/pdf/math/0512591),
page 3. Applied to f(w)=w^6 H(1/w), its first seven leading minors are
h0,h0 Delta1,...,h0 Delta6. The independent program verifies this matrix
identity too. Here f(0)=h0>0 and its leading coefficient h6>0; inversion
bijections the nonzero roots and preserves the sign of their real parts.
The source criterion thus supplies strict left-half-plane stability in the
precise convention used by the proof.

For any complex t with |t|<=R except t=-R, put z=(R-t)/(R+t). Then

\[
\operatorname{Re}z=\frac{R^2-|t|^2}{|R+t|^2}\ge0,
\qquad 1+z=\frac{2R}{R+t}\ne0.
\]

Strict stability excludes P(t)=0. The omitted point is covered by the
independently verified identity
\(h_0=4^6P(-R)/(mn)^3>0\). This proves the full closed-disk algebraic
claim for every real m,n>=4; there is no missing boundary point or limiting
argument.

For every denominator factor, i+j<4 and

\[
\frac{(m-i)(n-j)}{mn}
\ge(1-i/4)(1-j/4)
\ge1-(i+j)/4.
\]

All factors used in this comparison are positive. Therefore every root
\((m-i)(n-j)/(4-i-j)\) of Q is real and at least R. Together with A>0,
this gives zero exclusion for F in the open disk. Specializing m,n first
cannot make P identically zero because its leading coefficient is 12.
Polynomial gcd cancellation then only removes numerator roots. It cannot
introduce a closed-disk zero. At t=R the (0,0) denominator factor vanishes
while \(P(R)=(mn)^3h_6/4^6>0\), so the boundary point is indeed a pole,
possibly of higher order. The candidate makes no finite-value assertion
there.

Finally, for each fixed nonnegative cost array the minimum matching cost is
at most the average cost over all four-edge matchings. Edge symmetry gives
\(C_{4,m,n}\le4\sum X_{ij}/(mn)\). Hence for 0<=a<R,
\[
\mathbb E e^{aC_{4,m,n}}
\le (1-4a/(mn))^{-mn}<\infty.
\]
Choosing a larger real a for each compact subset of the disk gives the
domination needed for analytic expectation. The source identity and analytic
continuation identify this expectation with the rational expression on the
disk. Thus the conclusion concerns the MGF in the question, not only a
formal rational function.

## Contribution and bounded source comparison

The nearest zero-exclusion result is Proposition 15 and Section 4.3 of the
inspected Wästlund version: all k<=3. Proposition 16 leaves finitely many
possible exceptional pairs for each fixed k, with no explicit cutoff. I read
these statements and the concluding qualification on printed pages 28–34.
The live [arXiv record](https://arxiv.org/abs/2602.07563) still displayed only
v1 when checked during this job. The candidate removes every possible
exception for k=4, and proves the associated sextic statement on the entire
real quadrant m,n>=4.

The older transform computation is correctly attributed. The
[Alm–Sorkin publisher record](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/exact-expectations-and-distributions-for-the-random-assignment-problem/9D846C840A833AEDA38A969A2E4D295C)
and [IBM Research abstract](https://research.ibm.com/publications/exact-expectations-and-distributions-for-the-random-assignment-problem)
confirm explicit expectation/distribution work through k=4. This review
inspected those abstracts and bibliographic information, not that paper's
full body. Wästlund also explicitly discusses that older computation while
proving zero exclusion only through k=3. Reconstructing a transform is not
the accepted novelty.

Fresh search queries included `"2602.07563" "four"`,
`"Wästlund" "zero-free" "4"`,
`"matching" "Hurwitz" "moment generating"`,
`"Exact Expectations and Distributions for the Random Assignment Problem"`,
`"2602.07563" zero free proof`,
`"Moment generating functions in combinatorial optimization" matching zeros`,
and `"random assignment" "zero-free" four`.
These yielded the primary problem paper, the older distribution records,
mirrors and unrelated results. A search snippet concerning a uniform-cost
assignment central limit theorem was not used: it supplies no theorem about
this fixed-four-edge exponential-cost MGF. Matching-count partition-function
results likewise concern a different object. No equivalent uniform k=4
zero-exclusion result was identified in the primary material actually
inspected. This is a bounded novelty assessment, not proof of priority or
an exhaustive review of inaccessible or unindexed work.

The contribution passes for a result-note. It addresses the next full
matching-size range in the source's stated conjecture with two unbounded
parameters, rather than an arbitrary finite sample. It is not a direct
consequence of the ineffective finite-exception theorem or of an explicit
Laplace transform. The nonautomatic step is the universal positivity of all
six transformed determinants. It supplies a rigorous domain for the
four-edge cumulant expansion and a reproducible benchmark for further
zero-exclusion methods. The classical criterion and arithmetic algorithms
remain prior tools; no novelty for them is claimed.

## Gaps, limitations, and disposition

No mathematical gap was found in the exact submitted scope. The hypotheses,
recurrence boundary cases, normalization, determinant orientation, strict
positivity on the parameter boundary, omitted Möbius point, poles,
specialization, and expectation analyticity all pass. No theorem for k>=5,
Gaussian scaling limit, or global priority assertion is accepted.

The limitations above are the disclosed limits of the literature screen
and computational review, not substitutes for missing mathematical steps.
No scope change is requested. Acceptance is tied to the unchanged snapshot;
the next workflow step is its provenance/integrity gate, followed by writing
within this exact accepted scope. This report does not certify a manuscript,
citations in a future manuscript, or a release build.
