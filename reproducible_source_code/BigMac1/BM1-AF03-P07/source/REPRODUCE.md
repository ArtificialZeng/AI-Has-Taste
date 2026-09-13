# Reproduction

From the project root:

```sh
sh tests/test_discovery.sh
sh scripts/verify_n8.sh
python3 tests/test_fail_closed.py
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cd ..
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py \
  paper/main.tex --aux paper/main.aux
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py \
  paper/main.tex paper/references.bib
```

Expected verifier prefix:

```text
CERTIFIED_FINITE_RESULT verified_n=0,1,2,3,4,5,6,7,8
```

Expected adversarial-test output:

```text
FAIL_CLOSED_TESTS_PASS cases=6
```

The independent core rebuilds all tableaux, transitions, congruence classes,
and shape closures. It does not read `results/discovery_*.json` or
`src/discovery.cpp`.

