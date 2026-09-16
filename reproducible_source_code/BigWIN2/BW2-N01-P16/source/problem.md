# Frozen problem: five-prime small-component bound

Initial interpretation: `newwin-00001-p16-triage-b3295de4c9e7` (2026-09-12).
Research candidate: `newwin-00001-p16-research-ba4f5e168b06` (2026-09-12).
The verbatim source remains in `source.md`, SHA256
`8b4fed18ea31443b084f7ff6a5cca49f4221bce85a82b8c026ce64f0a125e6d2`.

For a positive integer m, define sigma(m) = sum of all positive divisors of m
and h(m) = sigma(m)/m. A positive integer n is **primitive non-deficient** if
h(n) >= 2 and h(d) < 2 for every positive proper divisor d of n.
Perfect numbers, if present in this domain, are included.

For every ordered tuple of five distinct odd primes
3 <= p1 < p2 < p3 < p4 < p5 and every tuple of positive integers
(a1,a2,a3,a4,a5), set n = product(pi^ai) and R = product(pi).
The exact assertion is

> If n is primitive non-deficient, then there exists i in {1,2,3,4,5}
> such that pi^(ai+1) < 2R.

The exponent is ai+1; the inequality is strict. There is no upper bound on
the primes, exponents, or n. This does not assert the stronger R bound, an
arbitrary number of prime factors, or a bound for all abundant numbers.
No correction to the source is proposed.

Checking all five inequalities h(n/pi) < 2 is equivalent to checking all
proper divisors: every proper divisor divides one n/pi, and h is monotone
under divisibility. This follows by writing each prime-power contribution as
1 + 1/p + ... + 1/p^a.

Auxiliary notation: D = product(pi-1) = phi(R), H = R/D, and E = R-2D.
For n > 1, h(n) = H product(1-pi^(-ai-1)) < H; hence non-deficiency
implies E > 0. All auxiliary computations use exact integers or rationals.

## Literature and proposed contribution

Source status: **open-supported**, in the limited sense that the current
primary source explicitly conjectures the general assertion and proves only
the three- and four-prime odd cases. This is not a proof that the five-prime
case has never been settled elsewhere.

Nearest inspected result: Joshua Zelinsky, *Must a Primitive Non-Deficient
Number Always Have a Small Component?*, Journal of Integer Sequences 29
(2026), Article 26.4.3, published July 3, 2026.
[Publisher PDF](https://cs.uwaterloo.ca/journals/JIS/VOL29/Zelinsky/zel14.pdf):
Conjecture 1, p. 2, states the general 2R bound; Lemma 4, p. 4, proves the
odd k=3,4 cases; Theorem 2, p. 2 and pp. 8–9, proves 2kR generally.
[arXiv v5 record](https://arxiv.org/abs/2005.12115v5) identifies the revised
July 3, 2026 version. The superseded R-bound snippets are not this claim.

Candidate delta: the unchanged k=5 odd case, in full scope. The complete
proposer proof is in `evidence/five-prime-proof.md`. A counterexample would
have p1=3 and h(n/3)>=(R-7/2)/D, forcing E in {1,3}. A congruence excludes
E=1. The exact factor certificate excludes E=3 through 13 proved-complete
prime prefixes and 95 divisor checks; a separate last-prime calculation
over 937 possible fourth values agrees. All six ordered integral pairs
have an explicit composite member. No exponent or arbitrary prime bound
is assumed. This is a resolution-paper candidate requesting fresh review,
not mathematical acceptance.

The current comparison is in `literature/research-screen.md`. No covering
result was verified in that bounded search; priority is not established.
The product inequality already occurs in the primary source's Lemma 9,
and is not claimed as a new technique. The supplied handoff was a lead,
independently tested; its historical registry screen cannot be revalidated
from the project-local files.

Decisive primary inputs for freezing are the byte-identical copies
`evidence/external/zelinsky-2026-20260912.pdf` and
`evidence/external/zelinsky-2026-20260912.txt`. Both preserve the actual
local primary source underlying the theorem and open-status comparison.
