# Triage evidence

Job: `primary-20260913-subsum-denominator-triage-e72bbaa7a9ab`.
Decision: **advance** to one bounded research pass. Candidate kind: none. Original workflow status: unresolved. No new resolution, accepted theorem, novelty claim, or manuscript.

## Source integrity and inspection

Read the requested skill and only its triage role reference, each in a separate tool result. Read source.md, checkpoint.md, problem.md, literature/outer-intake.md, and the existing local dedup report. Enumerated all literature filenames and specifically globbed `*handoff*.md`: none present. The outer-intake file served as the existing handoff and was checked rather than assumed.

Immutable source SHA256 before work:
`3d8e6928f3bd250dbdfde723603903f527d4ec0da8f85f5ac628b232991e240a`.

Cached input PDF fingerprints recomputed and matched:

- `literature/bbfm-subsum-journal.pdf`: `a0da6b8f736e5fc66084d2fa6913d89bce77254d7e9e4e5a5a2acce9b4a4ff31`.
- `literature/chen-ono-zhang-2605.21718v2.pdf`: `6593c03b6fb85a09c8e5d5a6a4f9a8f9b71d000ad394d1b2ce9292eafc8dae67`.

Retrieved primary pages on 2026-09-12 UTC / 2026-09-13 Asia/Shanghai:

1. [BBFM journal](https://link.springer.com/article/10.1007/s11139-026-01419-0): published 15 June 2026. Inspected live Proposition 3.8, Proposition 3.9, Proposition 3.10 and Conjecture 4, agreeing with cached text. Read cached definitions pp. 2–3, propositions pp. 11–12 and conjecture p. 18. These respectively give the product, weaker shape results, complete quotient recurrence, and the exact target.
2. [Chen–Ono–Zhang v2 metadata](https://arxiv.org/abs/2605.21718v2): revised 22 May 2026. Inspected [v2 full text](https://arxiv.org/html/2605.21718v2), especially Table 1 row 4, which labels this exact ordinary-denominator assertion open. Cached p. 4 repeats the claim and p. 6 contains the table. The binary correction remark p. 4 concerns another polynomial. Search snippets used stale wording about the binary disproof; inspected v2 content controls the interpretation.

Bounded live search queries included:

- `"subsum" "denominator" "log-concavity"`
- `"Reciprocals of subsum polynomials" log concavity`
- `"subsum" "log-concavity" proof denominator`
- `"product" "1+x" "log-concavity" distinct partitions smoothing`
- `"log-concavity" "den(n"`

No later resolution of this target was identified in the returned results. Only the inspected primary sources support the status decision; secondary snippets and broadly related partition papers do not establish a theorem for D_n. This search is bounded, not a priority proof.

## Reproducible finite computation

Run from project root:

```
python3 evidence/triage_probe.py --max-n 256
python3 evidence/smoothing_probe.py
```

Python integer arithmetic only, no floats or randomness. Multiplication by 1+x^s uses exact coefficient shift/add. The main script builds D_n incrementally from every dyadic quotient factor, compares with the independent direct exponent loop for 1<=n<=24, and checks symmetry, exact degree, and evaluation at x=1 for every tested n. Both construction routes use the same elementary shift/add primitive; this is an implementation cross-check, not an independent referee.

`evidence/triage_probe.json` records:

- 3,771,562 internal minors of D_n for 1<=n<=256; failures exactly n=3,5,6,7. Previously supplied calibration stopped at 128; this extends the finite observation but establishes no universal theorem.
- All 496 ascending dyadic intermediate stages for 9<=n<=256 are log-concave.
- Inequality H in problem.md passes every one of 7,659,550 stage/index checks, including support endpoints. The minimum new-minor / sum-of-old-minors ratio is 5/9, attained at n=12, shift 3, j=2. There is no claim that 5/9 is the optimal uniform constant.

The minimum-ratio certificate can also be read directly from low-degree factors: D_11 has initial coefficients 1,4,9,18. Before adding 1+x^3, T_2=9^2-4*18=9; afterwards T_2=9^2-4*19=5, while the shifted minor at -1 is zero. Thus a proposed ratio constant greater than 5/9 is already impossible; the tested constant 1/2 leaves slack.

Known exception certificates (one each): n=3,j=2 gives 2^2-2*3=-2; n=5,j=5 gives 14^2-11*18=-2; n=6,j=2 and n=7,j=2 both give 5^2-3*9=-2. All negative positions are retained in JSON. These are recalibrations of prior exceptions.

## Exact failed shortcut and replacement target

For b_j=a_j+a_(j-s), exact expansion gives

T_j(b)=T_j(a)+T_(j-s)(a)+C_(j,s)(a),

where C=2a_j a_(j-s)-a_(j-1)a_(j+1-s)-a_(j+1)a_(j-1-s).

The shortcut C>=0 is false even at the first n>=9 transition. With a=D_8, s=9 and j=8, the old triple is (114,159,215), the old minor is 771, the shifted minor is zero, C=-114, and the new minor is 657. Full D_8 coefficients are in JSON. This refutes that precise shortcut, not all convolution methods and not the source claim. Indeed C is necessarily negative at the first overlap j=s-1 when a_(s-2)>0.

H permits this negative mixed term: it is equivalent to C>=-(T_j(a)+T_(j-s)(a))/2. If H held uniformly, the zero extension makes old minors nonnegative at every index whenever the old polynomial is log-concave. Induction from D_8 then proves the original range n>=8; n=1,2,4 are covered separately. This implication is elementary, but the uniform premise H remains unproved.

At j=s-1, H requires the concrete boundary inequality T_(s-1)(a)>=2a_(s-2)a_0. Any future proof must control this boundary as well as the central coefficients. Finite agreement and qualitative unimodality do not supply such control.

The auxiliary smoothing probe checks (1+x)^k P_n with P_n=product_(i=1)^n(1+x^i), 1<=n<=128 and k=1,2,3,4. It records failures for each proposed fixed small smoothing power. For all n>=5, the stable low-degree witnesses are respectively (2,2,3), (4,5,7), (7,9,12), and (16,21,28), with minors -2,-3,-3,-7. These rule out just those four shortcuts; larger powers or other layer groupings are not excluded.

## Suitability and one next test

The precise unbounded target has source support, a stronger quantitative recurrence target H now has new exact evidence, and a negative certificate is short and reproducible. This justifies advance, with no candidate yet. A uniform bound remains a substantial gap; discovery of H is not an audited conjecture-note.

One next test: execute `python3 evidence/triage_probe.py --max-n 512` and inspect H in the new range 257<=n<=512, all stages/degrees. Retain any failing stage and its exact old/new minors. A negative H certificate changes the subsidiary target only; a negative D_n minor outside the four exceptions would address the original target. If H survives, the research pass must seek a uniform inequality rather than repeatedly extend the same calibration.
