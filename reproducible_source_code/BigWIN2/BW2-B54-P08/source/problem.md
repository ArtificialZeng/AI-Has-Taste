# Precise problem reading

## Frozen claim interpreted

Let \(P=(V,\le_P)\) be a finite nonempty poset and put \(n=|V|\). A linear extension is an order-preserving bijection
\[
f:V\longrightarrow\{1,\ldots,n\};
\]
the probability space is the finite set \(\mathcal E(P)\) of all such maps with the uniform distribution. For \(x\in V\),
\[
h_P(x)=\frac{1}{|\mathcal E(P)|}\sum_{f\in\mathcal E(P)}f(x)\in\mathbb Q.
\]

A chain is a nonempty subset whose elements are pairwise comparable. A **maximal chain** means inclusion-maximal, not necessarily a chain of maximum cardinality. Write it uniquely as \(C=\{y_1<_P\cdots<_P y_m\}\). Since every extension has \(f(y_i)<f(y_{i+1})\), the list
\[
0,h_P(y_1),\ldots,h_P(y_m),n+1
\]
is strictly increasing, and
\[
\operatorname{gap}_P(C)=\max\bigl\{h_P(y_1),h_P(y_2)-h_P(y_1),\ldots,
h_P(y_m)-h_P(y_{m-1}),n+1-h_P(y_m)\bigr\}.
\]
The width \(w(P)\) is the maximum cardinality of an antichain. “Width exactly two” means \(w(P)=2\), excluding both chains and posets of width at least three.

Define
\[
\mathcal A_n=\left\{P: |P|=n,\ w(P)=2,\ 
  \forall C\ (C\text{ an inclusion-maximal chain of }P\Rightarrow
  \operatorname{gap}_P(C)>4)\right\}/\cong.
\]
The requested number and classification are
\[
m_2(4)=\min\{n\ge1:\mathcal A_n\ne\varnothing\},
\qquad\text{and the complete list of classes in }\mathcal A_{m_2(4)}.
\]
The inequality is strict: a chain gap equal to \(4\) fails. Poset isomorphism is the only equivalence relation; order duality is not additionally identified unless the two posets are isomorphic.

## Computational scope required by the source

A complete computational resolution must:

1. enumerate without omission all isomorphism classes of width-exactly-two posets at every order \(n<m_2(4)\), and also the full order-\(m_2(4)\) domain needed to classify every minimizer;
2. canonicalize/deduplicate labeled presentations and emit a canonical order-relation encoding for every qualifying witness;
3. count linear extensions and rank sums as integers, hence compute every \(h_P(x)\) and every comparison with \(4\) in exact rational arithmetic;
4. enumerate all inclusion-maximal chains (not merely longest chains), test the universal chain quantifier, and retain enough counts/certificates for an independent replay; and
5. provide a completeness argument for the poset generator (a direct two-chain generator may use Dilworth's theorem but must canonical-deduplicate overlapping chain decompositions).

The natural canonical encoding is the lexicographically least strict-order adjacency bit string over all labelings of \(V=\{0,\ldots,n-1\}\); another fully specified, replayable canonical form is acceptable.

## Boundary cases

There is no admissible order-one poset because its width is one. At order two the only width-two poset is the antichain: each singleton maximal chain has expected rank \(3/2\) and gap \(3/2\), so it fails. At order three, the width-two isomorphism types are (i) one two-element chain plus an isolated point, (ii) the three-element V, and (iii) its dual. Their largest maximal-chain gaps are respectively \(2,3/2,3/2\), so all fail. Thus the exact elementary lower bound is \(m_2(4)\ge4\).

## Nearest prior result and status

Haqi, *On the Gap of Finite Posets*, arXiv:2608.12678v1 (retrieved 2026-09-07), Definition 1.2 gives the same chain-gap definition. Theorem 5.1 states that for every \(L>0\) a finite width-two poset exists with \(\operatorname{gap}_P(C)\ge L\) for every nonempty chain \(C\). Taking any \(L>4\) proves that the defining set for \(m_2(4)\) is nonempty. That theorem is asymptotic/existential and does not determine the first order or classify minimizers. Searches on 2026-09-07 for the exact notation and equivalent threshold language found no primary source computing this finite threshold; this is a limited literature screen, not a priority claim.

Source status: **new-question / status-uncertain beyond the cited existence theorem**. Proposed delta: determine the first strict threshold \(>4\) and all equality-order isomorphism classes. Verification route: exhaustive canonical generation plus two independently implementable exact linear-extension/rank and maximal-chain checks.

## Source-access note

The local PDF path named in `source.md` is not present inside this project. The v1 arXiv HTML was inspected directly at <https://arxiv.org/html/2608.12678v1>, especially Definition 1.2 (lines 73–77) and Theorem 5.1 with its deduction (lines 301–307 and 397–404).
