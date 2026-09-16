# Research pass 2: exact reproduction record

Provenance: `win-00036-p03-research-e91c25b72a82`.

The following checks were run from the project directory with Python 3.10.12.
They use integer equality and `math.gcd`; no floating-point predicates occur.

```sh
python3 evidence/verify_x529_coloring.py evidence/x529-coloring-certificate.json
python3 evidence/x529_coloring_certificate.py verify evidence/x529-coloring-certificate.json
python3 evidence/x529_coloring_certificate.py generate /tmp/x529-coloring-recomputed.json
cmp -s evidence/x529-coloring-certificate.json /tmp/x529-coloring-recomputed.json
sha256sum evidence/x529-coloring-certificate.json /tmp/x529-coloring-recomputed.json
```

The dependency-free verification returned `verified: true`, checked exactly
263 gaps and directly tested 147,843 same-color pairs.  The generator's
separate edge-verification path returned `verified: true`, recomputed 955,648
compatible edges, and found maximum color count 41, attained only at gap 42.
Regeneration succeeded and `cmp` found the regenerated file byte-for-byte
identical to the stored certificate.  Both complete files had SHA-256
`e0a1d4e76516a8c0a43df8bfc80e9e7e9339086c32f463d0b25e3545fd46ee37`;
their canonical payload SHA-256 was
`891877322b99abeb51b5fe38f883ce73625c8cb6017b69a58193e85188b60673`.

The 263 records are exactly the even gaps 2 through 526.  Together they
contain 28,231 vertices.  Each record gives a proper coloring of the exact
gcd-compatibility graph with at most 41 colors.  Thus each per-gap certificate
is a directly reproducible upper bound \(\omega(G_{529,d})\leq 41\), not a
timeout or an unsupported solver status.
