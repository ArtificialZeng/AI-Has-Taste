# Precise problem and research scope

Current job: primary-20260914-triangular-square-roots-research-8c4db654213f.
Research pass 1, 2026-09-14: proposed **result-note** for fresh review.
Workflow original status: **unresolved**. The inspected primary source states
the full conjunction as a conjecture; the candidate below addresses D^2 only.

The verbatim claim and source metadata remain in immutable `source.md`.
[Mao and Wang, The Narayana transformation, arXiv:2607.01572v1](https://arxiv.org/html/2607.01572v1),
Section 4, PDF pp.10–11, defines the objects and states Conjecture 4.1 on p.11
(HTML Conjecture 4.15). No correction of the original statement is proposed.

## Definitions and quantifiers

Let \(\mathbb N_0=\{0,1,2,\ldots\}\) and \([n]=\{1,\ldots,n\}\).
For a permutation \(\pi\) of \([n]\), put
\(\operatorname{des}(\pi)=\#\{i:1\le i<n,\ \pi(i)>\pi(i+1)\}\).
Define the infinite lower triangular matrix \(A\) by
\[
 A(0,0)=1,\qquad
 A(n,k)=\#\{\pi\in\mathfrak S_n:\operatorname{des}(\pi)=k-1\}
 \quad(n\ge1,\ 0\le k\le n).
\]
Thus \(A(n,0)=0\) for \(n\ge1\); its first four rows are
\((1),(0,1),(0,1,1),(0,1,4,1)\).

Define \(D(n,k)\), for \(n\in\mathbb N_0\) and \(0\le k\le n\), as the
number of lattice paths from \((0,0)\) to \((n-k,k)\), with steps
\((1,0),(0,1),(1,1)\). The empty path gives \(D(0,0)=1\).
Both matrices have entry zero outside \(0\le k\le n\). An exact equivalent
formula is
\[
 D(n,k)=\sum_{j=0}^{\min(n-k,k)}2^j\binom{n-k}{j}\binom{k}{j}.
\]
For \(M\in\{A,D\}\), use ordinary matrix multiplication:
\[
 (M^2)(n,k)=\sum_{i=k}^n M(n,i)M(i,k),\qquad
 P_{M,n}(x)=\sum_{k=0}^n (M^2)(n,k)x^k\in\mathbb Z[x].
\]
Every entry uses a finite sum; there is no infinite-series convergence issue.
The frozen assertion is precisely
\[
 \forall M\in\{A,D\}\ \forall n\in\mathbb N_0\ \forall z\in\mathbb C,
 \quad P_{M,n}(z)=0\Longrightarrow z\in\mathbb R\ \text{and}\ z\le0.
\]
At \(n=0\), both polynomials are the constant 1, so the condition is vacuous.
For \(n\ge1\), both have degree \(n\) and are monic. The Eulerian square
has a zero at 0; the Delannoy square has positive constant term. The claim
permits multiplicities. Matrix total nonnegativity, Hadamard squares, the
rectangular Delannoy array, and a differently shifted Eulerian square are
not interchangeable with this assertion.

## Nearest results, proposed delta, and verifier

Nearest prior results: Mao–Wang's PDF Corollary 3.6 (HTML 3.13) treats powers
of Pascal, Stirling and Narayana triangles. Athanasiadis's Theorem 1.1 treats
the Eulerian transform on a specified nonnegative cone. Chen–Fu–Ruan's
Theorem 1.3 gives a sufficient condition using a totally nonnegative left
production matrix. Exact tests below show why the last two direct
applications do not settle these squares; see `literature/triage_review.md`.

Research pass 1 candidate: for every n>=1, the ordinary Delannoy-square row
G_n has n distinct real roots, all in (-4-3 sqrt(2), -3+2 sqrt(2)); G_0=1.
The complete proposed proof is `evidence/delannoy_phase_proof.md`.
This is the D^2 half with simplicity and a uniform enclosure. The A^2 half
and consecutive strict interlacing are outside the submitted theorem.
A full resolution still needs both families, or an exact counterexample to
either. No finite cutoff is presented as the contribution.

Write \(G_n=P_{D,n}\). The source recurrence is
\[
 G_n=(x+3)G_{n-1}+(x-1)(G_{n-2}+G_{n-3})+xG_{n-4}\quad(n\ge4),
\]
with \(G_0=1\), \(G_1=x+2\), \(G_2=x^2+6x+5\),
\(G_3=x^3+10x^2+25x+12\).
The original verification route sought a finite interlacing invariant.
The current proof instead derives an exact divided difference by applying
the quadratic formula for d_n twice. A complex phase on one interval and
a trigonometric amplitude comparison on an adjacent interval produce n+1
ordered sign-alternating samples for every n. `evidence/phase_checks.py`
and `evidence/replay_phase_certificates.py` provide reproducible finite
checks; the all-n justification is the written argument.

The previous next test targeted the signs of
\(R_n=(x-1)(G_{n-2}+G_{n-3})+xG_{n-4}\) at roots of G_{n-1}.
No invariant proving those signs was established. Exact failures of broad
palindromic preservation and of one transformed companion's interlacing
are in `evidence/phase_checks.json`; neither refutes the original.

One next test: a fresh referee should audit the D^2 proof's strict-modulus
lemma and ceiling-index splice, including the integer threshold case and
the excluded join x=-3-2 sqrt(2), and replay the rational certificates.
The decisive primary PDF/text are preserved in
`evidence/external/2607.01572v1.pdf` and `.txt`. Current comparison and
access limits are in `literature/research_review.md`.
