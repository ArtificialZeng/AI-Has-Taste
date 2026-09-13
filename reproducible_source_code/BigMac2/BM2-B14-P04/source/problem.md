# Precise reading of the problem

Provenance: `bigMac-00014-p04-triage-c7125e032d58`.

## Frozen claim

Write \([3]=\{1,2,3\}\) and
\[
B_3=(2^{[3]},\subseteq).
\]
Thus the ground set is all eight subsets of \([3]\), including \(\varnothing\)
and \([3]\), and the order is ordinary (nonstrict) set inclusion. The string
`subseteq` in `source.md` is read as the relation \(\subseteq\). The claim to be
proved or disproved is exactly
\[
\operatorname{rdim}(B_3)=2.
\]
There are no asymptotic, fractional, weighted, or proper-part variants in scope.

## Definitions and quantifiers

For a subset \(S\subseteq B_3\), a **partial linear extension** (PLE) \(M\)
is a total order on \(S\) that extends the subposet induced by inclusion: for
all \(A,B\in S\), if \(A\subseteq B\), then \(A\le_M B\).

Let \(t\in\mathbb Z_{\ge 0}\) and let
\(\mathcal L=\{M_1,\ldots,M_t\}\) be a finite set of PLEs, with ground sets
\(S_1,\ldots,S_t\). It is a **local realizer** of \(B_3\) precisely when, for
every ordered pair \((A,B)\in B_3^2\):

1. there is an \(i\in[t]\) with \(A,B\in S_i\); and
2. one has
   \[
   A\subseteq B
   \quad\Longleftrightarrow\quad
   (\forall i\in[t]\text{ with }A,B\in S_i)\ A\le_{M_i}B.
   \]

The first condition makes the universal quantifier in the second condition
nonvacuous. Equivalently, every comparable pair must occur together in at
least one PLE, while every unordered incomparable pair must occur in both
relative orders (possibly in two different PLEs). The case \(A=B\) also
requires every element to occur. Repeated identical PLEs are immaterial: the
paper defines a set, and even if repetitions were allowed they could only add
cost and cannot improve the optimum.

The **total element-occurrence cost**, **relative frequency**, and **relative
dimension** are
\[
C(\mathcal L)=\sum_{i=1}^t |S_i|,
\qquad
\|\mathcal L\|_r=\frac{C(\mathcal L)}{|B_3|}
=\frac{C(\mathcal L)}8,
\qquad
\operatorname{rdim}(B_3)
=\min_{\mathcal L\text{ local realizer}}\|\mathcal L\|_r.
\]
Consequently, the frozen equality is exactly the finite optimization statement
\[
\min_{\mathcal L\text{ local realizer of }B_3} C(\mathcal L)=16.
\]
Its upper half is the existential assertion that a local realizer of cost 16
exists. Its lower half is the universal assertion that, for every
\(t\in\mathbb Z_{\ge0}\) and every set of \(t\) PLEs of \(B_3\), cost at most
15 implies that the set is not a local realizer.

## Exact upper witness already in the primary source

Relabel \([3]\) as \(\{a,b,c\}\). Figure 1 of the cited paper gives
\[
\begin{aligned}
L_1:&\quad \varnothing<a<b<ab<c<ac<bc<abc,\\
L_2:&\quad c<b<bc<a<ac<ab,\\
L_3:&\quad ac<b,
\end{aligned}
\]
where, for example, \(ab=\{a,b\}\). Each displayed order is a PLE.
The full PLE \(L_1\) supplies element and comparable-pair coverage. The nine
incomparable pairs are the three pairs of singletons, the three pairs of
two-element sets, and \(a\parallel bc\), \(b\parallel ac\),
\(c\parallel ab\). Relative to \(L_1\), \(L_2\) reverses all of them except
\(b\parallel ac\), and \(L_3\) reverses that last pair. Hence these three PLEs
form a local realizer, with exact cost \(8+6+2=16\), proving
\(\operatorname{rdim}(B_3)\le2\).

Thus a disproof of the equality in the stated scope must exhibit a valid local
realizer of integer cost at most 15. A proof must additionally exclude **all**
such families. As required by `source.md`, the exclusion must be independently
checkable (for example, a rational covering-dual certificate checked against
every PLE, or a replayable proof-checked SAT/UNSAT artifact); an optimizer's
status line is not a certificate.

## Prior-result boundary and proposed delta

Nearest inspected result: Dürrschnabel--Hodor--Micek--Stumme--Trotter,
*Relative Dimension of Posets*, arXiv:2609.05166v1, pp. 2--3 (definitions and
Boolean-lattice notation) and p. 8, Figure 1 / proof of Theorem 5 (the cost-16
upper witness). The inspected text proves only the upper bound for \(B_3\); it
does not give the matching lower certificate. The exact-value question is not
listed separately among the paper's open questions on p. 9, so its literature
status remains **status-uncertain**, not “open-supported.”

Target contribution: starting from the known cost-16 witness, either produce a
replayable lower certificate showing optimum at least 16, or find and directly
verify a cost-at-most-15 witness. The bounded verification route is exhaustive
enumeration of the PLEs of induced subposets of \(B_3\), followed by an exact
covering/ILP or proof-producing SAT formulation.
