# NOVELTY_LOCK — 2026-08-29

## Decision

Proceed as an apparently open problem, with a corrected bibliographic
boundary.  Under the searches recorded in `literature/search_log.md` and the
independent report `audit/literature_agent_report.md`, no public proof or
counterexample of the 3-packed specialization was located through 2026-08-29.
This is a bounded search conclusion, not a claim that no solution exists.

## Locked endpoint

The target is Sagan--Zhao, Conjecture **3.8** in the version-of-record PDF:

\[
u\in[3]^*,\quad\operatorname{alph}(u)=[3]
\quad\Longrightarrow\quad
C(u^k)=C(u^3)\quad(k\ge3),
\]

where each centralizer is a subset of all finite words \(\mathbb P^*\).

The Springer HTML currently mislabels this packed-word conjecture as 4.6.
In the official PDF, Conjecture 4.6 is instead a log-concavity conjecture for
\(b_{n,k}\).  The PDF numbering controls this project.

## Publication and source lock

- Bruce E. Sagan and Chenchen Zhao, “Properties of plactic monoid
  centralizers,” *Semigroup Forum* **113** (2026), no. 1, 242--262.
- DOI: <https://doi.org/10.1007/s00233-026-10652-4>.
- Version of record published online 2026-06-24; official PDF SHA-256 at audit
  time: `c332c049e9518d3bee6128ba8d5cce2d477b918bcd777e543413c29b711c4b8d`.
- arXiv:2512.21401 remained v1 at the cutoff and is not authoritative for the
  final theorem numbering/computation wording.

## Known frontier

- binary words: strongly stable (Theorem 2.13);
- permutations: \(m\)-stable (Theorem 3.7);
- decreasing permutation: strongly stable (Proposition 3.9);
- author-reported truncated test: packed \(m=3,4\), \(|u|\le8\), candidates
  \(w\in[m]^\ell\) with \(\ell\le10\), adjacent powers \(m\le k\le14\).

Colin Defant, arXiv:2605.19979v3, proves the bounded-row and evacuation
conjectures from this circle of work, not packed-word stability.  Oberwolfach
Report 2/2026 still records stability as an open problem in January 2026.

## Code lock

The older public Sagan--Wilson Sage notebook at
<https://github.com/wilsoa/Centralizers-in-the-Plactic-Monoid> does not visibly
implement the full 2026 reported grid and is not a certificate.  The project
must reproduce the published range independently.

## Release condition

Gate 1 permitted research to proceed.  The mandatory release search was run
again on 2026-08-29 after the full-DAG post-repair PASS; its queries and
bounded negative result are recorded under “Pass 3” in
`literature/search_log.md`.  No intervening public solution was located.  The
novelty gate is therefore closed, subject to the stated provider/query
limitation.  The subsequent independent citation, clean-build, pagewise PDF,
source-package, and release-manifest gates also passed.
