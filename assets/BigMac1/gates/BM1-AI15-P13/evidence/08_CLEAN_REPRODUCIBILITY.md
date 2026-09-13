# Clean release-package reproducibility audit

Audit date: 2026-08-29 (Asia/Shanghai)

Outcome: **PASS.** The final source archive was unpacked into a fresh
`mktemp` directory, and every command below used only the files present in the
archive (apart from the installed compiler, Python, TeX, and Poppler tools).

## Frozen archive

- Path: `output/source/sm_ir_counterexample_source.zip`
- SHA-256:
  `cf351d07c859a591a635d8833f9fbfbef50e164b2b7185628437a83149a846f1`
- ZIP integrity: 31 files tested, zero compressed-data errors.

## Isolated checks

The following all exited zero after extraction:

```bash
python3 verification/verify_stagnation.py certificates/binary64_stagnation.json
python3 verification/verify_stagnation_2x2.py certificates/binary64_stagnation_2x2.json
python3 verification/test_tamper_fail_closed.py
cc -std=c11 -O0 -frounding-math -ffp-contract=off \
  verification/verify_stagnation_hardware.c -lm -o hardware_check
./hardware_check certificates/binary64_stagnation.json
python3 notes/agent_builder_verify.py
python3 breaker_main_verify.py
python3 breaker_verify.py
cd paper && latexmk -C && \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The tamper suite reported `cases=12 all_nonzero=true`. The final LaTeX and
BibTeX logs had no warnings, undefined items, overfull/underfull boxes, or
errors. The isolated PDF had six letter-size pages, no encryption, and no
JavaScript. Its byte hash differed from the frozen PDF because PDF creation
metadata and the trailer identifier are regenerated, but `pdftotext` gave the
same SHA-256 for both files:
`6cdd1a94473d72cf963596776541814ef75a2810c9cc46cf7ec39425136cb06c`.
The regenerated `main.bbl` was byte-identical to the frozen one, SHA-256
`cec906f2ab0638e3462eced1f5ab2b413c7322f4c6c35666a64c6151709c1e71`.

## Environment

- Python 3.14.7
- Apple clang 21.0.0 (`clang-2100.0.123.102`)
- TeX Live 2026, pdfTeX 1.40.29, latexmk 4.88
- Darwin 25.5.0, arm64

The temporary extraction was intentionally left outside the project tree at
`/tmp/sm-ir-release.zcudkL` for immediate forensic inspection; it is not part
of the release manifest.
