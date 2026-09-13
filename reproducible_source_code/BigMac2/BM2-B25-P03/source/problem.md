# Precise problem reading

## Frozen target

The immutable wording is in `source.md`. Its precise mathematical reading is
the following universal finite claim.

Let
\[
G=\mathbb F_3^2=\{(x,y):x,y\in\{0,1,2\}\},
\]
with componentwise addition modulo \(3\), and let \(0=(0,0)\). For every
subset \(S\subset G\) with \(|S|=4\), put \(T=G\setminus S\), so \(|T|=5\).
The question is whether there is an injective map
\[
f:S\longrightarrow T
\]
such that, as a multiset,
\[
\biguplus_{s\in S}\{s-f(s),f(s)-s\}=G\setminus\{0\}.
\tag{1}
\]
Equivalently, the four unordered cross edges
\(\{s,f(s)\}\), \(s\in S\), are pairwise vertex-disjoint and have all four
possible nonzero directions in \(G\), one direction per edge.

The phrase “after possibly swapping the names of the parts” is read as one
global relabelling: \(S\) is the part of size \(4\) and \(T\) the part of size
\(5\). Edge orientation is immaterial because both signs of every difference
occur in (1).

## Definitions and equivalent normalization

For a cross edge \(e=\{x,y\}\), define its (unoriented) length by
\[
\ell(e)=\{x-y,y-x\}=\{d,-d\}.
\]
Because the group has odd order, \(d\ne-d\) for every \(d\ne0\). The eight
nonzero vectors split into exactly four antipodal pairs,
\[
\{\pm(1,0)\},\quad \{\pm(0,1)\},\quad
\{\pm(1,1)\},\quad \{\pm(1,2)\}.
\]
Thus (1) says precisely that the multiset of the four edge lengths is the
displayed set of four pairs. Injectivity of \(f\) makes the edges disjoint;
all four vertices of \(S\) and four vertices of \(T\) are used, leaving
exactly one vertex of \(T\) unmatched. Cross edges cannot be loops because
\(S\cap T=\varnothing\).

The affirmative quantifier is
\[
\forall S\subseteq G\ (|S|=4)\quad \exists\hbox{ injective }f:S\to G\setminus S
\quad\text{satisfying (1)}.
\]
A disproof must instead exhibit one explicit \(S\) of size \(4\) and prove
that every injection \(f:S\to G\setminus S\) fails (1). There are \(\binom94=126\)
labelled choices of \(S\) and \(5\cdot4\cdot3\cdot2=120\) injections for each
one, before symmetry reduction.

Here \(\mathbb F_3^2\) is used only as an additive group/vector space, not as
the field \(\mathbb F_9\). No assertion about other groups, larger dimensions,
or arbitrary part sizes is included.

## Source status and nearest results

Sources were inspected on 2026-09-09.

- Afifurrahman, Primaskun, Putri, and Wijaya, *On constructing 1-factors of
  labelled complete graph*, **Open Problem 2** (publisher version, pp. 9–10),
  asks for necessary and sufficient conditions for exactly this cross-part
  matching problem in every odd-order finite abelian group with balanced part
  sizes. DOI: <https://doi.org/10.1007/s40590-025-00772-2>.
- Yip, Yoo, and Yu, *Paley-type matrices and 1-factorizations of complete
  graphs*, arXiv:2601.12250v3, **Problem 1.6 and Theorem 1.7**, prove the
  corresponding same-part statement for every partition of every odd-order
  finite abelian group. The paragraph immediately after Theorem 1.7 identifies
  the cross-part analogue above and says their methods do not seem to extend
  directly to it. <https://arxiv.org/html/2601.12250v3#S1.Thmtheorem7>.
- The prime-cyclic Paley result in Theorem 1.4 of the latter paper concerns a
  special quadratic-residue partition (with an added centre); it does not
  settle arbitrary balanced partitions of the noncyclic additive group
  \(\mathbb F_3^2\).

Accordingly, the general cross-part framework is explicitly posed in primary
literature, but the truth of this particular finite layer was not separately
settled in the inspected sources. Its source status is therefore
**status-uncertain**, not a verified claim of novelty or openness.

## Triage target

Nearest prior result: the general cross-part Open Problem 2 above, together
with the same-part theorem of Yip–Yoo–Yu. Proposed delta: resolve the universal
cross-part assertion for the smallest noncyclic odd-order group,
\(\mathbb F_3^2\), either for all 126 labelled partitions or by one exact
counterexample. Verification route: exact enumeration of the finite search
space, followed by a checkable structural proof in the affirmative case or a
complete no-matching certificate for the first counterexample in the negative
case. This is a precise, bounded, nontrivial target and is admitted to research.
