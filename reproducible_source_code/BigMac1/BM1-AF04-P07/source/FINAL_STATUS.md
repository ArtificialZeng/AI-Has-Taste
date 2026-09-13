# Final status

## Terminal classification

`CERTIFIED_FINITE_RESULT`

`original_prompt_complete = true`

## Conclusion

For every tournament `T` on 11 vertices, `nu_3(T) >= 15`.  A cyclic
three-part tournament with parts of sizes `4,4,3` has packing number exactly
15.  Therefore

```text
nu_3(11) = 15.
```

This determines only the requested finite endpoint.  It does not classify
all minimizers and makes no claim for `n >= 12` or for the full Yuster
conjecture.

## Exact proof and certificate chain

1. `code/burnside_count.py` evaluates Davis's formula with exact
   `fractions.Fraction` arithmetic and returns 903,753,248 unlabeled
   tournaments at order 11.
2. nauty 2.9.3 `gentourng` generated a complete 192-residue partition.  The
   Builder accepted every representative with a target-15 exact
   pair-resource search.  Aggregate:
   `certificates/n11_builder_full_m192.json`.
3. A separately written Certifier regenerated all 192 streams, recomputed
   transitivity by internal outdegrees, and solved the different exact
   compatibility-clique formulation.  Aggregate:
   `certificates/n11_certifier_full_m192.json`.
4. `certificates/n11_sweeps_match.json` records exact total 903,753,248,
   `matching_slices=192`, equality of every slice count and stream SHA-256,
   and distinct scanner executable hashes.
5. `certificates/minimizer_11.json` gives the literal upper-bound tournament
   and a 15-packing.  `code/verify_minimizer.py` independently verifies 45
   distinct witness pairs, the cyclic cross-part orientation, all 15
   within-part hitting pairs, and all 117 transitive triples.

Key SHA-256 values:

```text
gentourng
4ab5521c4f311336d1c06d9eb253ed91edda918b90b9a2da1257710bf1b4e113
builder_scan
73da948b944358b1282d89a848edae0be34e1ba1477775345d243ed3c24e111a
certifier_scan
f7d2f914b52f1ddc0396671723b02ca2ce03605b91a72d1fa1beeac5ba5c9157
Builder aggregate certificate
dfd409434c400a52e146e0908226c90a70c4dd5784d18170eb054cea7a1112da
Certifier aggregate certificate
19c9c393b693d7844d3b3bbba216709e04e95d6e7ab099ae86da65ac565ae98a
explicit minimizer certificate
0ba6795a77cc37aef8d98a87040e1160da94efc6dd583b15d8cc0be03611681d
final PDF
715bc1f928b608988d528b234c3ec16ecd1ed3ecfdb0bc9997cd3fb0624ed5f2
```

Search-node totals (reported only for reproducibility, not as proof) were
14,481,704,095 for Builder and 16,972,027,052 for Certifier.  Their largest
single-instance counts were 90,842 and 203,790 respectively.

## Independent and adversarial audit

- Complete small-order baselines `n=3,...,8` passed in both programs with
  exact class totals and matching stream digests.
- The published 2026 frontier at `n=9,10` was independently reproduced by
  both programs and bound by two sweep-match certificates.
- All 32 cyclic `4+4+3` within-part variants and 100,000 seeded random labeled
  tournaments passed both target searches; these diagnostics are not used as
  the universal proof.
- A full exact maximum search on the literal minimizer returned 15.
- AddressSanitizer and UndefinedBehaviorSanitizer passed both scanners on all
  6,880 canonical order-8 inputs.
- Twenty-one deliberately corrupted inputs were rejected across the literal
  minimizer verifier, scanners, sweep aggregator, and sweep comparator.
- The Referee reconstruction is `audit/PROOF_AUDIT.md`.  Builder, Breaker,
  Certifier, and Referee records were produced serially; no subagents were
  used, as required by the execution contract.

## Literature and publication audit

Gate 1 `NOVELTY_LOCK`, a post-Builder search, and a post-certification exact
result search are recorded in `literature/search_log.md`.  No earlier public
determination of `nu_3(11)` was located as of 2026-08-30; this is a bounded
search conclusion, not an absolute priority theorem.

All six bibliography entries and all 30 frozen manuscript claims passed the
two-pass citation audit.  A clean LaTeX/BibTeX build has no undefined
citation/reference, missing/unused key, warning, overfull/underfull box, or
fatal condition.  Every one of the seven PDF pages passed visual inspection.
The PDF metadata, body, and LaTeX contain only:

```text
Zijian Zeng
Institute of Computer Science and Digital Innovation,
UCSI University, Kuala Lumpur, 56000, MALAYSIA
zijianzeng@foxmail.com
1002266693@ucsiuniversity.edu.my
```

Publishable artifacts are `output/pdf/nu3_11_certified.pdf` and
`release/nu3_11_source.zip`.  The source archive contains its own individual
file manifest; `release/MANIFEST.json` binds the final PDF and source archive.

## Trusted base and proof assistant disclosure

The substantive external trust assumption is that the pinned nauty 2.9.3
`gentourng` executable emits exactly one representative of every tournament
isomorphism class.  This is supported by all residues, exact smaller totals,
the exact order-11 Burnside total, and independent stream regeneration, but is
not formally proved here.  Remaining trusted components are the C compiler,
Python interpreter, macOS process/integer semantics, and SHA-256 for integrity
binding.

No proof assistant was used.  No floating-point calculation, modular
surrogate, optimizer failure, SAT solver result, wall-clock duration, or PDF
count is treated as mathematical proof.

## Clean replay

From the project root on the recorded environment:

```sh
make -C code
python3 code/burnside_count.py
python3 tests/test_small_baseline.py
code/run_sweep.sh builder 11 15 192 12 \
  903753248 n11_builder_full_m192
code/run_sweep.sh certifier 11 15 192 24 \
  903753248 n11_certifier_full_m192
python3 code/compare_sweeps.py \
  certificates/n11_builder_full_m192.json \
  certificates/n11_certifier_full_m192.json \
  certificates/n11_sweeps_match.json
python3 code/verify_minimizer.py certificates/minimizer_11.json
python3 tests/test_fail_closed.py
python3 tests/test_sweep_fail_closed.py
python3 tests/test_compare_fail_closed.py
cd paper && latexmk -C main.tex && \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Manifest replay commands are:

```sh
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py \
  release/source_tree release/source_tree/MANIFEST.json
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py \
  release/final release/MANIFEST.json
unzip -t release/nu3_11_source.zip
```
