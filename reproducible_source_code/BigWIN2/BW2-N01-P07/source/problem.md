# Precise problem

Current job: `newwin-00001-p07-research-4c610e4f54cc`.
Initial interpretation: `newwin-00001-p07-triage-19444324da60`.
Frozen input: `source.md`.
Its SHA-256 at intake is
`f55a25a1a14dbeef692d590d1d55513ad3e234065d61da1ae130416417c7a59e`.

For every integer \(n\geq0\), let \(S_n\) be the permutations of
\([n]=\{1,\ldots,n\}\), with one empty permutation in \(S_0\).
Write a permutation in one-line notation, so its \(i\)-th entry is its
value at \(i\). A permutation contains a pattern \(\sigma\in S_k\) if
some indices \(i_1<\cdots<i_k\) give entries with the same relative order
as \(\sigma\); avoidance means absence of such indices. Patterns are
classical, not necessarily consecutive. Powers mean function composition:
\(\pi^3(i)=\pi(\pi(\pi(i)))\).

Define
\[
B_n=\{\pi\in S_n:\pi\text{ avoids }312,321,
\quad\pi^3\text{ avoids }2143\},\qquad b_n=|B_n|.
\]
No restriction is imposed on \(\pi^2\). A composition of \(n\) is a finite
ordered sequence \(d=(d_1,\ldots,d_m)\) of positive integers with sum \(n\).
Only the empty sequence composes zero. Set
\[
C_n=\{d:\textstyle\sum d_i=n,\quad
|\{i:d_i\notin\{1,3\}\}|\leq1\},\qquad c_n=|C_n|.
\]
Repeated parts count at their distinct positions. The exceptional part,
if present, has size in \(\{2,4,5,\ldots\}\); it is not marked in any
additional way.

The frozen assertion is \(b_n=c_n\) for **all** integers \(n\geq0\),
equivalently the formal power-series identity
\[
\sum_{n\geq0}b_nz^n=
\frac1{1-z-z^3}+
\frac{z^2+z^4/(1-z)}{(1-z-z^3)^2}.
\]
The right side counts a sequence of parts 1 or 3, or two such sequences
separated by one exceptional part. All denominators have constant term one.
The source's initial values are \(1,1,2,4,7,13,23,39,66\) for
\(0\leq n\leq8\). The exact composition-count recurrence in
`evidence/research_check.json` reproduces these coefficients.

## Nearest prior result and candidate delta

[Archer–Bourne, arXiv:2505.05218v3](https://arxiv.org/html/2505.05218v3),
Lemma 3.1, encodes \(S_n(312,321)\) by
\(\pi=\epsilon_{d_1}\oplus\cdots\oplus\epsilon_{d_m}\), where
\(\epsilon_d=(2,3,\ldots,d,1)\), including \(\epsilon_1=(1)\).
For permutations \(\alpha\in S_a,\beta\in S_b\), the direct sum
\(\alpha\oplus\beta\) concatenates \(\alpha\) and the entries of
\(\beta\) increased by \(a\). Section 3 classifies square-pattern avoidance;
§5, second paragraph, explicitly conjectures the present cube enumeration.
The live arXiv version history inspected on 2026-09-12 ends at v3
(2026-05-13). Source status: **open-supported**, not a verified assertion
that no subsequent solution exists.

Candidate contribution: the same composition encoding restricts to a
bijection \(C_n\to B_n\). The exact structural assertion is
\[
\left(\bigoplus_i\epsilon_{d_i}\right)^3\text{ avoids }2143
\iff |\{i:d_i\notin\{1,3\}\}|\leq1.
\]
The complete argument is in `evidence/bijection-proof.md`: the
minimum-position recursion is a two-sided inverse for arbitrary block
lists; the cube of one block is computed directly; and the two inversions
of \(2143=21\oplus21\) establish both directions of the equivalence.
The empty objects and the formal generating series are included. This
is the full original scope; no replacement claim is proposed.

The decisive local primary text is
`evidence/external/archer-bourne-v3.html`, copied byte for byte from
`/home/ailab/4math-open-problems/batches/literature/newwin-00001/archer-bourne-v3.html`.
The copied complete HTML, rather than a summary, binds Lemma 3.1 and the
Section 5 conjecture. Its decisive passages were compared with live arXiv
on 2026-09-12; provenance and current search limits are in
`literature/research-screen.md`.

New exact attacks in `evidence/research_check.json` check all 61440
compositions of sizes 13--16, 4681 bounded block lists, 33825 arbitrary
direct-sum lists for the auxiliary lemma, and explicit boundary/large
cases up to a single block of size 4096, with no counterexample. The
general pattern detector was checked against all four-subsequence rank
tests on all permutations through size 7. The formal series coefficients
agree with a composition recurrence through degree 100. These are finite
observations; the complete all-n argument is the proof above.

Candidate workflow: resolution-paper, original_status=proved, requesting
fresh independent review. These fields record the scope of the proposed
proof and are not mathematical acceptance or release authorization.
