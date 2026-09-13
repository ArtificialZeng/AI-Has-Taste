# Formal statement

For every integer \(n\ge 6\), let \(V_n=\mathbb Z/n\mathbb Z\), and let
\(C_n^{(3)}\) be the simple graph on \(V_n\) whose edge set is
\[
 \bigl\{\{i,i+1\},\{i,i+3\}:i\in V_n\bigr\}
 \quad\text{together with}\quad
 \bigl\{\{i,i+n/2\}:i\in V_n\bigr\}
\]
when \(n\) is even (the last set is absent when \(n\) is odd).  Repeated
unordered edges, if any, are identified.

Let
\[
a(n)=\#\{c:V_n\to\{0,1,2\}:c(i)\ne c(j)\text{ for every edge }\{i,j\}\}.
\]

## Target theorem

Prove the fully quantified equivalence
\[
 \forall n\in\mathbb Z,\quad n\ge6\Longrightarrow
 \bigl(a(n)=0\iff n\in\{7,8,12,16\}\bigr).
\]

Equivalently, prove nonexistence of a proper three-colouring for the four
listed graphs and exhibit or prove existence of at least one such colouring
for every other integer \(n\ge6\).

## Normalizations

Colours are labelled; hence colour permutations count as different
colourings.  The zero-set assertion itself depends only on existence and is
unchanged by quotienting by colour permutations during a proof.

## Edge cases

The endpoint \(n=6\) is included.  All vertex arithmetic is modulo \(n\).
The graph is simple, so coincident chord, cycle, or diameter edges are counted
once.  No assertion is made for \(n<6\).

This definition agrees with OEIS A383733 (comments and executable graph
construction, accessed 2026-08-29) and with Definition 1.1 of
arXiv:2509.05845, apart from the source paper's generic restriction
\(k<n/2\).  The OEIS entry explicitly includes the endpoint \(n=6,k=3\),
where the offset-three and diameter edge sets coincide.
