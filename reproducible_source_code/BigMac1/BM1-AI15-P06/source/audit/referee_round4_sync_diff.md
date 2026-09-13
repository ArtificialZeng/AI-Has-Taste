# Round 4 synchronization: minimal post-fix diff audit

Date: 2026-08-29  
Role: independent narrow diff reviewer  
Scope: the three local issues from `audit/referee_round4_sync.md` only

## Verdict

**PASS: all three local issues are resolved.**  The edits are minimal and do
not change any mathematical claim, proof dependency, checker scope, novelty
qualification, or open-problem limitation.  No fatal, major, or remaining
local issue was found in the edited passages.

No target file was modified by this audit.

## Snapshot bindings

| Target | Pre-fix SHA-256 | Post-fix SHA-256 |
|---|---|---|
| `proof/structural_reduction.md` | `ef4a5e4e87e76a5ebcccb0ca84ecf323bf853e390fa249f2fb925884f1810280` | `6e8c1558fadb46d98b0aebf4b776749c7d7a00879d6776b453637599bd81931b` |
| `literature/claim_ledger.md` | `f33b43a28d75e02965f9ce60859b0497400833ad9271dd3ca003b5dd3d372585` | `f8d4c373793632e0c12425b07886c3ca09e935fe933059f7d1a667b72eb407be` |

Reverse-applying only the reviewed fixes in memory reproduces both pre-fix
hashes exactly.  This confirms that the relevant deltas consist only of the
declared notation addition, line reflow, strict-result metadata line, and
removal of the table-breaking blank line.

## Issue-by-issue review

### SYNC-T-NOTATION: resolved

Section 5 of `proof/structural_reduction.md` now begins:

\[
t=q=\sum_j\ell_j.
\]

Every subsequent use of \(t=15,16,17\) and \(t\ge18\) is therefore tied
explicitly to the positive-gap count \(q\) used in the earlier sections.
The surrounding sentence was reflowed only; the compression argument and
its scope are unchanged.

### SYNC-CLAIM-TABLE: resolved

The blank line between KUS-017 and KUS-018 has been removed.  A fresh Pandoc
GFM render produces one continuous claim table containing both KUS-017 and
KUS-018, with no literal pipe-row paragraph after the table.

### SYNC-CLAIM-FREEZE: resolved

The freeze metadata now distinguishes:

```text
Claim freeze: 2026-08-29 11:17 CST (UTC+08:00).
Strict-result update: 2026-08-29 12:20 CST (UTC+08:00).
```

This accurately records that KUS-018 uses the later S27--S36 strict-result
sweep while preserving the original Gate-1 freeze time.

## Reproducible checks

```bash
shasum -a 256 proof/structural_reduction.md literature/claim_ledger.md
pandoc -f gfm -t html literature/claim_ledger.md \
  -o /tmp/claim_ledger_postfix.html
```

Observed post-fix hashes are the values in the snapshot table above.  The
render contains one claim table, both `KUS-017` and `KUS-018` occur before
its closing tag, and there are zero literal pipe-row paragraphs.

## Proof-assistant disclosure

No proof assistant was used.  This was a textual/provenance diff audit only.
