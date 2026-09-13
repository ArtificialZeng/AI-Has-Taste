# Final status: Type `D_9` absolute order normalized flow

Terminal category: **CERTIFIED_FINITE_RESULT**  
Date: 2026-08-29 (Asia/Shanghai)  
Original prompt complete: **true**

## Conclusion

The finite endpoint is proved by exact certificate:

> The absolute order `Abs(D_9)` admits a normalized flow with unit vertex
> weights.

The primary certificate gives 284 positive rational totals on a 150-node
`B_9` conjugacy-orbit quotient.  The other 325 supported orbit pairs carry
zero.  Exact uniform lifting over the reconstructed biregular orbit-pair
cover graphs satisfies every normalized row and column equation on the full
92,897,280-element poset.

This does **not** prove the conjecture for every `D_n`, a recurrence
`D_n -> D_{n+1}`, uniqueness, strict positivity on every cover, or rank
symmetry.  No `n>9` result is used or claimed.

## Frozen primary evidence

| role | file | SHA-256 |
|---|---|---|
| formal endpoint | `problem/formal_statement.md` | `a423a584b8a229845dc64dbca6233df9d7d36ca7d9a0c1a5de55571d54aca084` |
| unique primary certificate | `certificates/d9_normalized_flow.json` | `d8fe947906c577f3a7c585fc07e0bcb6648e2555056a756af98bf307ab72ea7f` |
| unique primary verifier | `certificates/verify_d9_flow.py` | `a076f7dc4a715d0adb9d1c7b7946431a7f63de744b53a8782a6c50ed7580c706` |
| no-import referee verifier | `audit/referee_verify_d9.py` | `2b2ff8f48853ed534c7d98dc6e8aab45b0413871029b35ba80f1cbd62078a8c4` |
| full referee report | `audit/REFEREE_REPORT.md` | `4a6940936fb3e582996bf2a086cd78294ea0505b374cefd5692e5bc90b7c365f` |
| release PDF | `output/pdf/d9_normalized_flow.pdf` | `c8741981935f22594dcc944e2981b166b1084f58cf6d59c455ecb9f02c08d184` |

`certificates/PRIMARY_D9_BINDING.json` is authoritative about roles.  The
alternative `discovery/d9_orbit_flow_candidate.json` and
`tests/verify_breaker_orbit_candidate.py` are cross-check-only and must not
be substituted for the primary pair.

## Independent audit

The no-import referee rebuilt the quotient from signed permutations and all
72 reflections.  It verified:

- 150 orbit types and exact total mass 92,897,280;
- 609 supported adjacent-rank orbit pairs;
- 284 positive rational orbit-flow values;
- 3,344,302,080 full Hasse covers;
- all exact quotient marginals and their full `F/E` lift;
- all nine rank layers without a symmetry shortcut;
- rejection of nine targeted mutations.

Final unresolved severity counts are **fatal 0; major 0; local 0;
expository 0**.  Carter's reflection-length dependency was bound precisely to
*Compositio Mathematica* 25 (1972), Section 2, Lemma 2, journal page 3, and
its applicability to exactly the 72 type-`D_9` root reflections was checked.

## Novelty and publication audits

Gaetz--Gao's version of record is DOI `10.5802/alco.114`; the latest arXiv
record is `1903.02033v2`.  Their paper states the conjecture and reports
computer verification through `n=8`.  Two dated public searches through
2026-08-29 located no later public `D_9`, `n>=9`, or general type-`D`
resolution.  This wording does not exclude private or unindexed work, and
network failures were recorded only as access limitations.

The citation audit, LaTeX audit, clean build, manifest verification, and
six-page PDF inspection pass.  The release has one PDF and one source ZIP.

## Reproduction

```bash
python3 -I -S certificates/verify_d9_flow.py \
  certificates/d9_normalized_flow.json
python3 -I -S audit/referee_verify_d9.py
python3 -m unittest tests.test_verify_d9_flow tests.test_breaker_crosscheck
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py \
  . manifests/release_manifest.json
```

See `REPRODUCE.md` for manuscript build commands and exact expected outputs.

## Proof assistant statement

No Lean, Coq, Isabelle, or other proof assistant was used.  No formalization
claim is made; the endpoint is an exact finite certificate checked by two
ordinary fail-closed Python verifiers.
