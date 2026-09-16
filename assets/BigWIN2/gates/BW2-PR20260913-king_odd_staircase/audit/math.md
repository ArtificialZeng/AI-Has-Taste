# Independent mathematical referee report

Verdict: **accept the exact frozen candidate**.

Job: `primary-20260913-king-odd-staircase-referee-e431e72b5aed`.
Snapshot digest:
`266a13483bd24c161c5fed5df8af6ee4236ba5ce2c93af7989adb224aa6e317d`.
Frozen kind: `resolution-paper`. Frozen original status: `proved`.

The argument establishes the original formula for every positive odd r
and every positive k, with precisely the three unit King moves and with
empty destinations excluded. No restriction of the frozen scope is needed.
Acceptance certifies the mathematical scope and the substantive contribution
relative to the inspected primary v1. It does not certify current openness,
global priority, journal acceptance, or publication readiness. The frozen
qualification concerning the later uncompared SSRN text remains in force.

## Inputs and independence

I read the frozen `source.md`, `problem.md`, `claim.json`, snapshot, and the
listed proof, verification material, source extraction, literature screen,
transfer derivation, and phase-holdout material. I inspected the actual
relevant statements in the frozen original HTML and the live primary page.
No checkpoint, state file, earlier job transcript, owner verdict, or
unlisted local research evidence was consulted. Proposer confidence language
in mandatory inputs was ignored. No agents or other model processes were
used. This is a fresh-context review, not a claim of statistical independence.

The 13 file hashes and the canonical snapshot digest were recomputed and
matched before the mathematical tests. They matched again afterward.
No frozen file was edited; in particular `source.md` retains SHA256
`e4dc12773dcaea452c4710f74f8cea0715f792af5af8f043d8d73d5b30913ae8`.

## Reconstruction of the decisive argument

**1. Finite game and square transfer.** A move from a partition deletes one
row, one column, or both and strictly reduces its size. A subpartition
D_k[i,j] is nonempty exactly when the corresponding Young-diagram cell
exists. Deletions compose, including the removal of trailing nonpositive
parts. Consequently its legal successors are exactly the three neighboring
cells that exist. Conjugation exchanges the row and column moves and leaves
the moveset invariant; induction on size proves invariance of G. The shape
D_k is self-conjugate.

Direct block deletion gives D_k[r,0]=D_k[0,r]=D_(k-1), and
D_k[r,r]=D_(k-2) when k>=3. These are shape identities, not extra legal
moves. Thus the first r-by-r square has south/east edges B_(k-1), and
corner B_(k-2)(0); for k=2 only the corner is absent. All interior cells
exist. Descending induction on i+j gives uniqueness from these edges.
This is a finite induction: the infinite explicit array used next is only
an algebraic solution of a local recurrence.

**2. Local array identity.** Let L>=0, x=L mod 2, y=1-x, and let
(a,b) be (3,2) or (2,3). Order the coordinates as m=min(i,j), n=max(i,j).
The candidate's three tables are

    n<L:       P = [[x,a],[b,y]],
    m<=L<=n:   C = [[b,y],[x,a]],
    L<m:       T = [[y,b],[a,x]],

indexed by the parities of m and n, with F(L,L)=2 overriding the tables.
I reconstructed these values and checked the local mex proof, including
the exhaustiveness of its case division.

For i<j in ordinary P, the four parity cases have successor triples
(b,a,y), (y,x,b), (x,y,a), (a,b,x), and current values x,a,b,y.
Each follows from {x,y}={0,1} and {a,b}={2,3}. On a P diagonal the
triples are (a,a,y) or (b,b,x), with mex x or y. T follows by the
stated interchange. In ordinary C the current cell and its three neighbors
contain all four values. C cannot meet the diagonal in an ordinary case:
its only diagonal point is the exceptional (L,L).

For i<j, all remaining possibilities are exactly j=L-1, (i,j)=(L-1,L),
or i=L<j. I checked all ten displayed seam rows for both high-value
assignments. The two exceptional diagonal triples are (0,0,2), with
current value 1, and (1,1,0), with current value 2. For L=0 or L=1,
the negative-coordinate cases simply do not occur. The division is exhaustive:
j<=L-2 is ordinary P; j=L with i<=L-2 and j>L with i<L are ordinary C;
j>L with i>L is ordinary T. The equal-coordinate cases were accounted
for separately. Therefore every nonnegative i,j,L satisfies the claimed
three-successor mex identity.

**3. Base k=1.** The rectangle formula is proved in the dossier rather than
assumed from a citation. A unit side gives the alternating path with terminal
value zero at (1,1). For u,v>=2, the six cases u>v with the four parity
choices, and u=v odd/even, give the displayed option sets. Their mex values
are respectively 0,2,3,1 and 0,2. Symmetry supplies u<v. Thus induction
on u+v proves the rectangle formula. For the r-by-(r-j) rectangle with r
odd, the boundary is 0 at even j and 3 at odd j. This is W_1. The
candidate correctly avoids asserting its F-interior formula at k=1.

**4. Ordinary induction phases.** Put p=r+2, t=1+((k-1) mod p),
h=floor((k-1)/p) mod 2, L=p-t, a=3-h and b=2+h. For 2<=t<=p,
the preceding phase has threshold L+1, the same h, and interchanged low
values. Since r is odd, F(r,s) gives y/a on even/odd s<=L and b/x
on even/odd s>L. This is exactly W_(k-1)(s).

For t>=3, L<r and F(r,r)=x. The preceding-previous parameter is t-2,
whose root is (t-1) mod 2=x. For t=2, L=r and the override gives
F(r,r)=2. If k>2, the actual preceding-previous phase is p and its
root is also 2. The correct edges plus the local identity and finite
uniqueness prove the step.

At k=2 the corner is absent. Only (r-1,r-1) sees it. The two remaining
options have value W_1(r-1)=0 because r-1 is even; both {0} and the
fictitious {0,2} have mex 1. This proves the step without assigning an
SG value to the empty partition, and also works when r=1.

**5. Wraparounds.** If t=1 and k>1, write k=ell*p+1 with ell>=1.
The previous phase is p with parity 1-h, and the previous-previous
phase is p-1, whose root is 1. Here L=r+1 and [0,r]^2 lies entirely
in P. The positive-index edge entries agree with W_(k-1), and the
corner is correctly 1. The only possible discrepancies are the two
edge endpoints (r,0),(0,r), whose actual value is 2 while F assigns a.

For h=1, a=2 and no discrepancy remains. For h=0, a=3 and b=2:
replace the two prescribed endpoint values by 2. A unit-step predecessor
inside the square can see (r,0) only from (r-1,0), and can see (0,r)
only from (0,r-1). If r>=3, the option triple at either affected
interior cell becomes a permutation of (2,2,1); its mex remains the
proposed value 0. If r=1, the two affected cells coincide, and the
triple is still (2,2,1). Hence no interior value needs to change. This
checks both alternating phase transitions without assuming an incorrect
period p for the full boundary word.

**6. Original conclusion.** The preceding arguments prove W_k for every k
by induction, together with the supporting F-interior formula for k>=2.
At j=0, t=p gives the overridden value 2; otherwise the value is
(t+1) mod 2. Since t agrees with k mod p except that the zero residue
is represented by p, these are exactly the three original cases. There
is no unproved uniformity claim, limiting step, or reliance on finite
experimental coverage in this conclusion.

## Independent checks actually performed

`audit/referee-verify.py` is a new verifier. It imports neither proposer
script, invokes neither of their main routines, and does not overwrite
frozen computation output. Its results are in `audit/referee-verify.json`.

- All 14 unbounded-integer counterexample queries returned `unsat` with
  Z3. They cover the local mex identity, ordinary edges/corners, phase-two
  corner, absent corner, both wrap edge cases, wrap corner and modified
  boundary recurrence, base boundary, extraction of W from F, original
  root formula, and rectangle recurrence/base path. Every serialized query
  and its hash are retained under `audit/referee-smt/`.
- Direct rolling-row evaluation used the actual three permitted neighboring
  cells on each full Young diagram, with no block transfer. It checked 136
  boards, evaluating 27,464,908 cells and comparing all 26,800 entries in
  their first squares. No discrepancy occurred.
- Coverage was every k from 1 through 3(r+2)+2 for r in {1,3,5,7,9},
  plus k in {1,2,p-1,p,p+1,2p,2p+1}, p=r+2, for r in {15,37,39}.
  The latter choices include fresh block sizes and both wrap boundaries.
- A separate memoized partition-tuple evaluator explicitly constructed each
  of the three legal deletions and independently checked 245 subpartitions:
  all first-square entries for r in {1,3,5}, k=1,...,7.

The mex predicate in the SMT encoding asserts that the candidate value is
absent and every smaller nonnegative integer is present. The integer and
parity domains match those in the proof. These solver checks concern only
the explicit encoded identities; the partition interpretation, deletion
identities, and induction above remain a human-readable mathematical audit.
No proof-assistant certification of the complete theorem is claimed.

The older triage holdout script imports `boundary-test.py`, which is not
listed in this snapshot. I did not read or execute that dependency and do
not certify that historical computation as reproducible from this snapshot.
This does not affect the accepted proof: it has no computational premise,
the later proposer verifier is self-contained, and the fresh verifier above
independently evaluates the actual game. If that old holdout is advertised
as a reproducible ancillary experiment, its dependency must first be supplied
through the proper evidence-freezing workflow.

## Source comparison, contribution, and remaining limits

The actual primary Conjecture 5.1 and Definitions 2.1/3.1 match the frozen
statement. The relevant known results in the inspected v1 are the rectangle
formula (Theorem 3.8), ordinary staircases r=1 (Lemma 3.13), and equal
even blocks (Lemma 3.14). None provides the missing uniform odd-block
classification. The current proof supplies exactly that classification;
its two-phase boundary and three-region interior invariant constitute a
substantive uniform argument, not a finite check or a changed game. It also
provides explicit SG evaluation without constructing the whole staircase.
The supporting classification is part of this one coherent resolution,
not a separate publication target.

`audit/referee-sources.md` records the separate citation-check-skill pass and
the bounded live primary search. Current arXiv history shows only v1. A
search-indexed SSRN record reports a later 31-page version; its full text
could not be accessed and has not been compared. No equivalent proof was
found in the material actually inspected, but neither current openness nor
priority follows. The frozen candidate already states these limitations,
so accepting its exact mathematical scope does not remove them.

No unresolved mathematical gap was found. No substantive revision to the
frozen proof or statement is requested. The next literature check is to
obtain and compare SSRN 5649443 before asserting novelty or a first proof.
Writing, full bibliography review, clean compilation, and visual inspection
remain subsequent-role tasks. No manuscript or release audit was created.

**Final verdict: accept**, at the unchanged frozen kind and original status.
