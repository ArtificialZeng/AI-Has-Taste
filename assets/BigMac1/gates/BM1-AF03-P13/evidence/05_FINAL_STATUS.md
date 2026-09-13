# Final status: DISPROVED

Terminal date: 2026-08-29 (Asia/Shanghai).  The original prompt is complete.

## Conclusion

The coherent actual-length form of the generalized-snake Ehrhart root-disk
conjecture is false.  For the length-10 regular word

```text
epsilon LRLRLRLRLR
```

the order polytope has dimension 24, symmetry center `-7`, and conjectured
radius `6`, yet its Ehrhart polynomial has roots satisfying `|t+7|>6`.

The printed source display has both a center-sign conflict and an off-by-one
length parameter.  The endpoint certified here is the repair specified by the
user and forced by the source definition, fixed roots, and functional equation:

```text
word length m, center -(m+4)/2, radius (m+2)/2.
```

`NOVELTY_LOCK = PASS_WITH_STATEMENT_REPAIR`.  The current arXiv v2 retains
Conjecture 5.1.  Braun--Jal prove only its h-star real-rootedness part.  The
recorded pre-result and result-fingerprint searches through the terminal date
found no earlier disk proof, counterexample, or certificate.  This is a bounded
search conclusion, not a claim of absolute priority.

## Main exact certificate

Direct source-cover reconstruction and enumeration of 13,860 linear extensions
gives

```text
h* = [1,21,181,833,2241,3653,3653,2241,833,181,21,1].
```

The vector independently agrees with the source's regular-snake Delannoy
formula.  Integer arithmetic gives

```text
24! L(x-7) = 36 prod_{k=0}^6 (x^2-k^2) Q(x^2),
Q(y) = 385y^5+25789y^4+923223y^3+10769815y^2
       +70801492y+23924096.
```

A rational Rouché disk centered at `-53/2+29i` with radius `1/6` has strict
margin `177200631815/7776` and lies strictly outside `|y|=36` by separator
`2117/9`.  It contains exactly one algebraic root of `Q`, proving the strict
Ehrhart-disk violation without floating-point roots.

Frozen pair:

- certificate `experiments/breaker_counterexample_certificate.json`:
  `d74f094ca5e9829a4f6e7f12298e81557081dc153bc690cf57016dd0b5eeae68`
- verifier `discovery/breaker_verify_counterexample.py`:
  `7bcdf9e26c09493c2c81295f181821394ea41d0d8a7572ace60084f0a9b6bb73`

## Independent no-import audit

A six-field input is independently expanded from Definition 2.2: the verifier
rebuilds the cover relations, 46 order ideals, multichain Ehrhart values, every
h-star coefficient, the factorization, a Cayley polynomial, and an exact Routh
table.  Its Routh first column has signs `+ + + + - +`, hence exactly two
right-half-plane roots.  Positivity excludes positive real roots, so a nonreal
conjugate pair maps to `|y|>36`.

- input `certificates/routh_audit_input.json`:
  `5327157faf71ed22bbd968f317aa8a452909343751ced9e0da65cb92066c8fac`
- portable verifier `audit/independent_routh_verifier.py`:
  `a7ec89fe7b3597c77e97b805a7bf31848f8e3eb3ee4eb575e639adae1d2d8275`

The portable verifier passes under both Anaconda Python 3.13 and system Python
3.14.  Its mutation suite rejects 8/8 corruptions.  The primary length-10 suite
also rejects 8/8.

## Baseline reproduction and additional result

The full unquotiented exact scan covers every literal word of lengths 0 through
10.  Its outside counts are `0` for every length 0--8, `2` for length 9, and
`6` for length 10.  The original and Anaconda runs have identical mathematical
fields:

- `experiments/exact_scan_length0_10.json`:
  `8923c092e82f5668b09864068d711a16c6c228d3f645911c9fa6bd91ab7ae783`
- `experiments/exact_scan_length0_10_anaconda.json`:
  `105cd3681242d71e058b8700b94b306071df73bab094b3abf1bef09ebe2d57e0`

Thus the authors' reported length-at-most-9 baseline is not reproduced under
the repaired convention.  The regular length-9 word `epsilon LRLRLRLRL` has a
separate reconstructing Rouché certificate, strict margins, and an 8/8
rejection suite:

- certificate:
  `a7a3f1b78ed81b2817894ac16ee60fe16ccd97366dbdeddfa9695018edd44cf5`
- verifier:
  `f3abc48b63e7f4f0be49c0b55d71c9d654fae376c4c1ec61b6d26fcb7c0e38ed`

Length 10 remains the main theorem requested by the project.  The exact scan
does not replace the separate witness proofs.

## Audits and deliverables

- `audit/PROOF_AUDIT.md`: PASS
- `audit/CITATION_AUDIT.md`: PASS; 3/3 bibliography identities and 13/13
  frozen claim checks
- `audit/PDF_AUDIT.md`: PASS; clean six-page build and visual inspection of
  every page
- `paper/main.pdf`: SHA-256
  `97bc0949eca16e0225e89b21ec451b5de92df66878900d4fcd24000e05bf0b55`
- `release/snake_ehrhart_counterexamples_source.zip`: internal 42-file
  manifest verified, all decisive verifiers rerun from the isolated archive,
  ZIP SHA-256
  `b91156ab73352eefd7d184abd38e9745adf7f611c88e958411e9cc73057d5d55`
- `manifests/PROJECT_MANIFEST.sha256.json`: frozen-artifact manifest, verified
  from the project root after all terminal files were written

The paper author is Zijian Zeng.  The required UCSI University affiliation and
both required email addresses were checked in LaTeX source, extracted PDF text,
and PDF metadata.

## Reproduction

From the project or extracted source-archive root:

```bash
/opt/anaconda3/bin/python -I -B discovery/breaker_verify_counterexample.py experiments/breaker_counterexample_certificate.json
/opt/anaconda3/bin/python -I -B audit/independent_routh_verifier.py certificates/routh_audit_input.json
/opt/anaconda3/bin/python -I -B discovery/breaker_length9_verify_counterexample.py experiments/breaker_length9_counterexample_certificate.json
/opt/anaconda3/bin/python -B discovery/breaker_test_rejections.py
/opt/anaconda3/bin/python -B tests/test_independent_routh_verifier.py
/opt/anaconda3/bin/python -B discovery/breaker_length9_test_rejections.py
```

## Limitations and formal-method disclosure

No claim is made that length 9 is the first failing length, that reversal is a
general poset symmetry, that the six length-10 scan hits form a theorem-level
classification, or that the recorded database search proves absolute
priority.

No Lean, Coq, Isabelle, or other proof assistant was used.  No formalization is
claimed.  The actual theorem endpoints are covered by exact, fail-closed Python
verifiers using finite enumeration, integer/rational arithmetic, Rouché's
theorem, and the Routh theorem.
