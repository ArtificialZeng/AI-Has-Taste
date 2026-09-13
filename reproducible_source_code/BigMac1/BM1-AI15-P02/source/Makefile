PYTHON ?= python3
MATH_SKILL := /Users/mac/.codex/skills/prove-or-disprove-math

.PHONY: verify verify-core verify-independent verify-hardening verify-breaker paper latex-audit clean

verify: verify-core verify-independent verify-breaker latex-audit

verify-core:
	$(PYTHON) code/build_certificate.py
	$(PYTHON) code/verify_certificate.py certificate/a321614_certificate.json
	$(PYTHON) agents/builder/verify_certificate.py
	$(PYTHON) -m py_compile code/build_certificate.py code/verify_certificate.py agents/builder/verify_certificate.py agents/breaker/exact_audit.py agents/breaker/verify_audit.py

verify-independent:
	$(PYTHON) agents/referee/verify_no_import.py certificate/a321614_certificate.json

verify-hardening:
	$(PYTHON) code/test_fail_closed.py

verify-breaker:
	$(PYTHON) agents/breaker/verify_audit.py agents/breaker/audit_output.json

paper:
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex

latex-audit: paper
	$(PYTHON) $(MATH_SKILL)/scripts/audit_latex.py paper/main.tex paper/references.bib --log paper/main.log

clean:
	cd paper && latexmk -C main.tex
