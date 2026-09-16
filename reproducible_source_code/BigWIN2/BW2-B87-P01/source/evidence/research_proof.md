# Complete proof candidate for the frozen claim

Proposer job: `win-00087-p01-research-981c2d1e0004`  
Date: 2026-09-11

## Theorem

With the definitions and quantifiers frozen in `source.md`, for every integer
\(k\ge 3\),
\[
f(k-1,k)=k+3.
\]

The proof uses only the tournament definitions and elementary graph counting.

## Auxiliary-graph classification

For a tournament \(T\) on a vertex set \(V\), \(|V|=n\ge3\), put
\[
 ab\in E(H_T)
 \quad\Longleftrightarrow\quad
 a\to V\setminus\{a,b\}\ \text{or}\
 b\to V\setminus\{a,b\}.
\]
Then \(H_T\) is contained in a star, or \(H_T\) is exactly a triangle.

Indeed, first suppose that \(T\) has a source \(s\). If an edge
\(ab\in E(H_T)\) did not contain \(s\), one of \(a,b\) would beat every
vertex outside \(\{a,b\}\), hence would beat \(s\). This contradicts that
\(s\) beats every other vertex. Thus every edge of \(H_T\) is incident with
\(s\), so \(H_T\) is contained in the star centered at \(s\).

Now suppose that \(T\) has no source. If \(ab\in E(H_T)\) and, say, \(a\)
is a witnessing endpoint, then every possible in-neighbor of \(a\) lies in
\(\{b\}\). Since \(a\) is not a source, \(b\to a\); equivalently, the
witnessing endpoint has its mate as its unique in-neighbor. There cannot be
two disjoint edges \(ab,cd\in E(H_T)\): choosing witnessing endpoints
\(x\in\{a,b\}\) and \(y\in\{c,d\}\) would give both \(x\to y\) and
\(y\to x\). Hence the edges of \(H_T\) are pairwise intersecting.

For completeness, every pairwise-intersecting family of two-element sets is
contained in a star or is the three-edge family of a triangle. If it is not
contained in a star, choose two distinct edges \(ab,ac\). Some edge misses
their common vertex \(a\), and intersection with both chosen edges forces
that edge to be \(bc\). Any edge intersecting all of \(ab,ac,bc\) is one of
those three. This proves the classification, including empty and one-edge
families (which are star-contained).

## Lower bound: the two possible smaller orders

Fix \(k\ge3\) and write \(m=k-1\).

At order \(n=k+1\), for each \(x\in V\) consider the \(k\)-set
\(U_x=V\setminus\{x\}\). Its only possible outside witness is \(x\), so
covering \(U_x\) requires \(x\) to be a source in one of the \(m\)
tournaments. A tournament has at most one source: if two vertices were
sources, the arc between them would have to point both ways. Thus the family
can cover at most \(m=k-1\) of the \(n=k+1\) sets \(U_x\), not all of them.

At order \(n=k+2\), the \(k\)-sets are precisely the complements of vertex
pairs. Consequently, a family \(T_1,\ldots,T_m\) has the required property
only if
\[
 E(H_{T_1})\cup\cdots\cup E(H_{T_m})=E(K_n),
 \qquad m=k-1=n-3.                                      \tag{1}
\]
Apply the classification above. Call an index star-type if its auxiliary
graph is contained in a star, and triangle-type otherwise; in the latter case
the auxiliary graph is exactly a triangle. Let \(a\) be the number of
star-type indices. Choose one star center for each of them (arbitrarily if
the auxiliary graph is empty), let \(C\) be the set of distinct chosen
centers, and put \(r=|C|\) and \(q=n-r\). We have
\(r\le a\le n-3\), so \(q\ge3\).

Delete \(C\). No star-type auxiliary graph contains an edge with both
endpoints in \(V\setminus C\). Therefore (1) would force the
\(n-3-a\) triangle-type graphs to cover all \(\binom q2\) pairs in
\(V\setminus C\). Each has only three edges, and
\[
 n-3-a\le n-3-r=q-3.
\]
It would follow that
\[
 \binom q2\le3(q-3).
\]
But for every \(q\ge3\),
\[
 2\left(\binom q2-3(q-3)\right)
 =q^2-7q+18
 =\left(q-\frac72\right)^2+\frac{23}{4}>0,
\]
a contradiction. This also explicitly covers the boundary \(q=3\), where
the right side of the purported cover bound is zero. Thus neither admissible
order below \(k+3\), namely \(k+1\) or \(k+2\), can work.

## Explicit upper-bound construction

Partition a set \(V\) of size \(k+3\) into two triples \(A,B\) and
\(k-3\) singleton blocks. There are exactly \(2+(k-3)=k-1\) blocks. For
each block \(D\), define one tournament \(T_D\) as follows:

- orient every edge between \(D\) and \(V\setminus D\) outward from \(D\);
- if \(|D|=3\), orient the three edges inside \(D\) as a directed 3-cycle;
- orient all still-undirected edges arbitrarily.

These rules concern disjoint classes of unordered pairs and therefore define
a tournament after the arbitrary orientations are chosen.

Let \(U\subseteq V\) have size \(k\). Some singleton block is disjoint from
\(U\), or one of \(A,B\) meets \(U\) in at most one vertex. Otherwise \(U\)
would contain all \(k-3\) singleton vertices and at least two vertices from
each triple, giving
\[
 |U|\ge(k-3)+2+2=k+1,
\]
which is impossible.

If a singleton block \(D=\{x\}\) is disjoint from \(U\), then in \(T_D\)
the outside vertex \(x\) beats every member of \(U\). If a triple block
\(D\) has \(|D\cap U|=0\), any vertex of \(D\) is an outside dominator of
\(U\). If \(D\cap U=\{u\}\), the directed 3-cycle on \(D\) has a vertex
\(x\in D\setminus\{u\}\) with \(x\to u\); this \(x\notin U\) also beats
every member of \(U\setminus D\) by the outward cross-block orientation.
Thus every \(k\)-set has one common outside dominator in one of the \(k-1\)
tournaments. Hence \(f(k-1,k)\le k+3\).

Together with the two lower-bound cases, and since the definition permits
orders only from \(k+1\) upward, this proves \(f(k-1,k)=k+3\) for every
integer \(k\ge3\).

## Dependency and gap record

No external theorem is used beyond elementary facts proved above. No
mathematical gap is presently known in this written argument. It remains a
research candidate until a fresh referee verifies the frozen quantifiers and
the proof. The finite script replay in `evidence/research_replay.md` is only a
sanity check and is not used in the proof.
