# Exact finite proof certificate

## Claim proved

For every four-element subset \(S\subset \mathbb F_3^2\), there is an
injection \(f:S\to \mathbb F_3^2\setminus S\) whose four cross edges have
the four distinct unoriented nonzero directions.  By the equivalence recorded
in `problem.md`, this is exactly the affirmative answer to the immutable
statement in `source.md`.

## Completeness reduction

The universe is ordered as
\((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)\).
Every unordered \(4+5\) partition has a unique four-element part, so
`itertools.combinations(G, 4)` lists the full domain exactly once and has
size \(\binom94=126\).  After ordering the four elements of \(S\), every
injection from \(S\) into its five-element complement is uniquely represented
by a length-four permutation of the complement.  There are
\(5\cdot4\cdot3\cdot2=120\) such permutations.

For an edge \(\{a,b\}\), the search computes \(d=a-b\) componentwise modulo
3 and assigns it to exactly one of
\[
 \{\pm(1,0)\},\quad \{\pm(0,1)\},\quad
 \{\pm(1,1)\},\quad \{\pm(1,2)\}.
\]
The bit mask is 15 precisely when all four direction classes occur.  Since
there are four edges, this is equivalent to each class occurring exactly once.
All arithmetic and all comparisons are exact integers.

## Exhaustive result

`exhaustive_search.py` checked all \(126\cdot120=15120\) injections and emitted
`exhaustive_certificate.json`.  It found at least one valid injection for each
of the 126 subsets and serialized one such witness per subset.  As a redundant
exact statistic, 54 subsets have 8 valid injections and 72 subsets have 12;
thus the minimum is 8 and no subset fails.

## Independent check

`independent_verify.py` does not import the search implementation.  It rebuilds
the nine points and all 126 combinations, represents a direction instead by
the lexicographically smaller of \(d\) and \(-d\), checks the partition and
injection conditions for every serialized witness, and independently
re-enumerates all 15,120 injections.  Its frozen report
`independent_verification.json` records `verification: pass`, all 126 witnesses
verified, and the same 54/72 count distribution.  The certificate SHA-256 is
`cf3589e80b12bdf59e737e073cb690a0f01d99fb9ba4b6b4e2258c18f73d449e`.

## Reproduction

From the project directory, with the mandated interpreter:

```sh
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python \
  evidence/exhaustive_search.py --output evidence/exhaustive_certificate.json
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python \
  evidence/independent_verify.py evidence/exhaustive_certificate.json \
  --report evidence/independent_verification.json
```

The conclusion is a finite computer-assisted proof, not a claimed structural
proof or a claim about any larger group.
