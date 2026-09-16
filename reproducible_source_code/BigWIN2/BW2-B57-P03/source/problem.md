# Precise reading of the frozen problem

The original wording is frozen in `source.md`.  The following is the precise
reading used for research; it does not alter that wording.

## Instance and feasibility

An instance consists of a finite set of jobs \(J=\{J_1,\ldots,J_n\}\), two
dedicated machines \(M_1,M_2\), and one renewable auxiliary resource of
capacity one.  For every job \(J_j\):

- \(m_j\in\{1,2,3\}\), and its operations form a prescribed chain
  \(O_{1j}\prec\cdots\prec O_{m_jj}\);
- operation \(O_{ij}\) is assigned to \(\mu_{ij}\in\{M_1,M_2\}\), has
  nonpreemptive processing time \(p_{ij}=1\), and consecutive operations use
  different machines, as required by the cited paper's printed JSC model;
  revisiting a machine is allowed, so a three-operation route is either
  \(M_1M_2M_1\) or \(M_2M_1M_2\);
- a single bit \(r_j=R(J_j)\in\{0,1\}\) is the resource demand of every
  operation of that job.

A schedule assigns a start time \(s_{ij}\ge 0\) to every operation.  It is
feasible exactly when:

1. \(s_{i+1,j}\ge s_{ij}+1\) for every consecutive pair in a job;
2. intervals of operations assigned to the same machine are disjoint; and
3. intervals of operations belonging to two jobs with demand one are
   disjoint (equivalently, the sum of auxiliary-resource demands of running
   operations is at most one at every time).

There are no release dates, deadlines, preemption, setup times, or other
resources.  The makespan is
\[
 C_{\max}=\max_{j,i}(s_{ij}+1).
\]
The optimization problem asks for its minimum.  Its decision version has an
integer bound \(B\) and asks whether a feasible schedule with
\(C_{\max}\le B\) exists.  The requested classification is a polynomial-time
algorithm for all such finite instances or a valid strong-NP-hardness proof
for this decision problem.  Operation-level (rather than job-level) resource
demands, more than two machines, \(m_j>3\), and variable processing times are
outside scope.

## Inclusion issue

For a source instance \(I\) of
\(J2\mid p_{ij}=1,m_j\le3\mid C_{\max}\) satisfying the same alternating-route
convention, define \(\Phi(I)\) by retaining all jobs, routes, and processing
times and setting \(r_j=0\) for every job.  Zero is legal under the printed
definitions: Tellache--Azerine explicitly use requirements zero and one and
define \(S=\{J_j:R(J_j)=0\}\).

Every feasible schedule of \(I\) is feasible for \(\Phi(I)\), because the
auxiliary-resource load is identically zero.  Conversely, deleting the
vacuous resource data from any feasible schedule of \(\Phi(I)\) leaves all
machine and chain constraints of \(I\).  Both maps retain every start time,
so they retain \(C_{\max}\) and the optimum exactly.

If a convention merely requires at least one resource-using job, then for any
nonempty \(I\) choose one existing job \(J_{j_0}\), set \(r_{j_0}=1\), and set
all other requirements to zero.  Since no second job uses the resource and a
job's own operations cannot overlap, the resource constraint is still
vacuous; the same two-way, makespan-preserving argument applies.  Thus no
dummy job is needed.  A newly added one-operation dummy is not itself an exact
optimum-preserving map: depending on an available machine slot it may fit
without increasing the makespan or may create additional machine load.

This inclusion does **not** transfer the cited hardness.  The 1977
Lenstra--Rinnooy Kan--Brucker reduction for the two-machine, at-most-three-
operation job shop uses variable processing times derived from KNAPSACK; it
does not prove hardness of the unit-processing-time restriction and is not a
strong-NP-hardness proof.  In the opposite direction, Hefetz--Adiri (1982)
give a linear-time algorithm for the two-machine unit-operation-time job shop
with alternating consecutive machines, even without a bound of three on the
number of operations.  Therefore \(\Phi\) embeds a known polynomial subcase,
not a hard subcase.

## Status and proposed contribution

Source status for the exact \(m_j\le3\) resource-constrained boundary is
`status-uncertain`: Tellache--Azerine prove the \(m_j\le2\) resource case
polynomial and explicitly leave their unrestricted unit-time resource case
open, but they do not separately state the \(m_j\le3\) boundary.

Nearest prior result: polynomiality for \(m_j\le2\) with the job-level binary
resource (Tellache--Azerine, Corollary 1).  Proposed delta: prove polynomiality
for \(m_j\le3\), or find an exact obstruction to the proposed aggregation.
Verification route: with two machines, three unit operations, and one binary
job-level demand there are only twelve job types (six alternating routes times
two demands).  Test an aggregate state-space dynamic program whose coordinates
count jobs by type and completed prefix; compare it exhaustively with a labeled
exact scheduler on small instances before attempting a proof and runtime
bound.  This is a research target, not a theorem asserted at triage.

## Research-pass result

The target was met in research pass 1.  `evidence/polynomial-dp-proof.md`
proves that the aggregate prefix counts form a sufficient state and gives an
\(O((n+3)^{24})\) exact optimization algorithm.  The key preliminary lemma
converts every feasible continuous-time schedule into an integer-slot schedule
of no larger makespan.  This resolves the frozen \(m_j\le3\) problem as
polynomial-time solvable under the precise reading above.  The exact exhaustive
implementation check is supporting evidence, not a premise of the proof.
