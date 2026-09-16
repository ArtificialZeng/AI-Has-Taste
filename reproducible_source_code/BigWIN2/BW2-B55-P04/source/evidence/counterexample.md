# Exact four-job counterexample

Consider the labeled instance

\[
n=m=4,\qquad c=3,\qquad
T_1=\{1\},\quad T_2=\{1,2\},\quad
T_3=\{1,3,4\},\quad T_4=\{2,3,4\}.
\]

It is admissible: every job is nonempty, all four tools occur,
`max_j |T_j| = 3 <= c = 3 < 4 = m`, and the four job types are distinct.

## Reachability under either root orientation

The symmetric-difference scores of the unordered job pairs `(1,2)`, `(1,3)`,
`(1,4)`, `(2,3)`, `(2,4)`, `(3,4)` are respectively

\[
1,2,4,3,3,2.
\]

Thus `{1,4}` is the unique maximizing root pair. For either orientation, the
two remaining jobs have selection scores

\[
\min_{i\in\{1,4\}}|T_i\cup T_2|=2,
\qquad
\min_{i\in\{1,4\}}|T_i\cup T_3|=3.
\]

Consequently job 3 is selected uniquely, and every insertion position is a
child. If the root is `(1,4)`, the child
`sigma_+=(3,1,4)` is generated. If the root is `(4,1)`, the child
`sigma_-=(4,3,1)` is generated. Both are proper internal nodes because job 2
remains unsequenced.

## Forced KTNS fathoming

For `sigma_+`, KTNS has the unique magazine history

\[
(\{1,3,4\},\{1,3,4\},\{2,3,4\}).
\]

The first job fills the magazine, the second requires a subset, and the last
job forces replacement of tool 1 by tool 2. Hence `T_3 subset M_2` and `3>1`,
so the rule fathoms `sigma_+`.

For `sigma_-`, KTNS has the unique magazine history

\[
(\{2,3,4\},\{1,3,4\},\{1,3,4\}).
\]

The first two size-three tool sets force the first replacement, and the last
job requires a subset of the second configuration. Hence `T_3 subset M_3` and
`3>1`, so the rule fathoms `sigma_-`. There are no KTNS ties in either case.

Moreover, the remaining requirement `T_2={1,2}` is contained in neither
`{1,3,4}` nor `{2,3,4}`. Thus the Section 6.2 completion-pruning condition does
not hold at either node; the almost-exact rule is not preempted by that rule.

## Globally optimal completions

The global optimum is at least two. Indeed, jobs 3 and 4 force the distinct
full configurations `A={1,3,4}` and `B={2,3,4}`. If a full sequence used only
one switch, these would be its only two magazine configurations. But job 2
requires `{1,2}`, which is a subset of neither `A` nor `B`, a contradiction.

The completion `(2,3,1,4)` of `sigma_+` attains cost two: use `{1,2,3}` at job
2, replace tool 2 by tool 4 to obtain `A` for jobs 3 and 1, and replace tool 1
by tool 2 to obtain `B` for job 4. Similarly, `(2,4,3,1)` completes `sigma_-`
at cost two using the configurations `{1,2,3}`, `B`, `A`, `A`. Both are
therefore globally optimal.

Whichever orientation is retained by reversal symmetry, the unique root and
unique next-job choice generate a forced-tie fathomed node containing a
globally optimal completion. This directly disproves the universal claim in
`source.md`; the counterexample does not assert that every optimal branch is
lost.

The independent executable replay is `verify_counterexample.py`, with exact
output in `evidence/counterexample_verification.json`.
