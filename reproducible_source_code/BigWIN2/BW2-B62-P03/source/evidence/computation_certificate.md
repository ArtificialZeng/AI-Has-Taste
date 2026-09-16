# Exact dual-verifier computation certificate

## Submitted finite result

For the graph and distance conventions frozen in `source.md`, the exact values
are

| n | vertices | edges | Sort_n | D_n |
|---:|---:|---:|---:|---:|
| 6 | 120 | 300 | 6 | 7 |
| 7 | 720 | 2,160 | 10 | 10 |
| 8 | 5,040 | 17,640 | 13 | 14 |

Verifier A's lexicographically selected sorting witnesses are
`(1,5,4,3,2,6)`, `(1,6,5,4,3,2,7)`, and
`(1,7,6,4,5,3,2,8)`. Its selected diameter pairs are respectively

- `((1,2,3,5,6,4),(1,5,3,4,2,6))`;
- `((1,2,3,4,5,6,7),(1,6,5,4,3,2,7))`;
- `((1,2,3,4,7,8,5,6),(1,8,5,4,2,7,6,3))`.

Each output JSON contains a shortest generator sequence and every intermediate
vertex for both its sorting witness and its diameter witness. Verifier B also
constructs shortest paths, generally different ones because it scans generators
in numerical order, and serializes every intermediate vertex both as a cycle
word and as a one-line map.

## Why the searches are exhaustive

Verifier A enumerates all `(n-1)!` canonical cycle words `(1,a2,...,an)`.
Verifier B instead enumerates all `n!` one-line permutation maps and retains a
map precisely when the orbit of label 1 first returns after `n` steps. Thus its
retained maps are exactly the full cycles, again `(n-1)!` vertices.

A constructs a neighbor by swapping the two labels in a cycle word. B never
uses that operation to construct an edge: it builds the one-line map for
`s_i=(i,i+1)` and calculates `compose(s_i,compose(p,s_i))`. Both implementations
check that every vertex has `n-1` distinct nonloop neighbors, every labeled edge
reverses under the same generator, the root reaches all vertices, and the edge
counts are those in the table.

Each verifier performs an unweighted BFS from every retained vertex. Therefore
every entry in the full ordered distance matrix is computed exactly. Taking the
maximum of a root row gives `Sort_n`; taking the maximum of all rows gives
`D_n`. The complete histograms (including distance zero) are:

- n=6 root: `0:1, 1:5, 2:14, 3:27, 4:36, 5:28, 6:9`; all ordered pairs:
  `0:120, 1:600, 2:1620, 3:3134, 4:4268, 5:3424, 6:1162, 7:72`.
- n=7 root: `0:1, 1:6, 2:20, 3:48, 4:91, 5:140, 6:169, 7:146, 8:78,
  9:20, 10:1`; all ordered pairs: `0:720, 1:4320, 2:14400, 3:34962,
  4:67284, 5:103662, 6:123828, 7:103614, 8:51852, 9:12642, 10:1116`.
- n=8 root: `0:1, 1:7, 2:27, 3:76, 4:172, 5:329, 6:544, 7:784,
  8:970, 9:978, 10:729, 11:344, 12:77, 13:2`; all ordered pairs:
  `0:5040, 1:35280, 2:135936, 3:381656, 4:866404, 5:1676632,
  6:2826516, 7:4131396, 8:5081316, 9:4973336, 10:3461236,
  11:1486704, 12:319284, 13:20784, 14:80`.

## Independent agreement and replay

After its own computation, B compares with A. For every `n`, it reports true
for counts, both full histograms, both extrema, the selected witnesses, and all
three comparable SHA-256 streams (canonical vertices, canonical undirected
edges, and the entire ordered distance matrix). B additionally parses and
replays every A witness edge by direct map composition and independently checks
that each reported length is the endpoint distance. All flags are true in
`verifier_b_n6.json`, `verifier_b_n7.json`, and `verifier_b_n8.json`.

Replay from the project root:

```sh
for n in 6 7 8; do
  python3 evidence/verifier_a.py --n "$n" --output "evidence/verifier_a_n${n}.json"
  python3 evidence/verifier_b.py --n "$n" --compare-a "evidence/verifier_a_n${n}.json" --output "evidence/verifier_b_n${n}.json"
done
```

The recorded runs used CPython 3.10.12 and only the Python standard library.
Clean B reruns on all three orders were byte-identical. The local primary-source
PDF hash is `de5de1f1ddaec97f2f0bc784107c8f9fb27787242e459cd5b3387b34dfc3aa9b`,
matching `source.md`.

## Scope

The sorting values reproduce the primary paper's stated finite experiments;
the package adds independently replayable exhaustive certificates and computes
the requested diameters. No priority claim is made for the diameter values.
Nothing here proves or disproves either asymptotic Conjecture 7.1 or unimodality
Conjecture 7.2. The known mathematical gap list for the frozen finite claim is
empty; independent referee review of the code, argument, and scope remains the
next process gate.
