# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact nonexistence statement in `claim.json`, not a weakened
subsidiary statement.  The candidate says that the fixed labelled graph `B`
admits no incident-edge choice satisfying all length-14, length-15, and
length-16 capacities.  I independently rehashed all 16 files in
`audit/snapshot.json`; every file digest and the canonical snapshot digest
matched `3ac774183b824d2e691a0481a81677a129319bd9f0b0cb27bbdc6712048d40c5`.

## Reconstruction of the decisive argument

For a target cycle `C` of length `L`, let `a(C)` count its vertices whose
chosen edge is a cycle edge, and let `o(C)` count those whose chosen edge is
the third, noncycle edge.  Each checked cycle is chordless in the cubic graph,
so these alternatives partition its vertices and

```
o(C) = L - a(C) >= L - (3L - 33) = 33 - 2L.
```

For nonnegative integer cycle weights `w_C`, define `lambda(v,z)` as the sum
of the weights of cycles whose unique noncycle edge at `v` is `vz`.  Any
incident-edge choice `u` would therefore satisfy

```
sum_C w_C(33 - 2|C|)
 <= sum_C w_C o(C)
  = sum_v lambda(v,u(v))
 <= sum_v max_{z in N(v)} lambda(v,z).
```

The certificate has total weight `3,243,141` on length-14 cycles and `999`
on length-16 cycles.  Thus its required lower bound is

```
5(3,243,141) + 1(999) = 16,216,704.
```

Exact accumulation of all three possible contributions at every vertex gives

```
sum_v max_z lambda(v,z) = 15,153,552.
```

The required quantity exceeds the unconditional per-vertex upper bound by
`1,063,152`, a strict contradiction.  The maximization allows each vertex to
choose its best neighbour independently, exactly as the original function
does, so it introduces no unproved global consistency assumption.  Omitting
zero-weight constraints is harmless: a satisfying map would in particular
satisfy every positively weighted cycle constraint.

## Fresh exact checks

I first ran the listed incidence replay and reproduced the two totals and the
strict gap.  I then wrote a separate verifier,
`audit/referee-88e58f34133f-verify.py`, whose report is
`audit/referee-88e58f34133f-check.json`.  It uses only the frozen listed text
artifacts and does not import the candidate's checkers.  The verifier performed
the following checks.

- It parsed all 7,308 census rows, checked their lengths, simple vertex lists,
  canonical directions, ranges, and uniqueness, and obtained 2,030 cycles of
  length 14, none of length 15, and 5,278 of length 16.
- The union of the serialized cycle edges reconstructs a connected simple
  cubic graph on 812 labelled vertices with 1,218 edges.  An independent
  edge-deletion breadth-first computation gives girth 14.
- Independently encoding this reconstructed labelled graph in graph6, with
  the member's CRLF line ending, gives SHA-256
  `8b074cd755a5d1e1e6a1d09a7888173821372e6cdcd501cfd2baf1a34bfeb08e`,
  exactly the frozen graph-member digest.  Thus the cycles used in the proof
  are tied to the specified labelled base without reading an unlisted graph
  input during this review.
- For every census row, it checked the direct-instance requirement
  `33-2L`, the vertex order, the unique noncycle neighbour, and that the
  recorded choice index selects that neighbour in sorted adjacency order.
- It checked every certificate record against its stated census index,
  positivity, uniqueness, and metadata.  The 1,184 supported rows comprise
  1,172 length-14 cycles and 12 length-16 cycles.
- A fresh integer accumulation reproduced lower bound `16,216,704`, upper
  bound `15,153,552`, gap `1,063,152`, and per-vertex maxima ranging from
  `18,488` to `19,015`.

These checks also address the possible chord/"outside edge" ambiguity: every
supported cycle has exactly one neighbour outside its vertex set at each
cycle vertex.  The proof uses no division, limiting argument, floating-point
claim, census-completeness assumption, or solver status.  In particular, the
absence of length-15 cycles is not needed for the contradiction.

## Scope and contribution

The frozen source and the listed primary-source screen identify the nearest
result as arXiv:2609.04686v1, which reported this `p=29` instance unresolved.
The screen found no equivalent later exact certificate in its stated bounded
queries and explicitly disclaims exhaustive priority.  That is an honest
comparison: the result resolves the whole frozen decision problem and is not
a toy restriction, while it neither rules out other bases nor settles the
general `H15` route.  The exact certificate and compact elementary dual
argument are a nontrivial, independently checkable contribution suitable for
the claimed resolution-paper scope.  Any manuscript should preserve those
scope and literature limitations.

## Verdict

**ACCEPT.**  The exact frozen claim is disproved in its full stated scope.  I
found no mathematical or evidentiary gap requiring revision.
