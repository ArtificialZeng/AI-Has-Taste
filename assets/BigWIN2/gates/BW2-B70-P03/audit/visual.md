# Rendered-page visual audit

Release job: `win-00070-p03-release-f068e3c4ff94`  
PDF: `manuscript/main.pdf`  
PDF digest: `a876798d41a8d6fdae05279cf2446ffed848c2009e8fce796db542425f70af63`  
Renderer: `pdftoppm -png -r 144`  
Result: PASS

Every page was freshly rendered and individually viewed at full rendered
resolution.  Page 1 has a legible title, author block, abstract, opening
statement, theorem, and first display.  Page 2 has legible theorem and Cech
resolution material.  Page 3 has legible tensor decomposition, nerve reduction,
citations, and component formula.  Page 4 has legible conclusion, exact-check
data, disclosure, and references 1--4.  Page 5 cleanly contains reference 5 and
the page number.  No page has clipping, overlap, cropped content, broken glyphs,
illegible mathematics, orphaned citation markers, or margin overflow.  All
display equations, theorem labels, section numbers, reference numbers, and page
numbers are visible.  The short final bibliography page is intentional and not
a rendering defect.

Rendered evidence:

- `audit/rendered-pages/page-1.png`
- `audit/rendered-pages/page-2.png`
- `audit/rendered-pages/page-3.png`
- `audit/rendered-pages/page-4.png`
- `audit/rendered-pages/page-5.png`
