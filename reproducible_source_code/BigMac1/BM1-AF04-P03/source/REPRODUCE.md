# Reproduction guide

Run commands from the project root with Python 3. A C++20 compiler is needed
only for fresh replay; ordinary certificate verification uses the serialized
results.

## Short decisive checks

```sh
python3 code/verify_packing_certificate.py \
  certificates/packing12.json --expected-blocks 12
python3 code/verify_global_fixed_cover.py
```

Expected decisive facts:

- positive: 12 base blocks, 372 developed blocks, 3,720 distinct triples;
- negative:
  `{"branches":162,"covered_block_variables":4761,"status":"VERIFIED_GLOBAL_TARGET13_UNSAT"}`.

## Fail-closed regression checks

```sh
python3 tests/test_positive_verifier.py
python3 tests/test_fixed_clique_certificate.py
python3 tests/test_global_fixed_cover.py
python3 tests/test_negative_certificate.py
```

The tests include malformed and semantically corrupted certificates that must
be rejected.

## Full exact-model regression suite

```sh
python3 tests/test_enumeration.py
python3 tests/test_sat_encoding.py
python3 tests/test_exact_cover_encoding.py
python3 tests/test_opb_model.py
python3 tests/test_leave_opb_model.py
python3 tests/test_leave_patterns.py
python3 tests/test_multiplier_orbits.py
python3 tests/test_fixed_reductions.py
python3 tests/test_pattern_big_m.py
```

## Fresh search replay

One fixed branch can be rebuilt and replayed with:

```sh
python3 code/verify_fixed_clique_certificate.py \
  certificates/negative/fixed537_finite_manifest.json --rebuild-rerun
```

All 162 branches can be rebuilt and replayed with:

```sh
python3 code/verify_global_fixed_cover.py --rebuild-rerun
```

This rerun reproduces 68,377,851,660 branching nodes and can take substantial
CPU time. Runtime is not a proof premise; exact completion and accepted
outputs are.

## Paper build and artifact checks

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py \
  main.tex --aux main.aux
pdfinfo main.pdf
```

The released PDF and compact source archive are in `output/pdf/` and
`output/source/`. Their hashes are recorded in `FINAL_STATUS.md` and
`audit/PDF_AUDIT.md`.
