# win-00064-p04 — Exact ANF degree and leap of complete-raw finite-field inversion

Adopt without alteration the complete raw polynomial extension, algebraic degree, and joint ANF leap defined by Zhang–Zhang, arXiv:2609.04583v1. Decide whether, for every integer `n>=3`, the complete raw map has algebraic degree exactly `3(n-1)` and joint ANF leap exactly `n`. If either equality fails, find the least `n` and determine the exact value there.

The source proves only degree at most `3(n-1)` and leap at least `n`, with exact equality verified computationally for `n=3,4`. Do not replace the full Boolean polynomial extension by the function restricted to invertible basis matrices. Exact sparse-ANF computation may guide the proof but finite computation alone proves only the tested `n`.

Primary evidence: `batches/inbox/bigWin-64-materials/2609.04583.pdf`, SHA-256 `adccdaad3014a91760fe1af9686e7d75cd2c647a637dc9a3d69cc1476a5aa6bc`, theorem chain, Section 4, and Conclusion.
