# Independent mathematical referee report

**Verdict: accept the exact frozen candidate.** The argument proves the original
SC258 ordered associative-spectrum recurrence for every arity in its stated
range, including the initial values, and proves the additional equivalence
classification by pruned labeled trees. No mathematical revision is required.

Date: 2026-09-12. Referee job: `newwin-00001-p02-referee-667c860c9dea`.
Frozen kind: `resolution-paper`. Frozen original status: `proved`.
Snapshot digest: `8aca2d76efdb7c298a0274e627621944fae218d10fffef79f7925e9838d80b76`.

## Scope and integrity

The reviewed operation on A={0,1,2}, with the left operand indexing rows, is

    * | 0 1 2
    --+------
    0 | 0 0 0
    1 | 1 1 0
    2 | 1 0 1.

The terms use x_1,...,x_n exactly once in that order, with all full binary
bracketings allowed. Functions are compared on all of A^n, retaining the
identities of inessential coordinates. The accepted statement is

    a_1=a_2=1, a_3=2,
    a_n=3a_(n-1)-2a_(n-2)+a_(n-3) for every integer n>=4,
    sum_(n>=1) a_n z^n = z(1-z)^2/(1-3z+2z^2-z^3).

For two bracketings of the same ordered variables, equality of their functions
is also equivalent to equality of their pruned labeled trees, with pruning
exactly as specified in `claim.json`. This is the full original claim and the
additional frozen classification, not a restricted-arity substitute. No
variable permutations or other groupoid tables are included in this decision.

I read `source.md`, `problem.md`, `claim.json`, the snapshot, and its listed
mathematical and source evidence. I did not read checkpoint/state files, earlier
job transcripts, or an owner verdict. I recomputed all 13 file hashes and the
canonical hash of the snapshot's file mapping; all matched. The source hash is
`8d79f1e102ca5ec8f683c484ddfafbedb7fdfd8ac753b334df41c95bd8a857c0`.
The frozen inputs were not modified. `audit/referee-integrity.json` records the
initial checks; the independent verifier checked them again on completion.

## Reconstruction and attacks on the proof

**Pruning and coverage.** Every nonleaf term has values in {0,1}, directly from
the nine entries of the table. The restriction of the operation to {0,1} is
left projection. Thus at a node whose two original children u,v are composite,
the value of u*v equals the value of u on every ambient assignment. Structural
induction proves preservation by P. The same induction gives three structural
invariants: a composite tree retains at least two leaves, its first leaf
survives, and every internal node of its pruned tree has a leaf child. The
two-leaf case is the base of the first invariant; a deletion keeps the pruned
composite left child. Hence pruning never creates a lone leaf from a composite
child. This rules out hidden changes of root type. Coverage of all bracketings
follows from the induction; an assumption that every increasing comb is
attainable is neither needed nor made.

**Essential support.** For a two-leaf comb x_i*x_j, the two witnesses in the
submitted proof work: vary x_i between 0 and 1 at x_j=0; vary x_j between 0 and
2 at x_i=1. For a larger comb, the child g is composite and therefore Boolean.
The complete root sections are

    (x_i*g)|_(x_i=0,1,2) = (0, 1, 1-g),
    (g*x_j)|_(x_j=0,1,2) = (g, g, 0).

These sections preserve each essential coordinate of g, by selecting x_i=2
or x_j=0, respectively. The new left coordinate is essential because its first
two sections differ. For a new right coordinate, setting the child leaves to
1 makes g=1, so its 0 and 2 sections differ. Absent labels cannot affect the
function. This proves, without relying on finite tests, that the retained
labels are precisely the essential coordinates.

**Separation.** Equality of ambient functions first gives equality of their
leaf sets by essential support. For one or two increasing labels the ordered
tree is unique. For k>=3 labels, a comb has either a left leaf at the least
label i or a right leaf at the greatest label j. In the first case the section
x_i=1 is identically 1. In the second case that section is not constant: set
all leaves of its composite child to 1 and change x_j from 0 to 2. The distinct
labels make that variation legitimate, with x_i fixed at 1. Equal functions
must therefore have the same root type. The composite child is recovered by
1-f|_(x_i=2) in the left-leaf case, and by f|_(x_j=0) in the right-leaf case.
Induction on k determines the whole tree. The complements are applied only to
Boolean composite-child sections; the exceptional ternary-valued leaf case is
handled separately. Arbitrary gaps in the label set cause no problem. Combining
separation with preservation proves both directions of the frozen equivalence.

**Deleting a terminal interval.** Let S_n be the attained pruned forms and C_n
its subset retaining label n, for n>=2. If p in S_n has largest label m<n, a
raw root with right child x_n is impossible. A root with left child x_1 reduces
the claim to its right subtree on the shifted interval 2,...,n. The induction
on interval length gives n-m>=2 and a right-subtree realization on 2,...,m.
Adjoining x_1 realizes p on 1,...,m. If both raw children are composite, p
comes from the left interval 1,...,k, where k<=n-2. Either m=k or induction
on that left subtree realizes p on 1,...,m; also m<=n-2. These exhaust the root
types when n>=3; n=2 has no deleted terminal interval. Conversely, any member
of C_m is attained by a composite term on 1,...,m. Appending any composite
term on the next n-m>=2 labels makes a root that deletes that entire suffix.
Thus the submitted terminal-interval lemma includes both necessity and
sufficiency. In particular an ignored suffix of length one is impossible.

It follows as an equality of labeled sets that

    S_n = C_n disjoint-union union_(m=2)^(n-2) C_m,
    a_n = c_n + sum_(m=2)^(n-2) c_m,  where c_m=|C_m|.

The different largest labels guarantee disjointness. All sums are empty at
n=2,3 when appropriate. Comparisons of the same form across arities retain its
original labels and regard missing coordinates as ignored.

**Counting C_n.** A raw root realizing an element of C_n cannot have two
composite children, because it would delete x_n. For n>=3 its two possible
root types are disjoint. A left leaf x_1 leaves a shifted element of C_(n-1);
a right leaf x_n leaves an arbitrary member of S_(n-1). These constructions
are onto their respective root types, are injective as labeled trees, and
have composite children even after pruning. Every constructed form has a raw
realization. Hence c_2=1 and c_n=c_(n-1)+a_(n-1) for all n>=3. No counts of
raw realizations are confused with counts of distinct forms.

**Formal algebra and boundary cases.** With C(z)=sum_(n>=2)c_n z^n and
F(z)=sum_(n>=2)a_n z^n, the two set identities yield

    F=(1+z^2/(1-z))C,       C=z^2+zC+zF.

Eliminating F gives

    (1-3z+2z^2-z^3)C=z^2(1-z),
    F=z^2(1-z+z^2)/(1-3z+2z^2-z^3).

Adding the identity term z gives the asserted generating function. Its product
with the denominator is z-2z^2+z^3, so the coefficients of degrees 1,2,3 give
1,1,2 and every degree n>=4 gives precisely the claimed recurrence. There is
no use of a_0. As a direct check c_3=2, c_4=4 and a_4=5. All denominators
have constant term 1; the argument is in formal power series, with no analytic
limit, convergence, uniformity, or division-by-zero assumption.

## Independent exact checks actually performed

I wrote and ran `audit/referee_verify.py` using only the Python standard
library, with the exact table serialized in `audit/referee-input.json`.
It imports no proposer script. It enumerates raw Catalan trees, evaluates all
ternary assignments through integer bit planes using all nine table entries,
and compares complete function values. Raw-tree generation and function
equality do not use the proposed recurrence. A separate scalar table-lookup
evaluator checks every raw tree and every assignment through n=7.

The verifier's postorder normalization implements the same pruning map: the
composite-child invariant above ensures that normalizing children does not
change whether they are composite. Thus it is also an alternative implementation
of the root-based pruning procedure in the frozen evidence.

The successful output is `audit/referee-verification.json`. Its exact coverage:

- Every raw bracketing at each n=1,...,10, totaling 6,918 bracketings; at n=10
  alone, 4,862 bracketings and 59,049 assignments per bracketing.
- Pruning preserves every value; equal functions have exactly the same pruned
  tree; and essential support equals the retained labels, throughout that range.
- The independently obtained counts are 1,1,2,5,12,28,65,151,351,816. All ten
  sorted full-truth-table set digests match the frozen exact computation.
- The terminal-interval set decomposition and the numerical C_n root identity
  hold for every tested applicable arity. The recurrence passes n=4,...,10.
- All 1,644 ordered combs on nonempty subsets of eight labels were generated
  by filtering raw Catalan trees using the definition of a comb. Their full
  functions on 3^8 assignments have no collisions, and their essential supports
  equal their leaf sets. This includes unattainable forms and gaps in labels.

These checks are finite crosschecks, not the basis for the universal theorem.
The proposer's syntactic enumeration through n=14 was inspected but was not
independently rerun; the report does not claim truth-table coverage beyond n=10.
No proof-assistant formalization was performed. A fresh model review is a
separate review pass, not statistically independent evidence or journal peer
review.

## Source comparison, contribution, and limits

I independently extracted pages 1 and 17 of the frozen complete journal PDF
with `pdftotext`, checked them against its frozen text, and inspected the live
[author preprint, Definition 1.1 and Section 7](https://arxiv.org/html/2401.15786v1#S7).
The ordered-term definition, SC258 table, and nine reported counts agree with
this project. The 2024 article presents those values as computational evidence
without a general determination for these examples.
[Huang and Lehtonen, journal paper](https://ecajournal.haifa.ac.il/Volume2024/ECA2024_S2A29.pdf).

The precise advance over that inspected result is the all-arity classification
of term functions by pruned labeled combs and the resulting exact recurrence.
This solves the particular published question frozen in source.md and supplies
a decision procedure for equality of its ordered term functions. It is a
substantive resolution, rather than an extrapolation of the existing list.
No external theorem or OEIS recurrence is used as a premise of the proof.

A fresh bounded live search on 2026-09-12 included the following queries:

- `"SC258" "spectrum"`; `"Huang" "Lehtonen" "SC258"`;
  `"SC258" "associative" "proof"`.
- `"associative spectrum" "Padovan"`; `"associative spectra" "Padovan"`;
  `"Padovan" "groupoids"`.
- `"associative spectra" "three-element" 2025 2026`;
  `"associative-commutative spectra" Lehtonen 2025 2026` restricted to arXiv.
- `"SC258" "groupoids"` restricted to arXiv and the journal domain;
  `"Associative-commutative spectra for some varieties of groupoids" recurrence`;
  `"SC258" "normal form"`.

Relevant hits led back to the cited paper. Many SC258 searches returned
unrelated material and were excluded. The live
[arXiv version page](https://arxiv.org/abs/2401.15786) listed v1. I also inspected
the displayed recent entries in
[Lehtonen's publication list](https://n-ary.fi/publications.html) and
[Huang's faculty publication list](https://www.unk.edu/academics/math/faculty-staff/dr-jia-huang.php).
These provided no later equivalent-resolution lead. No later equivalent was
found in this bounded search; this does not establish exhaustive priority or
exclude unindexed or unpublished work. The candidate's own limited novelty
wording is appropriate.

The journal PDF prints DOI suffix ECA2024V4S3R29, while the frozen literature
record flags a different metadata suffix. Resolving that bibliographic issue
belongs to the citation phase; the directly inspected title, authors, journal,
article identifier, and URL already identify the mathematical source. It has
no effect on the theorem or this decision.

## Remaining gaps and disposition

No unresolved mathematical gap was found in the exact frozen statement or its
proof. No substantive claim change was made during review. Acceptance is based
on the reconstructed all-arity argument and the stated contribution comparison;
file hashes and successful finite computations do not replace that argument.

The next workflow test is the runner's `check-math` integrity/provenance gate
against this snapshot, followed by manuscript preparation for the accepted
scope. This referee job creates no manuscript, PDF, or publication release and
does not certify later citation, build, or visual checks.
