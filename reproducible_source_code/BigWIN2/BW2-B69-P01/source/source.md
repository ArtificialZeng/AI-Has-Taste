# win-00069-p01 — Subtraction-free bounded ratios in degree four and three variables

## Immutable primary-source record

- Primary source: Aayush Bathija, Prince Rohatgi, and Daniel Soskin, *Bounded ratios for Lorentzian polynomials*, arXiv:2609.05341v1 [math.CO].
- Official abstract: <https://arxiv.org/abs/2609.05341v1>.
- Official HTML: <https://arxiv.org/html/2609.05341v1>.
- Frozen conjecture location: §9, Definition 9.1 and Conjecture 9.2.
- Nearest-result location: §7.3, Proposition 7.4, especially the exact computation following it.
- Source-stated status: Conjecture 9.2 explicitly conjectures that every integral exponent vector in the product bounded-ratio cone gives a subtraction-free ratio. The source reports selected extreme-ray verifications but does not state the \((4,3)\) specialization as proved.
- Access record: the official arXiv abstract and HTML were read directly. No PDF or other source file was downloaded into staging.

## Source definitions and frozen assertion

Use the source's notation without changing its normalization. Let
\[
H(4,3)=\{\alpha=(\alpha_1,\alpha_2,\alpha_3)\in\mathbb Z_{\ge0}^{3}:
\alpha_1+\alpha_2+\alpha_3=4\}.
\]
For products of four nonnegative ternary linear forms, let \(P_\alpha\) be the ordinary coefficient indexed by \(\alpha\), exactly as in the source. Let
\(\mathrm{BR}_{\mathring Q}(4,3)\) mean the source's product bounded-ratio cone, with all of its balance, affine-quotient, and domain conventions retained.

For
\[
\gamma\in\mathrm{BR}_{\mathring Q}(4,3)\cap\mathbb Z^{H(4,3)},
\]
write
\[
N_\gamma=\prod_{\gamma_\alpha>0}P_\alpha^{\gamma_\alpha},
\qquad
D_\gamma=\prod_{\gamma_\alpha<0}P_\alpha^{-\gamma_\alpha},
\qquad
R_\gamma=\frac{N_\gamma}{D_\gamma}.
\]
Definition 9.1 says that \(R_\gamma\) is subtraction-free when there exists a positive constant \(C\) such that
\[
C D_\gamma-N_\gamma,
\]
expanded as a polynomial in the twelve parameters \(a_{ri}\), has only nonnegative coefficients.

Resolve the following complete specialization of Conjecture 9.2:

> For every
> \(\gamma\in\mathrm{BR}_{\mathring Q}(4,3)\cap\mathbb Z^{H(4,3)}\),
> there exists a constant \(C=C(\gamma)>0\) for which
> \(C D_\gamma-N_\gamma\) is coefficientwise nonnegative in the
> \(a_{ri}\).

The quantifier is over every integral point of the cone, not merely its extreme rays. The constant may depend on \(\gamma\); the project does not impose \(C=1\).

An acceptable resolution is either a proof of the displayed universal statement or one explicit integral \(\gamma\) in the exact source cone together with a coefficient certificate showing that no \(C>0\) can work.

## Nearest source result and precise delta

Proposition 7.4 proves
\[
\mathrm{BR}_{\mathring L}(n,3)=\mathrm{BR}_{\mathring Q}(n,3)
\qquad\text{for }n=3,4,5
\]
and gives the common cone by triangular rays. The numbers of distinct extreme rays for \(n=3,4,5\) are \(9,18,30\), respectively. Thus the target cone at \((4,3)\) has an exact 18-ray description.

Conjecture 9.2 then reports \(C=1\) checks for all nine extreme rays of
\(\mathrm{BR}_{\mathring Q}(3,3)\) and all eighty extreme rays of
\(\mathrm{BR}_{\mathring Q}(3,4)\). These are different parameter pairs. The paper does not report an all-integral-point verification for
\(\mathrm{BR}_{\mathring Q}(4,3)\).

The proposed delta is exactly the complete \((4,3)\) specialization, including non-ray lattice points and nonunimodular semigroup effects. It is not a new bound for a single ratio and not a claim about every \((n,k)\).

## Cheapest decisive attack

### Stage 1: exact primitive-ray falsification

Recover the 18 primitive ray generators from the exact cone description, audit that they lie in the same lattice used by Conjecture 9.2, and expand \(N_\gamma,D_\gamma\) exactly in
\[
\mathbb Z_{\ge0}[a_{11},a_{12},a_{13},\ldots,a_{41},a_{42},a_{43}].
\]
For a fixed \(\gamma\), subtraction-freeness is equivalent to support containment together with finitely many coefficient inequalities: every monomial having positive coefficient in \(N_\gamma\) must have positive coefficient in \(D_\gamma\), after which a sufficiently large rational \(C\) can be chosen as the maximum relevant coefficient ratio.

Consequently, a numerator monomial absent from the denominator is an immediate exact counterexample certificate. Record \(\gamma\), its verified cone decomposition, the monomial, and the two exact coefficients.

### Stage 2: sign-chamber Hilbert-basis proof

Passing the 18 primitive rays is not a proof. Intersect the rational cone with every realizable coordinate-sign chamber for \(\gamma\), and compute the exact affine semigroup and its Hilbert basis in the balanced lattice. Separate any lattice of units or lineality before applying a positive-monoid argument.

Within a fixed sign chamber, if \(\gamma\) and \(\eta\) have compatible signs, then
\[
N_{\gamma+\eta}=N_\gamma N_\eta,\qquad
D_{\gamma+\eta}=D_\gamma D_\eta.
\]
If constants \(C_\gamma,C_\eta>0\) certify the two ratios, then
\[
C_\gamma C_\eta D_\gamma D_\eta-N_\gamma N_\eta
=
C_\eta D_\eta(C_\gamma D_\gamma-N_\gamma)
+N_\gamma(C_\eta D_\eta-N_\eta),
\]
which is coefficientwise nonnegative. Thus exact certificates for every Hilbert-basis element of every sign chamber, plus a correct generation proof, imply the full frozen statement.

Use exact rational polyhedral arithmetic and exact integer polynomial expansion. Floating-point cone membership or sampled positive evaluations are not certificates.

## Mandatory checks and falsification risks

- Audit the source's distinction between ordinary coefficients \(P_\alpha\) and normalized coefficients. The factorial correction discussed after Conjecture 9.2 must not be silently moved into the wrong definition.
- Reproduce the source's balance equations, affine quotient, and \(\mathring Q\) domain exactly before computing primitive rays or Hilbert bases.
- Do not infer an integer-semigroup statement from a real conical generating set. Primitive extreme rays need not form a Hilbert basis.
- Do not add vectors from different sign chambers without accounting for cancellation between numerator and denominator.
- If the cone has lineality, handle its lattice units explicitly; a positive Hilbert-basis routine applied blindly may be invalid.
- A numerical inequality \(R_\gamma(a)\le C\) on sampled \(a\) does not prove coefficientwise nonnegativity.
- If an extreme ray already fails, independently verify its primitive scaling and exact membership before calling it a counterexample.

## Semantic neighbors and contribution boundary

The current and historical registries contain Lorentzian bounded-ratio projects win-00043-p01, win-00057-p01, and win-00057-p06. They arise from arXiv:2609.03934 and concern optimal constants for dimension-six hypermetric ratios or the CW7 symmetric family. They do not address the subtraction-free coefficient property, the cone of arXiv:2609.05341, or its \((4,3)\) integral semigroup. They remain semantic neighbors and must be cited in intake dedup, not treated as duplicates.

The project may report a failing ray, a verified finite subset, or a partial sign chamber as a scoped partial result. It may claim the full specialization only after every integral point is covered by a proved semigroup argument and all polynomial certificates receive fresh independent audit.
