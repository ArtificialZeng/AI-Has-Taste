# Eleven-vertex unique NAC-colouring certificate

This project certifies the \(n=11\) instance of Conjecture 6.1 from Clinch,
Garamvölgyi, Haslegrave, Huynh, Legerský, and Nixon, *Journal of Graph Theory*
(2026), DOI 10.1002/jgt.70064.

The exact result is:

> Every 11-vertex minimally rigid graph has exactly one NAC-colouring modulo
> global colour swap if and only if it lies in one of the two families stated
> in Conjecture 6.1.

The full certificate covers all 2,039,273 nonisomorphic 11-vertex Laman graphs.
It partitions them into 1,196 family-A graphs, 22,303 family-B graphs, 2,171
2-trees, and 2,013,603 graphs carrying two explicit inequivalent NAC
colourings.

## One-command verification

With a C11 compiler available as `cc`:

```sh
./scripts/build_and_verify.sh
```

This recompiles the independent checker, verifies all 1,815 relevant Laman
subset inequalities for every graph, checks every certificate row, and runs
five fail-closed mutation tests. To rerun discovery and require byte-identical
output as well:

```sh
RUN_DISCOVERY=1 ./scripts/build_and_verify.sh
```

The dataset is the independently published `LamanGraphs11.txt` from Zenodo
record 1245517. The source archive is retained under `experiments/upstream/`.

## Trust boundary

`src/discover_n11.c` is discovery code. The result relies on
`src/verify_n11.c`, the four-way certificate, the two structural lemmas in
`proof/main_proof.md`, and the independent canonical-universe comparison in
`certificates/generation_crosscheck.txt`. No floating point or proof assistant
is used.
