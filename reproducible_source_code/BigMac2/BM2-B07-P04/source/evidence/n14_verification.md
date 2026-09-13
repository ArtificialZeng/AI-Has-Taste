# Exact verification of the finite `n=14` layer

## Result and exact scope

In the polynomial-basis model

\[
K=\mathbb F_2[\alpha]/(\alpha^{14}+\alpha^5+1),
\qquad
\sum_{i=0}^{13}b_i\alpha^i\longleftrightarrow
\sum_{i=0}^{13}b_i2^i,
\]

the exhaustive integer computation proves the frozen assertion in `source.md`:
for each \(k\in\{3,5\}\), \(|\Delta_k|=8192\), and for every one of the
16,382 encodings \(\rho\in K\setminus\{0,1\}\),

\[
N_k(\rho)=33{,}554{,}432=2^{25}.
\]

This is only the finite \(n=14\), \(k=3,5\) layer. It makes no assertion for
arbitrary \(n\). Since the statement is invariant under field isomorphism, one
certified model of the unique field of order \(2^{14}\) suffices.

## Why the certificate proves the count

`verify_n14.c` performs the following exact steps.

1. It applies Rabin's irreducibility criterion to
   \(p(X)=X^{14}+X^5+1\). Modulo \(p\), the recorded remainders are
   \(X^{2^2}=\mathtt{0x0010}\),
   \(X^{2^7}=\mathtt{0x08c5}\), and
   \(X^{2^{14}}=\mathtt{0x0002}=X\); the gcds of the first two remainders plus
   \(X\) with \(p\) are both 1. These are precisely the checks associated to
   the prime divisors 2 and 7 of 14.
2. It enumerates all 16,384 encoded inputs to each map
   \(t\mapsto t^{d_k}+(t+1)^{d_k}+1\), for \(d_3=57\) and \(d_5=993\).
   Each image contains exactly 8192 values; more strongly, every image value
   has exactly two preimages.
3. It computes, with an integer Walsh--Hadamard transform and the explicitly
   constructed trace-pairing dual map, every coefficient
   \(S_k(a)=\sum_{x\in\Delta_k}(-1)^{\operatorname{Tr}(ax)}\).
4. Additive-character orthogonality gives

   \[
   2^{14}N_k(\rho)=
   \sum_{a\in K}S_k(a)S_k(a\rho)S_k(a(1+\rho)).
   \]

   `n14_certificate.tsv` contains all 16,384 coefficients for each \(k\),
   followed by the sum for every admissible encoded \(\rho\). In every one of
   the 32,764 count rows, the contribution from \(a\ne0\) is exactly zero.
   The \(a=0\) contribution is
   \(8192^3=549755813888=2^{39}\); division by \(2^{14}\) therefore gives
   \(2^{25}\) exactly.

There is no floating-point arithmetic in either implementation or in the
certificate.

## Separate implementation checks

`audit_n14.c` does not reuse the producer's primitive generator, logarithm
table, shift-and-reduce multiplication, or Walsh transform. It instead:

- proves irreducibility by testing all 127 monic constant-one possible factors
  of degrees 1 through 7 and finding no divisor;
- multiplies by forming a carryless polynomial product and applying long
  division by `0x4021`;
- reconstructs both Delta sets and all 32,768 saved Walsh coefficients by
  direct character summation;
- recomputes all 32,764 saved correlations through polynomial-basis linear
  multiplication maps; and
- directly enumerates \(8192^2\) pairs for each \(k\) at the held-out encodings
  `rho=0x1555` and `rho=0x3ffe`.

Every comparison passed. The producer separately directly enumerates the
counts at `rho=0x0002` and `rho=0x2000` for both \(k\)'s. AddressSanitizer and
UndefinedBehaviorSanitizer runs of both implementations were clean, and a
sanitized producer run generated a certificate byte-identical to the saved
one. These implementation checks are not a fresh mathematical referee pass.

## Reproduction

From the project directory:

```sh
cc -std=c11 -O3 -Wall -Wextra -Wpedantic \
  evidence/verify_n14.c -o evidence/verify_n14
./evidence/verify_n14 evidence/n14_certificate.tsv

cc -std=c11 -O3 -Wall -Wextra -Wpedantic \
  evidence/audit_n14.c -o evidence/audit_n14
./evidence/audit_n14 evidence/n14_certificate.tsv
```

The recorded run used Apple clang 21.0.0 on `arm64`. Decisive SHA-256 values:

```text
ad1b1a9988509a06970cb4c361e84510b2f825f390b56d9ca9b8942bf080b8b1  source.md
c85ec5bc9cb35bbd29198a5478c2c379e7bf73ed5a12ea4cf0a84c125f18a557  problem.md
b374b1559b3dbb57c54257ed0d9948a3308192f60dfa7fc65ad64bf9e23d5e5c  evidence/verify_n14.c
cdeea1311397f87ddf8909f130ab607544fa7b9a56163cdd439c5c1faf7e75c1  evidence/audit_n14.c
7f8d716a216aab3da464a26cbcb027060adcba50718762059ccd636ce7ae3d69  evidence/n14_certificate.tsv
ce17a9e9e6d91576c00426d150d873b03060dcf5a382ef5c9a7d11ea7bd68eec  evidence/n14_run.log
b76f50d62e8d6071129c8a9cdc5d90dea1a9de161fbb22981d345c199249d1e2  evidence/n14_audit.log
```
