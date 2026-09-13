# Gate 4 synchronization audit after the \(t=17\) exclusion

Date: 2026-08-29  
Role: bounded independent referee/synchronization review  
Policy: read-only review of the frozen proofs, checkers, logs, status, and
literature records; this report is the only project file created

## Verdict

**PASS with three local documentation issues.**  There is no fatal or major
mathematical/certificate issue in the reviewed snapshot.  The status,
structural summary, proof DAG, gap ledger, and literature records consistently
state the audited partial theorem

\[
t\ge18,
\qquad \sum_{j=1}^5q_j\ge23,
\]

for any hypothetical eleven-point equilateral set in \(\ell_1^5\).  They do
not promote it to a solution of the original problem: every \(t\ge18\)
branch remains untreated, no eleven-point witness is known, and
\(e(\ell_1^5)=10\) remains open.

The finite Python checkers are also described with the correct scope.  They
certify exact finite arithmetic, partition, endpoint, and loss enumeration;
they do not machine-prove the frame or singleton-compression implications.

## 1. External 16-process matrix

The matrix runner was invoked by absolute path with current working directory
`/tmp`, outside the project:

```bash
matrix='/Users/mac/Documents/ChatGPT/ai15-open-math-2026-08-28-batch/06_kusner_l1_5_equilateral/audit/run_t16_t17_checker_matrix.py'
cd /tmp
python3 "$matrix" > /tmp/referee_round4_sync_matrix.json
```

The fresh execution returned exit code zero and `status: PASS`.  Its four
cases, each run in normal, optimized, isolated, and optimized-isolated modes,
gave all 16 expected outcomes:

| Case | Modes | Expected | Observed exits/verdicts |
|---|---:|---|---|
| `t16_genuine` | 4 | PASS | four exit-0/PASS results |
| `t16_tampered_proof` | 4 | FAIL | four exit-1/FAIL results |
| `t17_genuine` | 4 | PASS | four exit-0/PASS results |
| `t17_tampered_proof` | 4 | FAIL | four exit-1/FAIL results |

Thus “16/16” means 16 expected genuine-or-tamper outcomes, not 16 genuine
proof validations.  The eight genuine executions passed and the eight
one-byte proof mutations failed closed.

The runner reported `external_workdir_inside_project: false`, four cases,
16 processes, and zero AST assert nodes in both checkers.  The bound hashes
were:

| Artifact | SHA-256 |
|---|---|
| `audit/run_t16_t17_checker_matrix.py` | `3fae216743c8f7f24f91cbf7315df5b681e19c360e0357a294661343540a7149` |
| `audit/referee_t16_check_postfix.py` | `12108c0614bf59e54403d7936821d0f23414927cc99fd1c4fe4a2b4008b66b69` |
| `audit/referee_t17_check.py` | `f7352bb8e590e163fe8d5c3d8af8b6917a52114dfdbfb868957079cdc58b17c3` |
| `proof/t16_branch.md` | `114d861529243e3eb96415e10f14920370b91f5085d1538fc0bb0f564e26d889` |
| `proof/t17_branch.md` | `5332a2acc28a5407b3837c28fe4d007fae64d8031ad18a64e6b8177e32e856a3` |

The fresh output SHA-256 was
`13a510283a47f0dbc42bafccc8893d2851ccf8e22c963ba5022f370f3efe22b5`.
The already recorded
`logs/referee_t16_t17_check_matrix.json` has SHA-256
`ff89b5da6ce26f2b21aea9b96cddbf1c53df6691535f9c4df222c6e53d4b2293`.
The two JSON files naturally differ in timestamps, temporary paths, and
captured command/output hashes, but their runner/checker/proof hashes, mode
list, assert counts, case count, process count, and all expected verdicts are
identical.

## 2. File-by-file synchronization review

### `TASK_STATUS.json`: PASS

SHA-256:
`8868998fa41c39eaf462dd80190b0ecb7a8eb6dd92d256399df8c15accf57dbb`

The file parses as JSON with no duplicate keys.  It remains in the nonterminal
`running` state with `original_prompt_complete: false`.  Its summary and
evidence distinguish the support-18 partial theorem from the unresolved full
problem and accurately cite the 48-process fail-closed matrix and the separate
16-process \(t=16/17\) matrix.  Every one of its 33 listed deliverable paths
exists.  No checker is represented as certifying the human linear-algebra
steps.

### `proof/structural_reduction.md`: PASS with local notation issue

SHA-256:
`ef4a5e4e87e76a5ebcccb0ca84ecf323bf853e390fa249f2fb925884f1810280`

Section 5 correctly summarizes the zero-set compression for \(R\le8\), the
unique-negative extension at \(R=9\), the two/three/five surviving patterns
at support 15/16/17, and the conclusion of at least 18 gaps and 23 levels.
It explicitly says that compression and frame deductions are human proofs
and that the checkers have finite arithmetic/enumeration scope.  The final
limitation correctly leaves every support-at-least-18 branch open.

Local issue **SYNC-T-NOTATION**: Sections 3--4 use \(q\) for the total
positive-gap count, but Section 5 switches to \(t=15,16,17\) and concludes
\(t\ge18\) without explicitly defining \(t=q\) in this document.  The
intended meaning is unambiguous from the cited branch notes, but one sentence
`put t=q` would make the summary self-contained.

### `proof/proof_dag.md`: PASS

SHA-256:
`ced179e562118c80e74599e417360ef198278d4e4f8e1e62f50346877f7ef5d0`

Steps 17--23 accurately record the successive exclusions at \(t=15,16,17\)
and the resulting support/level lower bounds.  The final paragraph correctly
limits independent computation to finite arithmetic and retains the frame
and compression deductions as human proofs.  The full target is explicitly
open on support at least 18.

### `proof/gap_ledger.md`: PASS

SHA-256:
`b216dfebf88465cf730869f9b915f399d8d6a1f8a7dbd8fe82380feb8614122d`

G07--G09 are accurately marked resolved through \(t\ge18\).  G01, G03, and
G10 remain open; in particular G10 identifies the untreated \(t\ge18\)
strata and the new \(R=10\) boundary.  This is consistent with both the proof
and the nonterminal task status.

### `literature/NOVELTY_LOCK.md`: PASS

SHA-256:
`324d97fb8f33cac0e041a15e9580fd0f560ef24807ecfce16afdd2efcf56302a`

The first lock continues to classify the original \(n=5\) problem as open.
The second lock states only a bounded no-match result for the internal
support-18 theorem, cites the proof/audit chain, and explicitly says that
unpublished, unindexed, or differently phrased prior work may exist.  It does
not convert the internal partial theorem into a full solution or an absolute
novelty claim.

### `literature/claim_ledger.md`: mathematical content PASS; two local issues

SHA-256:
`f33b43a28d75e02965f9ce60859b0497400833ad9271dd3ca003b5dd3d372585`

KUS-018 accurately states the support-18/23-level theorem, its audited proof
dependencies, bounded novelty confidence, and the open \(t\ge18\) limitation.
The earlier source claims remain compatible with the current open-problem
status.

Local issue **SYNC-CLAIM-TABLE**: a blank line separates KUS-018 from the
KUS-001--KUS-017 Markdown table.  A GFM render with Pandoc produces one table
ending at KUS-017 and renders the literal KUS-018 pipe row as a paragraph.
Removing that blank line would restore KUS-018 to the claim table.  The
absolute-value bars in KUS-005 and KUS-010 were also render-tested and remain
inside the intended cells under GFM math parsing; they are not counted as
additional issues.

Local issue **SYNC-CLAIM-FREEZE**: the only freeze metadata at the top says
`Claim freeze: 2026-08-29 11:17 CST`, but KUS-018 incorporates the later
S27--S36 sweep completed at 12:20.  `NOVELTY_LOCK.md` records the second lock,
so the evidence is available, but the claim ledger should label KUS-018 as a
post-freeze addendum or record a second claim-freeze timestamp.

### `literature/search_log.md`: PASS

SHA-256:
`a2cbbe06840b2e588d3af08f456ceef5fb33b4eb2b10e33d826ab1b7f298224c`

The initial Gate-1 sweep and the later structural-result sweep are separated
chronologically.  The log honestly records that S27--S35 first targeted the
support-16 version and S36 targeted the strengthened support-18 claim.  Its
final paragraphs state only bounded negative evidence and preserve the open
status of the original problem.

## 3. Format checks

`TASK_STATUS.json`, the recorded matrix JSON, and the fresh matrix JSON all
parse successfully with no duplicate keys.  All six reviewed Markdown files
have balanced code fences and valid relative Markdown link targets.  GFM
rendering found no broken table except the orphan KUS-018 row described above.

## Issue ledger

| Severity | ID | Finding | Effect |
|---|---|---|---|
| Fatal | -- | None. | The original problem remains honestly open rather than falsely closed. |
| Major | -- | None. | The support-18 theorem and certificate boundaries are synchronized. |
| Local | SYNC-T-NOTATION | `structural_reduction.md` switches from \(q\) to undefined \(t\). | Notational self-containment only. |
| Local | SYNC-CLAIM-TABLE | The blank line before KUS-018 leaves it outside the Markdown claim table. | Rendering/ledger structure only. |
| Local | SYNC-CLAIM-FREEZE | The claim ledger lacks metadata for the post-11:17 KUS-018 freeze/addendum. | Provenance timestamp only; the second search itself is logged elsewhere. |

## Proof-assistant disclosure

No proof assistant was used in this synchronization audit.  The external
matrix tests fail-closed execution and exact finite computations; it is not a
formal proof of the human frame/compression arguments.
