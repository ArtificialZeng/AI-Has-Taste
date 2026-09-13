# V18 portable-chain candidate independent final audit

## Verdict

**PASS — fatal 0, major 0, minor 0.**  The frozen PDF and ZIP may be promoted only byte-for-byte.  This audit does not authorize any mathematical claim beyond the local theorems actually stated in `main.tex`.

The audited bytes are:

- PDF: `2f04f9b65c6c31cc9b4f806bc9e264aec4ac951dcc525d2519206ecb3c1a89fc`;
- ZIP: `b641929fddeda5e596ca57dc64a693b4427ff072be9d4ecc16df14ccb7e17262`;
- JSON release manifest: `499ae3d1f371dbd0aae141f5f9ebbf48cf0bf47d092a997130903f6d52a57b75`;
- top portable-chain manifest: `df89279bc36a5c37e9b3a2ce5b7e5d3bd83c37566fe141e674c5be8de9ce5397`.

## Archive and portability

I extracted the ZIP afresh twice and did not use the mutable candidate directory as archive evidence.  Each replay found exactly 1,629 safe entries under one root.  There were no absolute paths, parent traversals, symbolic links, duplicate names, case-fold collisions, environment caches, concrete `/Users/mac`, `/home`, or `/tmp` paths, or secret-like material.  CRC passed.  The JSON release manifest covered the other 1,628 files with exact byte sizes and SHA-256 hashes.  The external PDF and packaged `main.pdf` were identical.

All 15 files responsible for the prior absolute-path failure are absent.  The previous incomplete eight manifests remain only as explicitly documented historical provenance anchors.  `README.md`, `certificates/PORTABILITY_NOTE.md`, the portable-layer README, and the index consistently say that the new parallel portable layer—not the old incomplete manifests—is the replayable chain.  No instruction still requires the historical failing `shasum` behavior.

The portable manifests replayed in both fresh extracts:

| cell | source | no-import referee | cell |
|---|---:|---:|---:|
| x627 | 38/38 | 50/50 | 16/16 |
| x63 | 37/37 | 56/56 | 16/16 |
| x16 | 41/41 | 60/60 | 16/16 |
| x7/10 | 45/45 | 60/60 | 16/16 |

The top chain was 24/24, and the unchanged historical principal index was 32/32.

## Independent exact replay

In each of two separate ZIP extracts I ran all four source normals and all four literal-free/no-import referee normals.  I also serially reran their optimized, dependency/hash, normalization, clearing, deleted-Q-squared, conjugacy, signed-z, danger-sign, coefficient, control, and seam attacks.  The two runs were 99/99 and 99/99, for 198/198 expected outcomes.  Normals returned zero and every mutation returned nonzero at an exact gate.

The machine Python initially lacked `sympy`.  I therefore reconstructed a disposable environment from the packaged `certificate_workspace/requirements-portable.txt`; no `.venv`, source coefficient table, or machine cache was copied from the candidate.  The initial missing-module event is an environment event, not a mathematical finding.

## Mathematical statement audit

The v17-to-v18 mathematical diff is confined to the new stitched local-box result, associated version prose, and certificate appendix.  The theorem states exactly

\[
 Z=\tfrac18,\quad \tfrac{313}{500}\le x\le\tfrac7{10},\quad
 |y|\le\tfrac1{100},\quad 0<h\le1,\quad \lambda>0,
\]

for both signed lifts.  Its proof partitions the interval at `627/1000`, `63/100`, and `16/25`.  The four exact lower bounds for `D` are respectively `481771/1000000`, `239/500`, `4653/10000`, and `3849/10000`; `det(C)/S=5/72`.  Each cell has 531/531 positive Bernstein controls and a complete 71/71 left seam.  The final unique weakest control is `C_1(0,2,2)=517/1000`.  The paper expressly labels the 81 nodes per cell as diagnostics and says that no sampled sign is proof.

I found no reuse of CE-046/048/059/060 as a positive route and no assertion of the full compact ball, a general common metric, arbitrary nodes or dimension, or the fixed-lens optimum.  Chart boundaries and local certificates are not described as raw-gate counterexamples or maximality results.

## Build, bibliography, and PDF

Two more fresh ZIP extracts were cleaned and built independently with the fixed source epoch.  Both generated PDF SHA
`2f04f9b65c6c31cc9b4f806bc9e264aec4ac951dcc525d2519206ecb3c1a89fc`, identical to both frozen copies.  Final `main.log` and `main.blg` had no fatal error, undefined citation/reference, multiply defined label, warning, overfull, or underfull box.  First-pass transient messages in `latexmk` output were not confused with the final logs.

The mechanical bibliography gate found five cited keys, five BibTeX entries, and five AUX citations, with no missing or unused key.  No new reference was introduced relative to v17.

`pdfinfo` reported 42 letter-size pages, the expected title and five authors, no encryption, and no JavaScript.  All 32 font rows were embedded and subset.  The TeX source contains `Yonghua Xiong$^{*}$`; extracted PDF text contains the author and the exact declaration `Corresponding Author: Yonghua Xiong.`  Affiliations and email addresses are present.  Text scans found no TODO/FIXME marker, `qqquad`/`qquad0` artifact, or machine path.

I freshly rendered all 42 pages with Poppler and inspected every page.  There was no clipping, overlap, abnormal blank page, broken table, or overflowing formula/hash.  Pages 1, 28, 35, 41, and 42 were additionally checked at original rendered resolution for the author mark, four-cell table, certificate data, references, and affiliations.

## Fail-closed audit

The independent verifier rejected altered PDF bytes, a dropped archive member, an unsafe traversal path, a symbolic-link entry, a case-colliding duplicate, a changed theorem endpoint, and a deleted certificate.  It also rejected a dropped portable-manifest record and a changed portable member hash.  Thus neither the package gate nor the local-scope gate is permissive under the tested mutations.

## Replay

From the workspace root:

```sh
python3 tmp/research/audit/verify_v18_portable_chain_candidate_independent_final.py \
  --zip tmp/research/v18_candidate_portable_chain/common_metric_three_positivity_islands_submission_2026-08-26-v18.zip \
  --pdf tmp/research/v18_candidate_portable_chain/common_metric_three_positivity_islands_submission_2026-08-26-v18.pdf \
  --v17-main output/source_packages/common_metric_three_positivity_islands_submission_2026-08-26-v17/main.tex
```

The detailed results and the two 99-case fresh execution summaries are adjacent to this report.  The audit manifest binds the external audit artifacts after they are frozen.
