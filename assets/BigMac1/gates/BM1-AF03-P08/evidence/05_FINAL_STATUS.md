# Final status: CERTIFIED_FINITE_RESULT

## Conclusion

For every comparable pair

\[
e\le u\le v\le v_{10}=[3,4,5,6,7,8,9,10,1,2],
\]

the exact finite verifier certifies

\[
\widetilde R_{u,v}(q)
=q^{\ell(v)-\ell(u)}\prod_i F_{h_i}(q^{-2}),
\qquad h_i\ge2.
\]

The interval contains 12,866 elements and 6,229,297 comparable ordered
pairs.  Every pair passes.  Thus the first endpoint not covered by the source
authors' reported computation, $n=10$, is certified; no counterexample occurs
there.

The verifier also certifies, for each $2\le n\le10$, that the set of observed
normalized polynomial classes is exactly the set of products indexed by
nondecreasing $h_i\ge2$ with $\sum_i h_i\le n-2$.  At $n=10$ there are 22
such classes and the maximum coefficient is 15.

## Scope and limitation

This is a complete theorem for the finite $n=10$ endpoint, not a proof of the
conjecture for arbitrary $n$.  Support multiplicativity and a capped-ladder
reduction are proved, but the proposed path-forest and disjoint-footprint
lemmas needed for an all-rank block explanation remain open.  Two recorded
novelty searches found no public resolution or duplicate $n=10$ result as of
2026-08-29; this is deliberately a bounded search claim, not proof of global
absence.

## Certificate and independent audit

- Verifier source SHA-256:
  `32fb92211a14e2db30ea54ade3a4713d0f2d7e5f9c43c63b501c90c0ee29a8c8`
- Serialized certificate SHA-256:
  `f04e1eda7610261b15c3a25f60707b6ea7e68d44c40b2c045c54b4a42baa513e`
- Rejection-test SHA-256:
  `3b83afc530210065d4b116572e21f6b0537a3af452526e5206009cbcc909b9e8`
- Deterministic $n=10$ fingerprint: `0x78cf5914f6aaeb37`

The standalone verifier does not import discovery polynomials or pair lists.
It reconstructs the full interval twice (rank matrices and subwords), scans
all comparable pairs, evaluates both the normalized Dyer recurrence and the
ordinary $R$ recurrence, and compares them through an exact change of
variables.  The complete Fibonacci multiplicative monoid is regenerated.
Eight altered certificates are rejected fail closed.  The latest-hash
independent referee rerun, a separate breaker implementation, a Python
cross-check through $n=8$, and UBSan executions all pass.

## Literature, build, and artifacts

The original source statement is preserved in `problem/source_statement.md`,
and the corrected quantified endpoint is in `problem/formal_statement.md`.
Gate 1 and the second novelty pass are recorded in
`literature/NOVELTY_LOCK.md`, `literature/claim_ledger.md`, and
`literature/search_log.md`.  All five bibliography entries were individually
checked against primary/official records.  The final LaTeX build is clean:
no undefined citations or references, BibTeX warnings, LaTeX errors, or box
overflow/underflow warnings.  All seven PDF pages were rendered and visually
inspected.  The PDF metadata and text contain only the required author,
affiliation, and email addresses.

Release artifacts:

- `output/pdf/kl_r_fibonacci_n10.pdf`
- `output/source/kl_r_fibonacci_n10_source.zip`
- `release_manifest.json`

## Reproduction

From the project root:

```sh
python3 certificates/verify_certificate.py
python3 tests/test_certificate_rejection.py
(cd paper && latexmk -C main.tex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex)
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py paper/main.tex --aux paper/main.aux
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py paper/main.tex paper/references.bib
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py . release_manifest.json
```

## Proof-assistant declaration

No Lean, Coq, Isabelle, or other proof assistant was used.  No formalization
claim is made.  The certified theorem endpoint is bound only to the exact
finite specification and verifier described above.
