# Precise problem: codimension-\(\dim A_0\) ideals and splitness

## Frozen source and source status

The immutable statement is `source.md` (SHA-256
`62db45a34c5b7fcbc91aac4c9f4955563f752eebfc6f9969d4307d5e9230c9e4`).
The cited arXiv v1 PDF was inspected on 2026-09-09 and has the stated SHA-256
`f1dff9a9f6decb301ce097bd319c2085f553e5e92f7dddafff63e772db41816e`.
Definition 1.1 (p. 1), Definition 4.1 (p. 4), and Question 6.1 (p. 9)
support the reading below. Thus the source status is **open-supported in that
specific primary source**; this triage statement is not a claim that later
literature contains no resolution.

Question 6.1 prints \(J\lhd\) without an object. The immediately preceding text
and Definition 4.1 make the only coherent reading \(J\lhd A\), a two-sided ideal
of \(A\). This is treated as a typographical omission, not a change of scope.

## Objects and definitions

The paper fixes a field \(k\); the source asks for an arbitrary field. Thus the
claim is read uniformly: quantify over every field \(k\) and every unital
associative graded \(k\)-algebra

\[
A_\bullet=\bigoplus_{i\ge 0}A_i,\qquad A_iA_j\subseteq A_{i+j},
\]

with all of the following properties.

1. **Semiconnected:** the grading is nonnegative and \(A_0\) is a semisimple
   \(k\)-algebra. Semisimple does not mean split semisimple or \(k\)-elementary.
2. **Standard graded:** \(A\) is generated as a \(k\)-algebra by \(A_0\cup A_1\).
3. **Locally finite:** \(\dim_k A_i<\infty\) for every \(i\).

Let \(J\lhd A\) be an arbitrary two-sided ideal; it need not be homogeneous, and
no tangent-dimension condition is imposed. Write
\(q_J:A\to A/J\) for the quotient map and \(\iota:A_0\hookrightarrow A\) for the
degree-zero inclusion. The ideal is **split with respect to the fixed grading**
when

\[
\theta_J=q_J\circ\iota:A_0\longrightarrow A/J
\]

is an isomorphism of \(k\)-algebras.

## Exact claim and its negation

The frozen question asks whether the following universal assertion is true:

> For every field \(k\), every \(A_\bullet\) satisfying the three conditions above,
> and every two-sided \(J\lhd A\) satisfying
> \(\dim_k(A/J)=\dim_k(A_0)\), the natural map \(\theta_J\) is an isomorphism of
> unital \(k\)-algebras.

Local finiteness makes \(A_0\) finite-dimensional, so under the displayed dimension
equality the domain and codomain of \(\theta_J\) have the same finite dimension.
Consequently the conclusion is equivalently any one of

\[
J\cap A_0=0,\qquad A=A_0+J,\qquad A=A_0\oplus J
\]

(the last equality is as \(k\)-vector spaces). A disproof therefore requires one
admissible tuple \((k,A_\bullet,J)\) with the dimension equality and
\(J\cap A_0\ne0\); one such field suffices, while a construction valid for every
field would be stronger.

No indecomposability, faithful \(A_0\)-action on \(A_1\), prescribed tangent
dimension, or positive-dimensional \(A_i\) assumption is present. Minimality is
also not part of Question 6.1 and must be proved separately if asserted.

## Nearest source result and bounded target

The nearest result in the cited source is Proposition 4.7 (pp. 5--6): ideals of
the special form \(\varphi^{-1}(B_+)\), arising from an ungraded isomorphism between
admissible graded algebras, are split. Question 6.1 removes that special origin
and retains only the codimension condition.

The cheapest proposed test is the finite-dimensional datum

\[
A=k\times k[\varepsilon]/(\varepsilon^2),\quad
A_0=\{(a,b):a,b\in k\},\quad
A_1=\{(0,c\varepsilon):c\in k\},\quad
A_i=0\ (i\ge2),\quad
J=k\times0.
\]

At triage this is a candidate test, not yet a certified result. The target delta
is an exact counterexample to the unrestricted Question 6.1; the verification
route is a line-by-line check of the grading, all three hypotheses, two-sided
ideal closure, both dimensions, and \(\ker(\theta_J)\).
