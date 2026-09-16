# Proof submitted for mathematical review

## Theorem

For every finite simple connected graph \(G\) with at least two vertices,
under the simultaneous-spread convention fixed in `problem.md`,
\[
  2b(G)-2\leq \gamma_R(G).
\]

## Proof

Among all minimum-weight Roman dominating functions (RDFs) on \(G\), choose
one, \(f\), for which \(|V_1|\) is as small as possible, where
\(V_i=f^{-1}(i)\).  Put \(a=|V_2|\) and \(c=|V_1|\).  Thus
\(\gamma_R(G)=2a+c\).

We first record three elementary properties of this choice.

1. There is no edge between \(V_1\) and \(V_2\).  Indeed, if
   \(u\in V_1\) had a neighbor in \(V_2\), changing only \(f(u)\) from 1 to
   0 would give a lighter RDF.
2. The set \(V_1\) is independent.  If adjacent vertices \(u,v\) both had
   label 1, change their labels to 2 and 0, respectively.  Every old
   0-vertex retains its old 2-neighbor, and the new 0-vertex \(v\) is
   adjacent to the new 2-vertex \(u\).  This is another minimum RDF, but it
   has two fewer 1-vertices, contrary to the choice of \(f\).
3. We have \(a\geq 1\).  Otherwise the RDF has no 0-vertices and labels all
   \(n=|V(G)|\) vertices 1.  Choose a vertex \(v\) of positive degree (it
   exists because \(G\) is connected and \(n\geq2\)), give \(v\) label 2,
   its neighbors label 0, and all other vertices label 1.  This RDF has
   weight \(n+1-\deg(v)\leq n\).  If the inequality is strict, the all-1
   RDF was not minimum; if equality holds, the new RDF is minimum and has
   fewer 1-vertices.  Both alternatives are contradictions.

These properties imply that every vertex of \(V_0\) is at distance 1 from
\(V_2\), by the RDF condition.  They also imply that every vertex of
\(V_1\) is at distance 2 from \(V_2\): a vertex of \(V_1\) has a neighbor
because \(G\) is connected and nontrivial; that neighbor is in \(V_0\), by
properties 1 and 2; and this \(V_0\)-neighbor in turn has a neighbor in
\(V_2\).

Consider the ordinary burning process.  During each of the first \(a\)
rounds, if an unburned vertex of \(V_2\) remains, choose one as the new
source; otherwise choose any unburned vertex.  (If the whole graph has
already burned, the asserted upper bound is already established.)  In every
such round in which some \(V_2\)-vertex remains unburned, at least one new
\(V_2\)-vertex burns.  Consequently all of \(V_2\) is burned by the end of
round \(a\).

We distinguish the possible values of \(c\).

- If \(c=0\), one further round burns every vertex of \(V_0\), since each is
  adjacent to \(V_2\).  Thus \(b(G)\leq a+1\).
- If \(c=1\), in round \(a+1\) choose the unique vertex of \(V_1\) if it is
  still unburned (and otherwise choose any unburned vertex).  During that
  same final round the fire already on \(V_2\) reaches all of \(V_0\).
  Hence again \(b(G)\leq a+1\).
- If \(c\geq2\), after two further rounds the fire on \(V_2\) has reached
  every vertex at distance at most 2, hence all of \(V_0\cup V_1\).  Thus
  \(b(G)\leq a+2\leq a+\lfloor c/2\rfloor+1\).

In all cases,
\[
 b(G)\leq a+\left\lfloor\frac c2\right\rfloor+1
 =\left\lfloor\frac{\gamma_R(G)}2\right\rfloor+1.
\]
Since \(b(G)\) and \(\gamma_R(G)\) are integers, this gives
\(2b(G)-2\leq\gamma_R(G)\), as required.  Every selected source above is
unburned when selected, so the construction obeys the required
simultaneous-spread convention (and therefore its sources satisfy the
distance condition in `problem.md`).

## Gap list

Empty.  The finite computation in `evidence/research_canonical_check.py` is
an off-by-one and structural sanity check only; it is not used to promote a
finite observation to the universal theorem.
