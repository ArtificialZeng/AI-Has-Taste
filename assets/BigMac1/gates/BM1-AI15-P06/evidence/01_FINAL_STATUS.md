# Final status

Terminal state: **PARTIAL_THEOREM**  
Date: 2026-08-29  
Original research workflow complete: **true**

## Exact result

If eleven equilateral points in \(\ell_1^5\) exist and \(q_j\) is the
number of distinct values in coordinate \(j\), then
\[
\sum_{j=1}^5(q_j-1)\ge19,\qquad \sum_{j=1}^5q_j\ge24.
\]
Equivalently, every hypothetical counterexample to Kusner's taxicab
conjecture in dimension five uses at least nineteen positive consecutive
coordinate gaps.

This is a strict structural partial theorem. It does **not** prove
\(e(\ell_1^5)=10\), construct eleven equilateral points, or exclude the
strata with nineteen or more gaps. The original \(n=5\) problem remains
open.

## Why this terminal state is justified

- The cut-chain/Parseval reduction and spectral deficit exclude
  \(t\le14\).
- Exact endpoint inequalities and singleton compression exclude
  \(t=15,16,17\).
- At \(t=18\), exact rational enumeration reduces 88 partitions to eight
  and forces \(8\le R\le10\) non-singleton copies.
- Rank-nine compression excludes \(R\le9\); the identity
  \(D_p+c_pJ=B_pGB_p^T\) and Sherman--Morrison force the ten oriented blocks
  to be pairwise intersecting and incomparable, contradicting five nested
  coordinate chains when \(R=10\).
- Independent referee rounds 1--5 passed. A final hash-bound referee
  attacked ambient/\(V\) kernels, the one-gap and \(|Z|=1\) boundaries,
  potentially negative \(c_r\), the \(Z=[11]\) boundary, complement
  orientation, repeated cuts/singleton labels, and strict inequality
  summation. The final manuscript received PASS.
- The second novelty sweep through 2026-08-29 found no matching
  support-\(19\) or rank-ten antichain theorem. This is bounded evidence,
  not a claim of absolute novelty.

## Separate certified finite result

The exact certificate for \(\{0,1,2,3,4\}^5\) proves that its largest
equilateral subset has size ten over all integer distances. This is a
finite-box theorem only and has no implication for unrestricted real or
integer coordinates.

## Fail-closed and dependency audit

The three foundational scripts and the \(t=18\) verifier contain zero AST
Assert nodes. External genuine/tamper matrices pass under normal, '-O',
'-I', and '-O -I' modes. The foundational matrix is 48/48 and the \(t=18\)
matrix is 60/60. Deleted fields, changed \(m,d\), gap count, point
coordinate, claimed distance, and frame data all fail with nonzero exit.

Python **3.10 or newer** is required. Homebrew Python 3.14.7 rebuilt the
side-five certificate under '-O -I'; Apple system Python 3.9 exits
fail-closed because 'int.bit_count' is unavailable.

No proof assistant was used.

## Release artifacts

- Manuscript source 'paper/main.tex'  
  SHA-256:
  d55cdd3cd7a6785bbacdb23b3817868af0ca973651532ed8aa5da0d26d163b11
- PDF 'output/pdf/kusner_l1_5_support19_partial_theorem.pdf'  
  SHA-256:
  23e7143150038d5dad511afdb0f49ca3118566b7371d933b1eaa371bb6e410b1
- Source ZIP
  'output/source/kusner_l1_5_support19_partial_theorem_source.zip'  
  SHA-256:
  dd3cfdb62e7c9abd952df1982fece973f5efaca4041ffa3cbc97437773d6de9d

The ZIP was extracted into a fresh external directory and its internal
67-file SHA-256 manifest verified. It contains no '.venv', '__pycache__',
'.pyc', PDF, rendered image, binary, or unreviewed 'proof/t19_branch.md'.

The last release-only edit removed the global emergency-stretch workaround,
repaired the 14.97638 pt overfull box locally, and made the PDF metadata title
explicitly say “five-dimensional ell-one.” The independently checked delta
contains no mathematical or citation change. The final converged LaTeX log
has zero warnings and zero overfull or underfull boxes; all eight rendered
pages passed visual inspection. Exactly one final PDF and one final source
ZIP are retained. The release README now distinguishes excluded generated
LaTeX auxiliaries ('.aux', '.blg', '.log', '.fls', and '.fdb_latexmk') from
the deliberately retained 'paper/main.bbl' used for portable builds.

## Reproduction

From the extracted source ZIP, with Python 3.10 or newer:

    python3 -O -I certificate/t18_verify_endpoint_manifest.py certificate/t18_endpoint_manifest.json
    python3 -O -I audit/referee_t18_check.py
    python3 -O -I certificate/verify_integer_box.py certificate/integer_box_side5.json
    python3 /path/to/verify_manifest.py . MANIFEST.json

Clean manuscript build:

    cd paper
    latexmk -C main.tex
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

Gate 5 citation/proof/dependency reports are in 'audit/', and the clean
eight-page visual audit is 'audit/PDF_AUDIT.md'.
