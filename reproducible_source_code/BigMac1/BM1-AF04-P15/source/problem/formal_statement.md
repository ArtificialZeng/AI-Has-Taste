# Formal statement

## Canonical decision problem

Let \(\mathbb N=\{0,1,2,\ldots\}\).  Determine the truth value of

\[
\exists A\subset\mathbb Z\;\exists a:\mathbb N\to A\quad
\bigl(1\le |A|<\infty\bigr)\quad\text{and}\quad
\forall i\in\mathbb N\;\forall \ell\in\mathbb Z_{\ge1},
\quad
\sum_{r=0}^{\ell-1}a(i+r)\ne
\sum_{r=0}^{\ell-1}a(i+\ell+r).
\]

The two blocks are consecutive, have the same **positive** length \(\ell\),
and equality is equality in \(\mathbb Z\).  A word satisfying all the displayed
inequalities is called *additive-square-free* (ASF).

For a finite word \(w=w_0\cdots w_{n-1}\), the same definition is used only
when \(i+2\ell\le n\).  Write

\[
g(A)=\sup\{|w|:w\in A^*\text{ is ASF}\}\in\mathbb N\cup\{\infty\}.
\]

For a fixed nonempty finite alphabet \(A\), finite branching and K\"onig's
infinity lemma give

\[
g(A)=\infty
\quad\Longleftrightarrow\quad
\text{there is an infinite ASF word over }A.
\]

Thus the decision problem is equivalently \(\exists A\subset\mathbb Z\),
finite and nonempty, with \(g(A)=\infty\).  The alphabet is not required to be
used surjectively; unused letters can simply be deleted.

## Prefix-sum formulation

Set \(S_0=0\) and \(S_n=\sum_{j=0}^{n-1}a(j)\) for \(n\ge1\).  Then the
factor starting at \(i\) with half-length \(\ell\) is an additive square if
and only if

\[
S_i+S_{i+2\ell}=2S_{i+\ell}.
\]

Consequently the problem asks for an infinite integer sequence \((S_n)\)
with \(S_0=0\), increments in one fixed finite subset of \(\mathbb Z\), and no
three-term arithmetic progression in values at equally spaced indices
\(i,i+\ell,i+2\ell\).  Conversely, every such bounded-increment integer walk
gives an ASF word by taking first differences.

## Exact normalizations and symmetries

If \(\alpha,\beta\in\mathbb Z\) with \(\alpha\ne0\), applying
\(x\mapsto\alpha x+\beta\) to every letter preserves and reflects the ASF
property, because the two compared blocks have the same length.  Therefore a
finite integer alphabet with at least two elements may be translated and
divided by the gcd of all translated letters to the primitive form

\[
A=\{0=x_0<x_1<\cdots<x_{k-1}\},\qquad
\gcd(x_1,\ldots,x_{k-1})=1.
\]

The reflection \(x\mapsto x_{k-1}-x\) is an additional involution, and word
reversal preserves finite ASF words.  These are the only identifications used
in the finite census; arbitrary relabeling is **not** a symmetry because sums
depend on the actual integer values.

## Edge and degenerate cases

- \(A=\varnothing\) admits no word and is excluded.  If \(|A|=1\), every word
  of length two already has an additive square of half-length one.
- Negative letters and zero cause no special case; translation reduces them
  to a nonnegative alphabet without changing any comparison.
- The empty finite word and one-letter words are ASF.  The empty blocks
  (\(\ell=0\)) are deliberately excluded.
- Every abelian square is an additive square under every integer labeling.
  Hence an infinite ASF word would in particular be abelian-square-free and
  must use at least four distinct letters.
- No compactness inference may vary \(A\) with the word length.  K\"onig's
  lemma applies only after one fixed finite alphabet has been chosen.

## Target and admissible partial endpoints

The full target is the displayed existential statement or its negation.  A
finite result must name the normalized alphabets and give exact values or exact
upper bounds for their \(g(A)\).  A substitution result must state the precise
morphism, starting letter, integer weight map, and a proof covering factors of
all lengths; checking an iterated prefix is not an infinite-word proof.
