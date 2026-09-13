# Independent breaker and exact finite certifier notes

## Endpoint

**Outcome: no counterexample at `n=5`; exact finite certification succeeds.**

The independent route proves, by characteristic-zero finite linear algebra,
that the 1920 classes in Lentfer's `B_5^(1,2)` form a basis of
`R_5^(1,2)`.  Every trigraded quotient dimension equals the candidate count in
that block.  There is therefore no exact dependency, missing quotient class,
or graded mismatch at `n=5`.

This route proves the basis endpoint in Conjecture 3.2 for the single finite
case `n=5`.  It does not identify an initial-term order for which the
candidates are literally Groebner standard monomials, and it does not prove
the conjecture for arbitrary `n`.

## Source-faithful definitions

The implementation was written from the published paper, independently of
root discovery code.  The pinned source is John Lentfer, *A conjectural basis
for the (1,2)-bosonic-fermionic coinvariant ring*, Algebraic Combinatorics 8
(2025), 711--743, DOI 10.5802/alco.424.  Relevant locations are the ambient
supercommutative algebra and quotient in equation (1) and pages 711--714, the
modified Motzkin paths and Kim--Rhoades weights on page 715, and Definition
3.1/Conjecture 3.2/Remark 3.3 on page 717.

Over `Q`, let

```text
A_n = Q[x_1,...,x_n] tensor Exterior(theta_1,...,theta_n,xi_1,...,xi_n),
R_n = A_n / <(A_n^{S_n})_+>.
```

All 2n fermionic generators mutually anticommute.  The symmetric group acts
diagonally on indices, including the signs introduced when an exterior word
is put back in canonical `theta`-then-`xi` order.

For subsets `T,S` of `{2,...,n}`, put `alpha_1=0` and

```text
alpha_i = alpha_{i-1} - 1 + 1(i not in T) + 1(i not in S).
```

The pair `(T,S)` is a modified-Motzkin-path weight exactly when every
`alpha_i >= 0`; Definition 3.1 then includes all `x^a theta_T xi_S` with
`0 <= a_i <= alpha_i`.  Direct enumeration gives 24, 192, and 1920 candidates
for `n=3,4,5` respectively.

## Finite structural reduction

The elementary symmetric polynomials `e_1,...,e_n` are positive-degree
invariants, so the target quotient factors through

```text
C_n = A_n / (e_1,...,e_n).
```

For lexicographic `x_1 > ... > x_n`, the polynomials

```text
h_i(x_i,...,x_n),  i=1,...,n,
```

form the standard Groebner basis of the symmetric ideal and have leading
monomials `x_i^i`.  Thus `C_n` has the exact monomial basis

```text
x_1^a1 ... x_n^an theta_T xi_S,  0 <= a_i < i,
```

of dimension `n! 4^n`; its maximum polynomial degree is `n(n-1)/2`.
Consequently, the `n=5` computation is a complete 122880-dimensional finite
calculation covering polynomial degrees 0 through 10 and exterior bidegrees
0 through 5.

Because characteristic zero Reynolds averaging is exact, invariants commute
with passing to this equivariant quotient: every invariant of `C_n` is the
image of an invariant of `A_n`.  Reynolds sums of every Artin/exterior basis
state therefore span `C_n^{S_n}`.  If `J` is the ideal they generate, its
trigraded pieces are reconstructed inductively as

```text
J_(d,t,s) = (C_(d,t,s)^{S_n})_+
          + sum_i x_i J_(d-1,t,s)
          + sum_i theta_i J_(d,t-1,s)
          + sum_i xi_i J_(d,t,s-1).
```

This recurrence is complete because the 3n listed elements generate `C_n` as
an algebra.  It also supplies an induction proof that every selected relation
column is an exact element of `J`.

## Exact rank certificate

The standalone verifier is `independent/verify_exact.py`.  It reads only the
small serialized configuration, its own implementation, and the pinned PDF;
it does not import `independent/core.py`, `discover_modular.py`, any root code,
or any discovery output.

For each block with `b>0` candidate columns in an `N`-dimensional ambient
space, Singular computes over `Q`

```text
rank(J generators) = N-b,
rank(selected J columns | B columns) = N.
```

The first equality proves that the ideal has no hidden extra relation on the
candidates; the second proves spanning and independence modulo the ideal.
For a block with `b=0`, the selected `N` columns are literal integer ideal
elements and Singular verifies their `Q`-rank is `N`, which already proves the
whole block is zero in the quotient.

A prime-field sparse eliminator only chooses which literal integer columns to
send to the exact checker.  It supplies no claimed dimension or terminal
conclusion.  In candidate-containing blocks the full generator matrix is
still checked over `Q`, so an unlucky or misleading modular rank cannot close
the endpoint.

## Recorded results

| n | Artin/exterior ambient | blocks | ideal rank sum | quotient | candidates | result |
|---:|---:|---:|---:|---:|---:|:---|
| 3 | 384 | 64 | 360 | 24 | 24 | PASS |
| 4 | 6144 | 175 | 5952 | 192 | 192 | PASS |
| 5 | 122880 | 396 | 120960 | 1920 | 1920 | PASS |

For all 396 `n=5` blocks,

```text
ambient_dimension - ideal_rank_Q = candidate_count,
combined_rank_Q = ambient_dimension.
```

The final uninterrupted `n=5` run took 7637.68 seconds and ended with exit
code 0 and verification-record SHA-256
`a886f61b0a487a72c1b826f5044839ec970e79fe803a82718d9ac2edd3b6a659`.

## Reproduction and negative tests

From the project root:

```bash
python independent/tests/test_fail_closed.py
python independent/verify_exact.py independent/certificate/certificate.json \
  --case 3 --output independent/certificate/exact_n3.json
python independent/verify_exact.py independent/certificate/certificate.json \
  --case 4 --output independent/certificate/exact_n4.json
python independent/verify_exact.py independent/certificate/certificate.json \
  --case 5 --output independent/certificate/exact_n5.json
```

Negative tests reject seven schema/count/hash/prime/case mutations.  A CLI
test with a tampered source hash exits 2 with
`FAIL_CLOSED: ... source PDF missing or SHA-256 mismatch`; see
`independent/logs/fail_closed.log`.

Final environment: Python 3.13.5, SymPy 1.13.3 (not used for decisive rank),
and Singular 4.4.1 with GMP 6.3.0 and FLINT 3.6.0 on arm64 macOS 26.5.

## Frozen hashes

```text
37f6b097ff430f9ea498ae2aaf70013e105d0b6221d642ac147103babe8768ca  source/Lentfer_2025_ALCO424.pdf
5b6349749cd3128f38a5158f5b5e088ef57585ad2a6430d745ab58daca6e604f  certificate/certificate.json
67db9be8adf3ae88d92cab1f5f08df304984a9b220d0050ea2bed5602c794cfa  verify_exact.py
dbcbf9458739a8f38b83f7afbed90978cbbe170f52c65688105e3a23781b0364  certificate/exact_n3.json
c67cfeb22e094235ccddaa37da2263bc27b2efc14262818b5e7e892db0c47d87  certificate/exact_n4.json
a886f61b0a487a72c1b826f5044839ec970e79fe803a82718d9ac2edd3b6a659  certificate/exact_n5.json
5f59cea44baa682178753a102376c7970d1849b159fd6086ba976e27d700777b  logs/exact_n5.log
```

Paths in the hash block are relative to `independent/`, except this notes
file.  The hashes of `verify_exact.py` and `certificate/certificate.json`
match the values embedded in every final exact record.

## Run provenance and limitations

Before the final run, two `n=5` exact attempts were deliberately stopped and
restarted.  The first still formed redundant wide generator matrices for
candidate-free blocks; the second still generated redundant columns after a
full integer ideal basis had already been selected.  The frozen final version
uses the logically equivalent exact optimization described above.  It passed
an all-block `n=3` regression before the final uninterrupted 396-block run.
These stopped attempts are not certificate evidence.

The modular `n=5` scouting job was also stopped after it had served its only
purpose of identifying costly blocks; its partial log is not used by the
verifier and must not be cited as proof.

No Lean, Coq, Isabelle, or other proof assistant was used.  The certificate
is exact rational/integer finite linear algebra checked by Singular.  The
endpoint is precisely `n=5`; no general-`n` recurrence theorem is claimed.
