# Fresh mathematical referee report

Verdict: **accept** the exact frozen `result-note` scope in `claim.json`.
The original arbitrary-tree problem remains **unresolved**. This review
accepts both shifted inequalities and the complete boundary classification
for every tree of order at least two and diameter at most three. No
hypothesis, quantifier, or asserted contribution has been changed.

Referee job: `primary-20260913-subtree-annulus-referee-93236865529a`.
Review date: 2026-09-13 +08.
Snapshot digest:
`659e9ac113cd79ab485c69e753b2c42325ccfab4c29996550379ee716dbc538a`.

## Scope, provenance, and evidence

I read the original statement, precise problem, frozen claim and snapshot;
the submitted analytic proof and verification materials; the exact-check
code and serialized inputs; and relevant primary-source passages in the
listed evidence. I also checked the current Jin–Ma–Wang version record and
concluding conjecture online and made a bounded search for an equivalent
family result. I did not consult checkpoint/state files, earlier audit
verdicts, or job transcripts. No agents or other research workers were
launched. This is a separate referee context and separately written
verification code, not a claim of statistical independence or external
journal peer review.

All 18 files in the snapshot, including `claim.json`, match their recorded
SHA-256 hashes. The canonical sorted compact JSON hash of the files mapping
also matches the snapshot digest. The immutable `source.md` has SHA-256
`780c2b23b0b5c8ff23910d73403f7abbeb0f811ea709caaf64323eefbab29f94`.
No frozen input was edited. The integrity record is
`audit/referee-integrity.json`.

The assessed theorem concerns connected induced vertex subsets counted
once, including singleton subsets. Its unbounded family is all pairs of
integers a,b >= 1, not a bounded-order census or a balanced subfamily.
Stars supply the remaining diameter-at-most-three cases, including n=2.

## Reconstruction of the decisive argument

Write q=a+b, n=q+2, w=1+z and c=(q+1)^(1/(q+1)). Partition connected
subsets by whether they contain neither, one, or both ends of the central
edge. A subset containing neither end is a singleton leaf. Consequently

    Phi_D(z) = z Q(z),
    Q(z) = q + w^a + w^b + z w^q.

The four classes are disjoint and exhaustive. In particular Q has degree
q+1, leading coefficient one, and Q(0)=q+2; the root zero of Phi_D is
simple. The formula has no symmetry-quotient or missing-singleton issue.

For the closed inner disk |z+1/2| <= 1/2, both |z| and |w| are at most
one, and Re(w) >= 0. If q>=4, the three nonconstant summands of Q have
total modulus at most 3<q. If q=3, outside z=0,-1 both |z| and |w| are
strictly less than one, so their total modulus is strictly less than 3.
The two exceptions give Q(0)=q+2 and Q(-1)=q. If q=2, necessarily a=b=1;
then |2+2w| >= Re(2+2w) >= 2, whereas |z w^2| <= 1. Thus Q has no root
anywhere in the closed inner disk for every permitted pair. This proves
strict inner exclusion for every nonzero root, including its boundary.

For the outer circle |z+1/2|=c+1/2, put t=|w| and s=|z|. Expanding the
squares independently gives

    s^2+t^2 = K = 2c^2+2c+1,
    c <= t <= c+1,       s=sqrt(K-t^2) >= c > 1.

All denominators below therefore stay positive, including at both real
endpoints of the circle. For every k>=1 let

    f_k(t) = t^(-k) (K-t^2)^(-1/2).

Logarithmic differentiation gives

    (log f_k)'  = -k/t + t/(K-t^2),
    (log f_k)'' = k/t^2 + (K+t^2)/(K-t^2)^2 > 0.

Since f_k is positive, f_k'' is positive as well. A convex function on
this compact interval is bounded above by the larger endpoint value.
Here those endpoints satisfy

    f_k(c+1)/f_k(c) = (c/(c+1))^(k-1) <= 1.

It follows that f_k(t)<=f_k(c) throughout the circle. This is a pointwise
analytic estimate, not an inference from numerical sampling.

For fixed t>1, convexity of t^x+t^(q-x) on [1,q-1] gives
t^a+t^b <= t+t^(q-1). The interval degenerates harmlessly when q=2.
The triangle inequality now yields

    |q+w^a+w^b| / |z w^q|
       <= f_(q-1)(t) + f_1(t) + q f_q(t)
       <= (c+c^(q-1)+q) / ((c+1)c^q) = F.

The exponents q-1,1,q are all at least one. To independently check the
claimed algebra, substitute c^q=(q+1)/c and c^(q-1)=(q+1)/c^2. Then

    1-F = [c+(q+1)-c^2-(q+1)/c] / ((c+1)(q+1))
        = (c-1)(q+1-c^2) / (c(c+1)(q+1)) > 0.

Indeed q+1>=3, c>1, and c^2=(q+1)^(2/(q+1))<q+1. This sign proof
covers q=2, arbitrary imbalance and every finite q. The margin need not
be bounded below uniformly as q tends to infinity, and the proof uses no
such assertion or limit exchange.

Hence |q+w^a+w^b|<|z w^q| at every outer-boundary point. The hypotheses
of polynomial Rouche are satisfied: both polynomials are entire, the
contour is a circle, and the strict comparison has no boundary zero.
The polynomial z(z+1)^q has precisely q+1 interior zeros counted with
multiplicity, at 0 and -1, both a distance 1/2 from the circle's center.
Therefore Q has q+1 interior zeros. Its degree is exactly q+1, so none
remain outside or on the circle. The separately handled zero of Phi_D
is also interior. This proves the submitted strict outer inequality.

Every diameter-three tree is a double star: the two middle vertices of
a longest path form a central edge, and a vertex farther than one edge
from that edge would make a path of length at least four to the opposite
end of the chosen path. Attachments at an endpoint likewise violate the
diameter. The two leaf populations are nonempty. Trees of diameter one
or two are stars.

For a star with m=n-1>=1, the known formula is
Phi(z)=z[(1+z)^m+m]. Nonzero roots satisfy w^m=-m and |w|=d=m^(1/m).
For m>=2, |w-1/2|>=d-1/2>1/2. For m=1 the sole nonzero root is -2,
so it also lies strictly outside the inner disk. The outer triangle
bound |w-1/2|<=d+1/2 has equality exactly at w=-d. This solves w^m=-m
exactly when m is odd, equivalently n is even. The resulting boundary
root is uniquely -1-d. Zero is simple since Phi(z)/z at zero is n.
Together with strict double-star containment this proves the entire
frozen boundary classification, including n=2 and n=3.

No circular lemma, missing degenerate case, unproved stability premise,
or unsupported all-parameter extrapolation was found. The optional P4
transform H(x)=4x^3+9x^2+8x+2 and determinants 9,64,128 are correct,
but the direct disk estimate already proves that case. The half-plane
identity in `problem.md` also has the correct sign and introduces no
pole root; it is neither needed for the main proof nor treated as new.

## Independent finite verification actually performed

I wrote and ran `python3 audit/referee-verify.py`. It imports no researcher
code and does not execute or alter the frozen research script. All checks
passed; exact inputs and outputs are in `audit/referee-exact-checks.json`.

- Exhaustive subset connectivity was recomputed by graph traversal for
  all 25 unordered pairs with 2<=a+b<=10. These counts match both the
  independently assembled counting formula and the serialized counts.
- All 144 unordered pairs with 2<=a+b<=24 were checked, with no missing
  or duplicate parameter pair. Homogeneous Horner substitution reproduces
  both submitted initial polynomials for every pair, after primitive
  normalization. Each rational outer radius was checked to be strictly
  smaller than c+1/2 using integer/rational exponentiation; its recorded
  mesh choice also matches the stated maximum on the 1/10000 grid.
- For each of the 288 region polynomials P(u), I formed
  (1-s)^d P((1+s)/(1-s)) and checked exact rational Routh first-column
  positivity. The Cayley transformation satisfies Re(s)<0 iff |u|<1.
  Degree loss at u=-1 is explicitly rejected. Every table had the full
  degree and strictly positive first column. This differs from the
  researcher's Schur recursion. Six separately chosen stable, unstable,
  boundary and delayed-failure controls behaved as expected.

For the inner substitution u=1/(2z+1), strict disk stability is precisely
|z+1/2|>1/2. The reconstructed polynomial has its full degree and constant
term one, so neither the pole nor an artificial zero was hidden. For
the outer substitution z=Ru-1/2 it gives |z+1/2|<R<c+1/2. Every root
is covered in each finite case; no approximate root solver was used.
The saved Schur intermediate hashes and success flags were not relied on.
The submitted Schur argument's sufficient direction was also checked:
its reversed polynomial has the same boundary modulus, and a boundary
root would descend to the reduced polynomial before Rouche is applied.

These computations are supplementary finite checks. The infinite theorem
is established by the analytic argument above, not by the 144 cases or
by passing an integrity or audit script.

## Primary-source comparison and contribution judgment

[Brown–Mol, arXiv:1810.08655v1](https://arxiv.org/pdf/1810.08655v1),
read from the frozen PDF on physical pages 1–3 and 14, uses precisely the
connected-induced-subset definition. Page 1 already gives the star and
path formulas. Conjecture 4.2 on page 14 is the full shifted annulus,
with prior verification through order 18. Those formulas and that census
are not new contributions here.

[Jin–Ma–Wang, arXiv:2608.07898v2](https://arxiv.org/html/2608.07898v2)
is still the current listed version, dated 14 August 2026, in the
[live version record](https://arxiv.org/abs/2608.07898). I checked its
Theorem 1.3, the Section 3 comparison/equality argument, and Section 5.
Its universal upper disk is centered at zero. The shifted annulus remains
Conjecture 5.1. The comparison lemma assumes |z|>=2; on the circle used
in this candidate |z| can equal c<2. Thus that lemma cannot simply be
invoked along this circle. Its radial theorem and equality classification
do not supply the submitted translated-circle theorem as a direct
corollary. The new argument instead controls |z| and |1+z| together.

[Wagner–Wang, arXiv:2605.03583v1](https://arxiv.org/html/2605.03583v1),
whose definitions and main statements were checked in the frozen primary
rendering, requires minimum degree at least alpha*n for fixed alpha>0
and sufficiently large n. Double stars have minimum degree one. The
asymptotic theorem therefore supplies no unrestricted double-star result.

I also checked the connected-set/node-reliability transformation and
principal root statements in the frozen passages of
[Brown–Mol, arXiv:1607.08496v1](https://arxiv.org/pdf/1607.08496v1).
They do not state this double-star annulus; their complex-density
construction concerns a broader graph class. The inspected contents,
star/path sections and root-keyword passages of
[Yu's thesis](https://repository.tudelft.nl/file/File_35464569-654a-4b1a-be98-fe8dce043f11)
also supplied no matching family theorem. These were bounded passage
checks, not full audits of those works.

Fresh queries included the phrases `subtree polynomial` with `double
stars`, `double-star`, `diameter three` and `bistar`, and `node reliability`
with `double star` and roots. No equivalent theorem was located in the
inspected sources. Search returns were mostly irrelevant; they are not
evidence of priority. An author-hosted 2019 slide PDF was a relevant
search lead but failed to open, and its contents are not claimed checked.
The frozen literature dossier also explicitly leaves a full Mol-thesis
and citation-network review outside its coverage. Raw fresh web returns
are preserved in `audit/referee-web-a.txt`, `audit/referee-web-b.txt` and
`audit/referee-web-c.txt`. The acceptable novelty wording remains limited
to no equivalent found in these bounded sources on this date.

The precise delta is a uniform proof of both conjectured shifted bounds,
with strictness, for the entire two-parameter double-star family, and
therefore a complete natural structural class with its equality cases.
This is a modest but nontrivial result-note contribution: its central
convex endpoint estimate is an additional analytic step absent from the
nearest radial result. The class allows arbitrarily large order and
arbitrary imbalance, so the theorem is not a restatement of known finite
verification or an arbitrary fixed toy case. A credible use is an exact
structural case of the annulus problem and a proved translated-circle
comparison for testing extensions to larger tree classes. Such extensions
are not asserted. The star calculations, transforms and finite checks
should remain supporting material in this one coherent note.

## Final disposition and remaining limits

The exact frozen scope passes correctness, evidence and contribution
review. No mathematical repair or claim revision is required. Acceptance
does not assert exhaustive priority, settle arbitrary trees, or constitute
journal acceptance. No manuscript or publication audit was performed.

The next workflow step is the runner's mathematical integrity/provenance
gate, followed by preparation of the result note at this accepted scope.
The arbitrary-tree original must remain explicitly unresolved, and the
bounded novelty language must be retained. Any substantive alteration of
the claim or decisive evidence requires a new snapshot and fresh review.
