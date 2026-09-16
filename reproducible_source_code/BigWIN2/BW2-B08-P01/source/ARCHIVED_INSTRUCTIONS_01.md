# Eight-vertex whiskered-graph WLP result

This archive accompanies the characteristic-zero finite theorem in
`paper/main.tex`.

## Build the paper

From `paper/` run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Verify the exact certificate

From the archive root run:

```sh
python3 audit/certifier_independent_verify.py
```

The independent verifier uses only the Python standard library. It decodes
graph6 directly, checks the full 12,346-record census relative to the saved
stream, recomputes every independence number and Hilbert vector, and verifies
all 6,021 nonzero integer kernel witnesses. Expected terminal output contains
`"status": "OK"` and `"alpha3_certificates_verified": 6021`.

The `experiments/` directory records the generation code, exact commands,
versions, and logs. The `certificates/` directory contains the graph stream,
kernel data, coordinate convention, and checksums. The `audit/` directory
contains the independent certificate and proof audits.

The proof and certificate concern characteristic zero. No proof assistant was
used. Canonical completeness of the unlabeled graph stream relies on nauty
2.7r3 and the independently published count of 12,346 classes.
