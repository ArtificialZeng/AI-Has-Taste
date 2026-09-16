# win-00079-p03 — covariance separation of the Lemma 7 MIMO sample family

## Immutable primary-source record

- Yang Li, *Has MIMO decoding been proved hard from lattice problems?*,
  arXiv:2609.05013v1.
- Official HTML: <https://arxiv.org/html/2609.05013v1>
- Official PDF: <https://arxiv.org/pdf/2609.05013v1>
- Local full text: `bigWin-79-materials/2609.05013.pdf`, SHA-256
  `98232771ee18abfc54e045df832ca91ae0d4ae5df34c4c10ca645c26a6466eca`.
- Primary construction under audit: T. Dean and A. Goldsmith,
  *Physical-Layer Cryptography Through Massive MIMO*, arXiv:1310.1861,
  Eq. (19) and the published Lemma 7. Local PDF
  `bigWin-79-materials/1310.1861.pdf`, SHA-256
  `d43826d974e494e06703c805546e98422d417ae02e6e6f4f7e1fc04382ec207b`.
- Locators in arXiv:2609.05013v1: Definition 2.9, Lemma 7 and Proposition
  5.1 (PDF pp.5, 9--10), Remark 5.3 (PDF p.11).

## Frozen assertion

For every sufficiently large integer `n`, set

```
epsilon = 2^(-n), L = Z^n, A = I_n,
r = k = n^2, alpha = 1/2, m = 3n^5,
```

and choose an integer

```
M > m * 2^(n log(log n)/log n).
```

Let `c=2M*1`, `delta=e_1/4`, and `y=c+delta`. Prove or disprove that this is
a valid BDD instance under every promise used by the Dean--Goldsmith Lemma 7
construction and that polynomially many resulting samples can be
distinguished, with overwhelming probability, from every legal
`D_(M,beta,k)` discrete-MIMO distribution with
`s in [0,M)^n intersect Z^n` and `0<beta<=alpha`.

The claim concerns joint sample distributions for this explicit family. It
does not claim an attack on general MIMO decoding or a hardness result.

## Nearest result and exact delta

Proposition 5.1 of arXiv:2609.05013v1 proves the constructed conditional law
is not exactly a legal discrete-MIMO law whenever the BDD coefficient lies
outside the constellation or the offset is nonzero. Remark 5.3 says it could
still be negligibly close in restricted instances, while the published proof
does not establish closeness for arbitrary targets. The target supplies one
fully explicit admissible family and asks for a polynomial-time constant-gap
statistical separator.

## Cheapest decisive attack and certificate

For the frozen parameters, `a=v` has law `D_(Z^n,n^2)`. Put
`X=sum_j a_j`. The constructed response is expected to obey

```
b = 2X + a_1/(4M) + e,
E[Xb]/E[X^2] = 2 + 1/(4Mn) > 2.
```

For every legal discrete-MIMO secret `s`, independence and coordinate
symmetry instead predict

```
E[Xb]/E[X^2] = (1/n) * sum_j (s_j/M) < 1.
```

Use the empirical statistic

```
theta_hat = sum_i X_i*b_i / sum_i X_i^2
```

with threshold `3/2`. A complete positive certificate must verify the
smoothing-parameter inequality, constellation and Lemma 7 bounds, the BDD
distance and uniqueness promise, the exact moment identities, and a uniform
tail bound showing that a polynomial number of independent samples gives
negligible failure probability for every legal `s,beta`. It must account for
the random denominator rather than divide expectations informally.

A negative certificate must point to a failed source promise or exhibit a
legal comparison law for which the statistic does not provide the asserted
uniform overwhelming separation. Exact non-equality alone is insufficient.
