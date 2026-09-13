# Formal statement and statement repair

## Source-level ambiguity

Hashemi--Nakatsukasa (arXiv:2510.01696v1, abstract and Algorithm 2) use the
phrases "bounded safely away from \(\epsilon_M^{-1}\)", "eventually", and
"accuracy is insufficient" without specifying constants, a stopping test, or
the behavior on a computed zero Sherman--Morrison denominator.  Consequently
the source conjecture is not, literally, a closed mathematical proposition.
The universal core below is the weakest natural precise claim implied by
"eventually produce a backward-stable solution"; disproving it does not settle
a repaired conjecture that adds a no-breakdown or scaling hypothesis.

## Tested universal core (C0)

Fix IEEE-754 binary64 arithmetic with round-to-nearest, ties-to-even, default
nontrapping exceptional behavior, unit roundoff
\(\epsilon_M=2^{-53}\), and no fused contraction of the displayed operations.
For every \(n\ge1\), every finite binary64 input
\(A\in\mathbb R^{n\times n}\), \(u,v,b\in\mathbb R^n\) for which the exact real
matrices \(A\) and \(B=A+uv^T\) are nonsingular and satisfy

\[
  \kappa_2(A),\kappa_2(B)\le c\epsilon_M^{-1}
\]

for some fixed safety factor \(0<c<1\), Algorithm 2 of
Hashemi--Nakatsukasa, with correctly rounded scalar solves in dimension one
(and a backward-stable \(A\)-solver in general), eventually returns a finite
iterate \(\widehat x\) whose normwise relative backward error

\[
 \eta_B(\widehat x)=
 \frac{\lVert b-B\widehat x\rVert_2}
      {\lVert B\rVert_2\lVert\widehat x\rVert_2+\lVert b\rVert_2}
\]

is at most \(C(n)\epsilon_M\), where \(C(n)\) is a modest dimension-dependent
constant independent of the data and iteration count.

The exact counterexample below refutes C0 for every choice of \(c\) satisfying
\(2^{-53}<c<1\): it has no exceptional operations, every iterate is finite,
and the relative backward error is exactly one.  Thus the conclusion fails for
every data-independent stability constant \(C(1)<2^{53}\), in particular for
every conventional modest constant.

## Uniform backward-stability core (C-uniform)

To remove the hidden-constant ambiguity, let \(p\to\infty\) through radix-two
formats with precision \(p\), round-to-nearest/ties-to-even, unit roundoff
\(\epsilon_p=2^{-p}\), and sufficient exponent range.  The natural uniform
form of the conjecture asserts that there is a constant \(C(n)\), independent
of \(p\), the data, and the iteration count, such that SM-IR eventually
returns an iterate with \(\eta_B\le C(n)\epsilon_p\), whenever

\[
 \epsilon_p\kappa_2(A_p)\to0,
 \qquad \epsilon_p\kappa_2(B_p)\to0.
\]

This is the precise meaning of the \(O(\epsilon_M)\) conclusion and
"safely below \(\epsilon_M^{-1}\)" used for the terminal disproof.  The
counterexample has \(\eta_B=1\) for every \(p\), so
\(\eta_B/\epsilon_p=2^p\to\infty\).  A concrete binary64 corollary also misses
the source paper's experimental threshold \(5\epsilon_M\).

## Algorithm fixed for certification

In dimension one, Algorithm 1 first computes, in the displayed order,

\[
 \widehat y=\operatorname{RN}(b/A),\quad
 \widehat z=\operatorname{RN}(u/A),\quad
 \widehat\alpha=\operatorname{RN}(v\widehat y),\quad
 \widehat\beta=\operatorname{RN}(1+\operatorname{RN}(v\widehat z)),\quad
 \widehat\theta=\operatorname{RN}(\widehat\alpha/\widehat\beta),
\]

then \(\widehat x=\operatorname{RN}(\widehat y-
\operatorname{RN}(\widehat\theta\widehat z))\).  Algorithm 2 reuses the same
\(\widehat z\) and \(\widehat\beta\) for every correction.

## Domain, normalizations, and edge cases

- The exact problem data are the real values of the finite binary64 inputs;
  \(B=A+uv^T\) is **not** assumed to have been formed in floating point.
- Dimension one is included by the source statement; for every nonzero scalar
  \(a\), \(\kappa_2([a])=1\).
- Overflow, underflow, subnormal arithmetic, and division by zero are absent
  throughout the decisive trace.
- The decisive certificate has a nonzero computed \(\widehat\beta\) and uses
  no exceptional value.  Computed-zero breakdown is retained only as a
  secondary structural route.
- The result does not assert failure if implementations add a scale/breakdown
  guard, recompute \(B\), or fall back to a direct solve; those are different
  algorithms.

## Repaired conjecture left outside C0

A meaningful variant must control the accuracy and cancellation of the full
SM corrector, for example by an explicit correction-residual contraction or
the source paper's \(h\)-term, and must specify the residual evaluation,
stopping rule, exception handling, and backward-error norm.  A lower bound on
\(|1+v^TA^{-1}u|\) alone is not enough: in the counterexample both the exact
and computed denominators are large and nonzero.  Whether such a repaired
fixed-precision iteration always enters an \(O(\epsilon_M)\) regime is not
claimed here.
