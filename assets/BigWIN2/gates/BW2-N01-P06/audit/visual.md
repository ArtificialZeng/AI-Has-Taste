# Rendered-page visual audit

PASS. Job `newwin-00001-p06-release-8c9ea9285eb1`, 2026-09-12 UTC. PDF `1d4d5f76dedc14044b6b0960650442dd054aa87bda00cb4e903c5468c49a8610`; manuscript `573155d648f7899400e851cb2492608a7a72d1c380e2a00cc6be30155780826d`.

Rendered the final five-page PDF using `pdftoppm -r 120 -png manuscript/main.pdf audit/recovery-page`. Actually opened and visually inspected every image with view_image: pages 1–2 in one tool call, pages 3–5 in the next. Text extraction and successful rendering were not used as substitutes for viewing. This report is tied to those exact image hashes and PDF bytes.

- Page 1: Title, affiliation, abstract, definitions, cited context and main theorem are readable. The inequality 1265 versus 1266 and bounded novelty wording render correctly; no clipping or overlap.
- Page 2: Direct-sum notation, unique-block lemma, summation bounds, square identity and residual formula are legible. Proof text, subscripts, equation numbers and end markers fit within margins.
- Page 3: Endpoint-domain argument, recurrence and boundary cases, scalar sequence and finite-certificate proposition are legible. Symbols and final proof lines do not overlap the page footer.
- Page 4: All nine permutation/square pairs and the full two-row count table are readable; commas distinguish 10 and 11, b_0 remains undefined. Table values match exact parsed source data. Both method citations and scope/assistance disclosures are visible.
- Page 5: Reproduction commands, pattern inequalities and file paths render legibly. All five references are visible and complete. The repaired reference explicitly displays Preprints.org, version 1, posting date and DOI; line breaks in links do not clip or obscure text.

No chart or external data graphic occurs. Both numerical tables were compared value-by-value with the exact local certificate and accepted counts in audit/recovery-data-verification.json. No clipping, overlap, missing glyph or illegible formula was found. All fonts are embedded. The PDF metadata identifies the intended title and Xiaojian Zeng.
