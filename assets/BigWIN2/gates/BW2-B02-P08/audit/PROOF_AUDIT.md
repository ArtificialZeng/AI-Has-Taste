# Proof audit

Status: **PASS** (second Referee pass, 2026-08-29).

## Endpoint reconstructed from definitions

For binary rooted leaf-labelled networks in the locked conventions and every
integer \(\ell\ge5\), no finite-degree polynomials \(A,B\in\mathbb Q[x]\)
represent \(\Delta_4(\ell)\) in Batle's proposed two bases. The stronger exact
replacement is
\[
\Delta_4(\ell)=A_0(\ell)(2\ell-3)!!+\frac{15}{16}(2\ell-5)!!
-B_0(\ell)2^{\ell-3}\ell!,
\]
with the displayed \(A_0,B_0\) in `proof/disproof.md` and `paper/main.tex`.

## Fatal/major dependency checks

- Chang--Fuchs Proposition 12 was checked in the published author revision;
  its lower summation limits give the vertex weights used here by an explicit
  index shift.
- Chang--Fuchs Lemma 7 and the exact Gunawan--Rathin--Zhang recurrence justify
  the finite numerator \(N_4\); no fitted asymptotic or floating point value is
  used.
- The decisive coefficient is isolated without a full graph enumeration. All
  non-star component graphs have largest \(X\)-exponent at most 2; the unique
  four-sink star contributes \([X^3]=5/16\).
- The two proposed bases have, respectively, positive odd powers only up to
  \(X^1\), and even powers only. A finite initial correction is a polynomial in
  \(z=(1-X^2)/2\), so the endpoint \(\ell\ge5\) creates no loophole.
- Pons--Batle equation (19d) and the later proof of the Pons--Batle identity
  support the tree-child subtraction.
- Every fatal and major entry in `proof/gap_ledger.md` is resolved.

## Independent exact checks

- SymPy discovery: parent-multiset graph generation, labelled sum divided by
  \(4!\), exact rationals.
- Standard-library verifier: all-topological-order generation, deduplication,
  canonical unlabelling, independently computed automorphism orders, and
  `fractions.Fraction` Laurent arithmetic.
- Third graph-count check: sink-row inclusion--exclusion gives
  \(7935=5\cdot1587\).
- Corrected closed form agrees exactly on \(5\le\ell\le30\); this is a check,
  while the theorem follows from coefficient extraction.
- The conjectured 14-parameter degree-bounded fit misses \(\ell=19\) by the
  exact positive integer \(98075577600000\).

Verification command:

```text
PYTHONHASHSEED=0 python3 code/verify_delta4_certificate.py
```

Result: `PASS`. No proof assistant was used.
