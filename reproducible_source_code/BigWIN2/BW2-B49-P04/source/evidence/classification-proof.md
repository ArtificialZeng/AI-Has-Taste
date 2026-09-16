# Complete classification of identifying edges in \(J_m\)

Throughout, \(m\ge 6\), subscripts are modulo \(m\), and
\(e_i=r_i r_{i+1}\).  Put \(G=J_m\).

## Theorem

The identifying edges of \(J_m\) are exactly
\[
   pw,\quad wr_0,\quad wr_1.
\]
Under \(\operatorname{Aut}(J_m)\), they form the two orbits
\(\{pw\}\) and \(\{wr_0,wr_1\}\).  Hence their total number is
\(3\).  The card of \(pw\) has multiplicity \(1\), and the common
unlabelled card type of \(wr_0,wr_1\) has multiplicity \(2\).

The complete edge-orbit list is as follows.  Let \(i\) range over a set of
representatives of the displayed equivalence relation:
\[
\begin{array}{c|c}
\text{edges}&\text{index relation}\\ \hline
\{pw\}&--\\
\{wr_0,wr_1\}&--\\
\{pr_i,pr_{1-i}\}&i\sim 1-i\\
\{qr_i,qr_{1-i}\}&i\sim 1-i\\
\{e_i,e_{-i}\}&i\sim-i.
\end{array}
\]
Repeated members in a displayed two-element set are retained only once.  Thus
the number of edge orbits is \(3m/2+3\) for even \(m\), and
\((3m+7)/2\) for odd \(m\).  Every orbit in the last three rows is
non-identifying, with explicit rival completions given below.

## All parents of the three identifying cards

We first use an elementary parent observation.  If \(C=G-e\), and a maximal
planar graph \(H\) has \(H-f\cong C\), identify \(H-f\) with \(C\).
Then \(H=C+xy\) for a nonedge \(xy\) of \(C\).  This is exhaustive because
the deletion retains all vertices and exactly one edge was removed.

For each of the cards obtained by deleting an edge incident with \(w\), the
vertex \(w\) is the unique degree-two vertex.  Every maximal planar graph on
at least four vertices has minimum degree at least three, so the added edge
\(xy\) must be incident with \(w\).  Moreover, the three neighbours of a
degree-three vertex in a plane triangulation form a triangle.  Consequently,
if the two neighbours of \(w\) in the card are \(a,b\), the other endpoint of
the added edge must be a common neighbour of \(a,b\).  Directly from the edge
set of \(J_m\), the possibilities are
\[
\begin{array}{c|c|c}
\text{deleted edge}&N_C(w)&\text{only possible added edges}\\ \hline
pw&\{r_0,r_1\}&wp,wq\\
wr_0&\{p,r_1\}&wr_0,wr_2\\
wr_1&\{p,r_0\}&wr_1,wr_{m-1}.
\end{array}
\]
Every listed addition is planar and has \(3|V|-6\) edges, hence is maximal
planar.  The two completions in the first row are isomorphic by interchanging
the two hubs.  In the second row, both completions are a bipyramid with \(w\)
stacked respectively in \(pr_0r_1\) or \(pr_1r_2\), and a rim rotation is an
isomorphism between them.  The third row is symmetric.  Thus all three edges
are identifying; this argument also proves that no possible maximal-planar
parent was omitted.

## Explicit rivals for every other edge orbit

Use the standard embedding inherited from the bipyramid and the stacking of
\(w\).  Each edge below is incident with the two indicated triangular faces;
their opposite vertices are nonadjacent.  Deleting that edge and adding the
other diagonal therefore gives another finite simple maximal planar graph:
\[
\begin{array}{c|c|c}
\text{deleted edge}&\text{opposite vertices}&\text{added edge}\\ \hline
pr_0&w,r_{m-1}&wr_{m-1}\\
pr_1&w,r_2&wr_2\\
pr_i,\ i\notin\{0,1\}&r_{i-1},r_{i+1}&r_{i-1}r_{i+1}\\
qr_i&r_{i-1},r_{i+1}&r_{i-1}r_{i+1}\\
e_0=r_0r_1&w,q&wq\\
e_i,\ i\ne0&p,q&pq.
\end{array}                                                    \tag{2}
\]
These recipes apply to every member, and hence to a representative, of every
orbit in the last three rows of the orbit table.

It remains to verify that none of these flip rivals is accidentally isomorphic
to \(J_m\).  In \(J_m\),
\[
 d(p)=m+1,\quad d(q)=m,\quad d(w)=3,\quad
 d(r_0)=d(r_1)=5,\quad d(r_i)=4\ (i\ne0,1).                 \tag{3}
\]
For \(e_0\), the rival has two vertices of maximum degree \(m+1\), whereas
\(J_m\) has one.  For \(e_i\), \(i\ne0\), the new edge \(pq\) raises the
maximum degree to \(m+2\).  For \(pr_0,pr_1\), and for every
\(pr_i\) with \(i\notin\{0,1\}\), the rival has maximum degree at most
\(m\) (the only other possible value is \(6\)), which is strictly below
\(m+1\) for \(m\ge6\).  Therefore all these degree multisets differ from
that of \(J_m\).

For a \(qr_i\) flip, \(q\) drops from degree \(m\) to \(m-1\), and every
changed rim degree is at most \(6\).  If \(m\ge7\), the rival consequently has
no vertex of degree exactly \(m\), while \(J_m\) has one.  For completeness,
when \(m=6\) the degree multisets are
\[
\begin{array}{c|c}
\text{graph or index}&\text{degree multiset}\\ \hline
J_6&7,6,5^2,4^4,3\\
i\in\{2,5\}&7,6,5^3,4^2,3^2\\
i\in\{3,4\}&7,5^5,4,3^2.
\end{array}
\]
Thus only \(i\in\{0,1\}\) can have the original degree multiset.  In either
of those exceptional cases both graphs have unique vertices of degrees \(7\)
and \(6\): they are the nonadjacent pair \(p,q\) in \(J_6\), whereas in the
rival they are \(p,r_1\) (for \(i=0\)) or \(p,r_0\) (for \(i=1\)), which are
adjacent.  Hence the rivals are nonisomorphic in all cases.  This proves that
every edge not incident with \(w\) is non-identifying.

## Automorphisms and card multiplicities

The degree data (3) force every automorphism to fix \(p,q,w\), preserve
\(\{r_0,r_1\}\), and preserve the remaining rim vertices.  On the induced
rim cycle it must stabilize the edge \(r_0r_1\), whose setwise stabilizer in
the dihedral group of the cycle consists of the identity and
\[
     r_i\longmapsto r_{1-i}.
\]
Both maps extend to automorphisms of \(J_m\).  Thus
\(\operatorname{Aut}(J_m)\cong C_2\), and its action gives exactly the orbit
table above and its even/odd counts.

Finally, deleting a non-\(w\) edge leaves minimum degree at least three, whereas
each of the three identifying cards has the unique degree-two vertex \(w\).
So no other edge contributes to either identifying card type.  The \(pw\)
card has maximum degree \(m\), whereas a \(wr_0\) or \(wr_1\) card has maximum
degree \(m+1\), so these are distinct types.  The reflection interchanges the
last two.  Their multiplicities are therefore exactly \(1\) and \(2\), as
claimed.

## Exact computational boundary check

`evidence/enumerate_cards.py` independently implements the following finite
exhaustion for each edge card: test every nonedge as the one possible added
edge, retain exactly the planar \(3n-6\)-edge graphs, and quotient edges,
cards, and parents using exact VF2 graph isomorphism.  The complete serialized
results for \(m=6,7,8,9\) are in `evidence/census-m6-m9.json`.  They give the
identifying types \(\{pw\}\) and \(\{wr_0,wr_1\}\), with multiplicities
\(1,2\), and a nonisomorphic parent for every other card.  The same check for
\(10\le m\le20\), recorded in `evidence/census-m10-m20.json`, found no new
card coincidence or exception.  These finite checks support but are not used
to justify the uniform proof.
