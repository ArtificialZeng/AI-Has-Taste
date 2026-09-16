# Certified partial result: 17-point unlabeled posets

This project proves and independently checks

```text
377293651326150106 <= U(17) <= 15754175376569459236
D(17) = 4554367168841547
```

It does **not** determine the exact value of `U(17)`.

Run the complete exact certificate gate from the project root:

```bash
python3 code/certificate_gate.py
```

Requirements are Python 3.10 or later (standard library only) and
`pdftotext` for the archived Table 59 transcription check. The individual
verifiers are documented in `results/partial_result.md`. No proof assistant
is used.

The submission-source archive does not redistribute third-party articles.
For the full Table 59 transcription check, obtain the cited
Brinkmann--McKay paper and place it at
`literature/sources/brinkmann_mckay_2002_posets.pdf`; all other certificate
checks are self-contained.
