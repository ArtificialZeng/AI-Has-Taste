# Research certificate for `win-00058-p03`

Job: `win-00058-p03-research-fa19420fa5ab`  
Frozen-source SHA-256: `93b1a6b9b99e1477d645853ce2e89be5b99db379d5c4c7e7535c7e1d912119b2`

All graphs below are finite, simple, connected, and undirected, and domination
and total domination have exactly the meanings fixed in `problem.md`.

## 1. The diameter-two pendant hypotheses are inconsistent

Let (a) be pendant with unique neighbor (u), and suppose
\(\operatorname{diam}(G)=2\). For every (x\notin\{a,u\}), every path from
(a) starts with (au). Since (d(a,x)\leq2), necessarily (ux\in E(G)).
Also (ua\in E(G)), so (u) is universal and \(\gamma(G)=1\). Consequently,
there is no graph with a pendant vertex, diameter two, and domination number
two. The implication printed as Theorem 4.2 is true only vacuously.

The following audit refers to PDF pp. 9--10 (the section heading and Lemma 4.1
start on p. 9; the proof continues and Theorem 4.2 appears on p. 10).

- Lemma 4.1's assertion that every member of a minimum dominating set must
  dominate a vertex outside that set is valid under its connectedness and
  \(\gamma(G)\geq2\) hypotheses. If \(d\in D\) has no neighbor outside
  \(D\), connectedness gives it a neighbor in \(D\); deleting \(d\) then
  leaves every vertex dominated. Applied to the pendant \(v\), this correctly
  implies that its support \(x\) lies outside \(D\).
- The next deletion step is invalid. If (x\sim v_i\), the length-two walk
  (v-x-v_i) does not mean that (v_i) dominates (v); domination requires
  adjacency, while the pendant (v) is adjacent only to (x\notin D).
- The later construction of (v-x-y-v_i) is therefore downstream of an
  invalid step. Even considered conditionally, the whole length-three route
  is unnecessary because the one-line universal-support argument already
  contradicts the hypotheses of Lemma 4.1.
- In Theorem 4.2, invoking Lemma 4.1 is unnecessary. Directly, any dominating
  set omitting (a) must contain (u). The subsequent split according as
  (u\sim v) is also unnecessary: diameter two already makes (u) universal
  and contradicts \(\gamma(G)=2\). Thus no nonvacuous conclusion about total
  domination is obtained from the printed hypotheses.

## 2. The diameter-three replacement is false, first at order six

The exact census in `diameter3_census.py` and `diameter3_census.json` gives:

| order | connected unlabeled | pendant | also diameter 3 | also \(\gamma=2\) | \(\gamma_t=2\) | \(\gamma_t=3\) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 1 | 1 | 0 | 0 | 0 | 0 |
| 3 | 2 | 1 | 0 | 0 | 0 | 0 |
| 4 | 6 | 3 | 1 | 1 | 1 | 0 |
| 5 | 21 | 10 | 5 | 5 | 5 | 0 |
| 6 | 112 | 51 | 31 | 30 | 28 | 2 |

Thus the least failing order is six, and there are exactly two isomorphism
classes there. Their canonical graph6 strings (defined as the lexicographically
least graph6 encoding among all (6!) labelings) are

```text
E@V_
EBYg
```

Equivalently, take a 5-cycle, attach one pendant vertex to a cycle vertex
(u), and either add no other edge or add the edge joining the two cycle
neighbors of (u). These are precisely the two classes.

For `E@V_`, the edges are

\[
05,14,15,23,25,34.
\]

The pendant is (0), the support is (5), \(\{3,5\}\) dominates, and
\(\{1,2,5\}\) totally dominates. A total dominating pair must contain 5
because of vertex 0, and its other member must neighbor 5. The choices
(0,1,2) respectively fail to dominate vertices outside the pair; in
particular, choice 1 misses 3 and choice 2 misses 4. Hence
\(\gamma=2\) and \(\gamma_t=3\): for the former lower bound, any universal
vertex would have to be the pendant's support 5, but 5 misses 3 and 4.

For `EBYg`, the edges are

\[
05,13,14,23,24,25,45.
\]

Again 0 is pendant with support 5. The set \(\{1,5\}\) dominates and
\(\{1,4,5\}\) totally dominates. A total dominating pair must be
\(\{5,x\}\) with (x\in\{0,2,4\}); choice 0 plainly fails, choice 2 misses
1, and choice 4 misses 3. Hence \(\gamma=2\) and \(\gamma_t=3\): again the
only possible universal vertex is support 5, which misses 1 and 3.

The JSON records every subset count by cardinality, all minimum witnesses,
adjacency lists, and hypothesis checks. Completeness is checked by two routes:
one representative of every unlabeled graph in NetworkX's Graph Atlas, and an
independent scan of all (2^{\binom n2}) labeled graphs for every (n\leq6).
The latter checks 33,867 labeled graphs in total, including all 32,768 graphs
at order six, then reduces all 720 labeled counterexamples to the same two
canonical strings. There are no labeled counterexamples at smaller order.

## 3. Repair of Theorem 4.6 under the unchanged definition

Let (F) be a graph and (F^{\mathbf m}) its independent-part blow-up from
Definition 1.1, with nonempty part (V_v) over each (v\in V(F)).

If (D) totally dominates (F), choose one representative in (V_v) for
each (v\in D). Every vertex in a part (V_x) is adjacent to a chosen
representative over some neighbor of (x) in (D). The representatives
therefore totally dominate the blow-up, so
\(\gamma_t(F^{\mathbf m})\leq\gamma_t(F)\).

Conversely, if (S) totally dominates the blow-up, let
\(I=\{v:S\cap V_v\ne\varnothing\}\). For every (x\in V(F)), take any
vertex in (V_x). Its neighbor in (S) lies in (V_y) for some
(y\in I\cap N_F(x)). Hence (I) totally dominates (F), and

\[
\gamma_t(F)\leq |I|\leq |S|.
\]

Taking (S) minimum proves Lemma 3.3 exactly:
\(\gamma_t(F^{\mathbf m})=\gamma_t(F)\). The proof does not need the duplicated
vertex to have degree two.

It remains to audit the base values rather than merely propagate them. For the
standard Petersen graph with outer cycle \(0,1,2,3,4,0\), spokes
\(05,16,27,38,49\), and inner edges \(57,79,96,68,85\), the set
\(\{0,1,2,6\}\) totally dominates all ten vertices. No set of at most three
vertices can do so. A three-vertex total dominating set has no isolated
vertex in its induced subgraph and hence, because the Petersen graph is
triangle-free, induces a three-vertex path. The graph is cubic, and the open
neighborhoods of the two path endpoints share the middle vertex, so the union
of the three open neighborhoods has size at most
\(3+3+3-1=8<10\). Therefore
\(\gamma_t(\operatorname{Petersen})=4\), not 6. The exact enumeration in
`petersen_total_domination.json` independently lists all ten minimum
four-sets and confirms that there are no smaller witnesses.

Each allowed degree-2 duplication is a single-vertex blow-up, so induction on
the number of duplications and the actual base values gives

\[
\gamma_t(G)=
\begin{cases}
3,&G\text{ descends from }C_5\text{ or }G_0,\\
4,&G\text{ descends from the Petersen graph}.
\end{cases}
\]

Thus the correct conclusion is \(\gamma_t(G)\in\{3,4\}\), and the printed
\(\{3,6\}\) conclusion is false. A graph cannot lie both in the Petersen
branch and a 3-valued branch, since invariance would force its
isomorphism-invariant total domination number to be both 4 and 3. On PDF p.
11 the final proof sentence is independently invalid/incomplete: after
introducing \(\Gamma\in\mathcal H\), it writes \(\gamma_t(G)=3\), both
switching the graph variable and erasing the Petersen branch.

The request in `source.md` to preserve the Petersen value 6 cannot be met
simultaneously with its instruction not to change the paper's definitions.
If 6 is accepted only as a counterfactual premise, Lemma 3.3 does formally
propagate it and yield \(\{3,6\}\); that conditional statement is not a repair
of the actual graph theorem. The branchwise \(\{3,4\}\) induction above is
the definition-preserving repair.

## Scope and limitations

The disproof/classification in Section 2 is finite and exact. It makes no
priority claim. The literature status recorded in `problem.md` remains
status-uncertain. Section 3 corrects an elementary false base value rather than
claiming priority for the Petersen computation. The source paper's Lemma 4.5
supplies the unchanged value \(\gamma_t(G_0)=3\); the new exact audit concerns
the Petersen base.
