# Proof audit

Audit date: 2026-08-29 (Asia/Shanghai)  
Endpoint: `Abs(D_9) admits a normalized flow with unit vertex weights`  
Decision: **PASS -- CERTIFIED_FINITE_RESULT**

## Frozen primary pair

| Role | Path | SHA-256 |
|---|---|---|
| formal theorem statement | `problem/formal_statement.md` | `a423a584b8a229845dc64dbca6233df9d7d36ca7d9a0c1a5de55571d54aca084` |
| unique primary certificate | `certificates/d9_normalized_flow.json` | `d8fe947906c577f3a7c585fc07e0bcb6648e2555056a756af98bf307ab72ea7f` |
| unique primary verifier | `certificates/verify_d9_flow.py` | `a076f7dc4a715d0adb9d1c7b7946431a7f63de744b53a8782a6c50ed7580c706` |
| primary binding | `certificates/PRIMARY_D9_BINDING.json` | `6440797ce594b1e07365e97f251b6796d0d3afc5acc8a23a63ca22d99de75e57` |

The alternative `discovery/d9_orbit_flow_candidate.json` encoding and
`tests/verify_breaker_orbit_candidate.py` checker are frozen as
cross-check-only.  They are not release substitutes for the primary pair.

## Independent no-import referee

The independent verifier `audit/referee_verify_d9.py` has SHA-256
`2b2ff8f48853ed534c7d98dc6e8aab45b0413871029b35ba80f1cbd62078a8c4`.
It uses only the Python standard library and the primary JSON certificate.
It neither imports nor executes `src/`, `discovery/`, `tests/`, or the
primary verifier.

Command:

```bash
python3 -I -S audit/referee_verify_d9.py
```

Independent reconstruction result:

- 150 signed-cycle orbits and 72 reflections;
- rank orbit counts `(1,1,3,5,11,17,29,35,34,14)`;
- rank sizes
  `(1,72,2220,38304,405174,2702448,11228300,27491616,34812945,16216200)`;
- 609 supported adjacent-rank orbit pairs;
- 284 positive exact rational orbit-flow totals;
- 3,344,302,080 full Hasse covers;
- exact rational and denominator-cleared integer marginal equations on all
  nine layers;
- uniform `F/E` lifting to every full-poset vertex equation.

The referee separately checked Carter's Lemma 2 at journal p. 3 and proved
that its root reflections are exactly the 72 reflections in the formal
`D_9` endpoint.  It also audited the `B_9` automorphism action, including the
legal re-fusion of split `D_9` conjugacy classes.

## Fail-closed tests

Every successful referee run also verifies rejection of:

1. primary hash mismatch;
2. missing rank layer;
3. missing positive flow;
4. valid orbit substituted at a wrong-rank endpoint;
5. altered source degree;
6. altered edge count;
7. negative rational;
8. noncanonical rational such as `2/2`;
9. altered rank size.

All nine mutations return `REJECTED`.  The parser also rejects duplicate
keys, floats, non-finite data, unknown or missing fields, and booleans used
as integers.

## Dependency closure and scope

| Dependency | Result |
|---|---|
| `B_9` acts by automorphisms of `Abs(D_9)` | PASS |
| signed-cycle orbit classification, parity, and centralizer masses | PASS |
| Carter reflection length and exact applicability | PASS |
| ranks and all rank totals | PASS |
| exhaustive cover support and both multiplicities | PASS |
| biregular orbit edge conservation | PASS |
| exact quotient marginals and full lift | PASS |
| no rank-symmetry shortcut | PASS |
| fail-closed verification | PASS |
| theorem restricted to `D_9` | PASS |

Final unresolved severity counts: **fatal 0; major 0; local 0; expository
0**.  The general all-`n` recurrence remains open and is outside this finite
endpoint.  No computation for `n>9` is present or used.

No Lean, Coq, Isabelle, or other proof assistant was used.  The result is an
exact, independently checked finite certificate, not a proof-assistant
formalization.
