# Fixed AGL(1,29) H15-orientation decision problem

## Frozen labelled base

Let `B` be the labelled graph encoded by the single graph6 record
`agl_29_g14.g6` in `../../batches/literature/bigMac-19/supplement.zip`.
The deposited parser and an independent replay establish that `B` is simple,
connected, cubic, and has 812 vertices, 1,218 edges, and girth 14.  The
archive, member, and replay digests are recorded in
`evidence/triage_recovery.md`; labels are not to be silently relabelled when
publishing a certificate.

## Exact quantified statement

For every vertex `v`, choose exactly one neighbour `u(v) in N_B(v)`.  For a
simple cycle `C` of `B`, define

```
a_u(C) = #{v in V(C) : {v,u(v)} is an edge of C}.
```

Decide whether there exists a map `u` satisfying

```
a_u(C) <= 3*ell-33
```

for every simple cycle `C` of every length `ell in {14,15,16}`.  Thus the
three explicit capacities are 9, 12, and 15.  Because `B` is cubic, each
vertex has exactly three possible choices.  The two cycle edges incident to
a cycle vertex both count as selecting a cycle edge, but the vertex itself is
counted only once.

## Scope of either outcome

- A positive answer requires a complete 812-entry neighbour-choice table,
  its hash, and a deterministic exhaustive check against a canonical census
  of every 14-, 15-, and 16-cycle of this exact labelled graph.
- A negative answer requires a direct encoding whose semantics are audited,
  a proof-producing UNSAT run, and an independently checked proof.  Solver
  exit status or an unchecked log is not a certificate.
- SAT yields the H15 expansion claimed for this fixed base (and hence the
  corresponding finite upper bound after the published window argument is
  checked).  UNSAT excludes only this fixed base/orientation construction.
  Neither outcome by itself settles all H15 bases or the general power-of-two
  cycle problem.

## Nearest primary evidence and novelty boundary

The intake source is Daniel Garcia, arXiv:2609.04686v1, Definition 3.1,
Lemma 3.2, Lemma 5.2, and the AGL search in Section 5, together with the
formal data deposit DOI `10.5281/zenodo.22180583`.  That version reports the
`p=29` instance as surviving the counting obstruction but unresolved after
its bounded computation.  This establishes the historical starting point,
not a claim about all later literature.  Any manuscript candidate must repeat
a current primary-source search and distinguish a new exact certificate from
the deposited scripts.

## Cheapest decisive test

Use the supplied graph6 parser and a separately implemented deterministic
cycle enumerator to canonicalize every simple 14--16 cycle.  Encode one
three-way choice per vertex and the three capacity families directly in
DIMACS for the available native CaDiCaL/Kissat executables.  Retain the cycle
census and either a fully rechecked assignment or a checker-accepted UNSAT
proof.  Optional PySAT, Z3, and NetworkX packages are not prerequisites.
