# A078590 counterexample ancillary files

Build the note:

```sh
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Run both exact verifiers from the project root:

```sh
python3 certificates/verify.py
ruby certificates/verify_independent.rb
```

Tested on 2026-09-02 with Python 3.10.12, Ruby 3.0.2, and pdfTeX
1.40.22.  No random seed, floating-point arithmetic, or external solver is
used.
