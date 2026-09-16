# Exact partial results proved in this owner pass

These elementary results separate proved structure from computational
evidence. No claim of novelty is made.

## Lemma 1: corner/min-cut interpretation

For every shape \(\lambda\) and integer \(k\ge0\), a union of \(k\)
independent sets in \(R_\lambda\) is the same object as a subgraph of
\(B_\lambda\) with every row and column degree at most \(k\). Bipartite edge
coloring decomposes every such subgraph into \(k\) matchings. The standard
capacitated matching min-cut formula, specialized to a Ferrers board, is (1)
in `problem/formal_statement.md`.

The last corner specialization uses Ferrers monotonicity: among choices of
\(i\) rows and \(j\) columns, choosing the longest \(i\) rows and tallest
\(j\) columns leaves the fewest uncovered cells. This is also Theorem 14 of
Chow–Tiefenbruck; the present project independently evaluates the same integer
quantity by max flow.

## Lemma 2: rectangles

If \(\lambda=(a^b)\), set \(m=\min(a,b)\) and \(M=\max(a,b)\). Then

\[
\rho_k=m\min(k,M),\qquad
\delta=(\underbrace{m,\ldots,m}_{M\text{ terms}}).
\]

Indeed, the smaller bipartition side gives the upper bound \(mk\) for
\(k\le M\), and the complete bipartite graph \(K_{a,b}\) contains \(k\)
edge-disjoint matchings saturating that side. Assuming \(b\le a\), the
explicit coloring \(c(i,j)=i+j\pmod a\) has exactly \(a\) classes of size
\(b\). Transposition covers \(a<b\).

## Lemma 3: hooks

Up to transposition, every hook is \(\lambda=(M,1^{m-1})\) with
\(M\ge m\ge1\). Its CDS is

\[
\delta=(\underbrace{2,\ldots,2}_{m-1},
\underbrace{1,\ldots,1}_{M-m+1}).
\]

For \(1\le k<M\), a degree-\(k\) subgraph contains at most \(k\) edges of
the long row and at most \(\min(k,m-1)\) remaining edges of the first column;
both bounds can be attained. At \(k=M\), all \(M+m-1\) cells are attained.
For an explicit CDS coloring, pair tail cell \((i,0)\) with long-row cell
\((0,i)\) for \(1\le i<m\); these are \(m-1\) matchings of size 2. Give each
remaining long-row cell its own color.

## Lemma 4: two-row shapes

For \(\lambda=(a,b)\) with \(a\ge b\ge1\) and \(a\ge2\),

\[
\delta=(\underbrace{2,\ldots,2}_{b},
\underbrace{1,\ldots,1}_{a-b}).
\]

Every matching has size at most 2. For \(k\le b\), the first \(k\) pair
classes in the construction below attain \(\rho_k=2k\). For \(b<k\le a\),
the long row contributes at most \(k\) cells and the short row at most \(b\),
and the construction attains \(\rho_k=k+b\). To construct it, match every
short-row column \(j\) to a distinct long-row column \(f(j)\ne j\): use the
cyclic shift on the first \(b\) columns if \(b\ge2\), and use \(f(0)=1\) if
\(b=1\). These give \(b\) size-2 color classes; the unused long-row cells are
singletons. The exceptional \((1,1)\) case is a rectangle.

## Lemma 5: staircases

For \(\lambda=(n,n-1,\ldots,1)\),

\[
\rho_k=kn-\frac{k(k-1)}2\quad(0\le k\le n),\qquad
\delta=(n,n-1,\ldots,1).
\]

Coloring cell \((i,j)\) by \(i+j\) partitions the board into antidiagonal
matchings of sizes \(1,2,\ldots,n\), giving the lower bound. In the corner
formula, choose \(i=0\) and \(j=n-k\). The residual staircase has
\(k(k+1)/2\) cells, so the resulting upper bound is
\(k(n-k)+k(k+1)/2=kn-k(k-1)/2\). Hence every prefix is optimal.

## Owner-context candidate Lemma 6: exact block-allocation equivalence

Group equal-length rows and equal-height columns into Ferrers blocks. A CDS
coloring exists if and only if nonnegative integer row-block/column-block/color
quotas satisfy every block total, every row-block and column-block per-color
capacity, and every CDS color total. Necessity is counting. Sufficiency uses
the Bahmanian--Rodger colored-detachment lemma to split row blocks and then
column blocks; the product block multiplicities become exactly one edge per
cell and the normalized per-color degrees become at most one.

The precise system, proof, external dependency, and audit obligations are in
`proof/two_level_candidate.md`. This lemma is not counted as independently
accepted until a fresh mathematical audit checks the detachment statement and
its sequential application.

## Owner-context candidate Theorem 7: two distinct row lengths

Every nonempty shape with at most two distinct positive row lengths is
CDS-colorable. For a genuine two-level shape

\[
\lambda=(a^p,b^q),\qquad a>b\geq1,\quad p,q\geq1,
\]

the exact formula

\[
\rho_k=\min\{pa+qb,ka,k(p+q),k(p+b),kb+p(a-b),kp+qb\}
\]

reduces the problem to three integer quotas per color. Positive-part sums of
the CDS increments are bounded by the last two corner lines, giving an
explicit feasible quota allocation in the two cases (a\geq p+q) and
(p+q\geq a). Candidate Lemma 6 then lifts the quotas to a coloring.

The complete derivation is `proof/two_level_candidate.md`. The six-line
formula and quotas were checked on 4,224 parameter quadruples (48,710 prefix
equalities), and fixed-quota cell colorings were found for 525 small parameter
quadruples; see `logs/verify-two-level-candidate.log`. These computations
attack transcription and endpoint errors but do not replace the pending fresh
proof audit.

## Limitation

The independently unaudited candidate Theorem 7 controls two row-length
blocks, but no argument here controls three or more blocks in general. The
exact obstruction in
`data/route-obstructions.json` also shows that an arbitrary maximum matching
cannot safely be selected as the first color class, so these constructions do
not yield a naive induction.
