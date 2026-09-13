# PDF audit

Status: **PASS**.

- Artifact: `output/pdf/kl_r_fibonacci_n10.pdf`
- SHA-256: `96b8154056468be7bf8f3f4a2f2156d121cf0e20be23645b6b7be837ad3f1d2c`
- Size: 375,872 bytes
- Pages: 7, US Letter, no rotation, unencrypted
- PDF metadata author: Zijian Zeng
- PDF metadata title: *The n=10 Case of a q-Fibonacci Product Conjecture for Kazhdan–Lusztig R-Polynomials*
- Fonts: all listed fonts are embedded subsets; all report Unicode mappings
- Text extraction: both required email addresses and the exact UCSI University affiliation are present

The PDF was rendered at 144 dpi with Poppler.  Every page was inspected at
original rendered resolution.  Page 1 has a centered title/author/abstract;
pages 2--6 have complete body text, equations, theorem/proof endings and the
enumeration table inside the margins; page 7 has all five references and the
required affiliation and email addresses.  No clipping, overlap, broken
glyphs, blank content page, missing equation, or unreadable table was found.

Reproduction commands:

```sh
(cd paper && latexmk -C main.tex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex)
cp paper/main.pdf output/pdf/kl_r_fibonacci_n10.pdf
pdftoppm -png -r 144 output/pdf/kl_r_fibonacci_n10.pdf tmp/pdfs/page
pdfinfo output/pdf/kl_r_fibonacci_n10.pdf
pdffonts output/pdf/kl_r_fibonacci_n10.pdf
pdftotext output/pdf/kl_r_fibonacci_n10.pdf tmp/pdfs/extracted.txt
```
