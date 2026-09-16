# Frozen source — win-00058-p02

## Problem

Fix the canonical 952 length-54 ternary codewords and the proof framework of Xu--Fu--Qiao--Tao, arXiv:2609.04122v1, Appendices D--E. With the published exact event-volume construction and the fixed charge parameters

```text
alpha = 51/100000, beta = 3/10,
```

determine the least integer denominator `D` that this same fully certified framework proves, where the desired conclusion is a non-strict normalized insertion/deletion distance gap at least `1/D` for all adjacent intervals. Decide `D=226` first.

Changing `D` changes both the exact LLL inequalities and the bounded one-/two-deletion shells. It is forbidden to reuse the published `D=227` exclusion list blindly. A proof for smaller `D` must cover every newly relevant event total by exact enumeration, an analytic bound, or a separately checked structural certificate. If `D=226` fails, report the first exact failed inequality or an explicit shell witness and scope the conclusion to this fixed method; do not claim global optimality of 227.

## Primary source and contribution boundary

- H. Xu, S. Fu, Y. Qiao and D. Tao, *Synchronization Strings over the Optimal Alphabet*, arXiv:2609.04122v1, Theorem 1.5 and Appendices D--E: https://arxiv.org/abs/2609.04122
- Accompanying primary artifact: https://github.com/xxxhhbb/ternary-synchronization-strings-artifact , frozen intake commit `5e9e0c05fca32a5d5735cab9914626ffe667c53c`.
- The source proves `D=227` and hence every `epsilon>226/227`. The artifact's exact-rational verifier exposes `--denominator`, while its published certificate exclusions are specific to totals needed for 227.
- Proposed delta: a rigorously covered `D<=226` is a genuine explicit-parameter improvement. Otherwise, an exact method-specific obstruction may be retained as research evidence but proceeds to publication only if referee finds independent value.

## Cheapest decisive test

Verify artifact integrity and the default `D=227` run first. Then run the exact LLL diagnostic for `D=226` without importing denominator-specific exclusions. Identify the small totals whose raw event bound is insufficient, and audit only those shells. Record interpreter versions, commit, file hashes, commands, exact outputs and wall times. Floating-point output is diagnostic only.

## Provenance

- Primary PDF: `batches/inbox/bigWin-58-materials/2609.04122.pdf`, SHA-256 `930511506e2363891fd289c662273b496a5839286f01cf4f7eeb185a3b64668a`.
- arXiv source: `batches/inbox/bigWin-58-materials/2609.04122-source.tar`, SHA-256 `ef907199aebdef27978c600b8987bcac0a06392d36385c858c160819530364de`.
- GitHub checkout: `batches/inbox/bigWin-58-materials/ternary-synchronization-strings-artifact`, commit `5e9e0c05fca32a5d5735cab9914626ffe667c53c`.

