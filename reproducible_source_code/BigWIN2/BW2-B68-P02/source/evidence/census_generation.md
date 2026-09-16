# Canonical cubic census generation

Research job: `win-00068-p02-research-353357b39b59`, 2026-09-07.

## Generator and provenance

The executable `tools/nauty-root/geng` was relinked locally from seven cached
objects copied verbatim to `tools/nauty-objects/`. Debug strings in `geng.o`
name `../nauty2_8_9/geng.c` and `../nauty2_8_9/nauty.h`; thus the object records
nauty 2.8.9 as its source tree. The objects, executable, and reproduction link
script are retained. This is pinned binary-object provenance, not a retained
copy of the nauty source distribution; that limitation must be removed or
explicitly accepted by review before publication-quality release.

The initial attempt to download Ubuntu's nauty 2.7r3 package failed because
the sandbox denied socket creation. No random seed or nondeterministic option
is used by `geng` here.

Object SHA-256 values:

```
aaab4836b2a3f8dc22b980875003680ec174595d1f31ca7260de9e05c84ea8b2  tools/nauty-objects/geng.o
63df465662548cb2540e011f3e017f92cf1ff2b23be6aabd53a102a2f7db5cfd  tools/nauty-objects/gtools.o
690e6c9db53bfe1ae1713b4adddec95038432406d8b12fc3034fc0e5ec2f1cfc  tools/nauty-objects/naugraph.o
2fa57ee3f5680fe49d5a3bce575273b1b48ea1a2bc467ad389e2a4ee614ac806  tools/nauty-objects/naurng.o
f2cee54c347c7bd3be4d81a75af220dea10731335cde0f4bf1cd7e9481f524de  tools/nauty-objects/nautil.o
acb6f848ab8e6cd95d3f1ddd173a05405a99763c524cf2d3207c64f5eead5dc8  tools/nauty-objects/nauty.o
cff20832f8584d03bdd9a71c006c4862c90acb25d5dae3ba5ff67b035d68270c  tools/nauty-objects/schreier.o
```

`tools/build_geng.sh` relinks these objects with Zig 0.13.0. The retained
generator SHA-256 is
`1060a28fdd58062fe3e50fc853f5a7535515be35a251772f622fb6c4fab21ac5`.

## Exact commands, ordering, and counts

For each `n` in `4 6 8 10 12 14 16 18`, the command was

```
tools/nauty-root/geng -cld3D3 n (3*n/2) census/nNN.g6
```

Here `-c` restricts to connected graphs, `-d3 -D3` forces every degree to 3,
and `-l` canonically labels each representative. Files are ordered by
increasing `n`, and rows retain geng's traversal/output order. Stderr command
and count records are in `evidence/logs/geng_nNN.stderr`.

| n | rows | SHA-256 |
|---:|---:|:---|
| 4 | 1 | `62073900de6d9451c02333f80b3c4de1105edb4559989fee6cfa91c1365d102b` |
| 6 | 2 | `ba21a6e2d7d66e9a1f87dc625de77b1a40a624c9d4c7ea323c225d028d0b038a` |
| 8 | 5 | `8e99bbe0d82a1c4aa946adea55cf3b13b9ed4aaf264931ae1ffb0adcca151066` |
| 10 | 19 | `90b5fc4c0d570031df68c7473358874923ad3772f92ce9e5d79bbb14b961eb31` |
| 12 | 85 | `ab1707a4c7b004582b444351104013d593ad037c6c4f4c6831dc97aeaa5d94bd` |
| 14 | 509 | `c0a97be1aa900640a651ce7fd68e9dc81d0465c3f910ee50ac1ecba5b03c4cd3` |
| 16 | 4,060 | `6b8bbbe66a6f8c110f3f289194b1c097e7f92c2a27cef5a9b4f73d4110956ea3` |
| 18 | 41,301 | `840a9c0925044b435d99337694f145309f8412db03066381c46972e0371c101b` |

The total is 45,982, exactly reconciling the source count. Concatenation in
the stated order has SHA-256
`91781c09a687e69fab0719e58a3dff3585aa25d1199960c585a494d07ddb99b6`.
`evidence/scripts/verify_census.py`, using NetworkX 3.4.2, independently
decodes/re-encodes every row and checks order, edge count, simplicity,
looplessness, cubicity, connectedness, literal code uniqueness, and counts.
The pinned executable was subsequently rerun on all eight orders; every output
was byte-for-byte identical to the retained census.  Commands, logs, counts,
and hashes are recorded in `evidence/census_regeneration.json`.

## Independent nonisomorphism and completeness check

`evidence/scripts/canonical_small.c` is an exhaustive individualization/
equitable-refinement canonizer for graphs of order at most 18.  It uses no
nauty code and no automorphism or branch pruning.  Applied to every one of the
45,982 rows, it produced distinct canonical adjacency strings within each
order; one deterministic random relabeling of every input produced exactly the
same strings.  Its canonicalization and automorphism counts were also checked
on all 208 nonempty NetworkX atlas graphs through order 6 using VF2.

For a completeness check independent of `geng`,
`evidence/scripts/labeled_cubic_count.py` exactly counts labeled simple cubic
graphs by recursively eliminating a fixed maximum-residual-degree vertex, then
subtracts disconnected graphs by the component containing a fixed label.  At
each order, the census orbit sum `sum_G n!/|Aut(G)|` equals that independently
computed connected labeled count.  Pairwise nonisomorphism plus this orbit-sum
identity proves that no connected cubic isomorphism class is missing.  Full
integer results, source/binary hashes, canonical tables, and search statistics
are in `evidence/independent_census.json`.  Thus the retained nauty source-
archive limitation affects generator provenance, but not the independent
finite completeness argument.
