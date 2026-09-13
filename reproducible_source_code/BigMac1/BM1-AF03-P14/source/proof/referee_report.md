# Independent hostile referee report: final cleanup revision

Date: 2026-08-30 (Asia/Shanghai)  
Role: independent hostile/no-import referee  
Formal verdict: **PASS**  
Publication claim: **none**

## 1. Verdict and finding counts

The complete classification claimed in `proof/main_proof.md` is supported by
the frozen proof, exact certificates, and independent reconstruction.  Up to
signed coordinate permutations,

\[
  \operatorname{LocExt}(\sigma_5)=\{d_1,d_2,d_5\}.
\]

Here $d_1$ is a strict local minimum, $d_2$ is a global maximum, and
$d_5$ is a strict local maximum.  The full-support critical set is exactly
$d_5$ and

\[
  v_\alpha\sim(\alpha,\alpha,1,1,1),\qquad
  \alpha={24+\sqrt{69}\over13},
\]

with tangent signature $(1+,3-)$.  The only lower-support non-diagonal
critical orbit is $(1,1,2,2,0)/\sqrt{10}$, also a saddle.

| Finding class | Count |
|---|---:|
| fatal | **0** |
| major | **0** |
| local | **0** |
| expository | **0** |

The former release blocker R-M1 and the former nonblocking findings L-01 and
E-01 are closed on this revision.

## 2. Frozen endpoint

The review binds these exact files:

```text
83fab549580aaa398cf8e0cedea8e3366a7b35550fb51f88459daf6a27878ce9  problem/formal_statement.md
1d53b2d70c0ee37e306929414e3c7d4b84baaa7469868c204bcf4a4fa03ea85f  proof/main_proof.md
99daef202ae37d65144543125a9dbf06828c4a01de2bd13c3eae408043af4965  proof/agent_builder_report.md
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

All 17 entries in `frozen_inputs.json` were rehashed and match, including the
current proof and paper.  The nine decisive certificate hashes are:

```text
3d5c97a23ad36956387e4ddbdaca0f74720953f34a59af422ed15944b23e1e6a  results/empty_highpair_classification_certificate.json
70cf7f980c89ff36e6b07ccecde268bcde6d8cf5f9da171759b5d8ba5c0e3fa7  certificates/star1_exact_certificate.json
fd591e360a57668ad818ba8adb8e48d5670a211da3f43528c7f3f68517310a80  results/star2_bernstein_no_go_certificate.json
f966e220261ffc316d37aaac9522e0484e2b931792c5fe985aae351052254024  certificates/star3_decomposition.json
b57cad6aeea0d3db3ac39999bfbdcdcacd48c36d5b2de4883e6806a080bfc935  results/breaker_star4_certificate.json
5e0bab27d028cdfc65027c3c346d3f0397dd13a623b1bf7782616823019278a1  results/triangle_highpair_no_go_certificate.json
6f704264551c322228d9af0fffcd03e7ae5071be2ddbe04d0f54ed583cb8db28  results/q3_classification_certificate.json
1c732a3b4c95b2bd743a05248dff841457ec11cdd70c76a96435dffb89a86c15  results/breaker_q4_baseline_certificate.json
6bac02ad20ab063e8db1bbe8f79d1495dcb3134788f43b760ad119131872d03a  results/breaker_saddle_certificate.json
```

## 3. Endpoint-by-endpoint hostile review

| Endpoint | Verdict | Independent basis |
|---|---|---|
| Formal quantifiers and symmetry | PASS | The formal statement includes antipodes, weak extrema, support loss, walls, and all degeneracies; signed permutations preserve local type. |
| Section formula and regularity | PASS | Coarea plus inclusion--exclusion gives the stated scale-invariant truncated-power formula. For $Q_5$, $x\lvert x\rvert^3\in C^3$, so pair-wall first and second derivatives match. |
| Dominant region and singleton wall | PASS | $F_5=R/a_0$; every positive smaller coordinate has derivative $a_j/S>0$, including the equality wall by matching. |
| Six graph exhaustion | PASS | Exact enumeration of all $2^{10}$ pair graphs leaves precisely empty, star1, star2, star3, star4, and triangle after shiftedness and intersection. Exact rational witnesses realize all six. |
| Pair-wall coverage | PASS | The strict-high graph at a wall is still shifted/intersecting and the point lies in its weak closure. Star4 leaf walls are impossible by a disjoint-edge sum; star-edge walls route to shorter stars. |
| Empty closure | PASS | The common nonzero quartic limits the number of coordinate values. All four two-value, six three-value, eight residual branch-ideal, and four-value Vieta cases are reconstructed exactly; only the diagonal remains. |
| Star1 closure | PASS | The 55-row degree-nine Bernstein identity forces $x=z=0$. The radical degree-15 residual ideal has component degrees $2,2,2,3,6$; exactly one nonnegative component survives. All original critical equations vanish there and its Hessian has signature $(1+,3-)$. |
| Star2 closure | PASS | The reconstructed derivative combination has 1125 strictly positive Bernstein coefficients and $P$ has 70, including closure endpoints; simultaneous criticality is impossible. |
| Star3 closure | PASS | The saturated radical ideal has degree 14 and components of degrees $2,4,4,4$. Rational Sturm isolation shows all positive real points violate $a_3\ge a_4=1$. |
| Star4 | PASS | Six exact ideal consequences exhaust leaf-equality patterns. Three $r>1$ branches violate the star margin; the all-leaves-one polynomial has no root on $(2,\infty)$. Boundary routing is complete. |
| Triangle closure | PASS | The exact dimension-one saturated basis forces $a_0=a_1$, then $a_0=a_2$ or $2a_2$, and then $a_2^2-a_3^2-1=0$, contradicting the weak high-edge inequality. |
| Full-support local types | PASS | The only roots are $d_5$ and $v_\alpha$; $d_5$ has four eigenvalues $-5\sqrt5/32$, while $v_\alpha$ is indefinite. |
| $Q_3,Q_2,Q_1$ supports | PASS | The raw $Q_3$ resultant leaves $a=b=1$; $Q_2$ is monotone off its diagonal; $d_1$ is a direct strict local minimum. |
| Complete $Q_4$ exhaustion | PASS | The written two-piece branch proof and the independent bidirectional ideal containments yield only the diagonals and $(2,2,1,1)$. The small Q4 certificate is used only for the latter's saddle form. |
| Support splice | PASS | An ambient extremum restricts to an extremum on its support subsphere. Every non-diagonal lower-support survivor is already a saddle there. |
| $d_1,\ldots,d_5$ types | PASS | $d_1$: strict local minimum; $d_2$: Ball global maximum; $d_3$: exact cubic crossing; $d_4$: support decrease plus exact transverse increase; $d_5$: negative definite Hessian. |
| Theorem wording | PASS | The theorem states exactly the classification supported by the proof and certificates. |
| Canonical/fail-closed integrity | PASS | All release loaders reject duplicate keys at every object depth and noncanonical booleans; semantic, schema, wall, interval, and Hessian mutations are rejected. |

## 4. Independent (Q_4) audit

The file `results/breaker_q4_baseline_certificate.json` was not treated as an
exhaustion certificate.  For (0<a\le b\le c\le d), the written proof splits
at (a+d=b+c).

In the (a+d\le b+c) piece, distinct (b,c,d) would imply

\[
 (b-c)^2+(b-d)^2+(c-d)^2=-2a^2,
\]

which is impossible.  The branch (b=c<d) would give
(1-2b^2-bd=a^2+d(d-b)>0), also impossible.  Thus (c=d); the Case-B
factor forces (a=b), and the remaining equation yields either the diagonal
or (c=2a).

In the (a+d\ge b+c) piece, the three Case-D differences are

\[
 (a+b+c-d)^2(a-b)(d(a+b+d)-1)=0
\]

and its analogues.  Strict balance excludes the first factor and forces a
repeated value among (a,b,c).  With exactly two equal, the residual equation
is

\[
 r(r-2)(10r^4+7r^3+15r^2-5r+4)=0.
\]

The quartic is positive for (r>0), so (r=2).  With all three equal, the
remaining factor is

\[
 (r-1)(r^4-5r^3+6r^2-3r-3),\qquad 1\le r<3,
\]

whose quartic is negative on that interval.  Thus (r=1).  The independent
reconstruction additionally checks quotient dimensions (8) and (20),
bidirectional elimination-ideal containment, and all five positive ordered
special fibres.  Finally, the non-diagonal tangent eigenvalues have two
negative signs and one positive sign.  This exhausts (Q_4) without assigning
that role to the small saddle certificate.

## 5. Divisions, saturation, and walls

No pair-wall form is divided out.  Saturation factors are only positive
coordinates, (P), and (S): coordinates and (D) are positive on full
support; (S\ge1) in the gauge; and (P>0) follows from positivity of the
central section and the exact formula.  The two star1 residual prefactors are
at least (1) and (3).  Empty-chamber divided differences are used only on
distinct-value branches.  In (Q_3), the removed factors (b^5) and
(b^2+1) have no zero in the positive domain, while reducing the exponent of
(b-1) retains that locus.  Hence no physical component is discarded.

## 6. R-M1 and cleanup findings

R-M1 is closed.  The six non-star1 primaries, the Q4 and Q5 saddle verifiers,
the independent star2 audit, both star1 loaders, and the no-import loader use
recursive duplicate-key rejection and recursive Boolean validation.  The
sole allowed Boolean is `star3.classification.radical=true`.

The following final tests passed:

- 17/17 duplicate/nested/Boolean attacks across Q3 and the six Q5 chambers;
- 11/11 corruptions across the Q4/Q5 saddle verifiers, with both valid
  controls accepted;
- 9/9 corruptions in the independent star2 audit, with its valid control
  accepted;
- 4/4 independent parser attacks, with the canonical star3 Boolean control
  accepted;
- 10/10 in-memory semantic mutations: chamber graph, coefficient, resultant
  factor, wall deletion, root interval, Hessian sign, support path, star1
  margin, duplicate key, and Boolean type confusion.

L-01 is closed: `paper/main.tex` now gives the second specialized $Q_3$
equation as $a^3(a-1)^2$, agreeing with direct reconstruction and the proof.
E-01 is closed: all five literal `,quad` strings and the literal `,qquad`
string in the proof are now the intended TeX commands.  No new local or
expository defect was found.

## 7. Reproduction evidence and scope

The frozen master log reports **23/23 PASS**, and every certificate hash in it
matches the current bytes.  I independently ran the no-import core with a
temporary result path:

```text
/opt/anaconda3/bin/python3 audit/independent_referee/independent_verifier.py \
  --result /tmp/q5-final-cleanup-result.json
PASS: independent exact referee core
```

The temporary output was byte-identical to the frozen result, SHA-256
`896229b63ac2d877c49e7272913e07f62d8d6612ab38c46e9816518b4052c3cf`.
The semantic mutation replay was likewise byte-identical to its frozen result,
SHA-256
`4a31dabad8f83d399c67e4fde472d02540ac2ca2ce8b815f71e143822b84d897`.

No generated paper PDF and no source ZIP is present.  PDFs under
`literature/sources/` are source literature, not a publishable artifact.  This
report is a theorem/referee verdict, not an assertion that every separate
novelty, citation, LaTeX-build, or publication gate has passed.

No Lean, Coq, Isabelle, or other interactive proof assistant was used.  The
audited computer assistance consists of exact rational/integer arithmetic,
Singular ideal computations, SymPy exact reconstruction, rational Sturm
chains, Bernstein identities, and algebraic-number sign checks.
