# STS(15) Pasch-switch quotient diameter

Exact result: the simple quotient has 258 edges and connected-component
orders 79 and 1. The 79-vertex component has diameter 11 and radius 6.
The isolated anti-Pasch representative is `V036`. In the released naming,
the diameter pairs are `V000`--`V006` and `V000`--`V028`.

## Reproduce the decisive checks

From the project root:

```sh
python3 code/independent_verifier.py certificate
python3 code/verify_bfs.py
python3 tests/test_verifier_rejects.py --output certificate/negative_tests.json
python3 code/verify_published_baseline.py
```

The first command is the decisive no-nauty verifier. It does not import
`code/discover_graph.py`; it validates all 80 systems, re-enumerates every
Pasch by a different method, proves every target with an exact isomorphism,
reconstructs the whole edge set, and reruns all-pairs BFS.

## Key artifacts

- `certificate/representatives.json`: all 80 normalized representatives.
- `certificate/quotient_edges.json`: complete 258-edge simple quotient.
- `certificate/switch_occurrences.json`: all 1,390 Pasch occurrences.
- `certificate/result.json`: components, eccentricities, diameter pairs,
  path, distance row, and BFS layers.
- `paper/main.tex` and `paper/references.bib`: manuscript source.
- `output/pdf/sts15-pasch-diameter.pdf`: audited five-page manuscript.
- `release_bundle/MANIFEST.json`: release integrity manifest.

## Discovery (optional)

Discovery requires nauty `labelg`:

```sh
python3 code/discover_graph.py --output certificate
python3 code/crosscheck_catalog.py --output certificate/catalog_crosscheck.json
```

The exact mathematical certificate does not require nauty after the
serialized representatives are present.
