# Polynomial aggregate dynamic program

## Theorem

Under the exact model in `problem.md`,
\[
J2\mid res^t111,\ p_{ij}=1,\ m_j\leq 3\mid C_{\max}
\]
is polynomial-time solvable.  In particular, an optimal schedule and its
makespan can be found in time (O((n+3)^{24})), with a constant factor for
enumerating slot actions.  (The exponent is intentionally crude.)

## Integral-slot lemma

Every feasible schedule has an integer-start schedule of no larger makespan.
To see this, make one vertex for every operation.  Include the prescribed job
arcs.  For each pair of operations that cannot overlap because of a machine,
the auxiliary resource, or common job membership, orient the pair in the
temporal order in which the given schedule executes it.  Every resulting arc
(u\to v) satisfies (s_v\geq s_u+1), so the digraph is acyclic.  Give each
vertex (v) start time
\[
 h(v)=\max\{\text{number of arcs on a directed path ending at }v\}.
\]
These starts are nonnegative integers, every arc has a unit separation, and
therefore every original precedence and nonoverlap constraint holds.  A path
ending at (v) with (h(v)) arcs contains (h(v)+1) unit operations and
already forced the original completion time of (v) to be at least
(h(v)+1).  Thus the new makespan does not exceed the old one.

If an integer schedule contains a globally empty slot before completion,
shift every operation after that slot left by one unit.  Feasibility is
preserved.  Hence some optimum consists of nonempty integer slots.

## State space

Write the machines as (A,B).  Consecutive operations alternate, so the only
routes of length at most three are
\[
A,\ B,\ AB,\ BA,\ ABA,\ BAB.
\]
Together with the demand bit (r\in\{0,1\}), these give twelve types (t).
Let the route length of (t) be \(\ell_t\), and let \(n_t\) be its number of
jobs.  A state is
\[
x=(x_{t,k}:t=1,\ldots,12,\ k=0,\ldots,\ell_t),
\]
where (x_{t,k}) is the number of type-(t) jobs having completed exactly
(k) operations.  It always satisfies
\(\sum_k x_{t,k}=n_t\).  The initial state has (x_{t,0}=n_t); the terminal
state has (x_{t,\ell_t}=n_t).

At a state, category ((t,k)), (k<\ell_t), is ready iff (x_{t,k}>0).
Its next operation has the fixed machine specified by position (k+1) of
the route and fixed resource demand (r_t).  A slot action selects either
one ready category or two ready categories subject to:

1. no machine is selected twice;
2. the sum of the selected demands is at most one; and
3. no category is selected more often than its current count.

For every selected ((t,k)), decrement (x_{t,k}) and increment
(x_{t,k+1}).  Give every transition cost one and find a shortest path from
the initial to the terminal state.  The graph is acyclic because every
transition increases the total number of completed operations.

## Correctness

Every DP transition is schedulable.  Select arbitrary jobs from the indicated
prefix populations and run their next operations in the next unit slot.
Different prefix populations contain different jobs; two selected operations
use different machines; and at most one has demand one.  Thus machine,
resource, job, and precedence constraints all hold, and induction realizes
every DP path as a schedule of the same length.

Conversely, take an optimal nonempty-slot integer schedule supplied by the
lemma.  Immediately before each slot, count its jobs by type and completed
prefix.  The one or two operations run in the slot form exactly an allowed
action: they were ready, occupy distinct machines, and have total resource
demand at most one.  The successive count vectors are therefore a DP path of
the same length.  The shortest DP path consequently equals the optimum
makespan.  Retaining which arbitrary job is chosen at each transition also
recovers a labeled optimal schedule.

## Polynomial bound

For type (t), the number of possible prefix distributions is
\(\binom{n_t+\ell_t}{\ell_t}\leq(n+3)^{\ell_t}\).  Since
\[
\sum_t\ell_t=2(1+1+2+2+3+3)=24,
\]
there are at most ((n+3)^{24}) states.  There are at most 24 ready
categories and hence fewer than (24+\binom{24}{2}) candidate slot actions
per state.  State generation, shortest-path optimization, and schedule
reconstruction are therefore polynomial in the explicit input size.

## Exact implementation check (not part of the proof)

`aggregate_dp_check.py` implements the preceding quotient-state recursion and
a separately coded exact recursion that retains every job label.  It exhausts
all weak twelve-part type-count vectors with total job count at most six.
There are
\(\binom{6+12}{12}=18{,}564\) such vectors (including the empty instance).
The recorded run found zero makespan mismatches; its complete aggregate output
and a digest over all `(counts, aggregate optimum, labeled optimum)` records
are in `aggregate-dp-output.json`.  This finite check tests the implementation
and the proposed quotient invariant; the proof above, not the experiment,
establishes the theorem.

## Gap list

Empty for the theorem under `problem.md`.  Publication novelty is a separate
question: the bounded search documented in `evidence/literature-screen.md`
found no exact prior statement but cannot establish priority.
