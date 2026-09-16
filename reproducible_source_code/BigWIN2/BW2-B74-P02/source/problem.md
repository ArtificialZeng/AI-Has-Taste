# Precise problem reading

## Frozen statement and ambient conventions

The immutable source is `source.md` (SHA-256
`1d3e86e773c0cff8e1d4cf1ab82845ff365401ba6a6d9caf6edc554a7a15af15`).
Its claim is read with the quantifiers

\[
  \text{for every field }K\text{ and every integer }c\ge 2.
\]

For each such pair, let \(R=K[x,y,z]\) with its standard total-degree
grading, let

\[
 I_c=(x^2,y^2,z^c,xyz)\subset R,
\]

and let \(\overline{I_c}\) be the integral closure of \(I_c\) in \(R\).
For a homogeneous ideal \(J\subset R\), interpret

\[
 v(J)=\min\{d\ge0:\text{ some homogeneous }f\in R_d\text{ has }
 (J:f)=\mathfrak p\in\operatorname{Ass}_R(R/J)\}.
\]

The exact simultaneous assertion to prove or disprove is

\[
 v(I_c)=2,\qquad v(\overline{I_c})=\left\lceil\frac c2\right\rceil
 \quad(c\ge2).
\]

The endpoint comparison is part of the frozen target: strict reversal
\(v(\overline{I_2})<v(I_2)\), equality for \(c=3,4\), and
\(v(I_c)<v(\overline{I_c})\) exactly when \(c\ge5\). No restriction on the
characteristic or cardinality of \(K\) is intended.

The claim is one universal simultaneous classification. A disproof requires
one explicit pair \((K,c)\), with \(c\ge2\), for which either displayed formula
fails. A proof must cover every field and every integer \(c\ge2\); checking a
finite range, or reproving only the published \(c=5\) instance, does not settle
the frozen claim.

Both ideals contain powers of every variable, hence are
\(\mathfrak m=(x,y,z)\)-primary. Thus their only associated prime is
\(\mathfrak m\), and \(v(J)\) is the least total degree of a nonzero socle
class in \(R/J\). For a monomial ideal this can be tested on monomials.

## Nearest verified primary result and proposed delta

Biswas--Mandal--Phukan, *A comparison of the v-number of a monomial ideal
and its integral closure*, arXiv:2609.05044v1 (submitted 4 September 2026),
Theorem 3.2 treats all monomial ideals in two variables. Example 3.3 (printed
p. 6) treats only \(c=5\), giving

\[
 \overline{I_5}=(x^2,xy,y^2,xz^3,yz^3,z^5),\qquad
 v(I_5)=2<v(\overline{I_5})=3.
\]

Primary record: <https://arxiv.org/abs/2609.05044>, inspected 2026-09-09.
The supplied v1 PDF has SHA-256
`e8ba90b5273578389918379df6e5b66fc899825ddb3b66dcb0f866f04e1561ab`.
Neither the full text nor exact-assertion searches located the parameterized
classification. This is limited search evidence, not a claim of priority or
proof that the question was previously open. Source status is therefore
**new-question / status-uncertain**, not “open-supported.”

The proposed contribution is: nearest prior result \(c=5\); delta an exact
all-\(c\ge2\) classification including endpoints; verification route the
Newton-polyhedron lattice criterion, complete socle classification, and an
independent exhaustive enumeration for \(2\le c\le20\).
