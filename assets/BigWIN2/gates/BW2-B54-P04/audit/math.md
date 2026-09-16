# Independent mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: for every
finite simple undirected connected graph (G) with at least two vertices, using
the simultaneous-spread burning convention and the standard Roman domination
definition in `problem.md`,

\[
2b(G)-2\leq \gamma_R(G).
\]

The SHA-256 digests of `claim.json` and every enumerated evidence file agree
with `audit/snapshot.json`.  Its binding digest is
`0bdd32f78a41b705c07c5b8f089f95bd483fee68b14720f5f535593876b0c63f`.
The theorem is full-scope equivalent to the frozen source statement; there is
no restriction of graph order or graph class in the submitted claim.

## Reconstruction of the decisive argument

Let (f\colon V(G)\to\{0,1,2\}) be a minimum-weight Roman dominating function
that, among all minimum-weight functions, minimizes the number of vertices
labelled 1.  Write (V_i=f^{-1}(i)), (a=|V_2|), and (c=|V_1|).  Then
(\gamma_R(G)=2a+c).

The three reductions used in the submission are valid:

1. (V_1) is anticomplete to (V_2).  Relabelling a 1-vertex adjacent to a
   2-vertex by 0 would preserve Roman domination and lower the weight.
2. (V_1) is independent.  If adjacent (u,v\in V_1) existed, relabelling
   (u) by 2 and (v) by 0 would preserve the weight and Roman domination but
   reduce the number of 1-labels by two.  Old 0-vertices retain their old
   2-neighbours, while the newly labelled 0-vertex (v) is defended by (u).
3. (a\geq1).  If (a=0), Roman feasibility forces every vertex to have label
   1.  For any positive-degree vertex (v), assigning 2 to (v), 0 to all
   its neighbours, and 1 elsewhere has weight
   (n+1-\deg(v)\leq n).  Strict inequality contradicts minimum weight, and
   equality gives a minimum function with fewer 1-labels.  Connectedness and
   (n\geq2) ensure such (v) exists.

It follows that every (V_0)-vertex has distance at most one from (V_2).  A
(V_1)-vertex has a neighbour because the graph is connected and nontrivial;
that neighbour can lie in neither (V_1) nor (V_2), hence lies in (V_0)
and in turn has a 2-neighbour.  Thus every (V_1)-vertex has distance exactly
two from (V_2).

For the burning construction, in each of the first (a) rounds choose an
unburned member of (V_2) whenever one remains.  Such a choice is legal under
the frozen simultaneous-spread convention because unburnedness is tested
before that round's spread.  Each such round burns at least one previously
unburned member of (V_2); if none remains, all of (V_2) is already burned.
Consequently all of (V_2) is burned by the end of round (a).

The remaining timing is correct, including the off-by-one boundary:

- If (c=0), round (a+1) spreads from the already burned set (V_2) to all
  of (V_0), so (b(G)\leq a+1).
- If (c=1), in round (a+1) the sole 1-vertex is chosen if still unburned,
  while the same round's spread covers (V_0); hence (b(G)\leq a+1).
- If (c\geq2), rounds (a+1) and (a+2) propagate fire to distances one
  and two from (V_2), so (b(G)\leq a+2\leq a+\lfloor c/2\rfloor+1).

If the graph becomes completely burned before a contemplated source choice,
the already completed process supplies the stronger upper bound; no illegal
post-completion source is needed.  Thus in every case

\[
b(G)\leq a+\left\lfloor\frac c2\right\rfloor+1
=\left\lfloor\frac{\gamma_R(G)}2\right\rfloor+1,
\]

which is equivalent, by integrality, to the claimed inequality.  The proof
uses neither compactness nor a limiting step, performs no division by a
possibly zero parameter, and covers the boundary case (n=2) (in particular,
(K_2) gives equality).

## Checks performed

I reran both supplied exact scripts with Python 3 and NetworkX 3.4.2.  The
canonical-RDF checker again examined all 995 connected unlabeled graphs of
orders 2 through 7, found the case counts 548, 422, and 25 for (c=0), (c=1),
and (c\geq2), and verified every structural and burning-strategy assertion.
The independent optimum enumerator again examined the same 995 graphs, found
no counterexample, and reproduced all stored order-wise margins and equality
counts.  These computations are consistent sanity checks only; acceptance
rests on the universal argument above.

The exact survivor appears in
`evidence/external/survivors_by_touch_normalised.txt` with touch 2294.  The
supplied AutoGraphForge paper states that the static dataset contains every
connected graph of orders 2 through 9 and explicitly distinguishes survival
of finite counterexample search from a general theorem.  It also describes
many high-touch survivors as requiring mathematical triage.  I therefore use
that source only to confirm provenance and scope, not as proof.  The submitted
argument itself invokes no external mathematical theorem beyond the definitions
fixed in the frozen problem.  The claim also expressly avoids a literature
priority or open-status claim, so the bounded literature limitations recorded
in `problem.md` do not enlarge the mathematical assertion under review.

## Verdict

**Accept.**  The proof is self-contained, its source-selection process matches
the frozen simultaneous-spread convention, all graph and parameter hypotheses
are used correctly, and it establishes the exact universal resolution claim.
I found no unresolved mathematical gap or scope mismatch.
