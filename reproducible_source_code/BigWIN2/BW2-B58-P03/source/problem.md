# Precise triage reading

## Frozen scope

This project interprets the three requests in `source.md` literally and does not
alter the paper's definitions.  The ambient object is a finite, simple,
connected, undirected graph \(G=(V,E)\).  The phrase "has a pendant vertex" is
existential: there is at least one \(a\in V\) with \(\deg(a)=1\).  Its unique
neighbor is its *support* \(u\).  Distances are shortest-path lengths and
\(\operatorname{diam}(G)=\max_{x,y\in V}d(x,y)\), so the displayed diameter
values below mean equality, not an upper bound.

A set \(D\subseteq V\) dominates \(G\) when
\[
  (\forall x\in V\setminus D)\quad N(x)\cap D\ne\varnothing,
\]
and \(\gamma(G)\) is the minimum size of such a set.  It totally dominates
\(G\) when
\[
  (\forall x\in V)\quad N(x)\cap D\ne\varnothing,
\]
and \(\gamma_t(G)\) is the minimum size of such a set.  Thus vertices of a
total dominating set must themselves have a neighbor in the set.

## A. Diameter-two vacuity and proof audit

Decide the existence statement
\[
 \exists G\;\bigl[G\text{ has a pendant vertex},\ 
 \operatorname{diam}(G)=2,\ \gamma(G)=2\bigr].
\]
The decisive observation is already exact: if \(a\) is pendant with support
\(u\) and \(\operatorname{diam}(G)=2\), then every
\(x\in V\setminus\{a,u\}\) must be adjacent to \(u\), because every path from
\(a\) begins with \(au\).  Hence \(u\) is universal and \(\gamma(G)=1\).
Therefore the displayed class is empty and Theorem 4.2's implication is
formally true only vacuously.

The requested audit is line-specific.  It must distinguish false reasoning
from merely unnecessary reasoning.  In the printed proof of Lemma 4.1:

- the claim that every member of a minimum dominating set dominates a vertex
  outside the set is valid under the lemma's hypotheses.  Indeed, if
  \(d\in D\) has no neighbor outside \(D\), connectedness supplies a neighbor
  of \(d\) in \(D\), and then \(D\setminus\{d\}\) still dominates every
  vertex.  Applied to the pendant \(v\), this correctly gives \(x\notin D\);
- the claim that deleting \(v\) still dominates \(v\) when its support \(x\)
  is adjacent to some \(v_i\in D\) is invalid: the length-two walk
  \(v-x-v_i\) does not make \(v\) adjacent to \(v_i\);
- all subsequent construction of a length-three path is unnecessary once the
  support-universal observation is made.

In Theorem 4.2, Lemma 4.1 is unnecessary.  Any dominating set omitting the
pendant \(a\) must contain its unique neighbor \(u\), directly by definition.
The later length-three-path argument is also unnecessary because diameter two
already makes \(u\) universal and contradicts \(\gamma(G)=2\).  The final audit
should quote/check the exact PDF positions before freezing these labels.

## B. First nonempty neighboring class

Let \(\mathcal C_3\) be the class of all finite simple connected graphs \(G\)
such that
\[
 G\text{ has a pendant vertex},\qquad
 \operatorname{diam}(G)=3,\qquad \gamma(G)=2.
\]
This class is nonempty: \(P_4\in\mathcal C_3\), and its two internal vertices
form a total dominating set.  Decide the universal assertion
\[
  (\forall G\in\mathcal C_3)\quad \gamma_t(G)=2. \tag{B}
\]
If (B) is false, a counterexample means a member of \(\mathcal C_3\) with
\(\gamma_t(G)>2\) (equivalently \(\gamma_t(G)\ne2\)).  Determine
\[
 n_0=\min\{|V(G)|:G\in\mathcal C_3,\ \gamma_t(G)>2\},
\]
give an exact graph at order \(n_0\), and list exactly one representative of
every isomorphism class of such graphs on \(n_0\) vertices.  Graphs with more
than one pendant vertex are included once.  An acceptable exhaustive
certificate records connected-unlabeled input counts, exact filters, canonical
graph6 strings, adjacency lists, and minimum dominating/total-dominating
witnesses (plus exhaustive nonexistence checks for smaller subset sizes).

## C. Repair of Theorem 4.6 and the inconsistent Petersen stipulation

For a graph \(F\) with vertices \(v_1,\ldots,v_n\) and positive integers
\(m_1,\ldots,m_n\), vertex multiplication replaces \(v_i\) by an independent
part \(V_i\) of size \(m_i\), joining two vertices in distinct parts exactly
when the corresponding base vertices are adjacent.  Duplicating a vertex is
the special case that replaces it by two false twins; *degree-2 vertex
duplication* applies this operation to a vertex having degree two at that
stage.

The family \(\mathcal H\) is the generated (smallest closed) family obtained
from one of \(C_5\), the depicted graph \(G_0\), or the Petersen graph by a
finite sequence, possibly empty, of degree-2 vertex duplications.  Under the
unchanged open-neighborhood definition the actual base values are
\[
 \gamma_t(C_5)=3,\qquad \gamma_t(G_0)=3,\qquad
 \gamma_t(\text{Petersen})=4.
\]
The first two agree with the source; the third follows from exact subset
enumeration (upper bound) and cubicity plus triangle-freeness (lower bound).
Thus the simultaneous instructions in `source.md` to keep the paper's
definition and preserve the value 6 are inconsistent.

Verify Lemma 3.3 for the printed independent-part blow-up definition and apply
it at every duplication.  The actual repaired statement is
\[
 \gamma_t(G)=
 \begin{cases}
 3,&G\text{ descends from }C_5\text{ or }G_0,\\
 4,&G\text{ descends from the Petersen graph},
 \end{cases}
\]
so in particular \(\gamma_t(G)\in\{3,4\}\).  If the generated branches could
overlap, invariance itself resolves that issue.  Counterfactually accepting 6
as a stipulated premise would make the same argument yield the formal set
\(\{3,6\}\), but that is not a true conclusion about total domination under
the paper's definitions.  Theorem 4.6 therefore has both a false Petersen base
value and a final proof line that erases the Petersen branch while switching
between \(\Gamma\) and \(G\).

## Triage status and contribution boundary

The nearest source is S. Bera, arXiv:2609.03512v1, Definition 1.1, Lemma 3.3,
Lemma 4.1, and Theorems 4.2 and 4.6 (PDF pp. 3, 6, 9--11), inspected on
2026-09-07 at <https://arxiv.org/abs/2609.03512v1>.  The local PDF has SHA-256
`785df29b61d399150418f5796aa43f0d8029e0755097b2830266f64ee1309824`.
A targeted web search found no primary source stating the exact diameter-three
assertion (B), so its literature status remains uncertain; this is not a
priority claim.  The registry lists `win-00058-p07` as the same family-\(\mathcal
H\) branch already merged here, while `win-00055-p03` concerns a distinct
six-vertex rank-six atlas.

Triage target: nearest printed results are Bera's Theorems 4.2 and 4.6;
proposed delta is the exact vacuity diagnosis plus a nonvacuous diameter-three
theorem or least-order counterexample atlas, with the three-branch invariant
repair; verification is by a short distance argument, exhaustive exact
unlabeled enumeration, and a direct two-sided proof of blow-up invariance.
