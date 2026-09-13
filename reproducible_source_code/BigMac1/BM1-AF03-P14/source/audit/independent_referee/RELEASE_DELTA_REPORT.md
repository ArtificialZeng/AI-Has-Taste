# Release-delta hostile referee report

Date: 2026-08-30 (Asia/Shanghai)  
Mode: independent standard-library CLI; no project imports  
Verdict: **PASS**  
Submission-gate delta: **PASS**

## Finding counts

| fatal | major | local | expository |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |

## Bound release inputs

```text
1bcccfa9a6db0660c1e3d349351ad4740ea7f9ea5b90e050701c94bb7f19bd58  paper/main.tex
1d53b2d70c0ee37e306929414e3c7d4b84baaa7469868c204bcf4a4fa03ea85f  proof/main_proof.md
af44b6d7739996eab1726eaca41f3078aa1b9efd20cb78cc8ca0e5efbcd375e5  audit/independent_referee/frozen_inputs.json
b781d39f0b89fda14a8969458d098942569d0ad191103546d8904ec4566bc1a2  src/verify_all.py
18f6a4fb55480a3d097d6b96b2d69fa7497f4e7ccf88b689083b267139de4903  audit/verification_log.json
e6ce6ac216afa419442acc9cb6cce3dd256826a5ab28f9262bfd9e5fba5ab73d  audit/independent_referee/independent_verifier.py
333821801a789688976abea57f6d76475f4b6c8eb955e4a6008ca4983289ff6b  audit/independent_referee/verification_result.json
7e65526dc9cb321003c2592a78058d1ac52b68de89e403988af15f17665823ee  audit/independent_referee/release_referee.py
```

The CLI recomputed all 17 hashes in the frozen binding.  It also bound the
current paper, proof, master verifier/log, independent verifier/result, all
nine decisive certificate files, bibliography, citation audit, claim ledger,
and release novelty log.

## Paper-only delta

PASS checks, unless a finding is listed below:

- release date is exactly August 30, 2026;
- Ambrus--Gargyan 2024 Conjecture 1.3 is stated with `n>=2` and `Q_n`;
- Ambrus--Gargyan 2025 is stated with `n>=4` and `3<=k<=n-1`;
- Pournin's correction is limited to the omitted proper-subdiagonal transverse
  constrained-Hessian term and explicitly preserves the main diagonal;
- the Q3 certificate-table row occurs exactly once and every endpoint row in
  that table is unique.

Reversing only those three textual replacements (date, Conjecture 1.3 sentence,
and AG25/Pournin paragraph) reconstructs the preceding paper SHA-256 exactly:
`1f2237109932b4b017e9d017187923b8d0f79a0ab2b1f93384ce8e53f217556a`.  The two theorem blocks have their frozen hashes, the
proof is byte-identical, and all nine certificate hashes are unchanged.

## Citation and novelty boundary

The citation surface is exactly five keys and matches the five-entry BibTeX
database.  The separately frozen audit contains exactly C01--C11 and reports
11/11 verified, zero unverified.  The release novelty rerun is dated 2026-08-30
and the paper uses only a database-bounded not-found statement.

## Exact gates

- frozen binding: 17/17;
- master log: 23/23 checks PASS;
- independent result: 17 hash-bound inputs PASS;
- decisive certificate hashes: 9/9 unchanged;
- Q3 table row: 1/1, with no duplicate endpoint row.

## Findings

None.

## Decision

**PASS: submission-gate delta PASS.**
