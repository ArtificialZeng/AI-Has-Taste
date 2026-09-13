# Independent referee/certifier report

Date of audit: 2026-08-29

Role: reconstruction from the source definitions, not acceptance of the
discovery narrative.  I did not modify the shared task status or manuscript.

## Bottom-line verdict

The current exact stagnation certificate is mathematically valid for the
displayed, fixed-precision SM-IR operation graph.  It is stronger than a mere
exception/breakdown example: every operation is finite, the computed
Sherman--Morrison denominator is nonzero, and the iteration has the exact
fixed point \(\widehat x_k=0\), whose normwise and componentwise relative
backward errors are both exactly one.

This refutes the natural uniform interpretation of the source conjecture:
condition numbers of \(A\) and \(A+uv^T\), by themselves, do not force SM-IR
to enter an \(O(\epsilon_M)\) backward-error regime.  It also refutes the
paper's concrete experimental success criterion \(\eta<5\epsilon_M\) in
binary64.

There is nevertheless an important wording qualification.  The source uses
"bounded safely away," "eventually," "accuracy is insufficient," and
"backward stable" without closing their quantifiers.  Thus the unedited prose
conjecture is not literally a truth-valued mathematical proposition.  A final
claim should say that the paper-faithful universal/uniform formalization is
disproved, and should not claim that every conceivable repaired algorithm is
disproved.

## Reconstruction of the source

The current primary record is arXiv:2510.01696v1, submitted 2025-10-02; as of
the audit date arXiv lists no later version.

The source contains three distinct levels of assertion:

1. The abstract conjectures backward stability when
   \(\kappa_2(A)\) and \(\kappa_2(A+uv^T)\) are both safely away from
   \(\epsilon_M^{-1}\).
2. Algorithm 2 computes one initial SM solution, reuses the same \(z\) and
   \(\beta\), forms a fixed-precision residual, applies SM to the correction,
   and repeats when "accuracy is insufficient."  No stopping predicate is
   specified there.
3. The proved theorem is conditional: one correction is backward stable if
   the explicit \(h(A,u,v,\widehat r)\) term is a modest multiple of the
   componentwise denominator.  The counterexample below does not satisfy that
   hypothesis and therefore does not contradict the proved theorem.

The experiments use the concrete componentwise stopping test

\[
  \max_i \frac{|r_i|}{(|B||\widetilde x|+|b|)_i}<5\epsilon_M.
\]

The paper also reports the normwise Rigal--Gaches quantity

\[
  \eta_B(\widehat x)=
  \frac{\|b-B\widehat x\|}
       {\|B\|\,\|\widehat x\|+\|b\|}.
\]

These two definitions coincide and equal one in the scalar certificate.

## Exact reconstruction of the binary64 certificate

The serialized input is

\[
 A=1,\qquad u=1,\qquad v=2^{53},\qquad b=1,
\]

in binary64 round-to-nearest, ties-to-even, with
\(\epsilon_M=2^{-53}\).  The exact real system coefficient is

\[
 B=A+uv=2^{53}+1\ne0.
\]

Since both matrices are nonzero scalars,
\(\kappa_2(A)=\kappa_2(B)=1\).  All inputs and all iterates below are finite;
there is no overflow, underflow, subnormal arithmetic, division by zero, NaN,
or infinity.

The initial SM trace is exact until the addition defining \(\beta\):

\[
 \widehat y=1,\quad \widehat z=1,\quad
 \widehat\alpha=2^{53},\quad
 \widehat\beta=\operatorname{RN}(2^{53}+1)=2^{53}.
\]

At exponent 53 the consecutive binary64 numbers are \(2^{53}\) and
\(2^{53}+2\).  The exact value \(2^{53}+1\) is their midpoint; the lower
significand is even, so ties-to-even selects \(2^{53}\).  Consequently

\[
 \widehat\theta=1,\qquad \widehat x_0=1-1=0.
\]

At \(\widehat x=0\), Algorithm 2 computes

\[
 \widehat r=1,\quad \widehat y_r=1,\quad
 \widehat\alpha_r=2^{53},\quad \widehat\theta_r=1,
 \quad T(0)=0+1-1=0.
\]

All of these operations are exact after the one certified midpoint rounding.
Determinism and \(T(0)=0\) prove by induction that
\(\widehat x_k=0\) for every \(k\ge0\); testing a large finite number of
iterations is not needed for that conclusion.  Finally,

\[
 \eta_B(0)=\frac{|1-B0|}{|B|\,0+|1|}=1.
\]

If backward error is defined using perturbations of the matrix only, the
failure is even more immediate: no finite \(\Delta B\) can make
\((B+\Delta B)0=1\).

I independently ran both supplied verifiers.  They reported:

```text
CERTIFIED: exact binary64 SM-IR stagnation counterexample
condition_numbers=1,1; beta_exact=9007199254740993; beta_fl=9007199254740992
all_iterates=0; normwise_backward_error=1; checked_iterations=32
HARDWARE-CHECKED: beta=0x1p+53, all_iterates=0, backward_error=1, iterations=32
```

The exact Python verifier does not trust host floating point for the decisive
trace.  The separately compiled C program is a useful hardware cross-check,
not the logical basis of the proof.

## Quantifier repair: a precision-parametric disproof

For fixed binary64 alone, the phrase \(C(n)\epsilon_M\) is still ambiguous if
"modest" is not quantified: formally, one could choose the meaningless
constant \(C(1)=2^{53}\).  The cleanest repair is a family over precision.

Let a radix-two format have precision \(p\), unit roundoff
\(\epsilon_p=2^{-p}\), round-to-nearest ties-to-even, and an exponent range
containing \(2^p\).  For every such \(p\), take

\[
 A=u=b=1,\qquad v=2^p.
\]

The same midpoint argument gives

\[
 \operatorname{RN}_p(2^p+1)=2^p,\qquad
 \widehat x_k=0,\qquad \eta_B(\widehat x_k)=1
 \quad(k\ge0),
\]

while \(\kappa_2(A)=\kappa_2(B)=1\).  Therefore no constant independent of
\(p\) can give \(\eta_B\le C\epsilon_p\).  This is the precise asymptotic
negation of standard backward stability.

The family also shows that "fixed precision" causes no problem: each run uses
one fixed \(p\); only the theorem audit varies \(p\) to interpret the
\(O(\epsilon)\) quantifier.

## A two-dimensional embedding

To eliminate any objection that scalar condition numbers are automatically
one, put \(m=\lfloor p/2\rfloor\) and define

\[
 A_p=\operatorname{diag}(1,2^m),\qquad
 u_p=b_p=e_1,\qquad v_p=2^p e_1.
\]

Then

\[
 B_p=A_p+u_pv_p^T
   =\operatorname{diag}(2^p+1,2^m),
\]

and hence

\[
 \kappa_2(A_p)=2^m,\qquad
 \kappa_2(B_p)=\frac{2^p+1}{2^m}.
\]

Both are \(O(2^{p/2})=o(\epsilon_p^{-1})\), indeed

\[
 \epsilon_p\kappa_2(A_p)=2^{m-p}\to0,
 \qquad
 \epsilon_p\kappa_2(B_p)=\frac{1+2^{-p}}{2^m}\to0.
\]

A diagonal division solver (equivalently LU on this diagonal input) computes
the first components \(\widehat y_1=\widehat z_1=1\) exactly, while all second
components remain zero.  Thus the scalar trace embeds verbatim and
\(\widehat x_k=0\), \(\eta=1\) for all \(k\).

For binary64, \(p=53,m=26\):

\[
 \kappa_2(A)=2^{26},\qquad
 \kappa_2(B)=\frac{2^{53}+1}{2^{26}}\approx2^{27},
\]

so each condition number is about eight orders of magnitude smaller than
\(\epsilon_M^{-1}=2^{53}\).  This is the recommended secondary statement if a
referee regards the scalar example as degenerate.

## Fatal ambiguities and required corrections to the formal statement

1. **Backward-stability constant.**  Replace "modest \(C(n)\)" by either a
   numerical threshold (the paper uses \(5\epsilon_M\)) or a uniform-in-\(p\)
   quantifier.  The precision-parametric family is preferable.
2. **Obsolete termination wording.**  The stagnation example does produce a
   finite iterate at every step.  It refutes eventual entrance into a
   backward-stable regime, not the weaker property "eventually produces a
   finite iterate."  Any text left over from a division-by-zero candidate must
   be removed.
3. **Safety factor.**  Quantify it as a fixed \(0<c<1\), independent of data
   and precision, and require \(\max\kappa_2\le c\epsilon_p^{-1}\).  The
   two-dimensional family satisfies this for every fixed \(c>0\) once \(p\)
   is large.
4. **Solver.**  A property such as "backward stable \(A\)-solver" is not a
   deterministic operation graph.  Pin direct scalar division or diagonal LU
   for the certificate.  A universal theorem would need to quantify over a
   stated class of solvers.
5. **Residual/update graph.**  Specify association, dot-product accumulation,
   fused contraction, and whether \(z,\beta\) are reused.  The fixed-point
   certificate is robust to the usual associations at zero, but a theorem
   cannot leave these unspecified.
6. **Stopping.**  State whether the exact or computed residual drives the
   test, the exact formula for the test, its zero-denominator conventions, and
   behavior after a maximum iteration count.
7. **Exceptional arithmetic.**  State trapping/nontrapping behavior and
   assumptions on overflow/underflow.  The stagnation certificate avoids all
   exceptional values, so adding a no-exception hypothesis does not repair the
   conjecture.
8. **Backward-error notion.**  Distinguish normwise perturbation of \(B\) and
   \(b\), matrix-only perturbation, componentwise perturbation, and structured
   perturbation of \(A,u,v\).  The paper uses both normwise and componentwise
   unstructured measures in different passages.
9. **Data interpretation.**  State that \(B=A+uv^T\) is the exact real sum of
   the floating inputs, not the rounded explicitly formed matrix.  This is the
   interpretation used by the SM algorithm and its analysis.
10. **Zero cases.**  Exclude or define conventions for \(b=0\), \(x=0\), and
    componentwise denominators equal to zero.

## A necessary correction to the proposed repaired conjecture

A lower bound on the computed or exact capacitance denominator is not enough.
In this certificate

\[
  1+v^TA^{-1}u=2^p+1,
  \qquad \widehat\beta=2^p,
\]

so neither denominator is small and no breakdown occurs.  The failure comes
from losing the unit term and then exactly cancelling the two large terms in
the SM solution/correction.  A meaningful repair needs a scale-sensitive
condition controlling the complete SM evaluation (for example the paper's
explicit \(h\)-term or an equivalent cancellation/factor-scaling quantity),
or it must change the algorithm through extra precision, compensation, or a
fallback solve.  Conditions only on \(\kappa_2(A)\), \(\kappa_2(B)\), and a
lower bound for \(|\beta|\) remain false.

This is consistent with the exact invariance
\(uv^T=(su)(v/s)^T\): the two condition numbers depend only on \(A\) and
\(uv^T\), whereas the floating SM path depends on the chosen factors.

## Minimum certificate for a terminal claim

For **DISPROVED** under the natural uniform formalization, the release must
contain all of the following:

- the literal radix, precision, exponent range, rounding, contraction, and
  exception semantics;
- exact serialized inputs and the declaration that \(B\) is the exact real
  composite;
- exact nonsingularity and \(\kappa_2\) calculations;
- the midpoint/ties-to-even proof for \(\widehat\beta\);
- one exact transition \(T(0)=0\) plus the induction, rather than a long
  numerical trajectory;
- exact normwise and componentwise backward errors;
- a fail-closed verifier reconstructing all of the above from serialized
  input, plus hashes and a separate evaluator;
- either an explicit binary64 threshold below one or the parametric-in-\(p\)
  proof establishing failure of uniform \(O(\epsilon_p)\);
- a scope statement that the conditional theorem in the source paper and
  materially altered safeguarded algorithms are not contradicted.

For **PROVED** after repairing the conjecture, the minimum burden would be
substantially larger: a completely specified arithmetic/solver/stop model; a
uniform recurrence with \(q<1\); constants independent of data, precision,
and iteration count; treatment of fixed points, cycles, exceptional values,
and all zero denominators; and an independent audit of every step converting
the recurrence to the selected backward-error definition.

## Referee recommendation on the endpoint

The evidence supports **DISPROVED** for the natural, paper-faithful universal
claim that the two condition-number hypotheses alone guarantee eventual
fixed-precision backward stability.  The most defensible theorem statement is
the precision-parametric fixed-point family, with the binary64 scalar
certificate and the two-dimensional embedding as concrete corollaries.

No proof assistant was used or needed for this audit; the decisive reasoning
is exact integer/dyadic arithmetic and induction.
