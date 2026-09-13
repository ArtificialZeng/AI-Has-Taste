# Checkpoint

Provenance: `bigMac-00026-p03-research-76cf6f402469` (research pass 1).

## Current exact result

- `source.md` remains immutable with SHA-256
  `89ab768f731deb6bf1cced9744fe07d7bbd5b865896b0b59dcf9e19bc59c2ac4`.
- `evidence/enumerate_gl32_subgroups.py`, run with the required research Python,
  constructs all 168 invertible binary matrices and enumerates subgroups by
  breadth-first single-element adjunction.
- The resulting `evidence/gl32_subgroup_irreducibility.json` contains 179
  subgroups. Counts by order are
  `1:1, 2:21, 3:28, 4:35, 6:28, 7:8, 8:21, 12:14, 21:8, 24:14, 168:1`.
- Exact conjugation partitions these 179 subgroups into 15 classes, of orders
  `1,2,3,4,4,4,6,7,8,12,12,21,24,24,168`. The orbit sizes sum to 179.
- Completeness is certified by checking subgroup axioms and all 30,072 pairs
  `(H,g)`: every generated subgroup `<H,g>` is again listed. Since `{1}` is
  listed, induction along any finite generating sequence proves that no subgroup
  is omitted.
- Direct action tests on all seven one-dimensional and all seven two-dimensional
  subspaces leave exactly three irreducible conjugacy classes, of orders 7, 21,
  and 168 (certificate class IDs 7, 11, and 14).
- `evidence/test_weak_ekr.py` checked all `16 * 256 = 4096` `(W,A)` pairs for
  each irreducible representative. All three classes fail. For every class the
  serialized witness is
  `W=span{(1,0,0)}` and `A={(0,0,0),(1,0,0),(0,1,0)}`: the exact orbit union is
  all of `V`, while `A-A` has four elements and `|A|=3>2=|W|`.
- `evidence/verify_certificates.py` is a standalone implementation that imports
  neither generating script. It reconstructed all matrices; repeated 45,473
  subgroup-product, 30,072 saturation, 50,400 conjugacy-element, and 12,288
  weak-EKR pair checks; retested irreducibility; and verified the three explicit
  witnesses. Every assertion passed in `evidence/verification_report.json`.
- `evidence/result.md` gives the complete argument and explicit matrix
  generators. `evidence/literature_check.md` records a focused primary-source
  comparison without making a priority claim.

## Obstacles and remaining gap

- No mathematical gap is known in the finite classification. The literature
  search was focused rather than systematic, so novelty/priority is not claimed.
- This is a researcher candidate only; it has not received the required fresh
  mathematical referee audit.

## Next test

A fresh referee should independently reconstruct `GL(3,2)` from the displayed
matrices, verify the single-adjunction completeness argument and conjugacy
partition, retest the 14 proper nonzero subspaces for each representative, and
check the three `(L,W,A)` witnesses directly before accepting the exact candidate
scope.
