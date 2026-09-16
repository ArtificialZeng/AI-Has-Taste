# Research-pass-2 validation

## Independent cubical implementation

`evidence/pass2_independent_check.py` is a second implementation and does not
import `evidence/anchored_cubical.py`.  It enumerates cells by iterating over
the complete vertex/edge factor alphabet, rather than first choosing edge
positions.  It independently constructs signed faces, checks the square of
the boundary, and row-reduces sparse matrices over finite fields.  For two
anchors it also constructs the compatibility nerve directly from all subsets
of injections and computes its simplicial boundary matrices.

The exact command

```sh
python3 evidence/pass2_independent_check.py
```

completed with `all_checks_passed: true`.  The script SHA-256 is
`2f403a8d5660f4b845560df35dd9c7f088fb0b022e408f741bceb0931a10e6c9`.
It exhaustively covered every connected labelled simple graph on at most four
vertices (the graph counts by order were 1, 1, 4, and 38), as follows:

- all 167 graph/one-anchor pairs at (n=3);
- all 241 graph/two-anchor pairs at (n=4).

For every case, independently enumerated cell counts agreed with the
inclusion-exclusion formula

\[
 \#C_d=\binom nd |E|^d
   \sum_{a=0}^{|K|}(-1)^a\binom{|K|}{a}(|V|-a)^{n-d},
\]

and every integral boundary satisfied (\partial^2=0).  Betti numbers over
(\mathbb F_2), (\mathbb F_3), and (\mathbb F_5) agreed in every degree with
the decomposition in `evidence/torsion_free_proof.md`.  The largest chain
groups encountered were ((37,126,108)) for one anchor and
((110,432,432)) for two anchors.

For the independently generated compatibility nerves (N_{2,m}), the cell
counts and field Betti numbers, identical over all three primes, were

| (m) | cell counts | Betti numbers |
|---:|---:|---:|
| 2 | ((2)) | ((2)) |
| 3 | ((6,6)) | ((1,1)) |
| 4 | ((12,36,32,6)) | ((1,0,1,0)) |

These agree with the homotopy types prescribed by Kozlov's Theorem 2.5.

## Reinspection of the proof dependency and exact Smith cases

The open-access publisher text of Dmitry N. Kozlov, *Stirling complexes*,
DOI `10.1007/s41468-022-00096-4`, was re-inspected on 2026-09-08.
Definition 2.4 defines exactly the anchored subcomplex for an arbitrary vertex
subset of a tree, and Theorem 2.5 states that it is homotopy equivalent to a
wedge of spheres of dimension (n-|K|).  Thus the proof's use of this theorem
does not silently assume that every tree vertex is anchored.

The earlier exact reproducer was also rerun on the two most symmetric cases.
For ((K_4,\{0\},3)), the integral cycle-coordinate Smith diagonal was
(1^{81}) in shape (90\times108), giving Betti ranks ((1,9,27)).  For
((K_4,\{0,1\},4)), it was (1^{311}) in shape (323\times432), giving
((1,12,121)).  The boundary ranks were unchanged over primes
(2,3,5,7,101).  These reruns agree with `evidence/computation.md`.

## Scope of this evidence

This finite computation cannot prove universal torsion-freeness.  Its role is
to test the exact cell convention, orientations, the two smallest nontrivial
anchor excesses, and the rank consequences of the proposed global chain
decomposition.  The universal conclusion rests on the complete argument in
`evidence/torsion_free_proof.md`, which still requires a fresh referee audit.
