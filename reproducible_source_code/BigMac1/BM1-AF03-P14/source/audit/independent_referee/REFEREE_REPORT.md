# Independent no-import referee report: final cleanup revision

Date: 2026-08-30 (Asia/Shanghai)  
Formal verdict: **PASS**  
Publication claim: **none**

## Finding counts

| fatal | major | local | expository |
|---:|---:|---:|---:|
| **0** | **0** | **0** | **0** |

The complete frozen endpoint passes.  Modulo signed coordinate permutations,
the locally extremal directions are exactly $d_1,d_2,d_5$.  The unique
non-diagonal full-support critical orbit is
$(\alpha,\alpha,1,1,1)$, where
$\alpha=(24+\sqrt{69})/13$, and has tangent signature $(1+,3-)$.  The
support-four orbit $(1,1,2,2,0)/\sqrt{10}$ is also a saddle.

## Bound hashes

```text
1d53b2d70c0ee37e306929414e3c7d4b84baaa7469868c204bcf4a4fa03ea85f  proof/main_proof.md
1f2237109932b4b017e9d017187923b8d0f79a0ab2b1f93384ce8e53f217556a  paper/main.tex
8f25404fc08ff0468cd413bdca66c80b8d3ffa791db6ea17e89c811ded89b699  audit/independent_referee/frozen_inputs.json
b781d39f0b89fda14a8969458d098942569d0ad191103546d8904ec4566bc1a2  src/verify_all.py
a480c22e49928e7ce8d7360b69869dec5c215f3009680778ff308710f1b98eab  audit/verification_log.json
e6ce6ac216afa419442acc9cb6cce3dd256826a5ab28f9262bfd9e5fba5ab73d  audit/independent_referee/independent_verifier.py
896229b63ac2d877c49e7272913e07f62d8d6612ab38c46e9816518b4052c3cf  audit/independent_referee/verification_result.json
e4a9e2008777dad92189772c2f967b2c1f9f7bc56a630e507964c3a4243982c4  audit/independent_referee/mutation_tests.py
4a31dabad8f83d399c67e4fde472d02540ac2ca2ce8b815f71e143822b84d897  audit/independent_referee/mutation_results.json
82db691efc8db2ee2f453cca9bd5519620592410befa518dcc5240fd1d13a946  audit/independent_referee/test_parser_failclosed.py
```

All 17 bound inputs and all nine decisive certificates match their stored
SHA-256 values.

## Coverage table

| Endpoint | Result |
|---|---|
| formal quantifiers, symmetry, support convention | PASS |
| coarea/truncated-power formula and $C^3$ wall regularity | PASS |
| dominant region and singleton balance wall | PASS |
| six shifted-intersecting chamber graphs | PASS |
| every full-support pair wall and coincident-wall stratum | PASS |
| empty closure | PASS: diagonal only |
| star1 closure | PASS: one algebraic saddle |
| star2 closure | PASS: no critical point |
| star3 closure | PASS: no ordered root |
| star4 interior and boundary routing | PASS |
| triangle closure | PASS: no ordered root |
| exact full-support Hessian typing | PASS |
| $Q_3,Q_2,Q_1$ supports | PASS |
| complete written and independently reconstructed $Q_4$ exhaustion | PASS |
| zero-coordinate support splice | PASS |
| local types of $d_1,\ldots,d_5$ | PASS |
| nonzero-factor/saturation audit | PASS |
| theorem wording versus certified endpoint | PASS |
| canonical fail-closed release integrity | PASS |

The $Q_4$ saddle certificate is used only to certify the tangent form at
$(2,2,1,1)$.  Exhaustion is supplied by the two exact branches in
`proof/agent_builder_report.md` Section 3 and the independent reconstruction:
the first piece forces either the diagonal or ratio $2$; the second piece
reduces to a positive quartic in the exactly-two-equal branch and a quartic
strictly negative on $[1,3)$ in the all-three-equal branch.  Bidirectional
ideal containments, quotient dimensions $8,20$, and all ordered positive
special fibres were rechecked.

The pair-wall splice uses the strict-high graph at the wall and weak chamber
closures; the wall term is $C^3$.  Star4 leaf walls are impossible by a
disjoint-edge sum, and star-edge walls route to shorter stars.  The
singleton wall has derivative $a_j/S>0$.  Coordinate-zero faces route to
supports $1,2,3,4$, where the exact $Q_3$ resultant, complete $Q_4$
classification, $d_3$ cubic crossing, and $d_4$ transverse increase close
all cases.

## R-M1, L-01, and E-01

R-M1 is closed.  Recursive duplicate-key and Boolean checks cover the six
non-star1 primaries, Q4/Q5 saddle verifiers, independent star2 audit, both
star1 loaders, and the independent loader.  Final attacks passed: 17/17
cross-primary, 11/11 Q4/Q5 corruptions, 9/9 independent-star2 corruptions,
4/4 independent parser attacks, and 10/10 semantic mutations.

L-01 is closed because the paper now prints $a^3(a-1)^2$ in the specialized
$Q_3$ equation.  E-01 is closed because the six malformed literal TeX
spacing strings in the proof are corrected.  No replacement finding arose.

## Exact rerun

The no-import core was run with output directed to `/tmp`; it returned PASS
and produced bytes identical to the frozen result.  The 10-mutation replay
also produced bytes identical to the frozen mutation result.  The frozen
master log records 23/23 PASS and binds the unchanged certificate hashes.

No generated paper PDF or source ZIP is present; source PDFs under
`literature/sources/` are literature inputs only.  No Lean, Coq, Isabelle, or
other interactive proof assistant was used.  Exact assistance consists of
rational/integer arithmetic, Singular, exact SymPy reconstruction, Sturm and
Bernstein certificates, and algebraic-number sign checks.

For the full endpoint-by-endpoint reasoning and (Q_4) branch audit, see
`proof/referee_report.md` on the same frozen revision.
