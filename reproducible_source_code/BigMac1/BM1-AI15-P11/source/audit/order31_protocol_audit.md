# Order-31 exact-enumeration protocol audit

Status: **PASS; all final exact, fail-closed, and release gates passed**.

## Frozen scope

- Order: exactly 31 vertices.
- Generator: `gentreeg` from nauty 2.9.3.
- Partition: all residues `0/120,...,119/120`.
- Concurrency: at most eight worker processes.
- Expected number of unlabelled trees: 40,330,829,030.
- Frozen implementation and arithmetic details:
  `certificates/order31_preflight.json`.

The production runner writes PID-qualified `.tmp` files and renames them to
paired `.summary.done` and `.exceptions.done` files only after the checker
returns successfully and emits a `RESEARCH_CHECK` record.  A residue is
resumed as complete only when both members of the pair exist.  Final
aggregation rejects missing, malformed, empty, duplicated, or unexpectedly
named residue records.

## Coverage argument

The bundled `gentreeg.c` identifies itself as a generator of unrooted (free)
trees and documents its parent-array `OUTPROC` interface.  Its `res/mod`
implementation assigns recursion nodes at the split level cyclically among
the residues.  Consequently, running every residue from 0 through 119 gives
a disjoint exhaustive partition of the unsplit generation.  This partition
mechanism was tested locally at order 23: the 24-way aggregate contained
exactly 14,828,074 trees and reproduced both order-independent fingerprints
of the unsplit run.

At order 31 the final fail-closed coverage condition is

\[
 \sum_{r=0}^{119} N_r=40{,}330{,}829{,}030,
 \qquad N_r=N_r^{\rm generated}>0.
\]

The same order-31 count appears in the nauty 2.9.3 generator source and in
OEIS A000055; the post-result literature audit must bind the archival source
for the public claim.

## Exact evaluator argument

For each generated parent array the C checker first validates the root
marker and every parent endpoint, reconstructs child lists, detects cycles or
repeated visits, and requires all 31 vertices to be reached.  In recursive
postorder it computes

\[
 A_v=\prod_{u\text{ child of }v}(A_u+B_u),\qquad
 B_v=x\prod_{u\text{ child of }v}A_u,
\]

using nonnegative integer polynomial addition and convolution.  The full
polynomial is `A_root+B_root`.  It must have constant coefficient 1 and
linear coefficient 31.

For every coefficient,

\[
 i_k(T)\leq {31\choose k}\leq {31\choose15}=300{,}540{,}195.
\]

Every intermediate DP accumulator counts a disjoint class of independent
sets in a processed induced subforest, so the same binomial argument bounds
it.  Products used for log-concavity diagnostics satisfy

\[
 300{,}540{,}195^2=90{,}324{,}408{,}810{,}638{,}025<2^{64}-1.
\]

Thus all decisive coefficient, convolution, and comparison arithmetic fits
in `uint64_t`.  The FNV multiplications and fingerprint sums intentionally
use unsigned arithmetic modulo \(2^{64}\); those are integrity fingerprints,
not coefficient calculations.

The unimodality scan permits equal adjacent coefficients.  Once it sees a
strict decrease it rejects any later strict increase, which is equivalent to
the absence of a strict triple valley and hence to weak unimodality.

## Independent checks

Already passed before the order-31 run:

1. A debug build serialized every parent array and coefficient vector for all
   436 unlabelled trees through order 11; direct subset enumeration rebuilt
   every coefficient exactly.
2. The independent referee evaluator checked the recurrence on 5,405
   graph-vertex cases and 8,477 rooted-tree cases, and checked the valley
   criterion on 21,844 finite sequences.
3. The 24-way order-23 partition matched the unsplit count and both
   order-independent fingerprints.

Final independent gates, all passed:

1. `experiments/aggregate_tree_sweep.py` must accept all 120 residue pairs.
2. `audit/order31_independent_aggregate.py`, which imports no project module
   and shares no parser with the production aggregator, must reach the same
   totals and fingerprints.  It also reconstructs every serialized exception
   from its parent array using exact Python integer DP.
3. `audit/rebuild_order31_checker.sh` must extract the frozen nauty tarball in
   a fresh temporary directory, rebuild release and debug binaries, reproduce
   a frozen order-23 partition fingerprint, and pass the direct-subset audit
   through order 11.
4. All frozen artifact hashes must agree with the preflight record.

## Materialized negative controls

The root driver `audit/fail_closed_rejection_tests.py` independently copied
the certificate into four temporary roots and required a nonzero verifier
exit after each single corruption.  It rejected: a missing residue-119
summary, a residue-000 checker/generator count mismatch, a changed final
coefficient in a serialized sequence, and a changed preflight artifact hash.
All four exited 1 with the expected fail-closed reason.  Exact stderr and
case data are in `results/fail_closed_rejection_tests.json`; the human-readable
record is `audit/FAIL_CLOSED_AUDIT.md`.

## Fail-closed endpoint

Any non-unimodal record is a candidate counterexample and stops the negative
enumeration claim.  Any process failure, missing pair, malformed summary,
count mismatch, hash drift, or verifier disagreement prevents certification.
Even a clean order-31 result proves only a finite statement; it does not prove
Erdős #993 for arbitrary trees.
