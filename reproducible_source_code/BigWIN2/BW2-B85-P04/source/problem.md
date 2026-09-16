# Precise problem reading

Provenance: `win-00085-p04-triage-e1da8dce0130`  
Frozen source: `source.md`  
Frozen-source SHA-256:
`fb5e568a92eb4fbe8628c4d9335211fc74eb7a97bafb597d0558b7d9305d38cf`

## Objects and quantifiers

For an integer `n >= 6`, put `[n] = {1,...,n}` and

```text
V_n = {A subseteq [n] : |A| = 3},
E_n = {{A,B} subseteq V_n : A intersection B is empty}.
```

The simple graph `(V_n,E_n)` is `KG(n,3)`. An ordinary red-blue edge
coloring is a total map

```text
c : E_n -> {R,B}.
```

A triangle consists of three distinct vertices `A,B,C in V_n` that are
pairwise disjoint. It is monochromatic when, for some `q in {R,B}`,

```text
c({A,B}) = c({A,C}) = c({B,C}) = q.
```

Define `P(n)` to be the quantified statement

```text
for every c:E_n->{R,B}, there exist pairwise-disjoint A,B,C in V_n
whose three joining edges all have one common color.
```

Then

```text
R_3^KG(3,3) = min {n >= 6 : P(n)}.
```

The property is monotone in `n`, since `KG(n,3)` is the subgraph of
`KG(n+1,3)` induced by triples contained in `[n]`. Triangles cannot occur
for `n < 9`; the cited upper bound `P(13)` makes the displayed minimum
well-defined. The frozen question asks for the unique exact value among
`11, 12, 13`—not merely another bound.

## Equivalent formulations

The two color classes of a coloring are two triangle-free spanning
subgraphs whose edge sets partition `E_n`. Conversely, if two triangle-free
spanning subgraphs cover `E_n` (overlap is allowed), assigning each edge to
one covering subgraph that contains it produces such a coloring. Thus `not
P(n)` is equivalent to coverability by two triangle-free spanning
subgraphs.

This does **not** require either covering graph to have fractional chromatic
number at most `5/2`; that is the stronger “2.5-colorable” condition studied
separately by Gujgiczer--Marits--Ozeki. It also is not a vertex coloring or a
coloring of the underlying 3-uniform hyperedges.

## Finite decision instances

Give each edge `e` a Boolean variable `x_e`, with true meaning red. For every
triangle with edges `e_1,e_2,e_3`, impose

```text
(x_e1 or x_e2 or x_e3) and
(not x_e1 or not x_e2 or not x_e3).
```

The resulting CNF is satisfiable exactly when `not P(n)`. Direct counting
gives:

| `n` | vertices | edge variables | triangles | CNF clauses |
|---:|---:|---:|---:|---:|
| 11 | 165 | 4,620 | 15,400 | 30,800 |
| 12 | 220 | 9,240 | 61,600 | 123,200 |

Here the triangle count is
`binom(n,9) * 9! / ((3!)^3 3!) = 280 binom(n,9)`.

## Current normalization and surviving target

Source-status classification: **open-supported** at the cited July 2026
primary source; research suitability: **advance** after the exact local
`n=11` witness reduced the remaining decision to one finite instance.

Heath--McCourt--Parker--Schwieder--Zerbib prove
`11 <= R_3^KG(3,3) <= 13`. Gujgiczer--Marits--Ozeki explicitly report the
ordinary triangle-free-cover cases `KG(11,3)` and `KG(12,3)` unresolved in
July 2026. The exact project witness `evidence/n11_coloring.txt`, replayed by
`evidence/check_n11_coloring.py`, establishes `not P(11)`. Hence the local
evidence narrows the frozen problem to

```text
R_3^KG(3,3) in {12,13}.
```

The research target is therefore: nearest prior result `11 <= R <= 13` and
the checked `n=11` witness; proposed delta, decide `P(12)`; verification
route, either a complete `n=12` coloring exhaustively checked against every
edge and triangle (giving `R=13`), or a proof-producing UNSAT run whose
standard certificate is independently replayed (giving `R=12`). A bare
solver status is not a mathematical resolution.

## Scope

The uniformity is exactly 3, there are exactly two edge colors, and the
forbidden monochromatic clique is exactly a triangle. Changing any of these,
or replacing triangle-free by 2.5-colorable, is outside the frozen problem.
