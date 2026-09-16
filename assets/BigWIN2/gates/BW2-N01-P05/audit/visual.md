# Rendered-page visual audit

Verdict: accept. Job `newwin-00001-p05-release-df34904a6a33`; 2026-09-12T10:11:20.355939+00:00.

All seven pages were rendered at 125 dpi with pdftoppm and actually inspected through image-view tools. The final sentence clarification changed only page 4; that page was viewed again, while all six other final renderings are byte-identical to the already viewed images. The hashes and comparison are saved in `audit/release-preview/manifest.json` and `audit/release-preview/render-comparison.json`. Text extraction was used only for supporting checks, not as a substitute for viewing.

- Page 1: Title/author/contact, abstract, map definition and neighboring count formula: all legible; citations visible; no clipping.
- Page 2: Main theorem quantifiers, maximal-time scope, first-letter formula and clump lemma: symbols, equation numbers and citation locators legible.
- Page 3: Clumped deletion proof, two-sided bound, gap reduction and multinomial counts: no overlap or missing symbols.
- Page 4: Both finite-base table rows match the exact certificate; library citation and its Section 4 qualification are visible; induction and section heading fit. Final changed page re-viewed.
- Page 5: Terminal corollary and k>=4 proposition, truncation identity and boundary table: all hypotheses, six times and markers match the source.
- Page 6: Corroboration counts and AI disclosure intact; appendix explanation and first code block readable, complete and indented.
- Page 7: Remaining code block completes the verifier; five printed references and all DOI/arXiv links legible; no nearly empty spill page.

All table values were compared individually with the exact finite-base and boundary evidence. The manuscript contains no quantitative plots requiring axis or scale checks. No clipping, overlaps, unreadable glyphs, hidden citations or mismatched table entries were observed. A4 margins and embedded vector fonts remain consistent. The long verifier is split at a function boundary and ends above the complete bibliography.
