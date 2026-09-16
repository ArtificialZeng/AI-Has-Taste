# Fresh mathematical referee report

**Job:** `win-00087-p04-referee-34c4ea0e1017`  
**Frozen snapshot:** `9636664ac1ced02b0532fb759266264f87f9e7412272411db0e05a053013d507`  
**Candidate:** `resolution-paper`, with frozen `original_status` equal to `proved`  
**Verdict:** **accept**

## Scope reviewed

I reviewed the exact statement in `claim.json`, without weakening it.  It is
the complete four-part statement frozen in `source.md` and interpreted in
`problem.md`: all connected simple graphs on one through five vertices, the
zero result through order four, the if-and-only-if classification at order
five, all seven exact nonzero polynomials, and the uniqueness and Hilbert
vectors of the least-edge failure.  The claim does not purport to settle the
general operations question, any graph on six or more vertices, a disconnected
or nonsimple graph, or an arbitrary matroid.

I recomputed the canonical snapshot digest and every listed file hash.  All
match `audit/snapshot.json`.  In particular, the immutable `source.md` retains
SHA-256
`d197b76f2478dc8bab3245b76621f36d9552d19c75502e0a19cfd41a7bd8077d`.

## Reconstruction of the decisive mathematics

For a graph $G=(V,E)$, a flat can be described independently of an
edge-subset closure routine.  If the connected components of $(V,X)$ form a
partition $\pi$ of $V$, flatness says that $X$ contains every graph edge
internal to a block of $\pi$.  Conversely, if every block of $\pi$ induces a
connected subgraph of $G$, the set of all graph edges internal to its blocks
has exactly those components and is a flat.  Thus graphic flats are in
bijection with partitions into connected induced blocks, and their rank is
$|V|$ minus the number of blocks.  This gives a second flat model, not a
rephrasing of the candidate's exhaustive edge-subset fixed-point test.

For adjacent flat ranks, proper inclusion is the cover relation.  In a simple
graphic matroid the atoms are precisely the edges.  If $X\lessdot Y$, then
$X\vee e=Y$ exactly for $e\in Y\setminus X$.  Hence Sinclair's quantities
specialize to

\[
  m(X,Y)=|Y\setminus X|,\qquad
  s(X)=|E\setminus X|.
\]

The matrices audited therefore have entries

\[
 (L_e)_{X,Y}=\mathbf 1_{e\in Y\setminus X},\qquad
 D_{X,Y}=r(Y)\frac{|Y\setminus X|}{|E\setminus X|},
\]

precisely as frozen.  The denominator cannot vanish: a lower member of a
cover is not the top flat.  Starting with the one-dimensional top-flat space,
concatenating the images under these matrices and taking their exact column
span is exactly the recurrence defining $C_{j+1}$.  Induction down the flat
rank therefore proves that the resulting exact ranks are the coefficients of
$H_M$.  Attaching a new vertex by one pendant edge creates a bridge, hence a
coloop, and its cycle matroid is $M(G)\oplus U_{1,1}$; the extension was
computed afresh rather than inferred from a direct-sum formula.

The source normalization also matches.  In the rescaled basis
$g_X=\beta_Xe_X$, the source's top generator $v_r$ is $g_E$, and its
cyclic grading is the same word-length recurrence.  All matrices here have
rational entries, so their ranks over $\mathbb Q$ equal their ranks after
scalar extension to $\mathbb R$.

## Checks actually performed

I inspected `evidence/independent_subset_check.py` in full.  Its closure,
rank, cover, $L_e$, $D$, recursive-span, and pendant-edge implementations
match the displayed definitions.  Its graph canonicalization genuinely ranges
over all vertex permutations, and its Gaussian elimination uses
`fractions.Fraction`; no floating-point or modular rank is used for a claimed
rational rank.

I then wrote and ran `audit/referee_verify.py`, a fresh checker using the
connected-partition flat description above and SymPy 1.14.0 exact rational
column spaces.  It reads the frozen census with SHA-256
`bdf7220c271156dc2a8526facab718bc6d24d982f5d10a54e4aa2db6f24834a3`.
Its detailed result is `audit/referee_replay.json`, SHA-256
`fb608cdad07cf2daa2ea84a2c37367f215f2683f932c1f672dfc84cc4f05a805`.
The replay established all of the following.

- Exhausting all labeled edge masks and independently minimizing adjacency
  words under permutations gives respectively $(1,1,2,6,21)$ connected
  isomorphism classes in orders $(1,2,3,4,5)$, covering respectively
  $(1,1,4,38,728)$ connected labeled graphs.  Thus the 31 census rows cover
  every graph in the quantified domain exactly once up to isomorphism.
- For every one of the 31 graphs and every one of its 31 pendant-edge
  extensions, the independently generated flat layers equal the serialized
  layers.  Every one of the 62 serialized exact cyclic-space bases is linearly
  independent and spans the independently recomputed cyclic space in every
  degree.
- A separate execution of the candidate program regenerated all 62
  certificates exactly, not merely their dimensions.  Repeating the fresh
  replay with a different `PYTHONHASHSEED` reproduced its JSON byte for byte.
- The one-vertex empty-edge case yields $H_M=1$, its coloop extension yields
  $H_{M^+}=1+q$, and no undefined denominator or empty-domain exception is
  hidden there.

The only nonzero rows found were exactly

| complement components | $H_M$ | $H_{M^+}$ | $\Delta$ |
|---|---|---|---|
| $P_5$ | $(1,6,11,6,1)$ | $(1,7,19,19,7,1)$ | $2q^2+2q^3$ |
| $P_4\sqcup P_1$ | $(1,7,13,7,1)$ | $(1,8,22,22,8,1)$ | $2q^2+2q^3$ |
| $P_3\sqcup P_2$ | $(1,8,15,7,1)$ | $(1,9,25,24,8,1)$ | $2q^2+2q^3$ |
| $P_3\sqcup2P_1$ | $(1,9,16,8,1)$ | $(1,10,26,26,9,1)$ | $q^2+2q^3$ |
| $2P_2\sqcup P_1$ | $(1,9,20,8,1)$ | $(1,10,33,28,9,1)$ | $4q^2$ |
| $P_2\sqcup3P_1$ | $(1,10,22,9,1)$ | $(1,11,36,31,10,1)$ | $4q^2$ |
| $5P_1$ | $(1,11,25,10,1)$ | $(1,12,40,35,11,1)$ | $4q^2$ |

Every order-at-most-four row has zero difference.  At order five, a linear
forest is uniquely specified up to isomorphism by the partition of five given
by its path-component sizes, and the seven partitions in the table exhaust
them.  The fresh computation independently checked both directions of the
claimed equivalence, not just the seven positive cases.

Among linear forests on five vertices, only $P_5$ has four edges.  Therefore
its complement is the unique six-edge failure and every other failure has at
least seven edges.  The six-edge representative is independently isomorphic
to the graph consisting of paths $0-1$, $0-2-1$, and $0-3-4-1$, proving
the stated $\Theta(1,2,3)$ identification.  Its two Hilbert vectors are exactly the
ones frozen in the claim.

## Source comparison and contribution

I checked Thomas Sinclair's
[arXiv:2608.18519v1](https://arxiv.org/html/2608.18519v1) directly.
Proposition 2.4 gives
the rescaled flat-cover formulas used above; Example 3.2 gives
$H_{\beta,M(K_5)}=(1,11,25,10,1)$, agreeing with the complete-graph census
row; and Question 6.3 asks about direct sum and other operations while warning
that simple formulas fail.  The paper does not state this order-at-most-five
classification.  A bounded arXiv search found no equivalent classification,
but neither this report nor the candidate treats that search as proof of
priority.  The honest contribution is the exact complete solution of the
frozen finite problem, not a solution of Sinclair's general question.

## Gaps and verdict

I found no mathematical or scope gap in the frozen candidate.  Bibliographic
polish and final citation checking remain tasks for the later manuscript and
release phases; they do not alter the mathematical verdict.  The exact frozen
scope, correctness/evidence, and stated bounded contribution pass.

**Final verdict: accept.**
