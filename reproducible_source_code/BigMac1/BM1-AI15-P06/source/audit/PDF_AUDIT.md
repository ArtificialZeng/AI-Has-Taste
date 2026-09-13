# Gate 6 PDF and LaTeX audit

Date: 2026-08-29  
Artifact: 'output/pdf/kusner_l1_5_support19_partial_theorem.pdf'  
SHA-256: 23e7143150038d5dad511afdb0f49ca3118566b7371d933b1eaa371bb6e410b1  
Pages: 8  
Build system: TeX Live 2026, latexmk 4.88, pdfTeX 1.40.29, BibTeX.

## Clean build

The build directory was cleaned with 'latexmk -C main.tex', then rebuilt
with:

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The final 'main.log' contains:

- undefined references: 0;
- undefined citations: 0;
- missing bibliography entries: 0;
- duplicate labels: 0;
- overfull boxes: 0;
- underfull boxes: 0;
- warnings: 0.

The previously reported 14.97638 pt overfull box in the AI-disclosure
paragraph was repaired locally: the paragraph was shortened and the global
'\\emergencystretch' workaround was removed. The converged clean-build log
therefore reaches zero overfull boxes without relying on that global stretch.

'pdfinfo' reports the exact metadata title
“Eleven equilateral points in five-dimensional ell-one require at least
nineteen coordinate gaps.” It does not contain the erroneous string 'l15'.

The independent key audit reports 3 cited keys, 3 bibliography keys, no
missing keys, and no unused keys. Placeholder and extraction scans found no
TODO, FIXME, “Insert,” undefined marker, or unresolved question mark.

## Page-by-page visual inspection

The PDF was rendered with Poppler at 150 dpi to eight PNG pages. Every page
was inspected at original rendered resolution.

| Page | Content | Verdict |
|---:|---|---|
| 1 | Title, abstract, introduction, author footnote | PASS |
| 2 | Main theorem, cut-frame reduction, Naimark lemma begins | PASS |
| 3 | Naimark boundary, spectral deficit, rational cost table | PASS |
| 4 | Endpoint table, singleton compression begins | PASS |
| 5 | Compression conclusion, finite strata and endpoint table | PASS |
| 6 | Rank-ten design and antichain lemma | PASS |
| 7 | Main proof conclusion, exact checks, finite-box theorem, limitations | PASS |
| 8 | References, affiliation, email | PASS |

No clipped text, overlapping equations, broken glyphs, cropped margins,
unreadable tables, blank accidental pages, or inconsistent headers were
found. The repaired disclosure paragraph on page 7 wraps cleanly. Page 8 is
intentionally short because the bibliography and author address close the
article.

## Content-scope check

The title, abstract, Theorem 1.1, conclusion, and limitations consistently
state the partial theorem \(t\ge19\). The paper explicitly says that
Kusner's \(n=5\) question remains open. Proposition 7.1 is labelled and
explained only as the finite-box result for \(\{0,1,2,3,4\}^5\), and the
Python \(>=3.10\) requirement and no-proof-assistant disclosure are visible
on page 7.

Final visual verdict: **PASS**.
