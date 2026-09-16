# Bounded primary-source comparison

Checked 2026-09-07.  This is a scope comparison, not a claim of priority.

1. Tellache and Azerine, *Minimizing the makespan in job shop scheduling
   under conflict graph constraints*, arXiv:2609.04161v1 (submitted 2026-09-03),
   <https://arxiv.org/abs/2609.04161>.  The current arXiv record still listed
   only v1 at the time of checking.  The local primary PDF is preserved as
   `evidence/external/2609.04161v1.pdf`, SHA-256
   `295cf1d99d1c439f3df33f36e236aea79d49e0ae2257c5bd30cf3fa5f4504ef3`.
   Its pp. 1--2 define alternating consecutive machines, job-level resource
   requirements at most one, and hence legal zero requirements.  Theorem 1
   explicitly assigns zero requirements.  Corollary 1 on p. 6 proves the
   resource-constrained unit-time case with at most two operations per job;
   the immediately following sentence leaves the unbounded-operation version
   open.  It does not state or prove the at-most-three-operation result.

2. N. Hefetz and I. Adiri, *An Efficient Optimal Algorithm for the
   Two-Machines Unit-Time Jobshop Schedule-Length Problem*, Mathematics of
   Operations Research 7(3) (1982), 354--360,
   <https://pubsonline.informs.org/doi/10.1287/moor.7.3.354>.  The publisher's
   abstract says the resource-free two-machine unit-operation-time job shop is
   solved in linear time.  That theorem is strictly different from the current
   problem because it has no clique of mutually conflicting demand-one jobs.

3. J. K. Lenstra, A. H. G. Rinnooy Kan, and P. Brucker, *Complexity of
   machine scheduling problems*, Annals of Discrete Mathematics 1 (1977),
   343--362; repository record and primary scan:
   <https://ir.cwi.nl/pub/18051> and <https://ir.cwi.nl/pub/9725/9725D.pdf>.
   As documented with page locators in `triage-sources.md`, its two-machine,
   at-most-three-operation hardness reduction uses variable processing times
   derived from KNAPSACK.  It does not imply hardness of the all-unit-time
   restriction.

Exact-notation and equivalent-language web searches included
`"J2" "res^t 111" "m_j <= 3" Cmax`, `"J2" "unit-time" job shop resource
constraints three operations`, and arXiv-restricted searches for job-level
unit-capacity resource and conflict-graph formulations.  No primary source
stating the exact at-most-three-operation result was located in this bounded
search.  Because the target paper was only four days old and database coverage
can lag, this negative search is especially weak evidence about novelty; the
mathematical claim does not depend on it.

The contribution relative to the cited v1 is exact and narrow: the aggregate
prefix-state proof extends its printed polynomial boundary from
\(m_j\leq2\) to \(m_j\leq3\).  It does not settle the paper's unrestricted
\(m_j\) open problem, since the number of route positions (and the DP exponent)
is no longer bounded there.
