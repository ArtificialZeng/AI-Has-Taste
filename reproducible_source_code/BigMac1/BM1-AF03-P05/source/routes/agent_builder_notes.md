# Builder notes: the positive structural route for order nine

## 1. Scope and conventions

These notes concern a simple graph \(G\) on exactly nine vertices and its
complement \(H=\overline G\).  The target endpoint is

\[
 H\text{ non-bipartite},\quad |E(H)|\leq 6
 \quad\Longrightarrow\quad q(G)=2.
\]

For a graph \(X\), \(S(X)\) means the real symmetric matrices \(A\) such
that, for distinct \(i,j\), \(A_{ij}\ne0\) if and only if \(ij\in E(X)\).
Diagonal entries are unrestricted.  All complement, component, and join
statements below use this convention.

This is a proof-builder record, not the final referee audit.  It does not
modify the shared route registry, gap ledger, manuscript, or status files.

## 2. Orthogonal/projection normalization from definitions

**Lemma 2.1 (two eigenvalues versus an involution).**  Let \(X\) be a graph
with at least one edge.  Then \(q(X)=2\) if and only if there is a real
symmetric \(A\in S(X)\) such that \(A^2=I\).

**Proof.**  If a symmetric \(M\in S(X)\) has precisely two distinct
eigenvalues \(\lambda\ne\mu\), then

\[
 A=\frac{2M-(\lambda+\mu)I}{\lambda-\mu}
\]

is symmetric, has the same off-diagonal zero/nonzero pattern as \(M\), and
has eigenvalues \(1,-1\); hence \(A^2=I\).  Conversely a symmetric
involution has spectrum contained in \(\{-1,1\}\).  If only one of these
two eigenvalues occurred, it would be \(I\) or \(-I\), which has no
off-diagonal nonzero entries.  Since \(X\) has an edge, both eigenvalues
occur and \(q(X)=2\).  There is no division by a possibly zero quantity:
\(\lambda-\mu\ne0\) is part of the hypothesis.  The edgeless graph is the
only excluded degeneracy, and has \(q=1\), not the endpoint considered here.

Equivalently, \(A=I-2P\), where \(P=P^T=P^2\) is a nontrivial orthogonal
projection.  This is the form used by the exact frame certificates.

## 3. The balanced connected-join route

The only external input in this section is the published theorem:

> If \(X,Y\) are connected graphs and
> \(\lvert |V(X)|-|V(Y)|\rvert\le2\), then \(q(X\vee Y)=2\).

The certificate binds this statement to Levene--Oblak--Smigoc, Theorem 3.4
(connected (k=1) case), DOI `10.1080/03081087.2023.2232090`.  Its precise
hypotheses still have to remain part of the citation audit; no SSP hypothesis
is inserted here.

**Lemma 3.1 (component routing).**  Let \(H\) be a finite simple graph, and
let its connected components be partitioned into two nonempty collections.
Let \(L,R\) be the unions of their vertex sets.  If
\(\overline{H[L]}\) and \(\overline{H[R]}\) are connected and
\(\lvert |L|-|R|\rvert\le2\), then

\[
q(\overline H)=2.
\]

**Proof from definitions.**  No edge of \(H\) has one endpoint in \(L\)
and one in \(R\).  Hence every such cross pair is an edge of
\(G=\overline H\), while \(G[L]=\overline{H[L]}\) and
\(G[R]=\overline{H[R]}\).  Thus, exactly (not merely as a spanning
subgraph),

\[
G=G[L]\vee G[R].
\]

The two factors are connected by hypothesis and their orders differ by at
most two, so the cited join theorem applies.  The collections are nonempty,
so neither factor has order zero.  A singleton factor is connected under the
standard graph convention; if the cited source excludes order one, that
would have to be checked separately.  In the order-nine routes actually
used here the two orders are at least three, so this endpoint ambiguity is
irrelevant.

**Corollary 3.2.**  If each of \(H[L]\) and \(H[R]\) contains at least two
components of \(H\), then their complements are connected.

Indeed, vertices in different \(H\)-components are adjacent in the
complement.  Two vertices lying in the same component have a length-two path
in the complement through any vertex of another component.  This proof also
covers singleton components and components having one vertex.

## 4. Why only three component-size patterns escape the elementary route

For a graph \(H\) on nine vertices with \(m\) edges and \(c\) connected
components, its cycle-space dimension is

\[
\beta(H)=m-9+c.
\]

If \(H\) is non-bipartite, it contains an odd cycle, so
\(\beta(H)\ge1\).  Since \(m\le6\),

\[
c=9-m+\beta(H)\ge4.
\]

**Lemma 4.1 (integer partition check).**  Let positive integers
\(s_1\ge\cdots\ge s_c\) sum to \(9\), with \(c\ge4\).  Unless their
multiset is one of

\[
(6,1,1,1),\qquad (5,2,1,1),\qquad (5,1,1,1,1),
\]

the parts can be split into two collections, each containing at least two
parts, whose sums are \(4\) and \(5\).

**Proof.**  Necessarily \(s_1\le6\).  If \(s_1=6\), the other at least three
positive parts sum to three, giving \((6,1,1,1)\).  If \(s_1=5\), the other
at least three parts partition four, giving exactly the two displayed
patterns beginning with five.  If \(s_1=4\), the remaining at least three
parts sum to five and contain a part one; all the remaining parts except one
such singleton sum to four, leaving the part four and that singleton on the
other side.  If \(s_1\le3\), then: a part three together with a part one
works; if there is a three but no one, the only possibility is
\((3,2,2,2)\), and \(2+2=4\); if there is no three, use two twos when
available, and otherwise use four ones (or \(2+1+1\)).  In every subcase at
least two parts remain on the other side.

By Corollary 3.2 and Lemma 3.1, every nonexceptional component-size pattern
has \(q(\overline H)=2\).  This is a structural proof of the entire join
route; it does not depend on floating-point search or on the graph6 labels.

## 5. Exact frame-completion lemma

The following lemma gives a human proof family for the hard sparse cores.  It
is not needed to validate the already serialized full Parseval frames, but it
explains why rank three is structurally natural.

**Lemma 5.1 (faithful orthogonality plus three vertices).**  Let \(C\) be a
simple graph on \(r\ge3\) vertices.  Suppose there are nonzero rational row
vectors \(m_1,\ldots,m_r\in\mathbb Q^3\), spanning
\(\mathbb R^3\), such that

\[
m_i m_j^T=0\quad\Longleftrightarrow\quad ij\in E(C)
\qquad(i\ne j).
\]

Then \(q(\overline C\vee K_3)=2\).

**Proof.**  Put the rows into \(M\in\mathbb Q^{r\times3}\).  If
\(S=M^TM\) is scalar, multiply one nonzero row by two.  This preserves all
zero/nonzero dot products and spanning, while replacing \(S\) by
\(S+3m_i^Tm_i\), which is nonscalar because a nonzero rank-one matrix cannot
be a scalar \(3\times3\) matrix.  Thus assume \(S\) is nonscalar.

Choose an integer \(\alpha>\lambda_{\max}(S)\), put
\(D=\alpha I_3-S\), and let \(L=D^{1/2}\).  Then \(D\) is positive definite
and nonscalar, while \(L\) is invertible and algebraic over \(\mathbb Q\).
There exists \(R\in SO(3)\) such that, for \(N=RL\), every entry of
\(MN^T\) and every off-diagonal entry of \(NN^T=RDR^T\) is nonzero.  Here is
an exact existence justification.  Each forbidden equality is a polynomial
equality on \(SO(3)\).  A cross equality is not identically zero because the
corresponding row of \(ML\) is nonzero.  An off-diagonal equality for
\(RDR^T\) is not identically zero because \(D\) is nonscalar: rotate through
\(45^\circ\) in a plane spanned by eigenvectors having unequal eigenvalues.
The zero set of each nonzero real-analytic function has empty interior on
the connected manifold \(SO(3)\), so finitely many such sets cannot cover it.
Moreover \(R\) may be chosen with rational entries, since rational unit
quaternions are dense in \(S^3\) and their images are dense in \(SO(3)\).
Thus all resulting entries are real algebraic numbers, not numerical limits.

Now define

\[
B=\begin{bmatrix}M\\N\end{bmatrix},\qquad
P=\alpha^{-1}BB^T.
\]

Since

\[
B^TB=M^TM+N^TN=S+L R^TR L=S+D=\alpha I_3,
\]

we have \(P^T=P\) and \(P^2=P\).  Its upper-left off-diagonal zeros are
exactly the edges of \(C\), its cross block is totally nonzero, and its
lower-right off-diagonal entries are totally nonzero.  Therefore
\(A=I-2P\in S(\overline C\vee K_3)\).  Because
\(0<\operatorname{rank}P=3<r+3\), \(A\) has both eigenvalues \(-1\) and
\(1\), and no others.

The proof handles repeated eigenvalues of \(D\): only the scalar case would
make all rotated off-diagonal entries vanish identically, and that case was
excluded.  It also contains no division by a row norm or by a potentially
zero dot product.

## 6. Faithful rational representations for the exceptional cores

**Lemma 6.1 (odd unicyclic graphs).**  Every connected non-bipartite
unicyclic graph has a faithful orthogonal representation by nonzero rational
vectors in \(\mathbb Q^3\), spanning \(\mathbb R^3\).

**Proof.**  Its unique cycle is odd.  A triangle is represented by the three
standard basis vectors.  For a cycle \(C_5=(1,2,3,4,5,1)\), use

\[
(1,0,0),\ (0,1,0),\ (1,0,1),\ (1,1,-1),\ (0,1,1).
\]

Direct dot products show that the five zero pairs are exactly the cycle
edges, no two vectors are parallel, and the vectors span \(\mathbb R^3\).
(For the present order-six core, an odd unicyclic graph has cycle length only
three or five.)

Every remaining vertex can be added in rooted-tree order, so it has exactly
one previously added neighbor, its parent \(p\).  Choose its vector in the
rational plane \(m_p^\perp\), avoiding: zero; the finitely many lines on
which it is orthogonal to any previous nonparent vector; and the finitely
many lines on which it is parallel to a previous vector.  None of the first
kind of forbidden lines is the whole plane because, inductively, no previous
vector is parallel to \(m_p\).  A finite union of proper rational lines does
not exhaust a rational two-dimensional vector space, so a rational choice
exists.  This preserves faithfulness, nonparallelity, and the spanning
property.  It also covers arbitrary attachment points and multiple branches.

We now discharge the three exceptional component patterns.

### 6.2 Pattern \((6,1,1,1)\)

Write \(H=C\cup3K_1\).  Connectedness gives
\(|E(C)|\ge5\), while a connected five-edge graph on six vertices is a tree
and hence bipartite.  Thus \(|E(C)|=6\), and \(C\) is non-bipartite
unicyclic.  Lemmas 6.1 and 5.1 give

\[
q(\overline H)=q(\overline C\vee K_3)=2.
\]

### 6.3 Pattern \((5,2,1,1)\)

Write \(H=C\cup K_2\cup2K_1\).  Edge counting forces \(C\) to be connected,
non-bipartite, unicyclic, and to have five edges.  If \(\overline C\) is
connected, then

\[
\overline H=\overline C\vee\overline{(K_2\cup2K_1)}
           =\overline C\vee(K_4-e),
\]

and the factors are connected of orders five and four, so Lemma 3.1 applies.

If \(\overline C\) is disconnected, then \(C\) is a nontrivial join.  A
cut of sizes two and three already contributes six cross edges, impossible;
hence \(C\) has a universal vertex \(u\).  The graph \(C-u\) has exactly one
edge, so its two isolated vertices \(x,y\) satisfy
\(N_H(x)=N_H(y)=\{u\}\).  In \(H-x\), group the four-vertex component
\(C-x\) with one isolated vertex, and group the \(K_2\) component with the
other isolated vertex.  The complements of these two disconnected induced
graphs are connected and have orders five and three.  Lemma 3.1 gives
\(q(G-x)=2\).  Finally, directly from the displayed equal neighborhoods,
\(G\) is the joined duplication of \(y\) in \(G-x\): the new \(x\) is
adjacent exactly to \(N_{G-x}[y]\).  The published joined-duplication lemma
therefore gives \(q(G)\le q(G-x)=2\), and \(G\) has edges, so equality holds.

### 6.4 Pattern \((5,1,1,1,1)\)

Write \(H=C\cup4K_1\), where \(C\) is connected non-bipartite and has five
or six edges.  If \(\overline C\) is connected, use the connected join
\(\overline C\vee K_4\) of orders five and four.

If \(\overline C\) is disconnected, \(C\) is a nontrivial join.  If every
complement component had order at least two, the only possible cut would be
\(2+3\), consuming all six edges and making \(C=K_{2,3}\), contrary to
non-bipartiteness.  Thus \(C\) has a universal vertex \(u\), and
\(F=C-u\) has one or two edges.  A faithful rational representation in
\(\mathbb Q^3\) is obtained by assigning \(u=(0,0,1)\) and using the
following vectors in the \(xy\)-plane (the displayed pairs are precisely
the edges of \(F\)):

| \(F\) | vertex vectors in order | edge pairs |
|---|---|---|
| \(K_2\cup2K_1\) | \(e_1,e_2,e_1+e_2,e_1+2e_2\) | \(12\) |
| \(P_3\cup K_1\) | \(e_2,e_1,e_2,e_1+e_2\) | \(12,23\) |
| \(2K_2\) | \(e_1,e_2,e_1+e_2,e_1-e_2\) | \(12,34\) |

All unspecified dot products in each row are nonzero, and the universal
vertex is orthogonal to all four plane vectors.  Lemma 5.1 first gives
\(q(\overline C\vee K_3)=2\).  Adding the fourth universal vertex is joined
duplication of any vertex in this \(K_3\), so
\(q(\overline C\vee K_4)=2\).

This completes a structural positive proof for every component-size pattern.
Its only external mathematical dependencies are the balanced connected-join
and joined-duplication theorems.

## 7. Independent audit of the serialized rational Parseval implication

The main certificate takes an even shorter finite route for every residual
graph.  For each witness it stores rational directions
\(w_i\in\mathbb Q^3\) and positive rational weights \(x_i\), and the verifier
checks, using `fractions.Fraction`,

\[
\sum_i x_iw_i^Tw_i=I_3,
\qquad
\langle w_i,w_j\rangle=0\iff ij\in E(H).
\]

Define the algebraic matrix \(V\in\mathbb R^{n\times3}\) by
\(V_i=\sqrt{x_i}\,w_i\), and \(P=VV^T\).  The checked rational identity gives

\[
V^TV=I_3,\qquad P^2=V(V^TV)V^T=P.
\]

For \(i\ne j\),

\[
(I-2P)_{ij}=-2\sqrt{x_ix_j}\,\langle w_i,w_j\rangle.
\]

Since every \(x_i>0\), the square-root factor is nonzero.  Hence this entry
vanishes if and only if \(ij\in E(H)\), and is nonzero if and only if
\(ij\in E(\overline H)\).  Therefore \(Q=I-2VV^T\in S(G)\) exactly; there
is no tolerance or sign assumption.  Also

\[
Q^2=I-4P+4P^2=I.
\]

The exact identity \(V^TV=I_3\) implies \(\operatorname{rank}P=3\).  For the
certified orders \(n=7,8,9\), both \(3\) and \(n-3\) are positive, so \(Q\)
has eigenvalue \(-1\) with multiplicity three and \(+1\) with multiplicity
\(n-3\).  Thus it has **exactly** two distinct eigenvalues, not merely at
most two.

The `orthogonality_order` field is discovery provenance only.  The serialized
direction rows themselves are indexed in graph6 vertex order, and the
verifier compares every dot product directly with the correspondingly
indexed graph edge.  A corrupted order field therefore cannot change the
support test (the parser only verifies it is a permutation).

## 8. Agreement with the finite routing and current gaps

Running the independent verifier gives the order-nine split

\[
72\text{ bipartite},\qquad24\text{ balanced join},\qquad12\text{ exact frame}.
\]

The 12 non-bipartite residual witnesses have component patterns

* 3 instances of \((5,1,1,1,1)\);
* 8 instances of \((6,1,1,1)\), exactly the eight non-isomorphic connected
  non-bipartite unicyclic cores on six vertices;
* 1 instance of \((5,2,1,1)\).

Thus the exact finite certificate and the definition-first structural
classification agree case by case at the level of component patterns.  The
command

```text
python verification/verify_n9_certificate.py certificates/n9_exact_frames.json
```

returned `VERIFIED` with 14 total frame witnesses (one each for orders seven
and eight, twelve for order nine).

No fatal mathematical gap was found in the implications

1. component partition \(\Rightarrow\) exact connected join;
2. checked rational frame \(\Rightarrow\) algebraic symmetric involution;
3. involution with exact support \(\Rightarrow q(G)=2\).

The following audit obligations remain outside this builder branch:

* **External-dependency obligation (major until citation audit closes it):**
  confirm the exact hypotheses and endpoint of the balanced connected-join
  theorem and of the joined-duplication lemma in the primary sources.
* **Enumeration-dependency obligation (major until the referee accepts it):**
  the independent verifier reconstructs components from NetworkX's graph
  atlas, whose completeness through order seven is an external finite-data
  fact.  The mathematical reason order seven suffices is exact: a nontrivial
  connected component with at most six edges has at most seven vertices.
  Nevertheless atlas provenance/version should be bound or replaced by an
  internally exhaustive generator if the release standard forbids trusting
  that catalogue.
* **No proof assistant was used.**  All implications here are ordinary
  mathematical proofs plus exact rational verification; no Lean, Coq, or
  Isabelle endpoint is claimed.
