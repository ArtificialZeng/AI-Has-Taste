# Mathematical referee report

Verdict: **accept the exact frozen result-note scope**. The original all-odd
global minimum and complete switching-equality classification remains
**unresolved**. No part of the frozen candidate has been dropped or weakened
to obtain this verdict.

Referee job: `primary-20260914-dumbbell-min-energy-referee-6a96192e6362`.
Snapshot: `c54ee1930645183cb069fba12fb9fd382eddca737522332f05cf84b9349a0cae`.
Review date: 2026-09-14.

This fresh review used `source.md`, `problem.md`, `claim.json`, the snapshot,
and the snapshot-listed evidence. It did not consult checkpoint/state files,
earlier job transcripts, or an earlier referee verdict. All thirteen frozen
file hashes and the canonical snapshot digest matched at entry. The original
source hash is
`ec7265dcc8f807c129c4343be3ebf171d3c8a7b56c87316810172368a8e016fa`.
The frozen files were left unchanged. The mathematical decision below comes
from reconstructing the proofs and checking certificates, not from their
proposer's assessment or the snapshot machinery.

The scope includes the coefficient and simple-zero identities for all allowed
lengths, the singular expansion and necessary conditions, strict local
sufficiency under the stated strict normal inequality, fixed-product strict
convexity and uniqueness, the asymmetric ratio and boundary criteria, the full
D331 classification with eight switching lifts, and the exact D335 descent
test. The exclusions already in the claim remain exclusions: equality in the
normal threshold, full-square sufficiency of singular boundary points, and
the original classification for all triples.

**Reconstruction of the spectral reduction and zero branch.** Removing one
edge from each cycle leaves a spanning tree. Diagonal unitary switching fixes
its gains to one, and the two oriented cycle products are the remaining
invariants. Determinant permutations consist of edge transpositions and
either or both of the two vertex-disjoint cycles. A transposition contributes
minus one; the sum of the two orientations of a cycle contributes minus
twice its real gain. This proves the four-term matching-polynomial formula
with its positive double-cycle term. Equality of real parts means equality
of spectra here, whereas equality of the oriented products characterizes
switching; the candidate correctly retains all lifts.

An odd cycle in a perfect matching of the dumbbell must use its incident
connector edge. The remaining connector and the two even paths then have
forced alternating matchings. Thus the full graph has one perfect matching.
For the cycle-deleted graph, an odd cycle of length s with a tail of 2L
vertices has s+L near-perfect matchings: the base count is s, and extension
of the tail by two vertices increases the count by one. Indeed, the last
vertex is either matched to its neighbor, reducing to the shorter tail, or
is the unique uncovered vertex, leaving one forced perfect matching.
The exchanged count is r+L. Substituting these coefficients, including
alpha=(-1)^((r+1)/2)a and beta=(-1)^((s+1)/2)b, gives

    P(0)=eps(1-4 alpha beta),
    P_x(0)=-2 eps[(s+L)alpha+(r+L)beta]=-2 eps H.

This also covers ell=1 and the empty remaining path. On alpha beta=1/4,
the two coordinates have the same nonzero sign, so H cannot vanish,
including at the four boundary points. There is exactly one zero root,
and it is simple. Fresh symbolic adjacency determinants verified both
coefficients for six triples covering both odd congruence classes and
connector lengths 1, 3, and 5.

At a fixed interior singular point, the implicit function theorem supplies
the analytic root lambda with

    d lambda[h]=-2(beta h_alpha+alpha h_beta)/H.

The other roots stay away from zero. Their positive and negative group sums
are analytic by contour integrals, even if roots inside either group
coincide. Calling their absolute sum F gives E=F+|lambda|. The characteristic
polynomial is monic and real, and division by x-lambda gives a monic real
polynomial Q whose constant term remains nonzero. The exact factorization

    |t^N P(i/t)|^2=(1+t^2 lambda^2)|t^(N-1)Q(i/t)|^2

isolates the entire absolute-value contribution, since the integral of
log(1+t^2 lambda^2)/(pi t^2) is |lambda|. Differentiating the Q integral is
legitimate: its differentiated integrand is uniformly O(1) near zero and
O(t^-2) at infinity in a sufficiently small neighborhood. At zero, reality
of the coefficients removes the linear term in the modulus squared; at
infinity, Q(0) is uniformly bounded away from zero. Compact intermediate
t intervals cause no problem because Q has only real roots. At the singular
point the fixed-t derivative of log(1+t^2 lambda^2) vanishes. Consequently
grad F=(2/pi)(I_alpha,I_beta), with convergent integrals, and Taylor expansion
gives precisely the claimed absolute-value term and O(||h||^2) remainder.
The remainder is uniform in directions h near the fixed point; no estimate
independent of all lengths or all base points is required by the claim.
The same domination argument applied directly to P proves the ordinary
interior stationarity equations away from the singular locus.

**Optimality and the strict sufficiency assertion.** Let g=grad F and
n=(beta,alpha). Nonnegativity of all directional derivatives is equivalent
to g=k n with |k|<=2/|H|: tangent directions first force normality, and the
opposite normal directions give the bound. Since alpha beta=1/4, this is
exactly

    alpha I_alpha=beta I_beta,
    |alpha I_alpha+beta I_beta|<=pi/(2|H|).

First-order conditions alone would not establish strict local minimality.
The candidate supplies the additional argument. In the local coordinates
p=alpha beta and u=(1/2)log(alpha/beta), on either fixed common-sign branch,

    E(p,u)=F(p,u)+|p-1/4|c(p,u),
    c(q)=2/|H(q)|,  F_p(q)=4J/pi.

The strict normal inequality is |F_p(q)|<c(q). Continuity then bounds
E(p,u)-E(1/4,u) below by a positive constant times |p-1/4| throughout a
small neighborhood. On p=1/4, tangential stationarity is the unique strict
constrained minimum by the convexity argument below. These two facts prove
strict local minimality in the square. There is no circular dependence:
the constrained convexity proof uses only the kernel representation.
The non-strict equality case is correctly left unclassified.

**Fixed-product structure and the length criterion.** For p>0, write
C=d+z+w, with d=(Z-pW)^2+2pXY>0, z=pX^2 exp(2u)>0 and
w=pY^2 exp(-2u)>0. Direct differentiation gives

    (log C)_uu=4[d(z+w)+4zw]/(d+z+w)^2>0.

Every energy integral is finite. Integrating the pointwise strict convexity
inequality proves strict convexity without a limiting exchange. The first
u derivative is integrable as well: its numerator is of order at least
t^(2 min(r,s)) near zero before division by t^2, and its logarithmic
derivative is bounded at infinity. The same holds for the second derivative.
Thus each nondegenerate compact interval of allowed u has one constrained
minimum. At p=1 there is only one point. Symmetry establishes the equal-cycle
case and simultaneous negation supplies the negative branch.

For r<s, solve the path recurrence using t exp(eta) and -t exp(-eta), with
eta=asinh(1/(2t)). Substitution into the source definitions gives

    X/Y = [sinh(s eta)+c_eta cosh(s eta)] /
          [sinh(r eta)+c_eta cosh(r eta)],
    c_eta=sinh((ell-1)eta)/(2 cosh(ell eta)cosh eta).

The ell=1 convention f_-1=0 agrees with this identity. One has
0<=c_eta<=L eta, because cosh(ell eta)cosh eta>=cosh((ell-1)eta) and
tanh y<=y. For fixed c>=0, the derivative numerator of
(sinh z+c cosh z)/(z+c) is

    z cosh z-sinh z+c z sinh z+c^2 sinh z>0  (z>0).

It follows that X/Y>(s+c_eta/eta)/(r+c_eta/eta)>=(s+L)/(r+L).
I independently checked the recurrence-to-hyperbolic identity algebraically
in four cases, including the equality case of the subsequent length bound;
the preceding analytic inequalities establish the all-length statement.

At u=0 the energy derivative is strictly positive, so the unique constrained
minimum has alpha<beta for p<1. At the left endpoint (alpha,beta)=(p,1),
p>=(r+L)/(s+L) implies pX>Y for every finite t>0. The endpoint derivative
is positive, and strict convexity puts the unique constrained minimum there.
In particular s+L>=4(r+L) forces the singular constrained minimum to
(1/4,1), including equality in this length inequality. Every other point
on that branch admits constrained descent, so no interior singular point
can be a full-square local minimum. This reasoning makes no assertion that
the endpoint itself minimizes the full square.

**Exact examples and falsification checks.** For D331, the sign reduction
strictly excludes every nonzero point with alpha beta<=0 by comparison to
the origin. For positive product, the kernel difference from its same-sign
diagonal point is X^2(alpha-beta)^2. On the diagonal the two stated cubic
factors were reproduced directly from the adjacency determinant.
For 0<=c<1/2, real-rootedness, products and traces give the asserted sign
counts and E(c,c)=2+2(U+v), where h(U)=1-2c, h(v)=1+2c and
h(z)=z^3+z^2-3z. For 0<c<1/2, v>U>1 and h' increases there, proving strict
decrease. For c>1/2, each cubic has one positive root: the negative
pairwise-root sum excludes three positives in the first, and the negative
trace excludes them in the second. The positive roots w>2 and v>1 have
strictly positive implicit derivatives, proving strict increase.
Continuity handles c=0,1/2,1. This proves the full closed-square minimizer
set, rather than inferring it from a numerical plot or a local cusp.

There are four oriented cycle-product lifts of each of (1/2,1/2) and
(-1/2,-1/2), hence eight switching classes on the fixed graph without an
automorphism quotient. Their energy, 2+sqrt(13)+sqrt(5), is verified by the
displayed factorization. The independent checks also reproduce the smooth
diagonal derivative

    G=-2/5-2 sqrt(13)/39+2 sqrt(5)/5,

the one-sided derivatives G-2/3 and G+2/3, and their jump 4/3. The rational
square bounds supplied for 0<G<2/3 are valid. Each stationarity numerator
at this positive minimizer is 2t^6(1+5t^2+7t^4), strictly positive. Its
integral converges and cannot equal zero.

For D335, a separately ordered symbolic adjacency matrix first reproduced
the entire diagonal characteristic polynomial, and thereby the claimed
half-diagonal polynomial Q and derivative P_c. A fresh verifier then used
the serialized rational root intervals, a Fraction-based Sturm sequence,
and exact midpoint Taylor enclosures for P_c/Q'. It did not call the
proposer's verifier or SymPy's root-isolation/interval routines. The Sturm
sequence proves squarefreeness and ten real roots. The nine listed nonzero
intervals, together with the exact zero root, are disjoint and each contains
one root; every derivative denominator enclosure excludes zero. The sum
of signed nonzero-root derivatives satisfies, in exact arithmetic,

    407/1000<G335<408/1000.

The zero-root derivative is -2/5. Thus the derivative in direction (-1,-1)
is 2/5-G335, strictly between -8/1000 and -7/1000. This certifies descent
and verifies the limiting example in the frozen claim. The supplied
floating diagnostics were read as diagnostics, not treated as proof;
they were not needed for acceptance.

Reproducible fresh checks: run `python3 audit/referee_verify.py` from the
project root. The run completed successfully and wrote
`audit/referee-checks.json`. Its finite checks supplement the universal
arguments above; they do not prove an infinite statement by enumeration.
Input integrity is recorded in `audit/referee-integrity.json`.

**Source comparison, contribution, and limits.** The nearest primary source
is [Huang and Pereyra, arXiv:2604.27785v2](https://arxiv.org/html/2604.27785v2).
I checked its definitions, matching identity, kernel, fixed-t minimization,
Theorem 4.7 and Proposition 4.9 in the frozen text. Direct extraction of
the frozen PDF's pages 14 and 17 and the live HTML corroborated the
unqualified stationarity equations and the later acknowledgement of the
D331 cusp. The [live version record](https://arxiv.org/abs/2604.27785)
lists v2, dated 26 May 2026, as the latest version on this review date.

The source's fixed-t optimizer does not by itself determine the integrated
energy optimizer when r differs from s. The candidate adds uniqueness for
that integrated problem and a uniform length criterion. It also provides
the missing graph-specific absolute-value coefficient and a sufficient
strict local-minimum test, together with a rigorous global example showing
that the source's unqualified zero equations fail. The known half-diagonal
energy, the already noted cusp, and general spectral nonsmooth calculus
are not counted as new contributions. These distinctions match the frozen
claim.

Fresh bounded searches used the exact arXiv identifier with correction and
stationarity terms; combinations of complex unit gain, dumbbell, minimum,
energy, singular, and fixed-product; and arXiv-restricted correction queries.
The inspected relevant results led back to the source and its author's
publication listing, rather than an equivalent correction. The
[Lu--Wang--Xiao primary abstract](https://arxiv.org/abs/1511.07589) confirms
its stated low-rank classification target. That abstract alone cannot
exclude overlap in supporting lemmas; no novelty of zero simplicity alone
is being certified. The Lewis primary PDF was located, but a complete
theorem-by-theorem comparison was not performed and no theorem here depends
on it. The inaccessible nullity paper noted in the frozen literature screen
is not a premise. This review establishes no global priority guarantee.

The contribution is a modest, coherent mathematical correction with
structural consequences, rather than an isolated repetition of a known
energy value. Its credible use is to retain and test singular candidates
that smooth stationarity would wrongly discard, identify a unique candidate
on each positive product curve, and rule out interior singular minima for
an explicit infinite range of lengths. The D335 contrast confirms why a
cusp and tangential minimality alone are insufficient. The parts should
remain together in one result note.

No unresolved proof gap was found within the exact frozen scope. No claim
was revised during review. The normal-threshold equality case, singular
boundary sufficiency, and the full original all-odd classification remain
open tasks in this dossier, not conclusions supplied by this audit.

Final verdict: **accept**. Next workflow test: run the release contract's
`check-math` against the unchanged snapshot before manuscript drafting.
