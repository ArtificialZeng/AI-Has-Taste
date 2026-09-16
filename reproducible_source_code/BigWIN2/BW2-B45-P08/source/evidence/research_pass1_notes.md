# Research pass 1 evidence notes

Job: `win-00045-p08-research-7bb1ede3b7fc`

## Official input located, but not staged

The official repository history was inspected on 2026-09-06. Commit
`f23f6388c5820e6ad7bfd8fbf1bad2b4d6d0eb3b` adds
`data/n9_margin1only_tournaments.rds`; the official commit page identifies it
as the adjacency data for the 254 order-9 tournaments in the target family and
reports a size of 5.54 KB. The repository README likewise describes that file
as the 254 tournaments. Primary URLs:

- https://github.com/Leonardini/Tournaments/commit/f23f6388c5820e6ad7bfd8fbf1bad2b4d6d0eb3b
- https://github.com/Leonardini/Tournaments/tree/main/data

The shell's network sandbox rejected both `git ls-remote` and direct `curl`;
the web reader could inspect GitHub HTML but could not materialize the binary
RDS file in the project. This is `access-blocked`, not mathematical evidence
for or against the frozen claim.

The same official package's `get_data.sh` pins McKay's `tourn9.txt` catalogue
at 7,086,832 bytes and 191,536 lines, matching the paper's order-9 count. McKay's
official archive independently labels its order-9 tournament collection as
191,536 non-isomorphic tournaments.

## Exact counterexample to one restricted construction

Consider the three orders on five vertices

```
(0,1,2,3,4)
(0,1,3,4,2)
(3,0,2,1,4).
```

A tempting recipe chooses one voter `r`, appends its reverse, and asks for the
fifth order to agree with `r` on every non-unanimous pair and reverse `r` on
every unanimous pair. Those comparison requirements are forced by exact 3:2
support. For each of the three choices of `r`, however, the forced orientation
is cyclic: it contains respectively the directed triangles
`1->2->4->1`, `0->3->2->0`, and `2->4->3->2`. Thus this restricted
"reverse one voter plus its forced partner" construction fails already on five
vertices. This does not obstruct other five-order profiles.

## Deterministic screen

`research_pass1.py` generated 10,000 seeded three-profiles on nine vertices,
fixing the first order to the identity. They induced 9,521 distinct labelled
tournaments. An exact Boolean encoding in Z3 found an `I_{3,1}` profile for
all 9,521; every returned profile was independently recounted. Consequently
the sample contained no member of the target boundary and no `I_{5,1}` test
was triggered. This is a documented failure of naive random-profile sampling,
not an exhaustive or isomorphism-deduplicated claim. Full parameters and
tallies are in `research_pass1_results.json`.
