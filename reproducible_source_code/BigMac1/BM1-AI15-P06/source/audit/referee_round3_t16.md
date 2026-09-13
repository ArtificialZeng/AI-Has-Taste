# Gate 4, referee round 3: the \(t=16\) branch

Date: 2026-08-29  
Role: independent referee, not proof editor  
Audited target: `proof/t16_branch.md`  
Target SHA-256: `2cdf4ec6316db12036add92dfdc6c86b52f9a9d6d44837ccd1599f467fa9b022`  
Independent checker: `audit/referee_t16_check.py`  
Checker SHA-256: `b37043b07ee4160c936633d11b38a188bf3ef4865132c9c1ba8b5461e85405b5`

## Verdict

**PASS with three local presentation issues.**  I found no fatal or major
mathematical defect.  The strengthened singleton-compression lemma is valid
without the former equality hypothesis \(|Z|=11-R\), and the three surviving
\(t=16\) gap-count patterns are all excluded.  Conditional on the previously
audited endpoint \(t\geq16\), the target therefore proves

\[
t\geq17,
\qquad \sum_{j=1}^5q_j\geq22.
\]

It does not exclude any \(t\geq17\) stratum and does not prove
\(e(\ell_1^5)=10\).  The target discloses this limitation correctly.

The local issues are:

1. **R3-KERNEL-V.**  Equation (12), read in the full space
   \(\mathbb R^{11}\), is false as written because \(C\mathbf1=0\) while
   generally \(\mathbf1\notin K_Z\).  The statement proved and used is
   \(\ker(C|_V)=K_Z\) for \(V=\mathbf1^\perp\); equivalently the full kernel
   is \(\operatorname{span}\{\mathbf1\}\oplus K_Z\).  This is a local
   notation/scope error, not a gap in the argument.
2. **R3-Z-ALL.**  Before orienting a cut to a nonempty subset of
   \(W=[11]\setminus Z\), the proof should explicitly dispose of
   \(Z=[11]\).  Constancy on all eleven labels would make every remaining
   cut trivial, already contradicting \(R\geq1\).  Hence \(W\ne\varnothing\),
   and the stated orientation is then valid.  This is a one-line omitted edge
   case.
3. **R3-TEX-QUAD.**  Equation (1) contains the literal source text
   `\mathbf1_S,quad g_a>0` instead of `\mathbf1_S,\quad g_a>0`.  This is only
   a typesetting typo.

No proof file, old verifier, frame audit, runner, or log was modified in this
round.

## 1. Singleton compression reconstructed from the frame identity

Let \(V=\mathbf1^\perp\).  After singleton copies are aggregated by their
labels and subtracted, the remaining operator is

\[
C=H\operatorname{diag}(c)H
 =\sum_{a=1}^R g_av_{S_a}v_{S_a}^{T}\succeq0,
\qquad g_a>0,
\]

with \(1\leq R\leq8\).  This argument never requires individual
\(c_r\) to be nonnegative.

For \(u\in V\), \(Cu=0\) is equivalent to
\(H\operatorname{diag}(c)u=0\), hence to
\(c_ru_r=\lambda\) for all \(r\).  If no \(c_r\) is zero, the solution
space in \(V\) has dimension at most one.  Because \(C\) kills
\(\mathbf1\) and maps into \(V\), its full rank equals the rank of its
restriction to \(V\), which is then at least nine.  This contradicts
\(\operatorname{rank}C\leq R\leq8\).  Thus \(Z\ne\varnothing\).

For nonempty \(Z\), a zero entry forces \(\lambda=0\), and the exact kernel
on \(V\) is

\[
K_Z=\{u:\operatorname{supp}u\subseteq Z,
               \sum_{z\in Z}u_z=0\}.
\]

Positivity of the rank-one coefficients gives, for every \(u\in K_Z\),

\[
0=u^TCu=\sum_a g_a\langle v_{S_a},u\rangle^2,
\]

so each individual cut indicator is constant on \(Z\).  Repeated cuts and
complementary representatives cannot cancel this sum.

Since \(R\geq1\), some remaining cut is proper and nontrivial.  Therefore
\(Z\ne[11]\); otherwise its indicator could not be constant on \(Z\).
Put \(W=[11]\setminus Z\).  Complementing each cut if necessary now produces
a nonempty \(U_a\subseteq W\).

The matrix \(S=(He_w)_{w\in W}\) has full column rank solely because
\(Z\ne\varnothing\): if \(Hx=0\) and \(x\) is supported on \(W\), then
\(x\) is constant on all eleven labels, while its coordinates on \(Z\) are
zero, so \(x=0\).  No relation between \(|Z|\) and \(R\) is needed.  With a
left inverse \(L\) satisfying \(LS=I_W\), applying \(L(\cdot)L^T\) gives

\[
\operatorname{diag}(c_w:w\in W)
=\sum_{a=1}^R g_a\mathbf1_{U_a}\mathbf1_{U_a}^{T}.
\]

Every off-diagonal entry on the right is a sum of nonnegative numbers.
It vanishes only if no \(U_a\) contains a pair of labels.  Since every
\(U_a\) is nonempty, every one is a singleton.  Thus every supposedly
non-singleton remaining cut ray is a singleton ray, a contradiction.

This confirms that dropping the old equality condition is legitimate.
The local `ker C` notation identified above should nevertheless be corrected
before reuse in a polished proof.

## 2. Chain costs, convexity, and all 48 partitions

The checker reconstructs the exact cost vector

\[
(c_0,\ldots,c_7)=
\left(0,0,\frac2{11},\frac{24}{25},\frac{19}{10},
\frac{23}{8},\frac{193}{50},\frac{243}{50}\right)
\]

and its increments

\[
0,\ \frac2{11},\ \frac{214}{275},\ \frac{47}{50},\
\frac{39}{40},\ \frac{197}{200},\ 1.
\]

They are nondecreasing, so the discrete-convexity/majorization argument has
the direction claimed in Lemma 1.

For \(c_7\), the comparison

\[
\frac{12}{10^{1/6}+1}>\frac{243}{50}
\]

is equivalent, with all quantities positive, to
\(10^{1/6}<119/81\), hence exactly to

\[
119^6>10\,81^6.
\]

The integer comparison is true, so no floating-point or radical-ordering
assumption is present.

Independently enumerating every nonincreasing five-tuple in
\(\{0,\ldots,7\}^5\) with sum sixteen gives exactly 48 partitions.  Exactly
three have cost at most six:

\[
\begin{array}{c|c}
(4,3,3,3,3)&287/50\\
(4,4,3,3,2)&1623/275\\
(5,3,3,3,2)&13061/2200.
\end{array}
\]

There is no cost-exactly-six boundary.  The least expensive eliminated
partition is \((4,4,4,2,2)\), with cost \(667/110>6\).  This verifies both
the completeness and all zero/one/two-minimum boundary cases of the prose
partition argument.

## 3. Endpoint penalties

For every increasing selected-prefix tuple of lengths two through five, the
checker recomputes

\[
\theta^2=\frac{a(11-b)}{b(11-a)}
\]

from its endpoint sizes.  It checks all \(45,120,210,252\) tuples,
respectively.  In every length, the nonregular minimum is \(1/45\), and the
minimum when neither endpoint is singleton is \(4/81\).

For \(n=\ell-1\), comparison of the endpoint bound with a rational target
\(L<2n\) is performed in the exact radical-free form

\[
\theta^2
\mathrel{\gtrless}
\left(\frac{L}{2n-L}\right)^{2n}.
\]

This independently verifies every entry used from (14), including the
non-strict double bounds \(2/11\) and \(4/11\), the strict quadruple
no-singleton bound \(9/4\), and the strict quintuple nonregular bound \(3\).
Ties are therefore treated correctly rather than rounded away.

## 4. The three pattern eliminations

As a stronger finite cross-check of the prose, the checker assigns to each
chain the exhaustive categories regular (`R`, two singleton endpoints),
one-singleton nonregular (`O`), or neither-singleton (`N`).  It checks all
\(3^5=243\) category assignments for each pattern, with exact rational sums
and explicit strict/non-strict flags.

The results are:

| Pattern | Deficit-compatible assignments | Minimum singleton copies | Maximum \(R\) |
|---|---:|---:|---:|
| \((4,3,3,3,3)\) | 10 | 8 | 8 |
| \((4,4,3,3,2)\) | 2 | 9 | 7 |
| \((5,3,3,3,2)\) | 1 | 10 | 6 |

For the first pattern, the proof's weaker statement "at most two
nonregular chains" is sufficient and correct.  For the second, only the
all-regular assignment and a one-singleton double survive.  For the third,
only the all-regular assignment survives.

In all three patterns, internal positions alone force at least six
non-singleton copies: an internal prefix can have neither size one nor size
ten because selected sizes are strictly increasing.  Thus \(R>0\), while
the endpoint counts give \(R\le8,7,6\), respectively.  Every pattern lies in
the exact range excluded by Lemma 2.  Duplicate cut rays across coordinates
remain separate positive copies and do not change either the counting or the
compression argument.

## 5. Independent checker and external-cwd execution

The checker uses only Python's standard library, exact integers, and
`fractions.Fraction`.  It imports no project verifier, frame checker, runner,
log, or discovery output.  It pins the audited proof hash and fails closed
on a mismatch.  All conditions use explicit exceptions; its AST has zero
`ast.Assert` nodes.

The four required modes were run from `/tmp`, outside the project directory:

```bash
t16_script='/Users/mac/Documents/ChatGPT/ai15-open-math-2026-08-28-batch/06_kusner_l1_5_equilateral/audit/referee_t16_check.py'
cd /tmp
python3 "$t16_script"
python3 -O "$t16_script"
python3 -I "$t16_script"
python3 -O -I "$t16_script"
```

All four returned `status: PASS` with byte-identical JSON records.  Each run
reported proof hash `2cdf4ec6...`, checker hash `b37043b0...`, 48 partitions,
three survivors, 243 endpoint-category assignments per surviving pattern,
and zero AST assert nodes.

The program certifies only the finite arithmetic, partition, endpoint, and
copy-counting core.  The singleton-compression lemma was reconstructed by
hand in this report and is not misrepresented as machine-certified.

## Issue ledger

| Severity | ID | Verdict |
|---|---|---|
| Fatal | -- | None. |
| Major | -- | None. |
| Local | R3-KERNEL-V | Restrict equation (12) to \(V=\mathbf1^\perp\), or add the ambient \(\mathbf1\)-kernel summand. |
| Local | R3-Z-ALL | Explicitly handle \(Z=[11]\) before choosing nonempty \(U_a\subseteq W\). |
| Local | R3-TEX-QUAD | Replace the missing `\quad` command in equation (1). |
| Scope, not a defect | R3-T16-OPEN | The original problem remains open on all \(t\ge17\) strata. |
| Dependency, not re-audited here | R3-T16-IMPORT | The endpoint \(t\ge17\) is conditional on the earlier audited \(t\ge16\) theorem and imported chain bounds. |

## Proof-assistant disclosure

No proof assistant (Lean, Coq, Isabelle, HOL, or comparable system) was used.
The exact Python checker is a finite arithmetic/enumeration audit, not a
proof assistant and not a formalization of Lemma 2.
