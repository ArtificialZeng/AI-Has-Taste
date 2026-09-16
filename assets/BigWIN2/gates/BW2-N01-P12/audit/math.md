# Mathematical referee report

Verdict: **accept** the exact frozen candidate.

Job: `newwin-00001-p12-referee-74e7464d934f`.
Snapshot digest: `15b54925124717536fdc8f74eeebc27eb327317456a6eb9d5e9178f67899308d`.
Frozen kind: `resolution-paper`. Frozen original status: `proved`.
Review date: 2026-09-12.

The argument proves the original restricted count for all 55 admissible
shapes and every prime power. Acceptance is for this exact statement; the
general-k conjecture is outside its scope. No substantive revision of the
claim or its frozen evidence was made in this review.

## Scope and inputs

The statement in claim.json agrees with the mathematical assertion in
source.md, including the inequalities on both partitions, ordered arrays,
arbitrary values at unrestricted entries, and the factor q^9(q-1)^6.
Nondegeneracy is the rank condition at every point of the projective line
over the algebraic closure, not just its rational points.

I read the frozen source, interpretation, claim, snapshot, decisive proof,
certificate data, coefficient table, the two verification programs, and
the listed primary-source evidence and literature comparison. No owner
checkpoint, workflow state, earlier referee verdict, job transcript, or
unlisted project evidence was used. Proposer assertions of completeness
were not evidence for the decision.

The 15 input file hashes and the canonical hash of their mapping were
recomputed. Every hash matches the snapshot. In particular source.md has
SHA-256 `f13440b8f2b246d10391b74172f52aeb59243c453e4684992a1c29cac3f8cacd`.
All frozen files remained unchanged through verification.

## Decisive argument reconstructed

Let E0 have columns e1,e2,e3 and E1 have columns e2,e3,e4. For sigma in
S4 and pi in S3, write L=P_sigma U and R=P_pi V, where U is unit upper
triangular with x_ab at inversions of sigma, and V is unit lower triangular
with y_ij at position (j,i) for inversions of pi. These produce precisely
the two matrices L E0 R and L E1 R used in the frozen certificate.

The applicable prior orbit reduction is Corollary 4.2 of the journal
paper, equivalently arXiv Corollary 4.19. Its augmented matrices have the
same conventions, and it applies over every finite field. The
algebraic-closure criterion is explicit in arXiv Lemma 2.5. The journal
PDF text extraction drops the overbar; that extraction was not used to
weaken the criterion. [Koprowski--Lewis, arXiv v1](https://arxiv.org/html/2602.22129v1)
and [journal paper](https://ecajournal.haifa.ac.il/Volume2027/ECA2027_S2A3.pdf).

Here is the normalization check. The two triangular groups have orders
q^6(q-1)^4 and q^3(q-1)^3. Each tensor has exactly q-1 acting pairs,
by the stated free transitive quotient action. Their ratio is
q^9(q-1)^6. Left multiplication by an upper triangular matrix preserves
the forbidden bottom portions of columns. Right multiplication by an
upper triangular matrix preserves them because permitted column heights
are nondecreasing. The inverse operations have the same properties, so
preservation is an equivalence. In the action notation the second
matrix is R-transpose, which puts that last triangular factor on the
correct side. Normalized augmented matrices parameterize assignments
injectively: equality of tensors gives a scalar relation between the
acting matrices, and their unit pivots force that scalar to be one.

For a fixed pair of permutations put n=inv(sigma)+inv(pi). There are six
constant entries, at rows sigma(pi(c)) on the front and sigma(pi(c)+1)
on the back. Direct multiplication shows that each is exactly 1.
Consequently a forbidden pivot makes the entire cell empty in every
characteristic. If no pivot is forbidden, setting every variable to zero
satisfies the constraints.

For the remaining cells let h be the number of forbidden entries that
are nonzero polynomials. For a forbidden front entry (r,c), set
a=sigma^{-1}(r), v=pi(c). The nonzero, nonpivot case has a<v and
r>sigma(v). Thus x_av exists. If b=pi^{-1}(a), the partition inequality
forces b>c: b<c would place an allowed earlier-column pivot in the same
forbidden row. The equation therefore has the form

    y_cb + x_av + sum_(a<t<v) x_at y_(c,pi^{-1}(t)) = 0,

with only existing variables included. Its target is y_cb. For a forbidden
back entry the target is x_(a,v+1); it has coefficient one, and every
other variable has column key at most v. Cases a>v on the front or
a>v+1 on the back give identically zero entries and impose no equation.

Order x_ab by (b,0,0,a), and y_ij by (pi(i),1,-pi(j),0).
Every other variable in either equation strictly precedes its target.
Front targets determine their row and column uniquely; back targets do
likewise; the two sets of targets are disjoint. Hence there are exactly
h different targets. Assigning the other n-h variables freely and solving
in this order gives every solution uniquely. This proves the count
q^(n-h) over every finite field. It also proves that projection to the
free variables is inverse to an integral polynomial parametrization.
There is no division, interpolation, limiting argument, or generic-
characteristic exception in this step.

The remaining task is a finite identity in Z[q]. An independent
enumeration of the containing six-dimensional integer box, filtered by
the exact inequalities, gives 55 shapes. Each uses all 144 permutation
pairs, with no symmetry quotient. For each shape the histogram of n-h
among nonempty cells equals the coefficients of the product of six
q-integers with lengths

    4-lambda_1, 3-lambda_2, 2-lambda_3,
    3-mu_1,     2-mu_2,     1-mu_3.

All lengths are positive, including the maximal shape. These identities,
combined with the orbit normalization and the cell bijections, prove
the frozen formula simultaneously for every prime power.

## Independent computation actually performed

`audit/referee_verify.py` is a fresh verifier. It imports no proposer
program. It uses dense SymPy matrix multiplication and exact symbolic
expressions, rather than the proposer's sparse-polynomial implementation.
The input certificates are comparison targets, not the source of the
reconstructed matrices or exponents.

Running `python3 audit/referee_verify.py` completed successfully with
Python 3.10.12 and SymPy 1.14.0. The durable output is
`audit/referee_verification.json`.

- All 3,456 entries of the 144 augmented tensors were reconstructed and
  compared with the serialized matrices.
- All 7,920 shape/cell cases were checked: 6,759 have an actual forbidden
  unit entry, and 1,161 are nonempty.
- All 997 equations have distinct coefficient-one leading variables in
  the stated order. Every serialized equation, free-variable list,
  dimension, and solution polynomial was checked against fresh algebra.
- Substitution in all 997 original equations gives zero in the integer
  polynomial ring. The maximum solution degree is 3.
- All 55 coefficient identities were checked by independent symbolic
  multiplication. Every row of the Markdown coefficient table matches.

The unrestricted row has coefficients
(1,5,13,23,30,30,23,13,5,1), agreeing with [4]!_q[3]!_q.
The maximal shape has the constant polynomial 1. Both boundary cases
are included in the complete check.

I inspected the supplied exhaustive binary program. Its full-rank-slice
pruning, polynomial maximal-minor gcd criterion, and treatment of
infinity are valid. I did not independently rerun its full 2^24-input
enumeration, and do not present the supplied binary totals as such a
rerun. Its 55 recorded counts agree with the independently verified
polynomials at q=2. Separately, dense determinant and polynomial-gcd
calculations reproduce its diagnostic witness: it has rank 3 at the
three rational points but common minor factor t^3+t^2+1 over F2. This
checks the distinction between rational-point and algebraic-closure
nondegeneracy. The universal proof does not depend on the binary run.

## Prior work and contribution

The nearest prior results are the two special product families,
the augmented-cell reduction and its pure-power count. Section 3.3
identifies 40 remaining k=3 shapes; Section 5.1 gives the permutation
sum without the complete k=3 product evaluation. The candidate supplies
that finite evaluation and its reproducible certificate. The general
method and cell principle are correctly attributed. [Journal paper,
Sections 3.3 and 5.1](https://ecajournal.haifa.ac.il/Volume2027/ECA2027_S2A3.pdf).

This is a modest, concrete completion for the first format beyond the
paper's complete k=2 treatment. It resolves the natural problem actually
frozen here, and its exact census can serve as a reference for further
general-k work. It is more than a field sample or an arbitrary restriction.
It does not warrant a claim of a new orbit method, a general-k solution,
or a large conceptual advance. It qualifies at the submitted scope
without predicting a journal's editorial decision.

I reopened both primary versions online; the journal PDF was accessible
through its index link. The arXiv record lists v1 as its only version.
Current searches on 2026-09-12 for `"2602.22129" proof conjecture`,
`"Koprowski" "Lewis" "hypermatrix" "k=3"`, and
`"Enumeration of Nondegenerate" "Hypermatrices"` found no equivalent
later resolution. This bounded check is not proof of priority.
[arXiv version record](https://arxiv.org/abs/2602.22129).

## Gaps, limits, and disposition

No mathematical gap remains in the exact frozen claim after these
checks. The final all-field implication rests on explicit integral
triangular bijections and complete polynomial identities, with the
correct hypotheses of the cited counting reduction.

This was a fresh model-context mathematical audit with separately
implemented computation, not external peer review or a formal
proof-assistant certification. PDF screenshots could not be retrieved
in this pass; primary HTML and PDF text supplied the relevant statements.
That access failure is not mathematical evidence. No publication
manuscript or release artifact was created.

Final disposition: accept `resolution-paper` / `proved` for the frozen
k=3 claim. The next workflow step is the runner's mathematical integrity
gate, followed by manuscript preparation preserving this scope and the
bounded attribution above.
