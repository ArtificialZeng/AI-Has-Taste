# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim in `claim.json`: for every
integer \(k\geq 3\), the frozen function satisfies
\(f(k-1,k)=k+3\), together with the stated classification of the auxiliary
graph \(H_T\). I used only `source.md`, `problem.md`, `claim.json`,
`audit/snapshot.json`, and the three additional evidence files named by that
snapshot.

I recomputed the SHA-256 digest of every frozen file. All six file digests
match `audit/snapshot.json`. I also recomputed the canonical digest of its
sorted compact `files` mapping; it is
`0241c53b5ef3368d41ea56e3fa928f2b43201af183c250167ad1ff34ae4901f2`,
equal to the recorded snapshot digest.

## Reconstruction of the decisive argument

For an edge \(ab\) of \(H_T\), one endpoint beats every vertex outside
\(\{a,b\}\). If \(T\) has a source \(s\), every such edge contains \(s\),
because an endpoint of an edge avoiding \(s\) would have to beat \(s\).
Thus \(H_T\) is contained in the star centered at \(s\).

If \(T\) has no source, a witnessing endpoint for \(ab\) has its mate as
its unique in-neighbor. Two disjoint edges would therefore have witnessing
endpoints \(x,y\) which simultaneously satisfy \(x\to y\) and \(y\to x\),
an impossibility. Hence the edges of \(H_T\) are pairwise intersecting. A
pairwise-intersecting family of two-subsets is either contained in a star or
is exactly the three edges of a triangle: from two edges \(ab,ac\), failure
of a common center supplies the forced edge \(bc\), and any edge meeting all
three is one of these three. This proves the structural lemma, including the
empty and one-edge cases.

At order \(n=k+1\), the \(k\)-set \(V\setminus\{x\}\) can only be witnessed
by \(x\), so \(x\) must be a source in one of the \(k-1\) tournaments. Each
tournament has at most one source, leaving at least two of the \(k+1\)
complements uncovered.

At order \(n=k+2\), covering all \(k\)-sets is exactly the assertion that
the \(n-3\) graphs \(H_{T_i}\) cover \(E(K_n)\). Suppose \(a\) of them are
star-type. Choose their centers, let \(C\) be the set of \(r\leq a\)
distinct centers, and put \(q=n-r\geq3\). After deleting \(C\), no
star-type graph supplies an edge, while the remaining \(n-3-a\leq q-3\)
triangle graphs supply at most \(3(q-3)\) edges. They cannot cover the
\(\binom q2\) required edges because
\[
  2\left(\binom q2-3(q-3)\right)=q^2-7q+18>0
\]
for every real \(q\), its discriminant being \(-23\). This argument remains
valid when star centers repeat and at the endpoint \(q=3\).

For the upper bound, partition \(k+3\) vertices into two triples and
\(k-3\) singletons, one block for each of the \(k-1\) tournaments. In the
tournament belonging to a block, orient every block-to-complement edge
outward and orient a triple block cyclically. Any \(k\)-set either misses a
singleton or meets one of the triples in at most one vertex; otherwise it
would contain at least \((k-3)+2+2=k+1\) vertices. A missed singleton is the
required common outside dominator. For a triple met in zero vertices, any
triple vertex works; for a triple met in the single vertex \(u\), one of the
other two cyclically beats \(u\) and, by the outward orientation, also beats
every selected vertex outside the block. The same outside vertex and the
same tournament therefore satisfy the frozen quantifiers. The prescriptions
fix disjoint classes of edges and extend to tournaments.

These arguments exclude every permissible order below \(k+3\), namely
\(k+1\) and \(k+2\), and construct order \(k+3\). The construction also
works without singleton blocks when \(k=3\).

## Checks performed and source comparison

I separately checked the possible degeneracies: looplessness forces the
witness outside the selected set; a tournament cannot have two sources;
triangle-type means an exact triangle; deleting repeated star centers only
strengthens the triangle-count bound; and the quadratic edge deficit is
strict for all \(q\geq3\). No compactness, limiting argument, division, or
external theorem is used.

I ran `python3 evidence/triage_check.py` from the project root. It exited
successfully and reproduced the frozen output: exhaustive structural checks
for all labeled tournaments of orders 3 through 6, construction checks for
\(3\leq k\leq12\), and the displayed finite inequality check. These are
sanity checks only; the verdict rests on the symbolic proof above.

Within the frozen source comparison, the cited source already provides the
upper-bound mechanism and SAT values for \(3\leq k\leq6\), while the exact
candidate adds the uniform lower bound and gives a direct construction. The
candidate does not assert publication priority or that the question was
explicitly source-listed. Its mathematical scope is the full frozen original
claim, rather than a downgraded subsidiary result.

## Gaps and verdict

I found no unresolved mathematical gap in the frozen claim. The auxiliary
classification, both lower-bound boundary orders, all parameter endpoints,
and the explicit upper construction are correct at the asserted scope.

**Verdict: accept.**
