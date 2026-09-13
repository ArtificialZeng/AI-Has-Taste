.PHONY: certificate verify breaker audit build clean

certificate:
	python discovery/enumerate_transitive.py --output certificates/transitive_arrays_n_le_5.json

verify:
	python verifier/verify_certificate.py certificates/transitive_arrays_n_le_5.json
	python verifier/verify_symbolic_expansion.py certificates/transitive_arrays_n_le_5.json
	python tests/test_verifier.py

breaker:
	python experiments/exact_sl2_breaker.py certificates/transitive_arrays_n_le_5.json

audit:
	python /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py paper/main.tex paper/references.bib

build:
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex

clean:
	cd paper && latexmk -C main.tex
