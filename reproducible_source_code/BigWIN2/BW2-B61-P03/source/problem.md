# Precise reading

## Frozen finite complex

Let \(V=\{0,1,\ldots,8\}\).  Let \(S\) be the abstract simplicial complex
whose facets are the following 18 distinct unordered triples:

\[
\begin{aligned}
F(S)=\{&105,053,537,374,741,410,\\
       &216,165,658,587,872,721,\\
       &023,236,364,648,480,802\}.
\end{aligned}
\]

Here, for example, \(105\) denotes \(\{1,0,5\}\); the order in a displayed
facet has no mathematical significance.  All faces of these facets are
included in \(S\).

## Circuits and decompositions

A **2-circuit** is a finite cyclic word
\(W=(v_i)_{i\in\mathbb Z/n\mathbb Z}\) in vertices of \(S\) such that:

1. every cyclic window \(T_i=\{v_i,v_{i+1},v_{i+2}\}\) is a three-element
   facet of \(S\); and
2. the map \(i\mapsto T_i\) is injective, so no facet occurs twice in the
   circuit.

Vertices may repeat in a word.  A **2-circuit decomposition** is a finite,
unordered collection of such circuits for which the sets of cyclic windows
are pairwise disjoint and have union \(F(S)\).  Consequently, the sum of the
word lengths in a decomposition is 18.  Define

\[
c(S)=\min\bigl\{m\geq 1:S\text{ has a 2-circuit decomposition into }m
\text{ circuits}\bigr\}.
\]

The three cyclic words

\[
105374,\qquad216587,\qquad023648
\]

give a decomposition, with the parenthesized suffixes in the frozen source
only displaying the cyclic wraparound.  Thus \(c(S)\leq3\).

## Quantified target and certificate requirement

Determine the unique integer \(c(S)\in\{1,2,3\}\).  An answer must include:

- an explicit decomposition into \(c(S)\) circuits; and
- an exact, independently replayable exhaustive certificate showing that no
  decomposition into any \(m<c(S)\) circuits exists.

The paper's informal statement that the displayed triangulation has no Euler
2-circuit is not accepted as the required exclusion of \(m=1\).  In
particular, the immediate unresolved test is whether a two-circuit
decomposition exists.  If it does, one must still certify nonexistence for
\(m=1\); if it does not, one must certify nonexistence for both \(m=1\) and
\(m=2\).

Optionally, without weakening or delaying that main target, count minimum
decompositions after identifying: cyclic rotations of each word; reversal of
each word when it is again a valid circuit; permutations of the circuits in
the collection; and the diagonal action of

\[
\operatorname{Aut}(S)=\{\pi\in\operatorname{Sym}(V):
\{\pi(T):T\in F(S)\}=F(S)\}.
\]

The count must come from a complete exact enumeration with a replayable orbit
calculation.  Because facets are unordered, reversing a valid circuit here
does preserve its facet set, but a verifier should check this rather than
assume it.

## Scope and source status

This is a finite exact combinatorial question about the fixed labeled complex
above, not a claim about all triangulated tori.  The nearest prior result is
Figure 1 of arXiv:2609.02701v1, which supplies the three-circuit decomposition
and leaves nonexistence of a single circuit to the reader; it does not settle
the two-circuit case in the inspected pages.  The proposed delta is the exact
minimum with a machine-replayable completeness certificate.  A bounded route
is exhaustive enumeration of compatible ordered facet transitions (or,
equivalently, valid cycle systems in the dual graph), followed by independent
certificate checking.

There is a bibliographic mismatch in the immutable source: the hash-matched
local PDF's title page gives Jens Harlander and Maizie Quatrone as authors and
the title *Circuit Decompositions for Triangulations of Surfaces*, whereas
`source.md` names Robert W. Bell and uses the singular “Decomposition.”  The
Figure 1 words and mathematical definition do match the frozen problem, so
this is recorded as metadata to correct, not as a change to the statement.

Primary source inspected 2026-09-07: arXiv:2609.02701v1, Definition 1,
Figure 1, and Theorem 1, PDF pp. 1–2; the inspected local PDF has SHA-256
`903f9946c9919a6ced917bcd768f7caeaac992d8e63907b79d1c606539eafbee`.
