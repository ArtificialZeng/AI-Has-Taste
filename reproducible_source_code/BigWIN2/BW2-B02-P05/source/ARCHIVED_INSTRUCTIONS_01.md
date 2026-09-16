LaTeX source package
====================

This archive contains the journal-neutral amsart source for
"A Shifted-Golomb Identity for the Full-Memory Prefix of Run-Constructed
Almost Golomb Sequences" by Zijian Zeng.

Build the manuscript from this directory with:

    pdflatex main.tex
    bibtex main
    pdflatex main.tex
    pdflatex main.tex

The accompanying exact-arithmetic programs use only Python 3.10 or later and
the standard library.  Recompute and verify the serialized finite diagnostic
with:

    python3 src/verify_finite_certificate.py

The files `src/run_length_search.py` and `src/endpoint_checker.py` are
independent implementations of the finite check; the verifier recomputes both
and compares their results with `certificates/finite_check.json`.  These
calculations are diagnostic only.  The theorem is established by the symbolic
proof in `main.tex`.

No proof assistant was used.
