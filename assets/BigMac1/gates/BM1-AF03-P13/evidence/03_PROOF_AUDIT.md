# Proof audit

Audit date: 2026-08-29.  Terminal endpoint under review:

> The corrected universal length-10 disk assertion is false; the word
> `LRLRLRLRLR` has an Ehrhart root outside ​\(|t+7|\le6\).

## Source and quantifier audit

- The original source statement was retained in `problem/source_statement.md`.
- `problem/formal_statement.md` fixes the literal universe of 1024 words, the
  actual word-length convention, dimension 24, complex-root quantifier,
  algebraic multiplicity, closed boundary, fixed roots, and degenerate cases.
- Independent referee reconstruction agrees that the printed conjecture has
  both a center-sign error and an off-by-one length error.
- The result attacks exactly the user-adopted repaired endpoint.  It does not
  pretend to disprove the malformed literal positive-center display.

## Primary exact certificate

Input: `experiments/breaker_counterexample_certificate.json`  
Verifier: `discovery/breaker_verify_counterexample.py`

The verifier uses only the Python standard library and does all of the
following from the literal witness word:

1. rebuilds the recursive source cover relation on 24 vertices;
2. constructs a natural labelling and enumerates all 13,860 linear extensions;
3. reconstructs the stated (h^*)-vector and (24!L(t));
4. checks
   \[
   24!L(x-7)=36\prod_{k=0}^{6}(x^2-k^2)Q(x^2)
   \]
   coefficient by coefficient;
5. recomputes every Gaussian-rational Taylor coefficient at
   (-53/2+29i);
6. verifies squared-norm upper/lower bounds and the strict Rouché margin
   (177200631815/7776>0);
7. verifies the strict separator (2117/9>0).

Therefore an algebraic (Q)-root satisfies ​\(|y|>36\), and either square
root yields an Ehrhart root with ​\(|t+7|>6\).  No decimal participates.

## Independent no-import audit

Input: `certificates/routh_audit_input.json` contains only schema, word,
length, dimension, center, and radius.  
Verifier: `audit/independent_routh_verifier.py`.

This verifier imports no discovery module or data.  It enumerates 46 order
ideals, counts multichains to obtain (L(0),\ldots,L(24)), finite-differences
those values to (h^*), rebuilds the factorization, and applies an exact
Cayley transform.  Its rational Routh first column has signs

```text
+ + + + - +
```

and no zero pivot or zero row, so there are exactly two right-half-plane
roots.  Positivity of every Cayley-polynomial coefficient excludes a positive
real root; hence the two are a conjugate pair.  The exact identity

\[
\operatorname{Re}\frac{y+36}{y-36}
=\frac{|y|^2-36^2}{|y-36|^2}
\]

maps them to a conjugate (Q)-pair with ​\(|y|>36\).  This independently
reaches the terminal endpoint by a different evaluator and root theorem.

## Baseline contradiction

`discovery/breaker_length9_verify_counterexample.py` independently rebuilds
the 22-vertex regular snake, enumerates 5,741 linear extensions, checks the
quartic factor and a rational Rouché disk centered at (-82+91i) of radius
(1/2).  The Rouché margin is (36899552259/16>0), and the whole disk is
outside ​\(|s|=121\) by the separator (971/4>0).  This proves failure no
later than length 9 and explains why the reported baseline could not be used
as an axiom.

The unquotiented exact scan `src/discover_snake_roots.py` was also run through
all literal words of lengths 0 through 10.  Its mathematical fields report
outside counts

```text
m=0,...,8: 0;  m=9: 2;  m=10: 6.
```

The original run (`experiments/exact_scan_length0_10.json`, SHA-256
`8923c092e82f5668b09864068d711a16c6c228d3f645911c9fa6bd91ab7ae783`)
and the `/opt/anaconda3/bin/python` rerun
(`experiments/exact_scan_length0_10_anaconda.json`, SHA-256
`105cd3681242d71e058b8700b94b306071df73bab094b3abf1bef09ebe2d57e0`)
agree in schema, method, maximum length, every length summary, and preferred
witness.  Runtime metadata alone differs.  This is exact baseline/search
evidence; the separately reconstructing length-9 and length-10 certificates,
not the scan record, support the manuscript's theorems.

## Adversarial and boundary checks

- Primary length-10 mutation suite: accepted witness; rejected 8/8 corruptions.
- Independent Routh mutation suite: accepted witness; rejected 8/8 corruptions.
- Length-9 mutation suite: accepted witness; rejected 8/8 corruptions.
- The independent Routh verifier passed under both Anaconda Python 3.13 and
  system Python 3.14; the portability-only `bin(ideal).count("1")` version is
  the hash-bound version below, and `py_compile` passed.
- Strict JSON key sets, exact Python `int` type checks, positive rational
  denominators, pinned endpoints, and recomputed arrays make the verifiers fail
  closed for the tested attack classes.
- The target disk is closed, and both certificates prove strict separation;
  there is no numerical tolerance or unclassified boundary event.
- Reversal symmetry and exhaustive search completeness are not used in the
  theorem.

## Hash-bound audited artifacts

| Artifact | SHA-256 |
|---|---|
| length-10 Rouché certificate | `d74f094ca5e9829a4f6e7f12298e81557081dc153bc690cf57016dd0b5eeae68` |
| length-10 Rouché verifier | `7bcdf9e26c09493c2c81295f181821394ea41d0d8a7572ace60084f0a9b6bb73` |
| independent Routh input | `5327157faf71ed22bbd968f317aa8a452909343751ced9e0da65cb92066c8fac` |
| independent Routh verifier | `a7ec89fe7b3597c77e97b805a7bf31848f8e3eb3ee4eb575e639adae1d2d8275` |
| length-9 Rouché certificate | `a7a3f1b78ed81b2817894ac16ee60fe16ccd97366dbdeddfa9695018edd44cf5` |
| length-9 Rouché verifier | `f3abc48b63e7f4f0be49c0b55d71c9d654fae376c4c1ec61b6d26fcb7c0e38ed` |

## Formal methods disclosure

No Lean, Coq, Isabelle, or other proof assistant was used.  The result is a
computer-assisted exact proof using direct finite enumeration, integer and
rational arithmetic, Rouché's theorem, and the Routh theorem.  No
formalization is claimed beyond these executable endpoint verifiers.

## Verdict

`PROOF_AUDIT = PASS`.  No unresolved critical or major gap remains for
`DISPROVED`.  Nonclaims are: absolute priority, minimal failing length, a
general reversal symmetry, and an all-words classification of outside roots.
