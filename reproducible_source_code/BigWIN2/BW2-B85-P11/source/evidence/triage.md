# Triage evidence (2026-09-11)

## Primary-source inspection

- Xiao-Ye Fu, Yue-Kun Li, Wei-Jie Wang, and Xuan Wang, “Turán problem on the
  union of three intervals of equal length,” arXiv:2608.15643v1,
  https://arxiv.org/abs/2608.15643 and
  https://arxiv.org/pdf/2608.15643 (retrieved 2026-09-11).
- PDF p. 1, equations (1.1)--(1.2): definitions of the continuous Turán
  constant and \(\Omega_\lambda\).
- PDF p. 2, Theorem 1.2: for reduced rational \(p/q>2\),
  \(T_{\mathbb R}(\Omega_{p/q})=q^{-1}T_{\mathbb Z}(A_{p,q})\), where
  \(A_{p,q}\) is defined by the three strict lattice inequalities.  Substitution
  of \((p,q)=(5,2)\) gives
  \(A=\{0,\pm1,\pm4,\pm5,\pm6\}\).
- PDF p. 9, Section 4.1: finite nonnegative-trigonometric-polynomial/PSD Gram
  formulation.  PDF pp. 9--11, Proposition 4.2: the explicit square-polynomial
  certificate proves only
  \((559+80\sqrt{42})/506\) as a lower bound.  PDF pp. 11--12, Lemma 5.1:
  \(T_{\mathbb R}(\Omega_\lambda)\leq(\lambda+2)/2\), hence \(9/4\) here.
- PDF p. 13, Discussion: finite arithmetic models remain to be evaluated; it
  does not isolate \(\lambda=5/2\) as a formal open problem.

## Search screen

The following exact/equivalent web searches were run on 2026-09-11: the full
paper title and arXiv identifier; `"559+80" "sqrt(42)" Turan`;
`"Omega_{5/2}" Turán constant`; `"λ = 5/2" "Turán" "three intervals"`; and
`arXiv exact Turán constant union three intervals 5/2`.  The only relevant
primary result returned was arXiv:2608.15643v1.  A secondary review merely
restated its one-sided result and was not used as evidence.  This supports the
label `status-uncertain`, not a claim that the question is open or novel.

## Cheapest discriminating computation

Using SciPy HiGHS, the objective was maximized subject to nonnegativity at
50,001 equally spaced points in \([0,\pi]\).  Result:

```
c = (0.566991453829015, 0.373411234019908,
     0.473050097853300, 0.221854424075459)
T_Z(grid) = 4.270614419555363
T_R(grid) = 2.1353072097776815
apparent cos(t) at active minima =
  0.7976663039, -0.4145293855, -0.9162005460
continuous local-minimum residuals: approximately -1.3e-8, -4.9e-8, -2.7e-8
```

This is floating-point route selection only.  Grid feasibility does not imply
nonnegativity for every real \(t\), and none of these numbers is asserted as a
bound or exact value.
