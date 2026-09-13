# Fresh build audit

This audit is bound to snapshot
`413f5c03360234d737d20f93f903d94a9e4c26eeddf3b27781609cb6e3077d6d`,
manuscript digest
`4a1028cc3fd0bec2bc05b44680917562548a3cf013a2a1ebc9353989ce504004`,
and PDF digest
`56d56ae31af8c465b707fb7a624bff35e8feafdb58bdbb3939ed5197fa0702e2`.

The preserved recovery record documents the forced clean `latexmk` build of
this exact source/PDF state.  I inspected the nonempty compiler transcript
`manuscript/main.log` (SHA-256
`cd8d66740d8d7a122f5ba9a420d173df20e828b07437f3bdeb99752d2b828287`).
It records successful production of `main.pdf`, four pages, and completion with
all targets current.  There are no compiler errors, emergency stops, undefined
citations or references, multiply defined labels, rerun requests, or overfull
or underfull box warnings.

`pdfinfo` reports a valid unencrypted four-page letter-size PDF with the intended
title, author, subject, and keywords.  `pdftotext -layout` is nonempty, contains
all four bibliography items, and contains the exact ASCII graph6 word
`LlthgsL` followed by byte `0x60` and `mEkLkL` in both prose occurrences.  The
shell reproduction examples retain an escaped grave accent.  Verdict:
**accept; clean build**.
