# Exact verifier hash lock

**Lock date:** 2026-08-29 (Asia/Shanghai)

The following hashes bind the correctness-critical programs and their exact
serialized inputs after the fail-closed repair and the transfer-automaton
addition.

| Role | Program SHA-256 | Input SHA-256 |
|---|---|---|
| canonical colour-block verifier | `a5e0fb1d56df089e5fe6ce3f4c44f26f712cceeb0056249f944330b916c54a00` | `d9d5589991ec9292f2844a93edb092a268d14de594cfdc5835d9f01e2350cdb8` |
| independent definition-level verifier | `9ed9fe4ad7cfc8c09dc23c2336f8b531585ac984588bd9b98b62975f2949e359` | `06805b48a6411beb2b9c4764b6420b29a314cfe067312dd820158b919705fd85` |
| repaired alternate one-flip verifier | `a142f97841cc7e74dccd5cf951de21d3e4f54a569a9df9ebc23b261107828268` | `ff2d77c2e21b883c6588036137c5482f72a2bbfff3723151d8ab5b72f66a677c` |
| seam-correct transfer/cone verifier | `73fd784626dd01a8749be6ac1cade2cf18c07c6b01c98185a6757f2562d871f2` | `3d805efc718fbbd507aabe3cf7e9595e4dfe9f51f4b9f54d6c73cb3885650774` |

The primary fail-closed regression harness has SHA-256
`226022fc6ee40687e2e10445f05f19f1b412d1ee565de31497cca7e59cda90d3`;
its 12-cell raw result has SHA-256
`214e68da395d7cbb96df1ae14159bf2f5f017bc9e9356cb647c143d4617d761c`.

All four verifiers pass under `python3 -O -I`.  The repaired primary verifier,
its adversarial harness, and the transfer verifier have zero Python AST
`Assert` nodes.  The builder and independent verifiers also contain no bare
language `assert`; their explicit failure branches remain active under
optimization.

No proof assistant was used.
