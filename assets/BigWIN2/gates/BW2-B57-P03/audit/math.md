# Fresh mathematical audit

## Frozen scope and integrity

I reviewed the exact `resolution-paper` statement in `claim.json` against the
original problem in `source.md`, its precise reading in `problem.md`, and every
file enumerated by `audit/snapshot.json`.  Recomputed SHA-256 hashes of the
claim and all enumerated evidence agree with the snapshot.  The snapshot digest
is `e891e3be3310c2bde190c97191bd8194ae9487029fcb768a23ba0032d6de75ef`.

The claim concerns all finite instances with two machines, unit nonpreemptive
operations, alternating prescribed routes of length at most three, and one
unit-capacity resource whose binary demand is constant over every operation of
a job.  It claims polynomial solvability of this full frozen class, not a
restriction or a statement about the unbounded-route problem.

## Reconstruction of the decisive argument

First, arbitrary real start times may be replaced by integer start times
without increasing makespan.  Given a feasible schedule, orient every pair of
operations subject to a nonoverlap constraint in its actual temporal order and
include all job-precedence arcs.  Every arc `u -> v` then satisfies
`s(v) >= s(u)+1`; hence the digraph is acyclic.  Assigning to each operation
the maximum number of arcs in a directed path ending there gives nonnegative
integer starts, preserves every precedence and disjunctive constraint, and
does not increase any terminal path's completion-time lower bound.  Thus it
does not increase makespan.  Any globally empty integer slot can then be
removed by shifting all later operations one unit to the left.

With machines denoted `A,B`, the only routes are
`A,B,AB,BA,ABA,BAB`.  Crossing these with demands zero and one gives twelve
types.  For each type and each completed-prefix length, record the number of
jobs at that prefix.  In one slot a transition advances one ready population,
or two ready populations when their next machines differ and their resource
demands sum to at most one.  Such a transition always has a labeled
realization: distinct prefix populations contain distinct jobs, and an
arbitrary job in each selected population can be advanced.  Conversely, each
nonempty slot of an integral feasible schedule induces exactly one such
transition.  Therefore DP paths and integral schedules have the same attainable
lengths, so a shortest path returns the true optimum and can retain labels to
recover a schedule.

For a type of route length `ell_t`, there are
`binomial(n_t+ell_t, ell_t)` prefix distributions.  The sum of the twelve route
lengths is 24, so the product state bound is at most `(n+3)^24`.  At most 24
prefix populations are ready, leaving only a constant number of one- or
two-operation actions per state.  Since jobs and operations are explicitly
listed and the dimension is fixed, this is a polynomial-time exact algorithm.

## Attacks and checks performed

- **Quantifiers and route coverage.** Routes of lengths one, two, and three,
  both initial machines, and both demand bits are all represented.  Machine
  revisits `ABA` and `BAB` are included.  The argument does not assume a fixed
  number of jobs or a favorable type distribution.
- **Normalization.** A cycle in the oriented disjunctive graph would sum to the
  impossible strict inequality `s(u) >= s(u)+q` for some positive integer
  `q`.  Longest-path starts preserve all constrained pairs, including
  demand-one pairs.  Removing an empty slot cannot violate a precedence arc
  crossing the slot because its earlier operation completed no later than the
  slot's left endpoint.
- **Quotient sufficiency.** No job identity affects a next operation once its
  type and completed prefix are fixed.  Jobs in different prefix populations
  are disjoint; two operations from one job cannot be selected in a slot.
  Same-machine and two-demand-one pairs are explicitly excluded.  There is no
  hidden setup, release-time, or operation-level demand information that the
  quotient discards under the frozen reading.
- **Degenerate cases.** A single selected operation is allowed, so forced idle
  time on one machine is represented.  Globally empty slots are unnecessary.
  Zero-demand jobs create no resource load.  If a nonempty instance were
  required to include a demand-one job, assigning demand one to exactly one
  existing job leaves the resource constraint vacuous because that job's own
  operations are already sequential; this preserves every schedule and its
  makespan.
- **Implementation evidence.** I inspected both transition implementations in
  `evidence/aggregate_dp_check.py`.  I also reran the frozen program through all
  6,188 weak type-count vectors with at most five jobs; it again reported zero
  aggregate-versus-labeled optimum mismatches.  This supports the quotient
  check but is not used as a premise of the proof.

## Source comparison and limits

The frozen Tellache--Azerine PDF defines the job-level resource variant, permits
zero requirements (and uses them explicitly in Theorem 1), proves the
`m_j <= 2` resource case in Corollary 1, and immediately states that the
unbounded-operation unit-time case remains open.  The present proof therefore
settles the frozen `m_j <= 3` boundary while leaving that unbounded case open.

The bounded literature reports identify the 1977 at-most-three-operation
hardness result as a variable-processing-time KNAPSACK reduction and the 1982
resource-free unit-time problem as polynomial.  Only the Tellache--Azerine
primary PDF is itself included in the frozen evidence; the older-source details
are supplied with precise citations and locators in the reports rather than
local primary copies.  This does not affect the self-contained polynomiality
proof.  The novelty search is appropriately reported as bounded, especially
given the recency of the target preprint, and makes no priority claim.

## Verdict

**Accept.**  The integral-slot lemma and aggregate-prefix dynamic program are
correct under the frozen model, cover the full claimed scope, and yield the
stated polynomial bound.  The result settles the original requested boundary
as polynomial-time solvable.  The computational run is corroboration only, and
the contribution language honestly limits both the literature search and the
unresolved unbounded-operation problem.
