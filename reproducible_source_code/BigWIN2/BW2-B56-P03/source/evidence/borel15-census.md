# Exact colength-15 Borel census

Computation date: 2026-09-07.  This is exact finite evidence; it does not
compute tangent-space dimensions and therefore does not resolve the frozen
maximum problem.

## Result

There are 6,879 coordinatewise downsets of cardinality 15 in
\(\mathbb N^3\).  Exactly 107 satisfy the standard-set form of strong
stability for \(x<y<z\).  Their counts by the least pure-power exponent are

| \(m_1\) | generator A | generator B |
|---:|---:|---:|
| 1 | 27 | 27 |
| 2 | 69 | 69 |
| 3 | 11 | 11 |

The two generators produced identical sets of all 107 canonical standard
monomial lists (zero keys occurred in either set difference), rather than
merely identical totals.

The canonical atlas is `borel-atlas-15.jsonl`.  It contains one compact JSON
record per ideal, sorted first by \((m_1,m_2,m_3)\) and then by the graded-lex
standard-monomial list.  Each record contains the 15 exponent triples, the
minimal monomial generators, the pure-power tuple, and an identifier derived
from its standard-set key.  Its exact byte length is 27,844 and its SHA-256 is

```
d8ffe256af56d0a66128b88d4eb16c995745f897369bf3d0d5973c4a6c20db6f
```

The literature candidate \(I_*\) from `problem.md` occurs uniquely as atlas
record `ddf69a6eddf5b96d`, with \(m=(3,3,6)\) and precisely the ten stated
minimal generators (written as exponent triples).

## Completeness arguments for the two enumerations

Generator A starts at the empty set and, at each cardinality, adds every outer
corner: a point outside the current set whose three applicable immediate
coordinate predecessors are already present.  Induction on cardinality shows
that every set reached is a downset.  Conversely, every nonempty finite
downset has a coordinatewise maximal element whose deletion remains a
downset, so reversing such deletions proves that every 15-element downset is
reached.  Frozenset deduplication makes the output a set of canonical shapes.
It then retains exactly those sets closed under

\[
(a,b,c)\mapsto(a-1,b+1,c),\quad(a-1,b,c+1),\quad(a,b-1,c+1)
\]

whenever the decreased coordinate is positive.  This is the strong-stability
criterion for standard sets fixed in `problem.md`.

Generator B does not enumerate arbitrary downsets.  It forms, for each point
of total degree at most 14, the transitive closure forced jointly by immediate
coordinate predecessors and the three displayed right shifts.  Starting from
the empty set, it recursively takes unions with these one-point closures and
discards unions larger than 15.  Every reached set has both closure
properties.  Conversely, any closed target \(O\) is the union of the
one-point closures of its elements, and each such closure lies inside \(O\),
so the recursion reaches \(O\) without triggering the size prune.  The degree
bound is complete because a downset containing a point of total degree \(d\)
contains a coordinate chain of \(d+1\) distinct points; hence a 15-element
downset has \(d\le14\).

Minimal generators are recovered as the monomials outside a standard set for
which every applicable immediate predecessor is standard.  The script checks
cardinality, down-closure, all right shifts, minimal-generator boundary
conditions, and \(m_1\le m_2\le m_3\) for every atlas record before writing.

## Replay

From the project directory:

```
python3 evidence/enumerate_borel15.py
```

The machine-readable summary is `borel-census-15.json`.  A replay with
`PYTHONHASHSEED=1` into a temporary directory produced a byte-for-byte
identical atlas (`cmp` exit status 0), providing a deterministic-ordering
check.  The immutable `source.md` retained SHA-256
`488760e5c9a3b14b4faa7f66c512041b56bedb96e7241f36f63db3895fe5e996`.

## Remaining gap

No value of \(T(I)\) has been computed here.  The next decisive task is exact
rational/integer nullity computation for all 107 ideals, followed by an
independent tangent-space verification for every maximizer and the best
\(m_1\le2\) competitor.
