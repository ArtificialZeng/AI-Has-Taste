# Owner-context candidate proof: the two-row-length case

Status: **candidate partial theorem, not an independently audited resolution**.
This proves only a strict subfamily of the original Latin Tableau conjecture.
It does not change the original problem's unresolved status and does not
authorize a manuscript or PDF.

## Claimed partial endpoint

Every nonempty Young shape with at most two distinct positive row lengths is
CDS-colorable. Rectangles are covered by Lemma 2 of partial_results.md. For
the nonrectangular case, write

$$
\lambda=(a^p,b^q),\qquad a>b\geq1,\quad p,q\geq1,
$$

and put $r=p+q$, $s=a-b$, and $N=pa+qb$.

## Lemma A: exact block-allocation equivalence

Let the distinct row lengths of an arbitrary nonempty shape be
$a_1>\cdots>a_t>0$, with multiplicities $r_1,\ldots,r_t$. Put
$a_{t+1}=0$, $c_j=a_j-a_{j+1}$, and let column block $j$ be the
$c_j$ columns of height $r_1+\cdots+r_j$. Thus row block $i$ meets
column block $j$ exactly when $i\leq j$, and that full rectangular block
has $r_i c_j$ cells.

Let $\delta=(\delta_1,\ldots,\delta_D)$ be the CDS, with its positive
terms only. The shape is CDS-colorable if and only if there are nonnegative
integers $z_{ij\ell}$, for $1\leq i\leq j\leq t$ and
$1\leq\ell\leq D$, satisfying

$$
\begin{aligned}
\sum_\ell z_{ij\ell}&=r_i c_j &&(i\leq j),\\
\sum_{j\geq i}z_{ij\ell}&\leq r_i &&(i,\ell),\\
\sum_{i\leq j}z_{ij\ell}&\leq c_j &&(j,\ell),\\
\sum_{i\leq j}z_{ij\ell}&=\delta_\ell &&(\ell).
\end{aligned}
\tag{BA}
$$

Necessity follows by counting cells of each color in every block. For
sufficiency, form a loopless edge-colored bipartite multigraph $H$ with one
vertex $R_i$ for each row block and one vertex $C_j$ for each column block.
Put $z_{ij\ell}$ parallel edges of color $\ell$ between $R_i$ and $C_j$.
The first equations give multiplicity $r_i c_j$ on every present pair, and
the next two inequalities give

$$
\deg_{H(\ell)}R_i\leq r_i,\qquad
\deg_{H(\ell)}C_j\leq c_j.
$$

Apply the colored detachment lemma of Bahmanian--Rodger, in the exact form
restated as Lemma 3.1 of Bahmanian, *Completing Multi-Latin Rectangles via
Factors With Prescribed Degrees in Bipartite Graphs*, Journal of
Combinatorial Designs 34 (2026), 31--36, DOI 10.1002/jcd.22008. First split
every $R_i$ into $r_i$ vertices. The color degrees at every split vertex are
0 or 1, because the lemma distributes each color degree within floor/ceiling
of its quotient by $r_i$. Moreover, each split row vertex has exactly $c_j$
edges to the still-amalgamated $C_j$, since $r_i c_j/r_i=c_j$. Then split
every $C_j$ into $c_j$ vertices. Its split color degrees are again 0 or 1,
and every allowed row--column pair receives exactly one edge, since
$c_j/c_j=1$. The resulting simple graph is $B_\lambda$, every color class
is a matching, and detachment preserves its total size $\delta_\ell$.
This proves sufficiency.

The sequential use is legitimate because later splitting only redistributes
the endpoints at column-block vertices; it does not change the already
bounded color degree at a split row vertex. Empty block widths do not occur
because the $a_i$ are distinct. No loop is present at any stage. The
two-vertex statement of the lemma can be iterated over all blocks, leaving an
auxiliary second vertex unchanged by assigning it split count one when
necessary.

## Lemma B: the six-line formula for two levels

For $\lambda=(a^p,b^q)$ and every integer $k\geq0$,

$$
\rho_k=\min\{N,ka,kr,k(p+b),kb+ps,kp+qb\}.
\tag{2}
$$

Indeed, in the corner formula the objective is separately affine in each
coordinate between the row breakpoints $0,p,r$ and column breakpoints
$0,b,a$. For each fixed row index its minimum over a column interval is at
an endpoint (or the function is constant there); after restricting to column
breakpoints, the same argument applies in the row coordinate. It therefore
attains its minimum at one of the nine breakpoint pairs. Three values are
dominated by $ka$ or $kr$, and the remaining six are exactly (2). This
argument also covers $k=0$.

The minimum of affine functions of $k$ is concave. Hence the increments
$\delta_i=\rho_i-\rho_{i-1}$ are nonincreasing. The maximum degree of
$B_\lambda$ is $D=\max(a,r)$, so the whole graph has degree at most $D$ and
$\rho_D=N$. A vertex of degree $D$ prevents $D-1$ matchings from covering
all edges, so $\rho_{D-1}<N$. Thus $\delta_D>0$, and concavity makes all
$D$ increments positive. For any integer $h\geq0$, monotonicity gives

$$
\sum_{i=1}^{D}\max(0,\delta_i-h)
=\max_{0\leq k\leq D}(\rho_k-kh).
\tag{3}
$$

## Lemma C: an explicit feasible allocation when $a\geq r$

At $k=a-1$, the term $kp+qb$ in (2) gives
$\rho_{a-1}\leq N-p$, whereas $\rho_a=N$. Thus $\delta_a\geq p$, and
monotonicity gives $\delta_i\geq p$ for every $i\leq a$. Also

$$
\delta_i\leq\delta_1=\min(a,r,p+b)\leq\min(r,p+b).
\tag{4}
$$

For each color $i$, let $x_i,y_i,z_i$ be its intended numbers of cells in
the top-left $p\times b$, top-right $p\times s$, and bottom-left
$q\times b$ blocks. Set

$$
z_i=\delta_i-p,\qquad
L_i=\max(0,\delta_i-b),\qquad
U=\min(p,s).
$$

By (4), $0\leq z_i\leq\min(q,b)$ and $0\leq L_i\leq U$. Equations (2)
and (3), using $\rho_k\leq kb+ps$, give

$$
\sum_iL_i\leq ps.
$$

Also $aU\geq ps$: if $p\leq s$, this is $ap\geq ps$, and if $s\leq p$,
it is $as\geq ps$. Consequently integers $y_i\in[L_i,U]$ can be chosen
with $\sum_i y_i=ps$, simply by starting at the lower bounds and distributing
the remaining units. Put $x_i=p-y_i$. Then

$$
x_i+y_i=p,\qquad x_i+z_i=\delta_i-y_i\leq b,
$$

and $y_i\leq s,z_i\leq q$. Finally,

$$
\sum_i z_i=N-pa=qb,\qquad
\sum_i y_i=ps,\qquad
\sum_i x_i=pa-ps=pb.
$$

Thus these three quotas satisfy (BA).

## Lemma D: an explicit feasible allocation when $r\geq a$

This is the transposed calculation. At $k=r-1$, the term $kb+ps$ in (2)
gives $\rho_{r-1}\leq N-b$, so every $\delta_i\geq b$. Also

$$
\delta_i\leq\delta_1=\min(a,r,p+b).
$$

Set

$$
y_i=\delta_i-b,\qquad
L_i=\max(0,\delta_i-p),\qquad
U=\min(q,b).
$$

Here $\delta_i\leq a$ and $\delta_i\leq p+b$ give
$0\leq y_i\leq\min(p,s)$, while
$\delta_i\leq r=p+q$ and $\delta_i\leq p+b$ give
$0\leq L_i\leq U$. Equations (2)--(3), using
$\rho_k\leq kp+qb$, give $\sum_iL_i\leq qb$. Since $rU\geq qb$, choose
integers $z_i\in[L_i,U]$ summing to $qb$, and put $x_i=b-z_i$. Then

$$
x_i+z_i=b,\qquad x_i+y_i=\delta_i-z_i\leq p,
$$

with all remaining capacities valid. The block totals are $pb,ps,qb$, so
(BA) again holds. The equality boundary $a=r$ is already covered by Lemma C;
the symmetric construction is consistent as an alternative.

## Conclusion and audit obligations

Lemmas C and D give (BA) for every genuine two-level shape; Lemma A lifts it
to a CDS coloring. Together with the rectangle construction, this yields the
claimed partial endpoint.

This owner-context proof has been attacked by:

- direct comparison of (2) with the full corner formula;
- exact quota checks in code/block_allocation.py;
- fixed-quota cell-level CP-SAT checks on all 525 parameter quadruples
  $2\leq a\leq7$, $1\leq b<a$, $1\leq p,q\leq5$, including the cyclic
  obstruction $(4,2,2)$; and
- separate block-allocation/max-flow verification on the recorded datasets.

It still requires a fresh-context mathematical audit of the detachment-lemma
statement and its sequential application, every inequality above, and the
mapping from (BA) back to the frozen target. It is not a candidate resolution
of the original universal conjecture.
