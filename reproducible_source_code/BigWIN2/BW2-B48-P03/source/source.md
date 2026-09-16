# Source statement — win-00048-p03

## Original lead and exact frozen question

For a finite simple graph \(G\), let

\[
\psi(G)=|\mathcal{AO}(G)|
\]

be the number of acyclic orientations of \(G\). Let \(P_n\) be the path on
\(n\) vertices and let \(\square\) denote the Cartesian graph product.

Prove or disprove the following fixed-width infinite subfamily of the source
conjecture:

\[
\boxed{\quad \psi\!\left(P_3\square P_{2k+1}\right)\equiv 2\pmod 4
       \quad\text{for every integer }k\geq 1.\quad}
\]

The quantifier is over every integer \(k\geq1\), not merely the three tested
values. The target is the congruence for the number of acyclic orientations;
non-Hamiltonicity of the associated acyclic-orientation graph is a consequence,
not a substitute for the congruence.

## Primary source and exact locator

Leonie Mühlherr and Germain Poullot, *Hamiltonicity of graphs of acyclic
orientations and acyclic polynomials*, arXiv:2609.02249v1, 2 September 2026.

- Lemma 3.1 states that \(\psi(G)\) is even for every graph.
- Lemma 3.2 (PDF around p.10) states that if \(G\) has an even number of edges
  and \(4\nmid\psi(G)\), then \(\mathcal{AO}(G)\) is non-Hamiltonian.
- Example 3.13(8) (PDF around p.15) reports exact computer experiments
  \(\psi(P_3\square P_m)\equiv2\pmod4\) for \(m=3,5,7\), but explicitly labels
  these as experiments.
- Conjecture 1(1) (PDF around pp.15--16) conjectures
  \(\psi(P_n\square P_m)\equiv2\pmod4\) for all odd \(m,n\geq3\).
- The deletion--contraction identity immediately following Conjecture 1 gives
  \(\psi(G)=\psi(G/e)+\psi(G\setminus e)\), providing an exact independent
  counting route.

Official primary endpoints:

- abstract: `https://arxiv.org/abs/2609.02249`
- HTML: `https://arxiv.org/html/2609.02249`
- PDF: `https://arxiv.org/pdf/2609.02249`

## Nearest result and proposed novelty delta

The nearest primary evidence is only the exact computation at widths
\(3\times3\), \(3\times5\), and \(3\times7\) in Example 3.13. The paper's
uniform statement covers every odd-by-odd grid and is explicitly conjectural.

The proposed contribution is strictly narrower: prove the complete
one-parameter family with first factor fixed at \(P_3\). This would turn three
finite observations into an all-\(k\) theorem, without claiming the general
odd-by-odd conjecture.

## Cheapest decisive test and proof route

First compute the smallest unreported case \(P_3\square P_9\) exactly by two
independent methods: deletion--contraction and evaluation of the chromatic
polynomial at \(-1\) (with the standard sign/absolute-value convention for the
number of acyclic orientations). A failure modulo \(4\) immediately disproves
the target.

For a proof, exploit the fixed width to construct a finite transfer matrix over
boundary set partitions/color-equality states. Evaluate the resulting recurrence
at \(-1\) and reduce the matrix modulo \(4\). It is enough to certify that the
initial state and every odd-length iterate remain in a finite invariant class
whose output coordinate is \(2\pmod4\). A guessed scalar recurrence is only a
discovery aid until derived from the complete transfer state space.

## Fast falsification

Any integer \(k\geq1\) with an exact deletion--contraction or chromatic-polynomial
certificate satisfying

\[
\psi(P_3\square P_{2k+1})\equiv0\pmod4
\]

is a decisive counterexample. Since Lemma 3.1 guarantees evenness, residues
\(1\) and \(3\) indicate a counting or convention error rather than a valid
graph value.

## Reproducible certificate requirement

A proof certificate should contain the full finite boundary-state list, the
integer transfer matrix, initial and terminal vectors, a derivation tying each
transition to a grid-column extension, and a machine-checkable modulo-4
invariant/recurrence valid for all \(k\). It must be cross-checked against exact
counts for \(m=3,5,7,9\).

A disproof certificate should contain the least located \(k\), the graph edge
list, an exact chromatic polynomial or complete deletion--contraction DAG, and
an independent evaluator reproducing \(|\chi_G(-1)|\) and its residue modulo 4.
No floating-point count or unverified solver output is evidence.

## PDF integrity and fallback provenance

The official arXiv v1 PDF bytes fetched from `https://arxiv.org/pdf/2609.02249`
on 2026-09-06 have SHA-256

`fc43647a3fd3beb1173645f93504570e546cb99edb531b62bee6319b0e6abaaf`.

This intake directory does not contain a local PDF copy. If a later worker must
fall back from HTML, it should retrieve the official versioned record
`arXiv:2609.02249v1`, verify the above hash before relying on page locators, and
record any newer arXiv version separately rather than silently replacing v1.

