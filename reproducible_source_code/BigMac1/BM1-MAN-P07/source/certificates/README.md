# Exact certificate for the bounded Lehmer search

## Certified statement

There is no composite integer \(n\) such that

\[
\varphi(n)\mid n-1
\]

and every prime divisor of \(n\) is at most \(347\). Since \(349\) is the
next prime after \(347\), every hypothetical solution therefore has
\(P^+(n)\ge 349\).

This is a finite computational result. It does not settle Lehmer's totient
problem and carries no independent novelty claim.

## Independent implementations

The complete certificate uses two independently written implementations of
the same exhaustive prime-set search.

1. The original exact branch-and-bound enumerator is replayed by a separately
   written tuple-based implementation. It exposes all 38 sets surviving the
   2-adic filter.
2. Small universes are also compared with an unpruned full power-set
   enumeration.

## One-command branch-and-bound verification

From any working directory, run:

~~~bash
bash /Users/mac/Documents/ChatGPT/math3/lehmer_totient_problem/tests/run_full_certificate.sh
~~~

The command uses a new temporary directory, runs the tests, regenerates the
cap-\(347\) output from source, compares every deterministic field with the
frozen result, and runs the structurally independent verifier. The temporary
directory is removed at exit; no committed result is overwritten.

Success ends with:

~~~text
FROZEN COMPARISON: PASS
selection_attempts: 27179711
ratio_eligible_sets: 17803010
two_adic_pass: 38
korselt_lcm_pass: 0
exact_divisibility_pass: 0
INDEPENDENT REPLAY: PASS
cap: 347
exact_divisibility_pass: 0
FULL CAP=347 CERTIFICATE: PASS
~~~

Any failed test, parse error, missing key, altered deterministic count,
changed retained-candidate list, changed search-source digest, independent
replay disagreement, or nonempty solution list terminates with a nonzero exit
status.

## Inputs and trust boundary

The branch-and-bound certificate consists of:

- **src/agent_hunter_search.py**: exact sieve/bitset discovery enumeration;
- **src/agent_hunter_verify.py**: independent trial-division/tuple replay;
- **src/agent_hunter_compare.py**: fail-closed frozen-endpoint comparison;
- **src/agent_hunter_test.py**: small exhaustive and cross-implementation tests;
- **results/agent_hunter_cap347.json**: frozen result and all 38 sets that
  survive the 2-adic filter;
- **tests/run_full_certificate.sh**: one-command clean rebuild.

Required dependencies are Bash, a POSIX-like userspace with **mktemp**, and
CPython 3.10 or later. All Python imports are from the standard library.
No network access, external solver, database, random seed, or proof assistant
is used by this route. Its trust boundary is the Python interpreter, integer
arithmetic, the operating system, and the auditable source files above.

## Incomplete pseudo-Boolean experiment

A separate research experiment is retained in **experiments/pb_partial**. It
is not part of this certificate. The four experimental instances for Lehmer
indices \(k=2,3,4,5\) pass the structural checker, and strict VeriPB proofs
were completed only for \(k=3,4,5\). The \(k=2\) solver run was stopped after
10,843 CPU seconds and 1,368,420 conflicts without an UNSAT conclusion; its
incomplete trace is excluded from the release.

The command **experiments/run_partial_pb_checks.sh** intentionally checks only
the three completed logs and prints an explicit warning that the result is
not a cap-347 certificate. This negative experiment does not affect the
complete direct enumeration above.

## Mathematical completeness

Suppose a composite \(n\) satisfies \(\varphi(n)\mid n-1\).

1. It is odd: for \(n>2\), \(\varphi(n)\) is even, whereas \(n-1\) would be
   odd if \(n\) were even.
2. It is squarefree: if \(p^2\mid n\), then \(p\mid\varphi(n)\), hence
   \(p\mid n-1\), contradicting \(p\mid n\).
3. Therefore \(n=\prod_{p\in S}p\) and
   \(\varphi(n)=\prod_{p\in S}(p-1)\) for a set \(S\) of distinct odd primes.
4. If \(p<q\) belong to \(S\), then \(p\nmid q-1\); otherwise
   \(p\mid\varphi(n)\) and \(p\mid n-1\), again contradicting \(p\mid n\).
   Hence every solution is a clique in the enumerated compatibility graph.
5. If \(k=(n-1)/\varphi(n)\) is integral, then \(k\ne1\) for composite \(n\),
   since \(\varphi(n)\le n-2\). Thus \(k\ge2\) and
   \(n/\varphi(n)>2\).

At a canonical search node with selected primes \(S\) and remaining compatible
primes \(C\), every extension \(S\cup T\), \(T\subseteq C\), obeys

\[
\prod_{p\in S\cup T}\frac{p}{p-1}
\le
\prod_{p\in S\cup C}\frac{p}{p-1}.
\]

The program prunes a subtree only when the right side is at most \(2\). The
comparison is an exact integer cross multiplication. All remaining increasing
prime sets are visited once. Sets with ratio above \(2\) are then checked by:

\[
2^{v_2(\varphi(n))}\mid n-1,\qquad
\operatorname{lcm}_{p\mid n}(p-1)\mid n-1,\qquad
\varphi(n)\mid n-1.
\]

The first two are necessary filters; the last is the target condition.

## Frozen key counts

The universe contains 68 odd primes. Of its 2,278 unordered prime pairs,
2,183 are compatible and 95 are incompatible.

| Deterministic quantity | Value |
|---|---:|
| Canonical selection attempts | 27,179,711 |
| Exact ratio-bound prunes | 5,457,679 |
| Nodes surviving the ratio bound | 21,722,032 |
| Sets with \(n/\varphi(n)>2\) | 17,803,010 |
| Sets passing the 2-adic filter | 38 |
| Sets passing the Korselt-lcm filter | 0 |
| Exact Lehmer hits | 0 |

The external audit log is **audit/CERTIFICATE_RUN.txt**. Source and result
digests are kept in the external audit artifacts and should not be copied into
the manuscript body.
