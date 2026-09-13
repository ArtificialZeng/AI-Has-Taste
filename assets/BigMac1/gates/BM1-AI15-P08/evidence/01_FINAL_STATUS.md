# Final status: Sheil--Small self-inversive covering problem

Terminal state: **PARTIAL_THEOREM**  
Secondary classification: **NEW_INFINITE_SUBCLASS**  
Frozen: 2026-08-29 (Asia/Shanghai)

## Exact scope of the result

For the standard conjugate-inversion definition of self-inversive,

\[
P(z)=\sum_{k=0}^n a_kz^k,\qquad
A(P)=\max_k|a_k|,
\]

the audited manuscript proves that `P(D)` contains an open disk of radius
`A(P)` in each of the following cases:

1. every exact degree `1 <= n <= 3`;
2. `n=4` or `n=5` when an endpoint coefficient realizes `A(P)`, or some zero
   lies off the unit circle, or all zeros are unimodular and
   `2|a_n| >= A(P)`;
3. every even degree `n=2m` whose support is contained in `{0,m,2m}`.

The cubic proof gives the stronger radius `7/6` in its all-unimodular
non-endpoint normalization and `3/2` otherwise.  These strengthened radii
are not needed for the radius-one conclusion.

## What is not solved

The unrestricted all-degree problem is **not solved**.  In particular, this
work makes no assertion on either residual stratum

```text
n in {4,5}; all zeros unimodular; no endpoint realizes A(P); 2|a_n| < A(P).
```

Those are the isolated-zero/punctured-disk gaps Q4-U and Q5-U.  Search on
them was stopped as directed, and no expanded numerical search is part of
the frozen result.  `original_prompt_complete=true` in `TASK_STATUS.json`
means that the requested research-and-audit workflow is complete, not that
the original conjecture is decided.

## Independent proof audit

The independent referee reconstructed the frozen proof from the definitions
and specifically attacked the cubic normal form, both Schur branches
including equality, the `C_s` center homotopy, and the isolated zero-boundary
case.  The final verdict in `audit/referee_low_degree.md` and
`audit/manuscript_consistency.md` is PASS for every stated theorem, with no
fatal or major mathematical defect.  Q4-U and Q5-U remain explicitly outside
the theorem.

The typo in `problem/formal_statement.md` after `z -> e^{i theta} z` was
repaired before the audit.

The post-referee `builder_notes` changes received a separate provenance/diff
audit.  The tool-patch log deterministically reconstructs a 10-hunk
`+83/-34` diff from a candidate pre-referee SHA-256 `4f60148d...3183ed8` to
the frozen SHA-256 `126ec412...34001df`.  Every hunk maps to referee findings
R1--R8 or R11.  The earlier phrase “five repairs” is only a broad
classification; the precise qualification and lack of an independently
stored pre-edit snapshot are recorded in
`audit/BUILDER_NOTES_DIFF_AUDIT.md`.

## Exact and fail-closed certificates

- `src/builder_symbolic_checks.py` contains no Python `assert` and uses
  explicit nonzero failure paths.
- `tests/referee_low_degree_identities.py` is an independent standard-library
  reconstruction.
- `tests/verify_serialized_low_degree_certificate.py` authenticates and
  exactly recomputes the 11 checks in
  `certificates/low_degree_identities.json` over rational Laurent
  polynomials.
- The serialized verifier now rejects unknown or missing fields at every
  schema level and authenticates the independently serialized
  `certificates/low_degree_certificate_manifest.json`.  That manifest freezes
  the certificate plus formal, builder, referee, and manuscript hashes.
- All three pass from an external working directory in normal, `-O`, `-I`,
  and `-O -I` modes.  Their injected-failure tests exit nonzero in all four
  modes.  Coefficient tampering, incomplete inventories, tautology-only
  inputs, and duplicate keys/labels are rejected.
- The independent Gate 4
  genuine/badhash/extra-field/drop-check/change-expression matrix is 20/20;
  the checked-in driver adds four in-memory expression-residual cells for a
  24/24 result.  A certificate and manifest whose expressions and digest are
  changed together are rejected by the pinned manifest digest.

The certificate SHA-256 is
`92a5280a7380c140ad758b9d2f346adf3ba4072393890c778056cd50acde8720`.
The certificate-manifest SHA-256 is
`a6a5ad4f655b315cf3def4e8f37d4bf89e993a63d0efbb3e3b7007fa480753c3`.
The strict verifier and matrix hashes are respectively
`5244545747cd200b07c87730b0188927e7193da2bf73d760dc4c8d62f7f81153`
and `43fb7d56d563667f2153d6392eec7a776ce860bcc2e58fdb3f4666108a73f384`.
The serialized layer is supporting exact evidence, not the sole proof; the
analytic proof, independent human referee, and hard-coded stdlib referee
checker remain decisive.

## Novelty and citation result

The second claim-specific novelty lock has verdict **PARTIAL NOVELTY
CLEARANCE; CLAIMS DISAGGREGATED**.  Searches through 2026-08-29 found no exact
prior match for the complete degree-two/three theorem, the stated new
degree-four/five branches, or the even sparse-support theorem.  This is a
dated, database-bounded negative search, not a proof that no prior result
exists.  The endpoint-maximal branch is prior/general (Solyanik), and the
endpoint-binomial observation is elementary and is not claimed as novel.

All five manuscript citations were checked against primary publisher,
DOI/arXiv, or official bibliographic records.  The Hayman--Lingham accessible
source literally prints `1/zeta` rather than conjugate inversion; the
manuscript discloses this source discrepancy and proves only the standard
conjugate-inversion formulation.

## Release and reproducibility gates

The LaTeX/citation audit, final clean build, page-by-page visual PDF audit,
Gate 4 tamper matrix, source-binding check, ZIP integrity test, and clean
rebuild from the extracted ZIP all passed.  The source package contains the
exact certificate, strict certificate manifest, verifier matrix, three exact
verifiers, dependency pins, proof/gap ledgers, two novelty audits, citation
audit, independent referee and diff reports, and SHA-256 manifest.  The
mathematical manuscript and retained PDF were not regenerated for Gate 4;
only the same-named source package was corrected in place.

```text
f5e502d6f122d8720a5871e6b435429102b9ca75eb2c58fa266f2da129be7260  output/pdf/sheil_small_low_degree_covering.pdf
ac9eb552f372a1ac92a5aedc6b43ac51e969ba935e0996ed45d6a6b25c9baa17  output/source/sheil_small_low_degree_covering_source.zip
```

Core reproduction commands are recorded in
`manifests/release_manifest.md`.  The source archive itself was verified by:

```bash
unzip -t output/source/sheil_small_low_degree_covering_source.zip
unzip -q output/source/sheil_small_low_degree_covering_source.zip -d CLEAN_DIR
cd CLEAN_DIR
shasum -a 256 -c manifests/source_files.sha256
cd paper
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Proof-assistant disclosure

No Lean, Coq, Isabelle, HOL, or other proof assistant was used.  The result is
an analytic proof supported by exact symbolic verifiers and independent
human-style proof reconstruction.
