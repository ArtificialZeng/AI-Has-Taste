# PDF audit

Audit date: 2026-08-29  
Artifact: `paper/main.pdf`  
Method: Poppler render at 150 dpi plus page-by-page visual inspection and
layout-preserving text extraction  
Verdict: **PASS after final rebuild**

## Global checks

- Five US-letter pages, portrait, no encryption, forms, JavaScript, or rotation.
- PDF metadata title matches the manuscript; author is exactly Zijian Zeng.
- All fonts and mathematical glyphs render legibly.
- No clipped text, overlaps, black squares, broken links, or margin overflow.
- LaTeX log has no overfull/underfull boxes, undefined references, citation
  warnings, fatal errors, or rerun warnings.

## Page-by-page inspection

1. Title, single-author attribution, abstract, opening section, date, and page
   number are centered/aligned and remain inside margins.
2. Definitions, four relations, enumeration bounds, and primitive-rule formula
   render cleanly; header and page number are unobstructed.
3. Theorem 4.1, proof, and six-column exact-count table are readable; the table
   fits horizontally with all nine rows and both horizontal rules intact.
4. Audit counts, open general gap, reproduction commands, AI disclosure, and
   proof-assistant statement render without code-line overflow.
5. The single reference, exact UCSI affiliation, and both email addresses are
   present and legible; the remaining whitespace contains no missing content.

The final output copy is byte-identical to the audited `paper/main.pdf` and is
bound by the release manifest.
