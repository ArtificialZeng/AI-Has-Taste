# PDF audit

Status: **PASS**  
Artifact: `output/pdf/nu3_11_certified.pdf`  
SHA-256: `715bc1f928b608988d528b234c3ec16ecd1ed3ecfdb0bc9997cd3fb0624ed5f2`  
Pages: 7, US Letter, unencrypted, PDF 1.7

## Build and log gate

- Cleaned all LaTeX auxiliaries and rebuilt with `latexmk`/pdfTeX 2026,
  including BibTeX and all required reruns.
- `audit_latex.py` reports six cited keys, six bibliography keys, no missing
  or unused key, and no substantive log problem.
- The independent BibTeX-key checker reports six `.aux` `bibcite` keys and
  exact agreement with the source citations.
- A strict scan of `main.log` and `main.blg` found no undefined citation or
  reference, missing database entry, BibTeX warning, repeated entry,
  overfull/underfull box, PDF-string warning, LaTeX error, fatal error,
  emergency stop, undefined control sequence, or runaway argument.

## Metadata and identity gate

`pdfinfo` confirms:

- Author: `Zijian Zeng`;
- Subject contains exactly the required affiliation and both emails;
- Title states the certified `nu3(11)=15` result;
- no encryption, JavaScript, or form fields.

Text extraction confirms the title and sole author on page 1 and the exact
affiliation plus `zijianzeng@foxmail.com` and
`1002266693@ucsiuniversity.edu.my` on page 7.  The LaTeX source has one
`\author` command and the same address/emails.  No other author is present.

## Page-by-page visual gate

Poppler rendered all seven pages at 150 dpi to `tmp/pdfs/page-1.png` through
`page-7.png`.  Every rendered page was inspected at original image detail.

| Page | Content checked | Result |
|---:|---|---|
| 1 | title, author, abstract, opening formula and citations | PASS |
| 2 | theorem, definitions, structural reductions, section transition | PASS |
| 3 | upper-bound arithmetic, literal bit string, 15 triples, enumeration setup | PASS |
| 4 | Builder/Certifier lemmas and certified-sweep proposition | PASS |
| 5 | baseline table, breaker/negative controls, trusted-base opening | PASS |
| 6 | trust limitations, wrapped replay commands, disclosure, bibliography start | PASS |
| 7 | remaining references, exact affiliation, both emails | PASS |

No text is clipped, overlapped, unreadably small, or outside the margins.
Equations, theorem headings, hyperlinks, table rules, monospaced commands, and
page furniture are aligned consistently.  Page 7 has intentional white space
after the short bibliography/address ending and is not a layout defect.
