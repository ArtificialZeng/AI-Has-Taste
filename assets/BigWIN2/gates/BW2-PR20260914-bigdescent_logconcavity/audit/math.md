# Independent mathematical referee report

Verdict: **accept the exact frozen result-note scope**.

Referee job: `primary-20260914-bigdescent-logconcavity-referee-942f0f5bf98c`.
Snapshot digest: `eb53a91aae391332997c181abb1a6520595e81df64ebfc2f9344d940702e1155`.
Review date: 2026-09-14 Asia/Shanghai (2026-09-13 UTC).
Frozen workflow fields: `kind=result-note`, `original_status=unresolved`.

The submitted theorem, its coefficientwise log-concavity consequence, the sharp
factor-two example, and the stated extension across adjacent fixed-event cuts
all pass. No substantive correction or reduced scope is needed. This acceptance
does not settle the original conjecture or unrestricted exceptional-class
log-concavity, and is not a judgment of journal acceptance or definitive priority.

## Inputs, independence, and integrity

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and the
listed proof, code, certificates, and literature comparison. For the saved
primary article I inspected the relevant passages of both the text and HTML,
and compared them with the live journal source. I did not use the owner's
workflow assertions or earlier research summaries as verification of the claim.
No checkpoint, scheduling state, previous referee report, job transcript, or
unlisted project evidence was consulted. No agents or other research workers
were launched.

All twelve frozen file hashes and the canonical mapping digest match, both
before and after the verification. In particular, the unchanged `source.md`
has SHA-256
`03ad82cdbcbee83701695f50050dcb184d5b934b99b6e53aeb2818a8da1c517f`.
No frozen file was edited. New referee artifacts are confined to `audit/`.

I wrote `audit/referee_verify.py`, which imports no proposer code and never
executes the proposer scripts. Its output is
`audit/referee-verification.json`. The new verifier derives the transfer
matrices from suffix transitions, reconstructs every certificate coefficient
by quadratic finite differences, and separately enumerates binary words.
This is an independent review pass and independent implementation, not a claim
of statistical independence or external peer review.

## Exact scope

An event is the ending position of a consecutive factor 10 or 011 in a binary
word of length n ending in 1. The count a_n(A) fixes the entire event set
exactly; it does not count words merely containing the events in A.

For n >= 1, disjoint S,J contained in {2,...,n}, and m=|J| <= 4, the submitted
pair polynomial is

    H_(S,J)(x,y) = sum_(T subset J) a_n(S union T)
                    a_n(S union (J minus T)) x^|T| y^(m-|T|).

Its coefficients h_j satisfy h_j=h_(m-j), and its two-variable Schur expansion
is

    H = sum_(j=0)^floor(m/2) (h_j-h_(j-1)) s_(m-j,j),  h_(-1)=0.

Thus the precise assertion to verify is h_j-h_(j-1) >= 0 throughout that
range. The count is uniform in n, spacing, and |S|, and includes impossible
event sets. Free coordinates are event positions in the binary word. They
are not asserted to be the positions of big descents in a permutation.

## Reconstruction of the proof

### Event transfer and boundary cones

Use states A=ending 0, B=ending 01, and C=ending 1 but not 01. From A,
appending 0 gives A and appending 1 gives B, both without events. From B,
appending 0 gives A with event 10, and appending 1 gives C with event 011.
From C, appending 0 gives A with event 10, while appending 1 gives C without
an event. With columns representing old states this gives exactly

    P = ((1,0,0),(1,0,0),(0,0,1)),
    Q = ((0,1,1),(0,0,0),(0,1,0)).

The initial vector v=(1,0,1)^T accounts for the two possible first letters;
u=(0,1,1) accepts endings in 1. Consequently
a_n(A)=u U_n ... U_2 v, where U_i=Q or P according to exact membership in A.
This also handles n=1: the empty matrix product gives u v=1.

The submitted output cone is a,b,c >= 0 with c <= a+b, and the input cone
is a,b,c >= 0 with b,c <= a. The four rays for each cone generate exactly
these sets: the splitting formulas in the proof have feasible nonnegative
coefficients under precisely these inequalities. Directly,

    (a,b,c)P=(a+b,0,c),       (a,b,c)Q=(0,a+c,a),
    P(a,b,c)^T=(a,a,c)^T,    Q(a,b,c)^T=(b+c,0,b)^T.

These maps preserve the respective cones. Both exterior word products
therefore give allowable boundary vectors. Splitting the transfer at free
sites reverses their natural order, but preserves subset sizes and complements.

### Exhaustion of arbitrary gap words

P^2=P allows every consecutive nonempty string of P's in a gap to be
replaced by one P. The identity Q^2=e0 e1^T holds with e0 in the input cone
and e1^T in the output cone. Hence a gap A Q^2 B factors exactly as

    (A e0)(e1^T B).

Both new boundary factors remain in the required cones, including when either
vanishes. If no QQ remains, the gap alternates P and Q. The four identities

    PQPQP = PQP+P,       QPQPQ = QPQ+Q,
    (PQ)^3 = (PQ)^2+PQ, (QP)^3 = (QP)^2+QP

give Fibonacci recurrences, with the first two words in each parity/endpoint
class as initial data. Every such gap belongs to one of the separate families

    cone(Id), cone(P,PQP), cone(Q,QPQ),
    cone(PQ,(PQ)^2), cone(QP,(QP)^2).

These recurrences cover all lengths, not just the finite contexts checked
by the verifier. The proof retains the five families separately; it makes
no unsupported assertion about their common positive hull.

### Complete finite polynomial verification

For a choice of gap families, expand the two boundaries in their four rays
and each gap in its one or two generators. Each scalar A_T is multilinear
in these independent parameter groups. Each Schur coefficient is therefore
homogeneous of degree two in every group. Checking every parameter coefficient
is sufficient for all nonnegative real parameters.

The independent verifier evaluates a quadratic group at e_a and e_a+e_b.
Its diagonal coefficient is its value at e_a; for a<b its mixed coefficient
is its value at e_a+e_b minus the two diagonal values. Applying this operation
along each parameter group recovers the entire multihomogeneous coefficient
table exactly. This differs from both the proposer's convolution of multilinear
tables and its tensor-product check. Python integer arithmetic is used
throughout, including NumPy arrays of object dtype; there is no numerical
tolerance or floating-point sign decision.

The domain is generated independently, rather than trusting the stored list
of cases. Each boundary contributes 10 quadratic monomials. Summed over the
five possible families, each gap contributes 1+4*3=13. The complete number
of positions, including zeros and the first Schur row, is thus
(floor(m/2)+1)*100*13^(m-1). The results are:

| m | family choices | coefficient positions | positive | negative |
|---|---:|---:|---:|---:|
| 2 | 5 | 2,600 | 1,597 | 0 |
| 3 | 25 | 33,800 | 15,633 | 0 |
| 4 | 125 | 659,100 | 240,445 | 0 |

All 695,500 coefficients, including every zero, agree exactly with the frozen
serialized certificate. This is a finite algebraic proof step valid for the
continuous parameter domain, not a finite sample of gap lengths.

### Rank-one induction and the larger-block statement

At a rank-one internal gap, A_T is the product of a left scalar depending
only on the free sites to its left and a right scalar depending only on those
to its right. Summing antipodal products therefore factors H exactly into
the two corresponding pair polynomials. No normalization constant or division
appears. Both subproblems have fewer free sites and valid boundary cones.
For m=0 the pair polynomial is (l r)^2; for m=1 it is
(l P r)(l Q r)(x+y). These supply the induction bases.

The product rule

    s_(a,b) s_(c,d) = sum_(i=0)^min(a-b,c-d) s_(a+c-i,b+d+i)

follows by multiplying their finite geometric sums and shows that this
factorization preserves two-variable Schur positivity. Together with the
five-family certificate, induction proves every stated case m<=4.

For the final clause of claim.json, two adjacent fixed-event positions
between consecutive free-site blocks give precisely such a Q^2 factor
inside the intervening gap. Cutting at all these factors produces components
with at most four free sites. The same product rule proves the exact stated
extension for arbitrarily many blocks. The proof requires no bound on total
degree or the number of common events.

### Coefficientwise log-concavity and sharpness

For a monomial of total degree 2k in g_k^2-g_(k-1)g_(k+1), let D be its
exponent-two coordinates and E its exponent-one coordinates. Then
|E|=2r with r=k-|D|. Its coefficient is exactly

    h_r(S union D,E) - h_(r-1)(S union D,E).

Indeed the two factors must both contain D and partition E, with respective
subset sizes (r,r) or (r-1,r+1). Coordinates outside D union E remain absent.
Here |E|<=4 and S union D is disjoint from E, so this is covered by the
proved theorem. For r=0 the coefficient is a square; indices outside the
polynomial range are zero. Monomials with other exponent patterns do not
occur. This proves the coefficientwise corollary, and evaluation at any
nonnegative weights preserves its inequalities. Impossible conditionings,
zero weights, and zero rows introduce no exceptional division.

Directly at n=4, S empty, J={2,4}, the exact word lists are
{0001,1111}, {1001}, {0011}, and {1011}; their counts are (2,1,1,1).
The m=2 inequality is AD<=2BC, and equality here proves optimality of 2.
The generic three-coordinate auxiliary weight with values 2 at the empty
and full sets and 1 elsewhere has AD=2BC on all six faces, but antipodal
coefficients (4,3,3,4). Its Schur difference is -1. I independently verified
this witness, including all six faces. It shows why the higher-order assertion
does not follow just from those face inequalities for general Boolean weights;
it is not a counterexample within the binary-word model.

## Additional finite checks actually performed

The direct-word implementation enumerates every length-n word ending in 1
for 1<=n<=12 and checks the transfer count for every event set, including
zero counts. It then checks all choices of at most four free sites and all
outside assignments: 198,399 configurations and 433,405 Schur coefficient
positions. It separately expands every g_k^2-g_(k-1)g_(k+1) through n=10,
checking 383,073 monomial positions. No negative coefficient occurs. These
finite checks confirm interpretation and the corollary; they are not the
reason the theorem holds for arbitrary n.

The structural checks also verify the cone images of all generating rays,
all displayed matrix identities, and the rank-one factorization on 3,969
pairs of contexts of lengths at most five. The written identities and cone
argument, rather than those finite context checks, justify arbitrary contexts.

Reproduction command from the project directory:

    python3 audit/referee_verify.py

The command completed successfully. It writes only its referee output and
rechecks the frozen hashes at completion. The initial unavailable `python`
alias was replaced with `python3`; this had no mathematical consequence.

## Source comparison and contribution assessment

The nearest enumerative source is Elizalde, Rivera, and Zhuang,
[Counting Pattern-Avoiding Permutations by Big Descents](https://link.springer.com/article/10.1007/s00026-026-00805-1).
I checked Theorems 3.5/3.8, Lemmas 3.6/3.9 and their surrounding discussion,
Conjecture 4.6, and Section 4.3. The source supplies the binary-word
interpretation and univariate enumeration; its quasisymmetric functions
in Section 4.3 encode permutation big-descent sets and are different from
the submitted two-variable antipodal polynomial. The frozen original
matches Conjecture 4.6, whose full 21-family assertion is not proved here.

I independently read the definitions and Theorem 1 on pages 1-2 of
Kahn and Neiman's
[A strong log-concavity property for measures on Boolean algebras](https://arxiv.org/pdf/0907.0243).
Their antipodal sums are divided by binomial coefficients. On two free
coordinates their APP requires AD<=BC. The actual-word counts (2,1,1,1)
violate that hypothesis, so their conditional APP theorem does not directly
prove this result. Their external-field/projection notions also must not be
identified with the fixed-indicator property used here.

The precise delta is a uniform theorem about conditioned multivariate event
counts, with a proved reduction from arbitrary matrix-word contexts to a
finite certificate. This is not supplied by the source's univariate generating
function. Its natural scope is a low-order conditional positivity property:
it excludes every potential negative monomial coefficient with at most four
singly occupied event positions, independently of n and the fixed event
count, and provides reusable Schur-positive factors across fixed-event cuts.
Those are concrete uses in the stronger coefficientwise problem. The rank-one
extension and sharp bound make this a coherent, nontrivial result-note; I do
not regard the four-position cutoff as merely a finite word-length experiment
or an arbitrary toy subfamily. No optimality of that cutoff is inferred.

Independent live searches included the exact source title with log-concavity,
`big descents log-concavity proof`, binary words with 10/011 and log-concavity
or Schur positivity, coefficientwise 10/011, conditional antipodal pairs,
and finite-state antipodal terminology. No inspected primary source stated
an equivalent theorem. Several broad queries returned only unrelated material.
This is a bounded novelty screen as of the stated date, not an exhaustive
survey or proof of priority. The two primary sources above are the decisive
comparisons; no unsupported assertion about all current literature is needed.

## Remaining limits and handoff

No mathematical gap remains in the exact frozen scope. All selected-site
counts, including degenerate cases, are covered by the reduction and checked
certificate. The original conjecture and unrestricted weighted or unweighted
exceptional-class problem remain unresolved by this work.

The contribution passes as one result-note, retaining its related corollaries
and sharp example together. A manuscript must preserve the distinction between
binary event coordinates and permutation big-descent positions, retain the
precise conditional and rank-one hypotheses, provide the computational proof
and reproducible certificate, and use bounded novelty language. No manuscript
or publication artifact was created in this referee job. The runner's
`check-math` integrity/provenance gate is the next workflow check before writing;
it is not a substitute for this mathematical assessment.
