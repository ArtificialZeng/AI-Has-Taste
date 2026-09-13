# Final status: Erdős #993 — tree independent-set sequence unimodality

## Terminal classification

**NEW_STRICT_BOUND** (2026-08-29).

The theorem proved here is only this: every tree on exactly 31 vertices has a
weakly unimodal independent-set sequence.  Together with the independently
reviewed order-30 computation, this raises the certified finite
no-counterexample frontier from 30 to 31.  The universal conjecture for
arbitrary trees remains open; no induction or reduction for (n>31) is
claimed.

## Exact evidence

- fixed partition: 120/120 residue classes, modulus 120, at most 8 workers;
- exact unlabelled-tree total: `40,330,829,030 = A000055(31)`;
- non-unimodal sequences: `0`;
- non-log-concave sequences: `159`, all serialized, rebuilt with Python
  integers, and independently confirmed unimodal;
- coefficient fingerprint modulo `2^64`: `92f46f1b00c219ad`;
- parent-array fingerprint modulo `2^64`: `d53b120ed8c90b52`;
- exact arithmetic bound:
  `300,540,195^2 = 90,324,408,810,638,025 < 2^64 - 1`.

The production aggregator and a separately written no-project-import verifier
agree on the total, exception counts, and both fingerprints.  A fresh nauty
source extraction and checker rebuild reproduced an order-23 chunk exactly;
its debug build matched direct subset enumeration on all 436 unlabelled trees
through order 11.  Gate 4 passed 24/24 checks.

Four fail-closed negative controls were materialized in separate temporary
certificate roots.  Missing residue 119, a residue-000 count mismatch, a
tampered terminal sequence coefficient, and a tampered preflight hash each
returned exit code 1 with its expected rejection reason.

## Novelty and submission audit

Post-result searches of the cited primary/live records through the cutoff
found no order-31 or stronger tree-unimodality census.  The inspected SciNet
record still places the public frontier at 30 and calls order 31 the next
layer.  This is a date- and database-bounded novelty conclusion, not a claim
that unpublished or unindexed work cannot exist.

The two-pass citation audit uses the formal Kadrawi--Levit journal record,
*Ars Mathematica Contemporanea* 25(4) (2025), P4.03, DOI
10.26493/1855-3974.3207.2ad.  Bibliography closure (9/9), isolated LaTeX
build, zero-warning log audit, and five-page visual PDF inspection passed.
The final source manifest binds 559 files.  Fresh-root manifest verification,
independent aggregation, all four fail-closed controls, a clean manuscript
build, and PDF text/byte comparisons all passed.

## Deliverables

- `output/pdf/tree_independence_unimodality_order31.pdf`
  - SHA-256: `22426d70897c55f8acac4e315ba7d132194ef55aa97027a7b195b92150786f7b`
- `output/source/tree_independence_unimodality_order31_source.zip`
  - SHA-256: `56e19265911e2c9ca236d2ed628b2ca9dc52e4832b4f5bf1413a859516189c26`

## Reproduction

From the extracted source archive root:

```sh
python3 audit/order31_independent_aggregate.py
python3 audit/fail_closed_rejection_tests.py
sh audit/rebuild_order31_checker.sh
```

The full production aggregation command is documented in `README.md` inside
the archive.  The original sweep is already complete and need not be rerun.

No theorem prover or proof assistant was used.  OpenAI Codex assisted with
literature search, exact computation, program/manuscript drafting, and
adversarial auditing.
