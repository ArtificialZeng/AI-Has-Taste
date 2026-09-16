# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the `result-note` claim bound to snapshot
`af0e3966bb0ff42fb5bbe70dab0d4cbcf76dff1ef54d58d225f4bdfe1d4bf3b7`.
The claim is deliberately partial: it asserts a valid ordinary red--blue edge
coloring of `KG(11,3)`, derives `R_3^KG(3,3) >= 12`, and leaves the original
exact-value problem unresolved between 12 and 13. I find that exact frozen
scope correct and the contribution nontrivial. **Verdict: accept.**

## Reconstruction of the decisive argument

The vertices of `KG(11,3)` are the `binom(11,3)=165` triples in `[11]`.
Each vertex is disjoint from `binom(8,3)=56` other vertices, so the graph has

```text
binom(11,3) binom(8,3) / 2 = 4,620
```

unordered edges. A graph triangle is exactly an unordered partition of some
nine-element subset of `[11]` into three triples. Hence there are

```text
binom(11,9) * 9! / ((3!)^3 3!) = 55 * 280 = 15,400
```

triangles. Thus it is sufficient to check that the witness assigns one of
`R,B` to every one of the 4,620 edges exactly once and that none of these
15,400 partitions has three equally colored joining edges.

I wrote `audit/referee_verify.py` without importing or reusing the submitted
checker. It parses the witness into bit-mask endpoints, generates every edge
once by first choosing its six-point union and then the unique side containing
the least point, and generates every triangle once by choosing its nine-point
union and canonically selecting the block containing the least remaining point
at each of two stages. This is a different enumeration from the submitted
checker, which loops over pairs and triples of all graph vertices.

The fresh verifier found exactly 4,620 distinct valid edges, equal as a set to
the independently generated edge set. There are 2,308 red and 2,312 blue
edges. It enumerated exactly 15,400 triangles: 7,720 contain one red edge and
two blue edges, while 7,680 contain two red edges and one blue edge. In
particular, there are zero all-red and zero all-blue triangles. The witness
SHA-256 was
`1ac9c2c19d8bdcf54adeb53ce1808233eb9b690e787debe33fa388da10aa9f01`,
matching the frozen snapshot. Negative controls confirmed that the verifier
rejects a deleted edge and detects a triangle whose three edges are forcibly
made red. The exact output is preserved in
`audit/referee_verification.log`.

As a second check, I ran the frozen `evidence/check_n11_coloring.py`. It also
reported 4,620 covered edges, 15,400 checked triangles, no monochromatic
triangle, and the same witness hash.

Consequently the witness is a total ordinary two-coloring witnessing
`not P(11)`. Monotonicity is in the correct direction: if `P(m)` held for some
`m <= 11`, restricting any coloring of `KG(11,3)` to the induced `KG(m,3)`
would imply `P(11)`. Therefore `not P(11)` implies the Kneser Ramsey number is
strictly larger than 11, i.e. `R_3^KG(3,3) >= 12`. No cover-coloring or
fractional-chromatic assumption is used.

## Source comparison and contribution

The cited primary sources match the stated boundary. Heath--McCourt--Parker--
Schwieder--Zerbib, arXiv:2510.25734v2, Definition 1 uses the same ordinary
red--blue edge-coloring definition; Theorem 11 gives
`R_r^KG(3,3) >= 3r+2`, which is 11 at `r=3`, and Theorem 12 gives the upper
bound 13. Its SAT section uses the same two clauses per triangle and records
the `KG(13,3)` computation, not a decision at 11 or 12.

Gujgiczer--Marits--Ozeki, arXiv:2607.12353v1, Section 4 explicitly says that
two-triangle-free-graph coverability of `KG(11,3)` and `KG(12,3)` remained
unresolved after the known positive case at 10 and negative case at 13. Its
separate question about covers by two 2.5-colorable graphs is stronger and is
not being substituted here. A fresh arXiv search on 2026-09-10 using the paper
identifiers and the exact `KG(11,3)`/`KG(12,3)` terms did not surface a later
primary resolution; this remains a bounded freshness screen, not a priority
guarantee.

The construction therefore settles one of the two directly adjacent finite
cases identified in the prior literature and improves the published lower
bound from 11 to 12. Its immediate use is to narrow the original exact value
from `{11,12,13}` to `{12,13}`. This is neither a routine restatement nor an
arbitrary toy restriction, and it satisfies the contribution threshold for a
`result-note`.

## Remaining limitation

Nothing in the witness decides `P(12)`. The exact original problem remains
unresolved, exactly as `claim.json` says. Deciding `KG(12,3)` would require a
separately checked full coloring or a replayable UNSAT certificate and is not a
condition for accepting this frozen partial-result scope.
