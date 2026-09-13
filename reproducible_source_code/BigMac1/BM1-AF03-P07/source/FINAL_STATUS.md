# Final status: K-Knuth shape-interval Conjecture 7.6：首个未验证字母规模 \(n=8\)

## `CERTIFIED_FINITE_RESULT`

The first previously unreported finite endpoint passes: every K-Knuth class of
straight increasing tableaux on an ordered alphabet of cardinality at most
eight has an order-convex shape set. In particular, there is no (n=8)
counterexample.

This is not a proof of Conjecture 7.6 for unbounded alphabets. The conjectural
prescribed-cover filling lemma in `proof/structural_reduction.md` is equivalent
to the general statement, but no construction controlling an arbitrary chosen
one-box cover is known.

## Exact certificate

At (n=8), the independent verifier reconstructed:

- 9,069,306 increasing tableaux;
- 6,773,991 initial tableaux;
- 988,384 initial K-Knuth classes;
- 215,295 URTs;
- 148 primitive rules and 1,342,257,288 primitive tests;
- 7,303,139 successful merges and 58,425,112 right-closure tests;
- zero missing intermediate shapes.

Certificate SHA-256:
`8e4bb76e15062fa0d60174d061f4a6f21ab8e934f56938d2e878faddd06f0d61`.
Verifier-source SHA-256:
`34adc8c26207209d039dc7a6452743b2e2711d2b5b742bb706a4b108059ca8b7`.

## Independent audit

The verifier uses shape-first row-major filling, a cellwise 80-bit code,
explicit-grid insertion, generic primitive-rule generation, and
upward/downward shape-closure bitsets. It reads no discovery state,
transition, component, or interval file. The exact (n\le7) baseline was
reproduced. Five malformed/tampered certificates were rejected and one intact
control was accepted.

Gate 1 `NOVELTY_LOCK` passed twice within the scope logged in
`literature/search_log.md`. The bounded conclusion is that no prior public
(n=8) certification was found in those databases, citation records, full
texts, exact-number searches, or public-code searches.

Citation, LaTeX, proof, referee, manifest, and five-page visual PDF audits all
pass. The final PDF is
`output/pdf/k_knuth_shape_interval_n8_certification.pdf`; its SHA-256 is
`befffe6e09fac9d8ac6e5d1c7759fbe74e7f6f65848134ef8fa25a6ecf3c6d8e`.
The source archive is `release/k_knuth_n8_source.zip` and all retained release
files are bound by `release/MANIFEST.json`.

## Reproduction

```sh
sh scripts/verify_n8.sh
python3 tests/test_fail_closed.py
```

The expected terminal markers are
`CERTIFIED_FINITE_RESULT verified_n=0,1,2,3,4,5,6,7,8` and
`FAIL_CLOSED_TESTS_PASS cases=6`.

No Lean, Coq, Isabelle, or other proof assistant was used. Consequently no
formalization claim is made beyond the exact executable certificate described
above.
