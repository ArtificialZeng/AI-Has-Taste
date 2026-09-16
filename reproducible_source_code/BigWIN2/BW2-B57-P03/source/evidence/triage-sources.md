# Triage source audit

Retrieved 2026-09-07.

1. N. E. Tellache and A. Azerine, *Minimizing the makespan in job shop
   scheduling under conflict graph constraints*, arXiv:2609.04161v1,
   <https://arxiv.org/abs/2609.04161>.  Inspected the local PDF with SHA-256
   `295cf1d99d1c439f3df33f36e236aea79d49e0ae2257c5bd30cf3fa5f4504ef3`.
   PDF pp. 1--2 define chains, two consecutive operations on different
   machines, job-level requirements, and requirements "at most" the indicated
   amount.  PDF p. 4, Theorem 1 explicitly assigns resource requirement zero
   to jobs not incident with an edge and defines both zero- and one-demand
   jobs.  PDF p. 6, Corollary 1 proves
   \(J2\mid res^t111,p_{ij}=1,m_j\le2\mid C_{\max}\) polynomial; the next
   sentence says the same unit-time resource problem without an operation
   bound remains open.

2. J. K. Lenstra, A. H. G. Rinnooy Kan, and P. Brucker, *Complexity of
   machine scheduling problems*, Annals of Discrete Mathematics 1 (1977),
   343--362.  CWI record and full text:
   <https://ir.cwi.nl/pub/18051> and <https://ir.cwi.nl/pub/9725/9725D.pdf>.
   The preprint's Table I (PDF p. 12 in the repository scan) marks the
   two-machine general-job-shop case with at most three operations NP-complete.
   The displayed reduction in Theorem 4(i) (scan p. 18) is from KNAPSACK and
   assigns processing times such as \(a_j,b,1,A-b\).  Hence the result has
   variable processing times and does not establish either the unit-time
   restriction or strong NP-hardness.

3. N. Hefetz and I. Adiri, *An Efficient Optimal Algorithm for the
   Two-Machines Unit-Time Jobshop Schedule-Length Problem*, Mathematics of
   Operations Research 7(3) (1982), 354--360,
   <https://doi.org/10.1287/moor.7.3.354>.  The publisher abstract states that
   the two-machine unit-operation-time job shop is in P via the
   longest-remaining-processing-time rule, with time and space linear in the
   total number of operations.  The source-compatible alternating-consecutive-
   machine condition is also stated in the job-shop survey full text at
   <https://ir.cwi.nl/pub/6563/6563D.pdf>, PDF p. 28 of that scan.

Searches for the exact \(m_j\le3\), unit-time, one job-level binary-resource
statement and equivalent two-machine conflict-clique language did not locate
another primary result in this bounded pass.  This is not a priority or
open-status claim.

