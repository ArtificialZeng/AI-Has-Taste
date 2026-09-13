# Exact classification and certificate map

## Result for the frozen target

The regular ordinary distance-magic graphs on eight vertices are, up to
isomorphism,

\[
  8K_1,\qquad 2C_4,\qquad K_{4,4},\qquad K_{2,2,2,2}.
\]

In this order their reduced binary adjacency nullities are respectively
\(7,4,6,4\). Every value is at least two. By the exact equivalence frozen in
`problem.md`, every graph in the classification therefore admits a generating
\((\mathbb Z/2\mathbb Z)^3\)-magic map. Thus the frozen universal assertion is
true.

## Exhaustive table

Every integer in the table was computed exactly. `Ordinary labels` is the
number, among all \(8!=40320\) bijections to \(\{1,\ldots,8\}\), having the
required constant open-neighborhood sum. The rank and nullity refer to the
induced operator on \(\mathbb F_2^8/\langle\mathbf 1\rangle\).

| ID | degree | graph6 | ordinary labels | reduced rank | reduced nullity |
|---|---:|---|---:|---:|---:|
| d0-1 | 0 | `G?????` | 40320 | 0 | 7 |
| d2-1 | 2 | ``G?r@`_`` | 384 | 3 | 4 |
| d2-2 | 2 | ``G?qa`_`` | 0 | 5 | 2 |
| d2-3 | 2 | `GCQR@O` | 0 | 6 | 1 |
| d4-1 | 4 | `G?~vf_` | 4608 | 1 | 6 |
| d4-2 | 4 | `GCzvbo` | 0 | 3 | 4 |
| d4-3 | 4 | `GEnfbW` | 0 | 5 | 2 |
| d4-4 | 4 | `GEnbvG` | 0 | 6 | 1 |
| d4-5 | 4 | `GQzTrg` | 0 | 3 | 4 |
| d4-6 | 4 | `GQyurg` | 0 | 5 | 2 |
| d6-1 | 6 | `G]~v~w` | 384 | 3 | 4 |

The four positive rows are displayed by the stored adjacency matrices as
\(8K_1,2C_4,K_{4,4},K_{2,2,2,2}\), respectively. Witness label vectors by
vertices \(0,\ldots,7\), with their magic constants, are

| graph | witness | constant |
|---|---|---:|
| \(8K_1\) | `(1,2,3,4,5,6,7,8)` | 0 |
| \(2C_4\) | `(1,8,2,7,3,6,4,5)` | 9 |
| \(K_{4,4}\) | `(1,2,7,8,3,4,5,6)` | 18 |
| \(K_{2,2,2,2}\) | `(1,8,2,7,3,6,4,5)` | 27 |

## Completeness and exactness

Double-counting gives \(8c=36k\), so the regular degree \(k\) is even. Since
a simple eight-vertex graph has degree at most seven, only
\(k=0,2,4,6\) occur. Nauty's `geng -q -dK -DK 8` produced respectively
\(1,3,6,1\) representatives. The graph6 stream and executable hash are stored
in `order8_classification.json`.

Coverage was also checked without using `geng` for the population count.
`verify_unlabeled_coverage.py` enumerates all \(8!\) relabelings of each
representative, computes its canonical 28-bit adjacency code and automorphism
order, and independently counts all labeled regular graphs by a degree-sequence
recursion. The orbit-size sums and independent labeled counts agree:

| degree | orbit-size sum | independent labeled count |
|---:|---:|---:|
| 0 | 1 | 1 |
| 2 | 3507 | 3507 |
| 4 | 19355 | 19355 |
| 6 | 105 | 105 |

The canonical codes within each degree are distinct. Orbit-stabilizer and the
equal totals therefore certify that the eleven pairwise nonisomorphic classes
exhaust every labeled graph in all feasible degree cases.

For each representative, `enumerate_order8.py` tests every label permutation.
It represents the quotient using \([e_0],\ldots,[e_6]\); each image is
normalized to last coordinate zero. The JSON contains the resulting seven by
seven binary matrix, an elementary row-operation transcript, its RREF, and a
kernel basis. `verify_order8_certificate.py` independently obtains adjacency
matrices through nauty `showg`, repeats all 443520 labeling tests, recomputes
every binary rank by a separate elimination routine, checks every kernel
vector, and replays the stored row operations. Its report is `pass`. No
floating-point arithmetic is used.

Reproduction commands:

```sh
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python evidence/enumerate_order8.py
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python evidence/verify_order8_certificate.py
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python evidence/verify_unlabeled_coverage.py
```

The earlier limited literature screen did not find this exact classification,
but it did not establish novelty or priority. Those bibliographic questions
remain separate from the exact resolution of the frozen assertion.
