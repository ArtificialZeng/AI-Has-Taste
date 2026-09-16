# Fresh mathematical audit

Job: `win-00036-p03-referee-eab04a7975f0`

Snapshot: `2b54434d20656f9511376a1186995ead57dc07fdd11a3ecac8a2ab78d0d32e67`

Verdict: **accept** the exact frozen `resolution-paper` claim. The supplied
certificate proves that no 42-column witness exists for any `x <= 529`, hence
`L_42 >= 530` and the original assertion `L_42 = 529` is false.

## Frozen scope and integrity

I reviewed the statement in `source.md`, its interpretation in `problem.md`,
`claim.json`, `audit/snapshot.json`, and every evidence file enumerated by the
claim. The SHA-256 digest of each frozen file agrees with the snapshot. I also
recomputed the snapshot digest as the SHA-256 of its sorted compact JSON file
map and obtained the bound digest above. The immutable source still has SHA-256
`377a023c95e7cab2168d3560250420b87ae89ebd1e1c8f0bfe0ec83831669a09`.

The frozen claim has full, rather than subsidiary, scope: it excludes the
existential witness at the endpoint 529 and explains why this excludes every
smaller endpoint as well. It does not rely on, or claim to verify, the supplied
but locally inaccessible report that `L_41 = 529`. No priority claim is made.
That access limitation therefore creates no gap in this disproof.

## Reconstruction of the proof

For a nonempty `V` at `x = 529`, the endpoint condition gives
`1 <= d <= 527`. If `d` is odd, each pair `(v,v+d)` contains exactly one even
integer. The 42 columns would therefore contain 42 even entries. They are
distinct by hypothesis, but any two have gcd at least 2, contradicting
pairwise coprimality. Thus only the 263 gaps `d = 2,4,...,526` remain.

Fix one of these even gaps. Let

`C_d = {v in {2,...,529-d} : gcd(v,v+d)=1}`.

Make distinct starts adjacent exactly when their four displayed entries are
distinct and pairwise coprime. A valid 42-element start set is then precisely
a 42-clique: the vertex condition checks coprimality within each column, and
adjacency checks distinctness and all cross-column gcd conditions.

For every one of the 263 gaps, the frozen JSON contains the entire recomputed
vertex set and a coloring. Exhaustive exact checks establish that each coloring
is proper and uses at most 41 distinct colors. Every clique in a proper coloring
has differently colored vertices, so each graph has clique number at most 41.
Hence no admissible gap supports 42 columns at `x = 529`.

Finally, any witness at an integer endpoint `x <= 529` would have
`V subseteq {2,...,x-d} subseteq {2,...,529-d}` and so would also be a witness
at endpoint 529. Therefore no witness exists for any `x <= 529`; by the
definition of `L_42`, this is exactly `L_42 >= 530`.

## Checks performed

I ran both frozen verification programs. The small verifier confirmed the
canonical payload hash
`891877322b99abeb51b5fe38f883ce73625c8cb6017b69a58193e85188b60673`,
all 263 gaps, and all 147,843 same-color pairs. The full verifier independently
reconstructed 955,648 compatible edges and reported no failures; the maximum
recorded color count is 41 and occurs only for `d = 42`.

I additionally performed a fresh check without importing either supplied
program. It parsed the serialized certificate, recomputed every vertex set from
the inclusive endpoint and internal gcd predicate, reconstructed adjacency
directly from entry distinctness and four cross-gcd tests (the two internal gcds
having already been checked), and required unequal colors on every reconstructed
edge. This independently reproduced 263 gaps, 28,231 vertices, 955,648 edges,
147,843 same-color pairs, and maximum 41 distinct colors, again only at gap 42.
All arithmetic was exact integer arithmetic using Euclid's gcd implementation;
there are no floating-point, solver-status, or timeout inferences.

I also checked the likely boundary failures: empty endpoint ranges, `d > 527`,
odd gaps, collisions of the form `v+d=w`, incomplete vertex enumeration,
internal column gcds, cross-column gcds, and the passage from endpoint 529 to
all smaller endpoints. None leaves an uncovered case.

## Gaps and decision

No mathematical gap remains in the frozen scope. A proper coloring is a direct
finite upper-bound certificate, not a heuristic coloring claim, and its full
coverage and correctness were recomputed. The exact frozen disproof is therefore
accepted. Any later substantive change to the statement or decisive evidence
requires a new snapshot and fresh review.
