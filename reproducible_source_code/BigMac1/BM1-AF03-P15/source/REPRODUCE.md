# Reproducing the certified `D_9` result

All commands below are run from the release root.  Python 3.10 or later is
sufficient; the decisive verifiers use only the standard library.

## Exact theorem checks

Primary frozen certificate and verifier:

```bash
python3 -I -S certificates/verify_d9_flow.py \
  certificates/d9_normalized_flow.json
```

Independent no-import full-DAG referee, including nine corruption tests:

```bash
python3 -I -S audit/referee_verify_d9.py
```

Expected terminal fields are respectively `"result":"VERIFIED"` and
`"status":"VERIFIED"`.  The referee output must also list all nine
mutations as `REJECTED`.

The authoritative roles and hashes are in
`certificates/PRIMARY_D9_BINDING.json`.  In particular:

- primary certificate SHA-256:
  `d8fe947906c577f3a7c585fc07e0bcb6648e2555056a756af98bf307ab72ea7f`;
- primary verifier SHA-256:
  `a076f7dc4a715d0adb9d1c7b7946431a7f63de744b53a8782a6c50ed7580c706`;
- formal statement SHA-256:
  `a423a584b8a229845dc64dbca6233df9d7d36ca7d9a0c1a5de55571d54aca084`.

The alternative certificate under `discovery/` is cross-check-only and must
not replace the primary pair.

## Regression checks

These tests remain within the published baseline and target range `D_4` to
`D_9`; they do not run any `n>9` instance.

```bash
python3 -m unittest tests.test_verify_d9_flow tests.test_breaker_crosscheck
```

## Manuscript build and audits

With TeX Live, build from a clean directory:

```bash
mkdir -p build
cd paper
env SOURCE_DATE_EPOCH=1788000000 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -file-line-error -outdir=../build main.tex
cd ..
```

Then run:

```bash
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py \
  paper/main.tex --aux build/main.aux
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py \
  paper/main.tex paper/references.bib --log build/main.log
```

The published PDF was built with the same deterministic timestamp variables.
Its SHA-256 is
`c8741981935f22594dcc944e2981b166b1084f58cf6d59c455ecb9f02c08d184`.

## Scope

These commands certify only that `Abs(D_9)` admits a normalized flow with
unit vertex weights.  They do not prove a recurrence or the conjecture for
all `D_n`.  No proof assistant was used.
