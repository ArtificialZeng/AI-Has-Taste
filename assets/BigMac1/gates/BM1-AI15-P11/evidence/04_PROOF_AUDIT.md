# Proof and computation audit

Date: 2026-08-29 (Asia/Shanghai)

Endpoint under audit: every tree on exactly 31 vertices has a weakly
unimodal independent-set sequence. Combined with the independently reviewed
order-30 record cited in the literature ledger, this raises the finite
no-counterexample frontier to 31. It does **not** prove Erdős #993 for trees
of arbitrary order.

## Gate 4: exact-certificate matrix — 24/24 PASS

| # | Check | Exact evidence | Status |
|---:|---|---|---|
| 1 | Scope frozen before the run | `certificates/order31_preflight.json`: order 31, modulus 120, workers 8, expected 40,330,829,030 | PASS |
| 2 | Checker source frozen | SHA-256 `38fad81aaae42ab4fe4d764abd03482535b54483aa308b9b6ce924d8edd4db36` | PASS |
| 3 | Checker binary frozen | SHA-256 `93a463c656872a4e977390fcae8110cbcd558570bf06a8b78e628dad7752c00e` | PASS |
| 4 | nauty source archive frozen | SHA-256 `9fc4edae04f88a0f5883985be3b39cf7f898fd6cc96e96b9ee25452743cc1b5b` | PASS |
| 5 | Runner and aggregator frozen | Six orchestration/source hashes recorded in the preflight and rechecked by the independent verifier | PASS |
| 6 | Coefficient arithmetic fits `uint64_t` | \(i_k\leq\binom{31}{k}\leq300{,}540{,}195<2^{64}\) | PASS |
| 7 | Comparison products fit `uint64_t` | \(300{,}540{,}195^2=90{,}324{,}408{,}810{,}638{,}025<2^{64}-1\) | PASS |
| 8 | Enumeration counters fit `uint64_t` | \(40{,}330{,}829{,}030<2^{64}-1\) | PASS |
| 9 | Rooted recurrence reconstructed from definitions | `notes/referee_report.md`, including empty-product boundaries | PASS |
| 10 | Weak-unimodality predicate has two-sided failure power | exact triple-valley equivalence plus 21,844 sequence tests | PASS |
| 11 | C coefficients independently rebuilt by subsets | all 436 unlabelled trees through order 11, coefficient by coefficient | PASS |
| 12 | Deletion identity independently tested | 5,405 graph-vertex cases through order 5 | PASS |
| 13 | Rooted recurrence independently tested | 8,477 rooted cases through order 6 and 126,126 labelled rooted trees through order 7 | PASS |
| 14 | Unsplit generator count checked at order 23 | exactly 14,828,074 trees | PASS |
| 15 | Partition mechanism checked at order 23 | 24-way count and both hashes equal the unsplit run | PASS |
| 16 | All order-31 summary chunks present | 120/120 `.summary.done` files | PASS |
| 17 | All order-31 exception chunks present | 120/120 paired `.exceptions.done` files; no unexpected `.done` names | PASS |
| 18 | Checker/generator local counts agree | `trees=generated>0` in every residue | PASS |
| 19 | Exhaustive total matches the tree census | \(\sum_rN_r=40{,}330{,}829{,}030=A000055(31)\) | PASS |
| 20 | No order-31 unimodality failure | aggregate `nonunimodal=0`; no `NONUNIMODAL` serialized line | PASS |
| 21 | Production fail-closed aggregation | `results/order31_aggregate.json`, status PASS | PASS |
| 22 | Independent no-project-import aggregation | same total, exception count, and two 64-bit fingerprint sums | PASS |
| 23 | Every saved exceptional sequence rebuilt | all 159 non-log-concave parent arrays independently reconstructed with Python integers; all are unimodal | PASS |
| 24 | Isolated source rebuild | fresh tar extraction, rebuilt release/debug binaries, exact order-23 chunk fingerprint match, and subset cross-check through order 11 | PASS |

The two order-31 aggregate fingerprints are

- coefficient-sequence hash sum modulo \(2^{64}\):
  `92f46f1b00c219ad`;
- parent-array hash sum modulo \(2^{64}\):
  `d53b120ed8c90b52`.

The ordered raw-summary SHA-256 is
`6735a8eefacd2a037b16921ba11feed5d017432374389628ad068ed946894c38`;
the independent verifier's hash of the complete serialized `.done` set is
`74dfaded1fdfe4db832c0e3bb138b6f6fa0a9584bcf87940892e2fee3d23cbe9`.

### Root fail-closed negative controls — 4/4 PASS

Four fresh temporary certificate roots were corrupted one at a time.  The
independent verifier returned exit code 1 for each: missing residue 119,
residue-000 count mismatch, tampered terminal sequence coefficient, and
tampered preflight artifact hash.  The exact expected and observed messages
are recorded in `audit/FAIL_CLOSED_AUDIT.md` and
`results/fail_closed_rejection_tests.json`.

## Gate 5: adversarial roles

- **Builder:** derived the rooted gamma-cone invariant and double-leafy
  identity, then correctly made no novelty claim. The local proof is sound,
  but the endpoint is covered by Hibi--Kara--Vien (2026).
- **Breaker:** ran exact grammar, family, mutation, and rooted-tree searches,
  retained independently verifiable specimens, and found no counterexample.
  It also refuted four tempting closure lemmas. Negative discovery searches
  are not used as premises of the finite theorem.
- **Referee:** rebuilt the definitions, recurrence, and valley equivalence;
  identified and repaired the formal-statement gaps; supplied a direct subset
  evaluator sharing no DP implementation with the discovery code.
- **Root audit:** froze the order-31 implementation, proved the integer bounds,
  required a complete residue census, wrote a second parser/evaluator without
  project imports, and performed the isolated source rebuild.

No role found a logical route from the finite result to all tree orders. The
fatal gap for the original universal conjecture therefore remains explicitly
open.

## Scope and reproducibility

Primary commands:

```sh
bash experiments/run_tree_sweep_all.sh 31 120 8 results/order31_sweep
python3 experiments/aggregate_tree_sweep.py --order 31 --modulus 120 \
  --expected 40330829030 --results-dir results/order31_sweep --project-dir .
python3 audit/order31_independent_aggregate.py
sh audit/rebuild_order31_checker.sh
```

No proof assistant was used. The certificate is an exact finite enumeration
with independently audited integer evaluators and serialized logs.

## Gate 6: novelty and release — PASS

- Post-result `NOVELTY_LOCK` pass 3 found no order-31 or stronger finite
  census in the searched primary databases through the 2026-08-29 cutoff.
  This is explicitly a database-bounded conclusion.
- Citation audit: the original 24/24 claims and the terminal-revision 5/5
  claims passed; all 9 cited bibliography keys were matched to verified
  records, with no missing or unused entry.  Kadrawi--Levit is recorded by
  its formal 2025 journal publication and DOI.
- LaTeX audit: isolated build, zero warnings/errors and 9/9 citation closure.
- PDF audit: all five rendered pages passed individual visual inspection.
- Release audit: the final archive's exact file count and hashes are recorded
  externally in `audit/RELEASE_AUDIT.md`; fresh-root manifest verification,
  independent aggregation, fail-closed controls, LaTeX build, and PDF text
  comparison all passed.

The audited terminal classification is `NEW_STRICT_BOUND`: the rigorous
finite frontier is 31, while the unrestricted conjecture remains open.
