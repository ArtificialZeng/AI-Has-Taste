# Fresh build audit

The current publication snapshot identifies `manuscript/article.pdf`, SHA-256
`7fee8ba75b86b6cd4fc2725c8ba0bb88367935e3155ef08c586d5c00ba9acc1f`,
as the output of the recorded `latexmk`/pdfLaTeX plus Biber build.  I inspected
the complete nonempty compiler log `manuscript/article.log`, SHA-256
`fe0e53f9abeab83e1b16557a428bb7f1fca72e20478fe7343c4a8a1ecdb050df`,
and the Biber log.

The log terminates normally with `Output written on article.pdf (5 pages,
333549 bytes)`.  It contains no TeX error, fatal stop, missing file, undefined
control sequence, undefined citation or cross-reference, empty bibliography,
rerun request, overfull box, underfull box, or package warning.  The Biber run
resolved all three database entries.  Cross-references to Theorem 1, Lemma 2,
Proposition 3, Table 1, and equations (1)--(14) are present and resolved in the
extracted PDF.

`pdfinfo` reports a valid unencrypted PDF 1.7 with five letter-sized pages,
title *The Grid-Traffic Threshold: A Proof for Every n >= 496*, and author
Xiaojian Zeng.  `pdftotext` yields nonempty text covering the title, proof,
table, disclosures, and all three references.  `pdffonts` reports that every
font is embedded and subsetted with Unicode mapping.

**Verdict: ACCEPT.  The bound existing build log documents a clean build.**
