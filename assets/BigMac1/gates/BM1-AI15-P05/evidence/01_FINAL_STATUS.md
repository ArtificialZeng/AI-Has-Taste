# Final status: `NEW_STRICT_BOUND`

Completed 2026-08-29.  This terminal state is **not** `PROVED` or `DISPROVED`.
Erdős Problem 647 remains open.

## Exact result

The frozen, fail-closed replay certifies that no integer in

\[
9{,}174{,}471{,}185{,}880{,}000{,}000<n\le
9{,}180{,}628{,}549{,}092{,}000{,}000
\]

satisfies

\[
\max_{m<n}(m+\tau(m))\le n+2.
\]

The computation reconstructs all 96 elementary sieve residues and all
50,784 subprogressions.  It replays 5,078,450,784 cells: 5,078,450,763 are
rejected by exact divisor lower bounds, the remaining 21 are factored exactly,
and zero remain unresolved.  The canonical certificate SHA-256 is
`19f8f31a1d037ddae404448ba13863f10607a23f24414b57628bf13b6ecc83c3`.

Together with the fixed prior *reported* endpoint, this advances the reported
computational frontier to

\[
9{,}180{,}628{,}549{,}092{,}000{,}000.
\]

This is the sole release claim: `NEW_STRICT_BOUND`.

## Gate decisions

- Gate 1: PASS.  Claims C01--C12 were locked before the new search; a second
  exact-endpoint novelty pass immediately before release found no exact or
  larger bound in the recorded sources and queries through 2026-08-29.
- Gate 2: PASS.  Proof, disproof, structural-reduction, and adversarial routes
  were maintained; the fatal global tail gaps remain explicitly open.
- Gate 3: PASS.  Exact integer coverage and exact factorizations form a finite,
  serialized, independently reconstructed certificate.
- Gate 4: PASS.  The verifier and tests contain no `assert`; normal, `-O`,
  outside-project `-I`, and outside-project `-O -I` modes pass with identical
  outputs, and every requested mutation fails closed.
- Gate 5: PASS.  Dependency, second-novelty, proof, and seven-reference audits
  pass.  Only the theorem-grade 2520/96-residue prerequisite is imported; the
  later 55/41 split and problem-specific axiom are not used.
- Gate 6: PASS.  A new-directory build has an empty error/warning scan; all
  fonts are embedded; all four pages passed visual inspection.  The final ZIP
  was extracted, its 55-file manifest checked, its paper rebuilt, and its
  verifier fully replayed from `/tmp` with `python3 -O -I`.  The rebuilt text
  equals the release PDF text and the decisive stdout equals the canonical
  certificate byte-for-byte.

## Release artifacts

| Artifact | SHA-256 |
|---|---|
| `output/pdf/erdos647_strict_bound.pdf` | `3064f945793bb825c945fd666b99a47ad596b638f4a23a01e8edd46019b6b98f` |
| `output/source/erdos647_strict_bound_source.zip` | `62374d07bd8f5fc1a974a91511a6a7243836f1cecf6a464ab9b53b61b9e39879` |
| ZIP internal `MANIFEST.sha256` | `fec1a52dde5dc2906040443d3ce28f3d6a61341561ad968795eb6414cf180c81` |
| frozen decisive-code manifest | `d83fbf6155eb96edfd8eb9e220689d236bd989ec30348d8ce7b97d2e2626d9d2` |

The outer artifact manifest is `output/MANIFEST.sha256`.

## Reproduction

From the project or extracted source root:

```text
shasum -a 256 -c verification/FROZEN_CODE_MANIFEST.sha256
python3 verification/test_verifier.py
python3 verification/verify_extension.py --threads 12
```

For the optimization/isolation replay, substitute the absolute extracted path:

```text
(cd /tmp && python3 -O -I /ABS/verification/verify_extension.py --threads 12)
```

For the published artifacts:

```text
shasum -a 256 -c output/MANIFEST.sha256
unzip -t output/source/erdos647_strict_bound_source.zip
```

## Limitations and proof-assistant disclosure

No finite search proves existence or nonexistence in the remaining infinite
tail.  The earlier prefix through the left endpoint was audited but not fully
rerun.  The bounded novelty audit cannot speak for unpublished work.

The new replay used **no proof assistant**, and no proof assistant was invoked
locally.  Its necessary modular prerequisite was formalized in Lean 4 in the
fixed Hughes dependency; that imported boundary is documented in
`audit/DEPENDENCY_AUDIT.md`.
