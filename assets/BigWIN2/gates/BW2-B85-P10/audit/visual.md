# Fresh rendered-page visual audit

Job: win-00085-p10-release-67ea8095309a. Checked 2026-09-12 UTC.

Rendered the final six-page PDF with `pdftoppm -r 120 -png` and actually viewed
every resulting page image through the image-viewing tool, in order 1-3 and
4-6. Earlier views preceded compatibility edits and were superseded; the views
reported here followed the final rebuild and refreeze. Text extraction alone
was not used as visual review.

- Page 1: Title, author, affiliation, abstract, definitions, positive-leg comparison and Theorem 1 are legible; initial-zero convention and library citation appear in ordinary text.
- Page 2: Endpoint-state decomposition, equations (2)-(4), and the full convolution lemma/proof are unclipped. Equation numbers and proof square are aligned.
- Page 3: Coefficient formulas, ten-center lemma and main proof are legible. The exact-verification section and filenames fit; no missing glyphs or unresolved cross-references.
- Page 4: Finite ranges and counts are printed correctly. Limitations and AI disclosure are explicit. All five compact formulas and the R,2 coefficient table are complete.
- Page 5: The R,3, S,2, S,3 and S,4 coefficient tables have clear exponent headers, integer cells and zero-as-blank convention. The widest nine-column table fits within margins.
- Page 6: All five bibliography entries are visible and legible, including the 27-author SymPy entry and distinction between Zijian and Xiaojian. URLs break within margins.

No clipping, overlap, illegible symbols, spurious blank pages or missing
references were observed. Table entries were also compared mechanically with
the exact arrays and generator output; the scale factors 12, 144 and 2880 and
the displayed exponent labels agree. There are no statistical charts or figures
requiring axis or uncertainty checks. The normal white space below the final
tables and bibliography is intentional. The six-page article remains readable
at the rendered size. Verdict: accept.
