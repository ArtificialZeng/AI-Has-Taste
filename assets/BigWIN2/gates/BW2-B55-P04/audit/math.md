# Fresh mathematical referee report

## Frozen scope and evidence integrity

I reviewed the claim frozen by snapshot
`da7676dfd73599ffdc0d5820eb713ac8b5f4d7209378668b5b2cc01287850fe5`.
I recomputed the canonical snapshot digest and checked the SHA-256 digest of
every listed file; all values agree with `audit/snapshot.json`. The candidate is
a `resolution-paper` claiming to disprove the universal assertion in
`source.md`, so a single admissible four-job instance with a reachable unsafe
node suffices. No weakening of the original quantifiers is needed.

The primary source was checked directly. Section 4.2 selects a root pair by
maximizing symmetric difference, selects the next job by maximizing the
minimum union cardinality, and generates every insertion position. Section
6.2 gives the completion-pruning test. Section 6.3 fathoms a node when, for an
optimal KTNS magazine history, some consecutive pair satisfies
`T_{sigma_i} subseteq M_{i+1}` and `sigma_i > sigma_{i+1}`. The paper's own
example has five jobs and explicitly shows only that an optimal completion can
be removed; it states no four-job lower bound. Thus the submitted
counterexample addresses the exact proposed minimality claim.

## Reconstruction of the counterexample

Take

\[
n=m=4,\quad c=3,\qquad
T_1=\{1\},\quad T_2=\{1,2\},\quad
T_3=\{1,3,4\},\quad T_4=\{2,3,4\}.
\]

This is admissible: all job requirements are nonempty, their union is all four
tools, and the largest requirement has size three, equal to `c` and strictly
less than `m`.

For unordered pairs `(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)`, direct symmetric-
difference calculation gives respectively `1,2,4,3,3,2`. Hence `{1,4}` is the
unique root pair. Relative to this root, job 2 has selection score

\[
\min(|T_1\cup T_2|,|T_4\cup T_2|)=\min(2,4)=2,
\]

whereas job 3 has score `min(3,4)=3`; therefore job 3 is selected uniquely.
Every insertion position is a child. If the retained root orientation is
`(1,4)`, the front insertion gives `(3,1,4)`. If it is `(4,1)`, the middle
insertion gives `(4,3,1)`. Thus the source's unspecified root orientation and
reversal convention do not remove the construction.

Let `A={1,3,4}` and `B={2,3,4}`. For `(3,1,4)`, the KTNS history is necessarily
`(A,A,B)`: jobs 3 and 4 fill the capacity and job 1 is already covered between
them. At the first adjacent pair, `T_3=A` is contained in the next
configuration `A`, and `3>1`; Section 6.3 therefore fathoms this node. For
`(4,3,1)`, the corresponding forced history is `(B,A,A)`. At the second
adjacent pair, `T_3=A` is contained in the next configuration `A`, and again
`3>1`. The triggering histories are forced, so no KTNS filler or eviction tie
is being selected silently.

The only unsequenced job is job 2, whose requirement `{1,2}` is contained in
neither `A` nor `B`. Consequently the Section 6.2 completion-pruning condition
does not preempt either event.

## Optimality and unsafety

Jobs 3 and 4 force the two distinct full configurations `A` and `B`. If a
complete order had total switch cost at most one, these would be the only two
full magazine configurations it could visit: the transition between them
already inserts one tool. But neither configuration covers job 2. Hence every
complete sequence costs at least two.

For the node `(3,1,4)`, deleting job 2 from `(2,3,1,4)` recovers the node. The
configuration sequence

\[
\{1,2,3\}, A,A,B
\]

has cost two, so this completion is globally optimal. Likewise,
`(2,4,3,1)` completes `(4,3,1)` and is covered by

\[
\{1,2,3\},B,A,A,
\]

also at cost two. Each orientation therefore contains a node that the
almost-exact rule fathoms despite a globally optimal completion. This is
exactly the definition of an unsafe node in the frozen statement.

## Independent checks performed

I reran the supplied verifier in a fresh temporary directory; its regenerated
JSON has SHA-256
`d11e212339b64102e0443788ee8f432974cfbe058d87f492fade6a8af6053e50`,
identical to the frozen certificate. Separately, I implemented a small dynamic
program over the four size-three magazine states for all 24 permutations,
without importing the submitted verifier. It independently returned global
optimum two, the pair scores above, unique root `{1,4}`, next-job scores
`2` and `3`, both subsequence completions, both trigger conditions, and failure
of Section 6.2 coverage. The elementary lower-bound argument above also
establishes optimality without relying on either program.

## Contribution assessment and verdict

The counterexample is not a toy restriction or a subsidiary result: it lies
inside the full frozen domain and directly falsifies its universal conclusion.
Its orientation robustness, unique selection decisions, forced KTNS histories,
and explicit globally optimal completions remove the material convention and
tie ambiguities identified in `problem.md`. It also corrects the proposed
inference that the source's five-job example is minimal. I found no unresolved
mathematical gap in the frozen candidate scope.

**Verdict: accept.**
