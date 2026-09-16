# Fresh mathematical referee report

## Verdict

**Accept** the frozen `result-note` claim at exactly order seven.  The original
all-order assertion remains unresolved.  The acceptance is bound to snapshot
`5a3f365ec462b4f4bb72cd2a3a590413faf9c27b29030fa6dd8fddf807e383bf`.

## Snapshot and scope checks

I recomputed every SHA-256 digest in `audit/snapshot.json`; all ten frozen-file
digests agree, and a canonical sorted compact JSON serialization of its `files`
mapping reproduces the declared snapshot digest.  In particular, `source.md`
still has SHA-256
`b71158a55cdb4fa03de594447a51ba4e88261de47df066fe822dc14354abf8b6`.

The claim is strictly the following finite statement.  Among loopless labeled
digraphs on seven vertices, permitting antiparallel arcs and forbidding a
not-necessarily-induced copy of the cyclic regular tournament on five vertices,
the maximum of \(\sum_v d^+(v)^2\) is 186; the 105 labeled maximizers are
exactly the complete bidirected four-partite graphs with part sizes
\(2,2,2,1\).  This neither proves nor disproves the source assertion for every
\(m\), and `claim.json` says so explicitly.

## Reconstruction of the decisive argument

There are 42 independently selectable ordered arcs.  In the primary program,
the six off-diagonal entries of each adjacency row form one six-bit block, so
the seven blocks bijectively encode all \(2^{42}\) labeled digraphs.  A row of
popcount \(d\) contributes exactly \(d^2\).  A partial seven-row word of current
score \(s\) is discarded only when
\[
s+36(7-\text{number of completed rows})<186.
\]
Consequently every digraph of score at least 186 reaches a leaf.

For each five-element support, all 120 vertex orderings of the representative
with arcs \(i\to i+1,i+2\pmod 5\) are generated and deduplicated.  Its
automorphism group has order five, leaving 24 distinct arc sets per support and
\(\binom75\cdot24=504\) in total.  The containment predicate asks whether all
ten arcs of one such set occur.  It imposes no condition on reverse or other
extra arcs, so it is exactly the required non-induced containment relation.

The integer row-score generating function gives 439,992 words of score 186 and
6,937,603 of larger score.  The score-pruned traversal visits their sum,
7,377,595, with the same score-by-score histogram.  Every strict candidate
contains `Reg5`; at score 186 exactly 105 candidates do not.  Thus this is a
complete upper-bound computation, not sampling or floating-point evidence.

The lower bound is direct.  In \(T_4(7)\), the singleton-part vertex has
out-degree six and the other six vertices have out-degree five, giving
\(6^2+6\cdot5^2=186\).  Five selected vertices include two in one of four
parts, and that pair has no arc, so no tournament copy occurs.

For classification, every reported equality mask was checked to have, for each
unordered pair, either both arcs or neither.  Its graph of empty pairs consists
of three disjoint edges and one isolated vertex.  Those four components are
precisely independent parts of sizes \(2,2,2,1\), with both arcs between every
two parts.  Conversely the number of labeled such partitions is
\[
\frac{7!}{(2!)^3 3!}=105,
\]
equal to the complete equality census.

## Independent checks actually performed

I reran both frozen computations from the project root.  The primary run again
reported maximum 186 and 105 maximizers; the degree-vector replay again checked
all 6,937,603 strict candidates and found a `Reg5` in each, then validated all
105 equality masks as \(T_4(7)\).  These programs are materially differently
organized: the first branches over row masks above a score threshold, while the
second first enumerates the 2,647 strict degree vectors and then the Cartesian
products of rows having those degrees.

I also made a fresh exact CP-SAT reconstruction without using either dense-mask
enumerator.  It used 42 Boolean variables indexed directly by ordered pairs,
seven integer degree variables, exact allowed pairs
\((d,d^2)\) for \(0\le d\le6\), and one inequality saying that at most nine of
the ten required arcs occur for each of the 504 labeled `Reg5` arc sets.  A
single-worker deterministic solve returned `OPTIMAL` with objective 186
(56,733 branches and 14,288 conflicts).  After constraining the objective to
186, exhaustive solution enumeration returned `OPTIMAL` with exactly 105
distinct labeled solutions; an independent unordered-pair test classified every
one as \(T_4(7)\).  This also independently covers the equality level, which the
frozen degree-vector replay reads from the primary output.

I checked the possible edge cases: the domain has no loops; opposite arcs are
separate variables; containment is non-induced; all five-vertex supports and
all embeddings are covered; no division, limiting argument, or probabilistic
step occurs; and the equality count is labeled rather than isomorphism-class
count.

## Source comparison and contribution

The frozen PDF uses the same loopless, digon-permitting conventions and states
the all-order formula as Conjecture 3.3.  Its conclusion says that a formal exact
result for `Reg5` remains future work.  It mentions computations for unspecified
small orders but states no order-seven theorem, certified range, or equality
classification.  Relative to that source, the precise delta here is a complete,
replayable exact theorem and labeled extremal census at \(m=7\).  This is a
nontrivial next finite case and a useful exact benchmark for attacks on the
all-order conjecture, rather than an arbitrary restriction.  The snapshot does
not establish a global priority claim, and acceptance should not be represented
as one; the literature conclusion is only that no equivalent result appears in
the frozen cited source.  The descriptive phrase “first order left unchecked by
the preceding small-order work” is consistent with the candidate's stated
research sequence but is not needed for, and is not stronger than, the audited
order-seven theorem.

## Remaining limitations

The computation supplies no structural upper bound for \(m\ge8\), and the
original conjecture remains open.  Standard solver correctness and the Python/
Numba runtime remain part of the trusted computational base, mitigated here by
three exact formulations and direct inspection of their encodings.  These are
limitations of scope and implementation trust, not gaps in the frozen finite
claim.
