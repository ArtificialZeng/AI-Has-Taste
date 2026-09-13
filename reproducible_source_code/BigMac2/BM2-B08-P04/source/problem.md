# Precise problem statement

## Frozen claim and quantifiers

Let $K$ be an arbitrary field, let $R=K[x,y,z]$ have its standard total-degree grading, and let
\(\mathfrak m=(x,y,z)\). For every proper \(\mathfrak m\)-primary monomial ideal \(I\subset R\) satisfying

1. its **unique minimal** monomial generating set \(G(I)\) has \(|G(I)|\le 4\); and
2. every \(u\in G(I)\) has total degree \(\deg u\le 4\),

decide whether

\[
v(\overline I)\le v(I).
\]

The universal quantifier is over all such labeled ideals in the three fixed variables and over every field $K$. The degree restriction is not a restriction on a redundant presentation. No characteristic, algebraic-closure, or infinitude assumption on $K$ is intended.

This is the precise reading of the immutable statement in `source.md`; it neither asserts that the question was posed as open in the cited paper nor changes the degree-four boundary.

## Conventions and definitions

- For a homogeneous ideal $J\subset R$, the paper's convention is
  \[
  v(J)=\min\{d\ge 0:\text{ for some }f\in R_d\text{ and }\mathfrak p\in
  \operatorname{Ass}_R(R/J),\ (J:f)=\mathfrak p\}.
  \]
  Here \((J:f)=\{g\in R:gf\in J\}\). (The paper writes \(\operatorname{Ass}(J)\) for the associated-prime condition.)
- An element is integral over $I$ in the usual ideal-theoretic sense, and \(\overline I\) is the ideal of all elements integral over $I$.
- For a monomial ideal with generator exponent set $A\subset\mathbb N^3$,
  \[
  \operatorname{NP}(I)=\operatorname{conv}(A)+\mathbb R_{\ge0}^3,
  \qquad
  x^u\in\overline I\iff u\in\operatorname{NP}(I)\cap\mathbb N^3.
  \]
- Since $I$ is \(\mathfrak m\)-primary, so is \(\overline I\), and each has the sole associated prime \(\mathfrak m\). Thus for either $J=I$ or $J=\overline I$, the definition reduces exactly to the monomial-socle formula
  \[
  v(J)=\min\bigl\{|u|:u\in\mathbb N^3,\ x^u\notin J,
  \ x^{u+e_x},x^{u+e_y},x^{u+e_z}\in J\bigr\}.
  \]
  This also makes the comparison independent of the characteristic of $K$.

## Complete finite parameterization of the input class

Every admissible ideal has exactly three or four minimal generators. After retaining the fixed variable labels, it has exactly one of the forms

\[
(x^a,y^b,z^c)
\]

or

\[
(x^a,y^b,z^c,x^r y^s z^t),
\]

where $1\le a,b,c\le4$, and in the four-generator case

\[
r,s,t\in\mathbb N,\quad r+s+t\le4,\quad
r<a,\ s<b,\ t<c,\quad |\{i:r_i>0\}|\ge2.
\]

These conditions are necessary and sufficient: \(\mathfrak m\)-primaryness forces one minimal pure power of each variable; at most one further generator remains; and the displayed strict inequalities plus mixed support say precisely that the fourth generator is incomparable with all three pure powers. Variable permutations may be used to reduce a computation only if orbit representatives and their lifting back to all labeled ideals are recorded.

For exact finite verification, every monomial outside $I$ or \(\overline I\) lies in the box
\(0\le u_x<a\), \(0\le u_y<b\), \(0\le u_z<c\), containing at most $64$ lattice points.

## Prior boundary and proposed contribution

The inspected primary source is Biswas--Mandal--Phukan, *A comparison of the v-number of a monomial ideal and its integral closure*, arXiv:2609.05044v1 (4 September 2026), local PDF SHA-256 `e8ba90b5273578389918379df6e5b66fc899825ddb3b66dcb0f866f04e1561ab`, inspected 7 September 2026. Its definition and Newton-polyhedron convention occur on PDF/printed page 1; Theorem 3.2 and Example 3.3 occur on page 6; and the three-variable equigenerated result, Theorem 3.12, occurs on page 9. The paper proves the inequality in two variables and for three-variable equigenerated monomial ideals, while Example 3.3 reports

\[
I=(x^2,y^2,z^5,xyz),\qquad v(I)=2<3=v(\overline I),
\]

a four-generator counterexample whose largest minimal-generator degree is five.

Accordingly, the target contribution is: nearest prior boundary = the degree-five example and the stated positive classes; proposed delta = either a degree-at-most-four exact counterexample or a complete proof for the finite exponent-antichain class above; verification route = exhaustive exact enumeration using rational Newton-polyhedron membership and independent monomial-colon/socle checks, accompanied by the displayed completeness parameterization. The source describes this degree-four boundary as a newly proposed finite question, not as an openness claim by the paper's authors.
