# Fresh mathematical referee report

## Binding and verdict

- Referee job: `win-00058-p03-referee-23281c2efbdb`
- Frozen snapshot: `7c170127d22ef17b22a9c72967130546b0f67ff753db6c820e39f492671f48c4`
- Candidate scope: the exact `resolution-paper` statement in `claim.json`, with frozen original status `disproved`
- Verdict: **accept**

I checked every digest in `audit/snapshot.json` before reviewing the argument.  I
read the cited definitions and statements in the frozen arXiv PDF itself, and I
did not use an earlier verdict or owner confidence.  The candidate resolves all
three parts of `source.md` without silently retaining the false Petersen base
value.  The instruction to preserve that value is mathematically incompatible
with the simultaneously frozen open-neighborhood definition; the candidate
correctly proves and exposes this incompatibility rather than treating it as an
assumption about the actual graph.

## 1. Diameter-two pendant case and line audit

Let (a) be pendant and let (u) be its unique neighbor.  If
\(\operatorname{diam}(G)=2\), then for every
\(x\notin\{a,u\}\), a path from (a) to (x) starts with (au) and
has length at most two.  Hence (ux\in E(G)).  Also (ua\in E(G)), so
(u) is universal and \(\gamma(G)=1\).  Thus there is no graph satisfying
all three hypotheses “pendant vertex, diameter two, and \(\gamma=2\).”  The
printed Theorem 4.2 is only a vacuous implication.

The PDF check of pp. 9--10 gives the following exact audit.

1. The initial minimality assertion in Lemma 4.1 is valid under its hypotheses.
   If (d) in a minimum dominating set (D) has no neighbor outside (D),
   connectedness and \(\gamma(G)\ge 2\) give (d) a neighbor in
   (D\setminus\{d\}), while deleting (d) leaves all vertices outside (D)
   dominated.  Applied to a pendant (v\in D), this correctly puts its support
   (x) outside (D).
2. The next claimed deletion is invalid.  From (x\sim v_i) one obtains the
   length-two path (v-x-v_i), not the adjacency (v\sim v_i) required for
   (v_i) to dominate (v).  Thus (D\setminus\{v\}) need not dominate (v).
3. The subsequent length-three construction is downstream of that invalid
   inference and is unnecessary.  The universal-support observation already
   contradicts \(\gamma(G)\ge2\) in the diameter-two setting.
4. In Theorem 4.2, Lemma 4.1 is unnecessary: any dominating set omitting (a)
   must contain (u) simply to dominate (a).  The later adjacency split and
   length-three argument are also unnecessary because (u) is already
   universal.

These labels agree with the actual printed proof, including its phrase that
(v) is dominated by (v_i) “through (x).”

## 2. Diameter-three boundary and least-order classification

The neighboring class is nonempty: (P_4) has pendant vertices, diameter
three, domination number two, and a total dominating pair consisting of its
two internal vertices.

I independently scanned all (2^{\binom n2}) labeled simple graphs for every
(1\le n\le6) using integer adjacency bitsets.  This verifier does not import
NetworkX or either submitted program.  Connectivity, diameter, domination,
and total domination were recomputed directly; every vertex subset was tested.
The numbers of labeled graphs meeting the three hypotheses for orders
(1,\ldots,6) were respectively

\[
0,0,0,12,300,9750,
\]

and the numbers among them with \(\gamma_t>2\) were

\[
0,0,0,0,0,720.
\]

Canonicalizing every one of the 720 failures over all (6!) labelings yields
exactly two graph6 strings, `E@V_` and `EBYg`, each accounting for 360 labeled
graphs.  This proves both least order six and completeness up to isomorphism,
independently of the submitted Graph Atlas route.

For `E@V_`, the adjacency lists are

\[
0:5;\quad 1:4,5;\quad 2:3,5;\quad 3:2,4;\quad
4:1,3;\quad 5:0,1,2.
\]

Vertex 0 is pendant with support 5, the diameter is three, and
\(\{3,5\}\) dominates.  There is no universal vertex: only 5 could dominate
the pendant from a singleton, and 5 misses 3 and 4.  Hence \(\gamma=2\).
The set \(\{1,2,5\}\) totally dominates.  Any total dominating pair must be
\(\{5,x\}\) with (x\in\{0,1,2\}); these choices fail respectively on
vertices outside the pair (in particular, (x=1) misses 3 and (x=2)
misses 4).  Thus \(\gamma_t=3\).

For `EBYg`, the adjacency lists are

\[
0:5;\quad 1:3,4;\quad 2:3,4,5;\quad 3:1,2;\quad
4:1,2,5;\quad 5:0,2,4.
\]

Again 0 is pendant with support 5 and the diameter is three.  The set
\(\{1,5\}\) dominates, while 5 is not universal because it misses 1 and 3,
so \(\gamma=2\).  The set \(\{1,4,5\}\) totally dominates.  A total
dominating pair must be \(\{5,x\}\) with (x\in\{0,2,4\}); (x=0) plainly
fails, (x=2) misses 1, and (x=4) misses 3.  Therefore \(\gamma_t=3\).

The independent output, including all subset counts and witnesses, is
`audit/referee_verification.json`; the reproducible verifier is
`audit/referee_verify.py`.

## 3. Blow-up invariance and Theorem 4.6

Definition 1.1 on PDF p. 3 replaces each base vertex (v) by a nonempty
independent part (V_v), with edges between parts exactly when the base
vertices are adjacent.  Lemma 3.3 on p. 6 asserts the relevant invariance.
It has a direct two-sided proof.

If (D) totally dominates a base graph (F), choose one representative in
(V_v) for every (v\in D).  Every vertex in (V_x) is adjacent to a chosen
representative over a neighbor of (x) in (D), so
\(\gamma_t(F^{\mathbf m})\le\gamma_t(F)\).

Conversely, let (S) totally dominate the blow-up and put

\[
I=\{v:S\cap V_v\ne\varnothing\}.
\]

For each base vertex (x), choose any vertex of the nonempty part (V_x).
Its neighbor in (S) lies in (V_y) for some (y\in I\cap N_F(x)), because
parts are independent and cross-part adjacency copies (F).  Hence (I)
totally dominates (F), and

\[
\gamma_t(F)\le |I|\le |S|.
\]

Taking (S) minimum proves equality.  The argument applies to each allowed
single-vertex duplication and does not require the duplicated vertex to have
degree two.

I also recomputed all three base values.  The cycle (C_5) has
\(\gamma_t=3\).  Interpreting Figure 3's (G_0) as the central vertex with
three subdivided spokes to an outer triangle, exhaustive subset testing gives
\(\gamma_t(G_0)=3\); directly, a central vertex, one incident subdivider, and
its outer endpoint form a three-set, while an adjacent pair of any of the
three possible edge types misses a vertex.  For the standard Petersen graph,

\[
\{0,1,2,6\}
\]

is a total dominating set in the labeling serialized in the frozen evidence.
There is no total dominating set of size at most three.  Indeed, total
domination is monotone under taking supersets, so such a set could be enlarged
to three vertices.  A three-vertex total dominating set in a triangle-free
graph induces (P_3).  In the cubic Petersen graph the open neighborhoods of
the two path endpoints share the middle vertex, so the union of the three open
neighborhoods has size at most (3+3+3-1=8<10), and cannot cover the graph.
Thus

\[
\gamma_t(\text{Petersen})=4,
\]

not 6.  Independent enumeration finds no total dominating sets of sizes
0--3 and exactly ten of size four, reproducing the frozen certificate.

Because the generating family permits zero duplications, the Petersen graph
itself already disproves the printed `{3,6}` assertion.  Applying invariance
at every duplication gives the actual branchwise repair

\[
\gamma_t(G)=3\quad\text{on the (C_5) and (G_0) branches},\qquad
\gamma_t(G)=4\quad\text{on the Petersen branch}.
\]

Thus the definition-preserving range is \(\{3,4\}\).  If 6 were imposed only
as a counterfactual premise, invariance would propagate it and formally yield
\(\{3,6\}\), but that conditional statement would be false as a statement
about total domination of the actual Petersen graph.  The candidate therefore
handles, rather than evades, the inconsistency in the frozen instructions.
The final sentence of the printed proof on p. 11 additionally switches from
\(\Gamma\) to (G) and assigns 3 to all descendants, thereby erasing even
its own stated Petersen branch.

## Source comparison, scope, and remaining gaps

The frozen PDF confirms the open-neighborhood definition (p. 1), the
independent-part multiplication definition (p. 3), Lemma 3.3 (p. 6), the
invalid Lemma 4.1 line and vacuous Theorem 4.2 (pp. 9--10), and the false
Petersen value plus variable/branch error in Theorem 4.6 (p. 11).  The
candidate makes no priority claim for the elementary Petersen correction or
the finite atlas.  Its bounded literature statement is correspondingly not
used as a proof premise.

There is no unresolved mathematical gap in the frozen candidate scope.  The
vacuity proof is complete, the order-six classification is exhaustively and
independently certified, and blow-up invariance plus the corrected base values
fully repairs the generated-family conclusion.  The coherent contribution is
strictly more than a variable-name correction: it includes a false base value,
an empty theorem class, and an exact least-order two-class counterexample atlas.

