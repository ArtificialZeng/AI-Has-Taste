# Gate 4, referee round 2: the dense branch at \(t=15\)

Date: 2026-08-29  
Referee role: independent mathematical audit, not proof editing  
Target: `proof/t15_dense_branch.md` only  
Target SHA-256: `a7f92fe2fdb56c7ef84107c4100cc0a5d43bda7e41ae2afe1af42afb3ef52649`  
Finite-check script: `audit/referee_t15_check.py`  
Script SHA-256: `0b7d3a481c1bcb1aa1f6f8242d417fbce37816b387a1cca5a57402fd2752f522`

## Verdict

**PASS.**  I found no fatal, major, or local mathematical error in the
target snapshot.  Conditional on the two imported facts from the frozen
`proof/builder_notes.md`--namely \(t\geq 15\), and that equality leaves only
the patterns \((3,3,3,3,3)\) and \((4,3,3,3,2)\)--the note rigorously
eliminates both patterns.  It therefore does prove

\[
t\geq16
\]

for every putative eleven-point equilateral set in \(\ell_1^5\).  It does
**not** eliminate any \(t\geq16\) stratum and does not settle
\(e(\ell_1^5)=10\).  The theorem's own scope statement is accurate.

The target changed once while this audit was in progress: an initially
observed snapshot had SHA-256 beginning `4a470a`, whereas the final audited
snapshot is the full hash recorded above.  Every verdict below refers to the
final `a7f92...` snapshot, which I re-read in full.

## Reconstruction from the definitions

### 1. Endpoint ratios and deficit separation: PASS

For nested nontrivial prefixes of sizes \(1\leq a<b\leq10\), direct
centering gives

\[
 \theta^2=\frac{a(11-b)}{b(11-a)}.
\]

Enumeration of every increasing size tuple of lengths two, three, and four
confirms the two endpoint minima used in Lemma 1:

* among nonregular endpoint pairs, \(\min\theta^2=1/45\), attained at
  \((1,9)\) and \((2,10)\);
* when neither endpoint is a singleton ray,
  \(\min\theta^2=4/81\), attained at \((2,9)\).

Writing \(n=\ell-1\) and
\(u=(\theta^2)^{1/(2n)}\), the endpoint lower bound is
\(2nu/(1+u)\).  Its comparison with a rational target \(L<2n\) is exactly

\[
 \frac{2nu}{1+u}>L
 \quad\Longleftrightarrow\quad
 \theta^2>\left(\frac{L}{2n-L}\right)^{2n}.
\]

Thus all radical comparisons in the note reduce to positive integer
comparisons.  In particular,

\[
29^4>45\,11^4,\qquad 2\cdot121>25\cdot9,
\qquad64>45,\qquad49>45.
\]

They respectively verify the strict bounds \(11/10\), \(5/4\), \(2\),
and \(1/4\).  The general double bound is correctly non-strict: for the
regular pair \((1,10)\), it is exactly \(2/11\).  The general triple and
quadruple comparisons are strict.  No equality boundary was silently
discarded.

The independent script checked all \(45\), \(120\), and \(210\) increasing
size tuples for chain lengths two, three, and four.  The regular,
nonregular, and neither-singleton counts were respectively

\[
\begin{array}{c|rrrr}
\ell&\text{all}&\text{regular}&\text{nonregular}&\text{neither}\
\hline
2&45&1&44&28\\
3&120&8&112&56\\
4&210&28&182&70.
\end{array}
\]

### 2. Deficit case splits: PASS

For \((3,3,3,3,3)\), exact enumeration of the three categories
regular/one-singleton/neither-singleton gives 243 assignments.  The only
assignments not immediately exceeding total deficit five are the all-regular
assignment and the five assignments having exactly one one-singleton
exception.  The decisive arithmetic is

\[
2\frac{11}{10}+3\frac{24}{25}=\frac{127}{25}>5,
\qquad
\frac54+4\frac{24}{25}=\frac{509}{100}>5.
\]

For \((4,3,3,3,2)\), all 32 regular/nonregular assignments were checked.
Only the all-regular assignment survives the conservative deficit test.
The three displayed lower sums in Proposition 4 are strictly greater than
five.  Strictness is valid even though the general double bound is
non-strict, because each displayed sum contains strict triple or quadruple
bounds (and the nonregular-double term itself is strict in the third sum).

### 3. Singleton compression, kernel, and rank: PASS by independent hand proof

After aggregating every singleton-ray copy at label \(r\) into weight
\(\alpha_r\), subtraction from the frame identity gives

\[
C=H\operatorname{diag}(c)H
 =\sum_{a=1}^R g_av_{S_a}v_{S_a}^{T}\succeq0,
\qquad c_r=\tfrac12-\alpha_r.
\]

The argument does not assume \(c_r\geq0\); individual entries of \(c\) may
be negative.  On \(V=\mathbf1^\perp\), the kernel equation is exactly
\(c_ru_r=\lambda\) for every \(r\).  If no \(c_r\) vanishes, its solution
space in \(V\) has dimension at most one, hence
\(\operatorname{rank}C\geq9\), contradicting \(R\leq8\).  If
\(Z=\{r:c_r=0\}\ne\varnothing\), a zero coordinate forces
\(\lambda=0\), and

\[
\ker(C|_V)=\{u:\operatorname{supp}u\subseteq Z,
                    \sum_{r\in Z}u_r=0\}.
\]

It has dimension \(h-1\), so the full matrix (which also kills
\(\mathbf1\)) has rank \(11-h\).  Therefore \(h\geq11-R\).  This checks
the ambient-versus-\(V\) rank bookkeeping.

Because all \(g_a>0\), a kernel vector annihilated by the positive
rank-one sum is orthogonal to every individual \(v_{S_a}\).  This forces
each cut indicator to be constant on \(Z\).  This conclusion remains true
with repeated cuts: repetitions add positive copies and cannot cancel.

At equality \(h=11-R\), complementing a cut if necessary leaves a
nonempty subset \(U_a\subseteq W=[11]\setminus Z\).  Nonemptiness follows
from the original cut being proper.  Since \(Z\ne\varnothing\), the
vectors \((He_w)_{w\in W}\) are independent.  Applying an actual left
inverse on both sides yields

\[
\operatorname{diag}(c_w:w\in W)
 =\sum_a g_a\mathbf1_{U_a}\mathbf1_{U_a}^{T}.
\]

Every off-diagonal entry on the right is a sum of nonnegative terms.
Consequently every nonempty \(U_a\) has size one.  Negative diagonal
entries of the matrix before this step cause no loophole: the equality
itself then also implies the relevant diagonal values are nonnegative.
Repeated cuts likewise provide no cancellation.

The finite script deliberately does not claim to certify this linear
algebra; this paragraph is the independent human reconstruction.

### 4. Zero-set endpoint counting: PASS

If \(r\in Z\), then \(\alpha_r=1/2>0\), so label \(r\) occurs in at least
one singleton endpoint copy.  For any regular triple or quadruple, an
internal prefix contains the minimum endpoint label and excludes the maximum
endpoint label.  Constancy on \(Z\) therefore prevents both endpoint labels
from lying in \(Z\).  For the exceptional triple in Proposition 3, its
exactly one singleton endpoint still belongs to such a separated endpoint
pair, so it contributes capacity at most one.  These are union bounds, so
coincident endpoint labels across coordinates can only decrease the number
of distinct \(Z\)-labels; no distinctness assumption is being made.

The resulting counts are exact:

* all-regular \((3^5)\): \(R=5\), hence \(h\geq6\), but endpoint capacity
  is at most five;
* one-exception \((3^5)\): \(R=6\), hence \(h\geq5\), and endpoint capacity
  is at most five, forcing \(h=5=11-R\) and the equality-compression
  contradiction;
* all-regular \((4,3,3,3,2)\): \(R=2+3+0=5\), hence \(h\geq6\); four
  coordinates with internal cuts have capacity one each and the double has
  capacity two, forcing \(h=6=11-R\) and the same contradiction.

Zero gaps have already been removed in the imported positive-gap model.
Selected prefix sizes in one coordinate are strictly increasing, so there
are no repeated cuts within a coordinate.  Complementary or repeated cut
rays across coordinates are harmless because the compression uses outer
products and positive aggregated weights.

## Independent finite checker

The checker uses only Python's standard library, exact integers, and
`fractions.Fraction`; it imports no project verifier, frame audit, runner,
log, or discovery output.  Every failure is an explicit exception/exit-1
path.  Its parsed AST contains zero `ast.Assert` nodes, and optimization
cannot remove any decisive condition.

Reproduction commands:

```bash
python3 audit/referee_t15_check.py
python3 -O audit/referee_t15_check.py
python3 -I audit/referee_t15_check.py
python3 -O -I audit/referee_t15_check.py
python3 - <<'PY'
import ast
from pathlib import Path
p = Path('audit/referee_t15_check.py')
t = ast.parse(p.read_text(encoding='utf-8'))
print(sum(isinstance(n, ast.Assert) for n in ast.walk(t)))
PY
shasum -a 256 proof/t15_dense_branch.md audit/referee_t15_check.py
```

All four execution modes returned `status: PASS` with identical mathematical
records.  The AST command returned `0`.  The checker's scope is only the
finite cut-size/deficit/case/counting core; it is not a proof assistant and
does not machine-certify Lemma 2.

## Issue ledger

| Severity | ID | Finding | Disposition |
|---|---|---|---|
| Fatal | -- | None in the audited target. | PASS |
| Major | -- | None in the audited target. | PASS |
| Local | -- | None in the audited target. | PASS |
| Scope, not a defect | R2-T15-OPEN | The proof stops after excluding \(t=15\); all \(t\geq16\) strata remain open for the original Kusner problem. | Correctly disclosed in the target. |
| Dependency, not re-audited here | R2-T15-IMPORT | The conclusion uses the frozen builder theorem \(t\geq15\) and its two-pattern classification at equality. | The present verdict is conditional on that imported audited result. |

## Proof-assistant disclosure

No proof assistant (Lean, Coq, Isabelle, HOL, or comparable system) was used.
The compression lemma was checked by hand from the displayed matrix identity.
The accompanying Python program is an exact finite arithmetic/enumeration
checker only.
