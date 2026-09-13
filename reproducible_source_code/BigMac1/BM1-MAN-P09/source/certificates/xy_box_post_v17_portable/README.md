# Parallel portable chain for the four post-v17 cells

The directory `xy_box_post_v17/` preserves the 32 principal historical
artifacts and their original hashes.  Some historical manifests in that
layer name generated transcripts intentionally omitted from the portable
archive.  They are provenance anchors, not package-local replay promises.

This parallel directory supplies a self-contained replay layer without
rewriting any historical evidence.  Each rational cell has fresh
relative-path source and independent-referee runs, fail-closed attacks,
source/referee portable manifests, and a 16-record cell manifest.

| cell | source manifest | referee manifest | cell manifest |
|---|---|---|---|
| `313/500..627/1000` | `079e807d4d6ae7d109884d9ccd6dacbe03ccd39bd2e82f4bd8ab4b69108ee800` | `8000cfbd28c4deeb4edd0341564fdb114fc91b789bdd993ae01cb3a8dcecd816` | `6945bdc3d36e5faab9feaa0539fc7b3ba9dbb4ff60d9a86079dba79456c2f8d8` |
| `627/1000..63/100` | `ad996685d1e50a582b3f927061537e00c6f73bab512e55b51b6d303e29d58d21` | `4f399a4cec98b1471da3908df3a155b8263024264b1071a05030a62f4411a4f6` | `de5bb56df9852f584b4c4d2ad736df9345dcc396aff6de8d3e31bc43c7f15c08` |
| `63/100..16/25` | `5d2d5af1fde67e04cfc45864712c60b7f37dd7196ccba9a6566396590d11c215` | `bcc24dd2b210aedd3e37e2e27b312651bd5c26bd4ae8115bbf230e2a6d5ced62` | `850cb604657c0abc27a9f64440c85e1f4d8c8f31a9acd19aa6477e442e3b0dcf` |
| `16/25..7/10` | `bf1217f238efb5d9bae91970b2c76e894236e7a23fb66b782dde9525cbec5b83` | `b50be35985017a5e5ee6ccd7dc73467db665f1a05156bdb1ab94fa5c2c048d5c` | `8ef52afcb9c9bb840f82933f743a84d12a54f236b60cc1c7fa62edc5d88a71f1` |

From the package root, run `verify_portable_manifest.py` on each cell manifest
with `--kind cell --expected-count 16`, then on
`PORTABLE_CHAIN_MANIFEST.sha256` with the count recorded in that file's
companion replay log.  Every source/referee verifier also rejects injected
missing-record and bad-member-hash attacks.

The mathematical scope is unchanged: this is a strict stitched local theorem,
not the full compact ball or the general common-metric problem.
