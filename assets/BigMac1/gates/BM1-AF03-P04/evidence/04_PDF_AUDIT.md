# PDF audit

Status: **PASS**.

Audit date: 2026-08-29.

- Build: clean `latexmk` run with no warnings, undefined references,
  overfull boxes, or underfull boxes.
- Page count: 4.
- Page size: US letter, 612 by 792 points.
- PDF metadata title: *The transitive-array conjecture for the classical
  Yang--Baxter equation*.
- PDF metadata author: Zijian Zeng.
- Final-page render hashes at 160 dpi:
  - p. 1: `c41318492fd44517ef7647007fa2bc22da56d4ea346d8ab4f0b28febe54b9727`
  - p. 2: `1abf5f34fcb3dfed0e8039a002df571a2af10462c4f07b8d1ec6ddd0369adac2`
  - p. 3: `d5519b787c8fc490e0dbf5ff61b2e0857d3fe59e64aa2327f098e5c1c84b6988`
  - p. 4: `0996a2e5c4b1e2087b56eccf70cd8ad71e95e9f35cd7374f89869b665acbeec6`

Page-by-page visual findings:

1. Title, author, abstract, opening equation, citation links, date, and page
   number are aligned and legible.
2. Definitions and component-identity setup have no clipped equations or
   malformed glyphs.
3. Proof, theorem, degeneracy remark, and count table are aligned; rules,
   caption, and numeric columns are intact.
4. Exact breaker paragraph, verification command, disclosure, bibliography,
   affiliation, and both email addresses are legible; final-page whitespace
   is balanced and contains no stranded heading.

No clipping, overlap, missing glyph, broken table, black box, or raw tool token
was found.  The clean-rebuild render was pixel-identical to the inspected
render on all four pages.
