# R-M1 coordinated repair and freeze record

Date: 2026-08-29 (Asia/Shanghai)  
Status: repair complete; same hostile referee final verdict PASS

The mathematical theorem and every certificate datum are unchanged.  The
authorized text-only minors remove the unsupported word “global” from the
description of (d_1), state the parser contract precisely in the paper, and
remove the duplicated word in the proof DAG.  The final publication cleanup
also corrects the paper's Q3 exponent from (a^2) to (a^3) and restores six
missing TeX backslashes in the proof.  No theorem scope or certificate datum
changed.  No generated paper PDF or source ZIP exists.

## Exact repair scope

All release-gate JSON loaders now reject duplicate object keys at every depth
and reject booleans outside explicitly boolean fields.  This includes the six
non-star1 Q3/Q5 chamber loaders, the Q4 saddle verifier, the Q5 saddle
verifier, the independent star2 verifier, and the no-import referee loader.
The star1 primary and independent loaders were already hardened and were not
changed.

The added/revised attacks prove rejection as follows:

- `tests/test_nonstar1_json_failclosed.py`: 17/17 attacks rejected across Q3,
  empty, star2, star3, star4, and triangle;
- `src/breaker_test_verifiers.py`: valid Q4/Q5 controls accepted and 11/11
  corruptions rejected, including six new duplicate/nested/bool attacks;
- `src/breaker_star2_audit_tests.py`: valid control accepted and 9/9
  corruptions rejected, including three new duplicate/nested/bool attacks;
- `audit/independent_referee/test_parser_failclosed.py`: four malformed parser
  attacks rejected; the sole canonical star3 boolean is accepted as a control.

The expanded master run reports 23/23 checks PASS.  The no-project-import
referee core reports PASS on 17 hash-bound inputs and embeds the verifier and
binding hashes listed below.

## Frozen SHA-256 values

```text
b781d39f0b89fda14a8969458d098942569d0ad191103546d8904ec4566bc1a2  src/verify_all.py
a480c22e49928e7ce8d7360b69869dec5c215f3009680778ff308710f1b98eab  audit/verification_log.json
8f25404fc08ff0468cd413bdca66c80b8d3ffa791db6ea17e89c811ded89b699  audit/independent_referee/frozen_inputs.json
e6ce6ac216afa419442acc9cb6cce3dd256826a5ab28f9262bfd9e5fba5ab73d  audit/independent_referee/independent_verifier.py
896229b63ac2d877c49e7272913e07f62d8d6612ab38c46e9816518b4052c3cf  audit/independent_referee/verification_result.json
e4a9e2008777dad92189772c2f967b2c1f9f7bc56a630e507964c3a4243982c4  audit/independent_referee/mutation_tests.py
4a31dabad8f83d399c67e4fde472d02540ac2ca2ce8b815f71e143822b84d897  audit/independent_referee/mutation_results.json
82db691efc8db2ee2f453cca9bd5519620592410befa518dcc5240fd1d13a946  audit/independent_referee/test_parser_failclosed.py
09cf73ba05de8a6e5cb09300c73514aa9b9f1ae1ada6c81f8c90cb7690e21292  tests/test_nonstar1_json_failclosed.py
44936e45e6562098fbaece6d97964ed299d5f2daee892d140163d1f5927bf740  src/breaker_test_verifiers.py
92f7dcc77c8be50bdd59fd28500864d67cc69675d8b3ddf84571a5b11814cab1  audit/saddle_mutation_log.json
d41b43ad60382393e0375f596e38f04d8ceedc3c76711bdee4e21c2b0f091ca6  src/breaker_star2_audit_tests.py
c287e1c78314d197ac175e64f3a9485382d731968a3910b675a68c3419c42d42  audit/star2_audit_mutations.json
17a76acbfc92a7f1be82425c4d07ad03299be862866dfdb7eecc1e905c3ce20a  src/breaker_verify_q4_baseline.py
7b8a9f4bd4a2397ca55872c441fed22f1e3eba30040c9ec3367192571091eba4  src/breaker_verify_saddle.py
968c765dcf648ab47daef92dd1ef44188633e9a8219190b201de176fce9e6b31  src/breaker_star2_audit.py
721fef86dbf05f771ecf753aa2ef79c02204596f720cd775ef6ce36ad0edba4f  src/verify_q3_classification.py
8c4116ca8b9826ac0d1275fb2b35511798e43569e67369dfd594407cd65ea29c  src/verify_empty_highpair_classification.py
cd62fc35a8feb969a54100e6a8f8e3b72d9849a75656dd1769aa0356ce1368a2  src/verify_star2_bernstein.py
c4d1c14890cafec57c654dcf3fadbed4a7b629f7396778a5b89b1cd9e3f40943  src/builder_verify_star3.py
d83386a7256562094b3bee44dcb1115efc58e755509a1130c3ba6815fa081dbb  src/breaker_star4_verify.py
a7b854f04269cb8aa746dabf3217fc0b623b365b13f074b11b1b2c95dc7a0626  src/verify_triangle_highpair_no_go.py
541f96588b6b5a599b9264dc2fe816a1bf269af19a70f4fd6665e9ee90bd082c  src/builder_verify_star1.py
095eaa7a5d1ba0553e46368fbe66075880b1de6a3e1248fea9d789baef61485a  src/breaker_star1_audit.py
9efea55706eff402c44716dddba1a7e8e2258a0d75c164d4a86beffd75e783e2  src/breaker_star1_audit_tests.py
1d53b2d70c0ee37e306929414e3c7d4b84baaa7469868c204bcf4a4fa03ea85f  proof/main_proof.md
1f2237109932b4b017e9d017187923b8d0f79a0ab2b1f93384ce8e53f217556a  paper/main.tex
7c592c2baaafb86c50a06a1c013e1cfb26d601eff3cfed69dc9e70d20c1ca749  proof/proof_dag.md
e5e6f978e300788fd1d79666461e464251dd4636df0f4fd5434082b8b2465f31  proof/referee_report.md
8786f25cdb545b73b4f10d2e242e176c64b2353c8cb2ba7783b78e6c12b9a67e  audit/independent_referee/REFEREE_REPORT.md
d622bd2395f475d5b0411695df13d7c8b7277c5f0decc818ef77141278d3d2fc  audit/independent_referee/hostile_referee_verdict.json
```

The certificate hashes remain the values already bound in
`audit/independent_referee/frozen_inputs.json`; in particular star1 is
`70cf7f98...`, empty `3d5c97a2...`, star2 `fd591e36...`, star3
`f966e220...`, star4 `b57cad6a...`, triangle `5e0bab27...`, Q3
`6f704264...`, Q4 saddle `1c732a3b...`, and the Q5 saddle certificate
`6bac02ad...`.
