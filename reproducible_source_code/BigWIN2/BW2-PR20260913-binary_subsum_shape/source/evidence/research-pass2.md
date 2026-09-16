# Research pass 2 decision

Job: `primary-20260913-binary-subsum-shape-research-9e631dc6dcdd`.
Outcome: **candidate**, kind=result-note, original_status=unresolved.
This requests fresh review; it does not assert acceptance or a full resolution.

The assigned all-parameter K3 question is answered affirmatively. Closed tail
formulas separate parity and the halfway cutoff. A complete chamber covering
gives 144 exact nonnegative expansions with 12325 monomials. A separate
Fraction polynomial implementation verifies every identity, domain containment,
and complete coverage through 68 parity roots and 4119 clipped vectors.
It also checks 20790 literal entries, but these finite checks are not the
universal proof. Supplementary positive expansions prove strict compensation
and T3(A)>0; explicit n=6,8 triples complete the small cases.

This supplies strict log-concavity at the first three positions and their
reflections for every n>=6, using the earlier first-two-position proof.
The full all-index recurrence invariant is still unproved, and the previous
abstract carry-one obstruction remains valid.

A separate elementary argument gives a more substantial unbounded range.
The mean number of ones satisfies mu_n/n<=(1+o(1))/log_2 n, by grouping
partition counts and summing expected weights of powers-of-two parts.
Union bounds give coefficient lower bounds; coefficientwise domination by
(1-x)^(-n) gives upper bounds. The resulting uniform estimate proves, for
each 0<epsilon<1 and all sufficiently large n, strict log-concavity through
floor((1-epsilon)*sqrt(log_2(n)/2)) at both ends. Its exact finite rational
criterion is also stated and proved. No asymptotic enumeration result is used.

`research_growing_boundary.py` performs 4095 exact mean-bound checks and
49085 coefficient-envelope checks for n<=4096, plus 4037 checks where its
sufficient criterion is compared with actual low coefficients. The low-degree
construction is only through degree 13, not a new all-coefficient prefix.
The criterion certifies j=1,...,22 at n=2^1024 without computing that N_n.
All infinite assertions come from the written proofs.

Candidate scope is frozen in `claim.json`; its primary contribution is the
growing boundary theorem with explicit criterion, accompanied by the uniform
first-three-position result. The central range remains unresolved. Bounded
live primary comparisons found no equivalent in the accessed sources; novelty,
significance, and all proofs still require a fresh referee. The decisive primary
PDFs and full extracted texts have been copied into `evidence/external/`.

Known gap list for the submitted scope: none. Limitations: no optimality of
the square-root-logarithmic constant, no explicit sharp n_epsilon, no theorem
for the unresolved central indices, and no independent referee in this job.
No manuscript or generated publication PDF has been created. No worker or
other model process was spawned. The original source hash is unchanged.

One next test: fresh referee review of the submitted boundary claim, focusing
on the occupation bound, coefficientwise product comparison, uniform-in-j
limit, kernel coverage and exact identities, with a primary-source novelty
comparison. The prior K3 test should not be repeated as an unresolved target.
