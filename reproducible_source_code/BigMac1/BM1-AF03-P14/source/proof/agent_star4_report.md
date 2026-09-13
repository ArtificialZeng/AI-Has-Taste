# Exact no-go for the ordered `star4` chamber

## Result

Let (a_0\ge a_1\ge a_2\ge a_3\ge a_4=1), put

\[
 T=\frac12\sum_{i=0}^4a_i,
\]

and consider the open polygon chamber in which the four pairs

\[
 (0,1),(0,2),(0,3),(0,4)
\]

are high, (a_0+a_j>T), while all six pairs among (1,2,3,4) are low,
(a_i+a_j<T).  The saturated critical ideal of the corrected box-spline
piece has **no real root in this ordered chamber**.

This is an exact finite chamber result.  It neither uses nor assumes a
floating-point root search.  It does not classify the other five graph
chambers, subset-sum walls, or zero-coordinate strata.

## Correct chamber polynomial and critical ideal

In this polygon chamber the unscaled box-spline numerator is, up to a fixed
positive rational factor,

\[
 P=T^4-\sum_{i=0}^4(T-a_i)^4
 +\sum_{1\le i<j\le4}(T-a_i-a_j)^4
 -\sum_{j=1}^4(T-a_0-a_j)^4.
\]

The negative sign on a high pair is essential: it is the contribution of the
complementary triple when (T-a_i-a_j<0).  For

\[
 S=\sum_{i=0}^4a_i^2,
\]

the homogeneous section function is proportional to
(S^{1/2}P/\prod_i a_i).  Its logarithmic critical equations, after the
gauge (a_4=1), are

\[
 g_i=a_iS\frac{\partial P}{\partial a_i}+(a_i^2-S)P=0,
 \qquad 0\le i\le3.
\]

Euler homogeneity then forces the fifth logarithmic-gradient component to
vanish as well.  Let

\[
 I=(g_0,g_1,g_2,g_3),\qquad
 J=I:(a_0a_1a_2a_3PS)^\infty.
\]

No chamber root is removed by this saturation: all coordinates and (S) are
positive, and (P>0) because it is a positive scalar multiple of the density
numerator of a nonempty central section.

An exact Singular 4.4.1 computation, independently reconstructed by the
verifier from the high-pair list, gives

\[
 \dim J=0,\qquad \dim_{\mathbb Q}(\mathbb Q[a_0,a_1,a_2,a_3]/J)=48.
\]

Thus the saturated ideal has 48 complex roots counted with multiplicity.
The proof below does not infer anything from decimal approximations to them.

## Six certified low-degree consequences

Exact reduction modulo a reduced Gröbner basis of (J) gives zero for each of
the following polynomials:

\[
 h_{23}=(a_2-1)(a_2-a_3)(a_3-1),
\]

\[
 h_{13}=(a_1-1)(a_1-a_3)(a_3-1),
\]

\[
 h_{12}=(a_1-1)(a_1-a_2)(a_2-1),
\]

\[
 k_3=(a_3-1)\bigl(a_0a_3+a_0-a_1a_3-a_1-a_2a_3-a_2
 -a_3^2+2a_3-1\bigr),
\]

\[
 k_2=(a_2-1)\bigl(a_0a_2+a_0-a_1a_2-a_1-a_2^2+a_2-a_3^2-1\bigr),
\]

and

\[
 k_1=(a_1-1)\bigl(a_0a_1+a_0-a_1^2-a_2^2-a_3^2-1\bigr).
\]

These are not guessed factor equations: the verifier rebuilds (I,J) and
checks their six normal forms exactly.

## Ordered semialgebraic exclusion

By order, it is enough to impose the high inequality for the smallest leaf:

\[
 a_0+1>T
 \quad\Longleftrightarrow\quad
 M:=a_0+1-a_1-a_2-a_3>0.
\]

This inequality already implies the largest low-pair inequality
(a_1+a_2<T), hence all six low-pair inequalities.  The polygon inequality
(a_0<T) remains part of the chamber definition but is not needed in the
contradiction.

### Case 1: (a_3>1)

Since (a_2\ge a_3>1), (h_{23}=0) forces (a_2=a_3).  Similarly
(h_{13}=0) forces (a_1=a_3).  Write their common value as (x>1).
Then (k_3=0) gives

\[
 (x+1)a_0=3x^2+1.
\]

Consequently

\[
 M=a_0+1-3x=\frac{2(1-x)}{x+1}<0,
\]

contrary to the chamber inequality.

### Case 2: (a_3=1)

The equation (h_{12}=0), together with
(a_1\ge a_2\ge1), leaves only two branches:

1. (a_2=1);
2. (a_1=a_2).

On the first branch, if (a_1=x>1), then (k_1=0) gives

\[
 (x+1)a_0=x^2+3,
\]

and therefore

\[
 M=a_0-x-1=\frac{2(1-x)}{x+1}<0.
\]

If instead (a_1=1), all four leaves equal 1.

On the second branch, write (a_1=a_2=x).  If (x>1), then (k_2=0)
gives

\[
 (x+1)a_0=2(x^2+1),
\]

and again

\[
 M=a_0-2x=\frac{2(1-x)}{x+1}<0.
\]

The endpoint (x=1) again has all four leaves equal 1.  Thus every remaining
possibility has

\[
 (a_1,a_2,a_3,a_4)=(1,1,1,1).
\]

### Case 3: all four leaves equal 1

Direct specialization of the independently reconstructed critical equations
gives

\[
 g_0=-4R(a_0),\qquad g_1=g_2=g_3=R(a_0),
\]

up to the same harmless positive primitive scaling, where

\[
 R(X)=X^6-12X^5+51X^4-96X^3+96X^2-64.
\]

The chamber condition is now (M=a_0-2>0).  A primitive Sturm chain for
(R) is

\[
\begin{aligned}
 &R,\\
 &X^5-10X^4+34X^3-48X^2+32X,\\
 &3X^4-20X^3+32X^2-64X+64,\\
 &-5X^3-40X^2+272X-320,\\
 &-19X^2+92X-100,\\
 &379X-540,\\
 &1.
\end{aligned}
\]

At (X=2) its signs are

\[
 +,+,-,+,+,+,+,
\]

with two variations.  At (+∞), the leading-coefficient signs are

\[
 +,+,+,-,-,+,+,
\]

also with two variations.  Sturm's theorem therefore gives exactly zero
roots in ((2,+∞)).  The last branch is excluded.

This completes the exact no-go for the ordered `star4` chamber.

## Independent certificate and verifier

The serialized certificate is
`results/breaker_star4_certificate.json`.  It contains the chamber graph,
gauge, saturated-ideal invariants, six ideal consequences, final polynomial,
primitive Sturm chain, variation counts, branch-margin numerator, and exact
endpoint.

`src/breaker_star4_verify.py` does not import the discovery emitter or any
root-search output.  It:

1. reconstructs (P) twice, once by paired high/low signs and once by direct
   enumeration of all 32 subsets at the exact interior sample
   ((3,1,1,1,1));
2. reconstructs the four critical equations using rational polynomial
   arithmetic from the Python standard library;
3. invokes Singular only for exact saturation, dimension, vector-space
   dimension, and six normal-form checks;
4. reconstructs the all-leaves-one polynomial directly from the four
   critical equations;
5. recomputes the Sturm chain and variation counts using a separate
   standard-library univariate implementation;
6. checks the three branch-margin identities, all of which have numerator
   (2(1-x));
7. rejects unknown, missing, or altered certificate data.

The accepted verification record reports:

* saturated vector-space dimension: 48;
* roots of (R) in ((2,+∞)): 0;
* Singular 4.4.1;
* certificate SHA-256
  `b57cad6aeea0d3db3ac39999bfbdcdcacd48c36d5b2de4883e6806a080bfc935`;
* emitted Singular script SHA-256
  `195856c3e4e1463872515b2b65e8731cd6c2105537ab53320a3ac60f8a2133ee`.

`src/breaker_star4_test.py` accepts the valid certificate and checks rejection
of five mutations: changed chamber edge, changed vector dimension, weakened
ideal consequence, changed Sturm entry, and missing conclusion.  All tests
pass; the log is `experiments/breaker_star4_verifier_tests.json`.

Reproduction commands:

```bash
python src/breaker_star4_verify.py results/breaker_star4_certificate.json
python src/breaker_star4_test.py \
  --output experiments/breaker_star4_verifier_tests.json
```

No Lean, Coq, Isabelle, or other proof assistant was used.  Singular is used
as an exact computer-algebra engine; the short semialgebraic branch argument
and Sturm endpoint are separately exposed above rather than inferred from a
numerical solver.

## Audit note on the obsolete floating-point candidate

An earlier discovery log for the complementary low-pair graph contained a
four-equal-leaf candidate with an apparently positive Hessian.  That log was
generated before the polynomial retained the negative branch of each high
pair.  Substitution into the corrected box-spline gradient gives a nonzero
affine logarithmic-gradient component of approximately (0.498), so it is
not a critical point.  This decimal is only a diagnostic explaining the old
artifact; it is not used anywhere in the exact no-go proof.
