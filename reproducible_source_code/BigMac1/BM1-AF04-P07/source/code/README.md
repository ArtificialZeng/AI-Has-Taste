# Exact computation

Build on the recorded macOS environment with:

```sh
make -C code
```

The two target decision programs are intentionally different.

- `builder_scan.c` models transitive triples as three-pair masks and branches
  on a live pair: cover it by each available triple or declare it uncovered.
- `certifier_scan.c` independently tests transitivity by internal outdegrees,
  builds the compatibility graph of pair-disjoint triples, and performs exact
  include/exclude clique search.

Each reads strict upper-triangle binary tournament strings, checks each found
witness internally, stops with a literal `BELOW_TARGET` record on failure,
and otherwise emits one summary containing the stream SHA-256 and exact
integer search counters.

`run_sweep.sh` invokes nauty 2.9.3 `gentourng` over a complete residue
partition and is resumable only when its endpoint and scanner hash match.
`aggregate_sweep.py` validates every status/summary and exact total;
`compare_sweeps.py` then requires Builder and Certifier to have processed
identical residue streams while their executable hashes differ.

The other exact components are:

- `burnside_count.py`: Davis's tournament-count formula with
  `fractions.Fraction`;
- `verify_minimizer.py`: no-search verifier for the literal cyclic `4+4+3`
  tournament and its 15-packing;
- `exact_max.c`: Breaker-only full maximum search on retained candidates;
- `make_blowups.py` and `random_tournaments.py`: diagnostic input generators.

Principal replay commands appear in `paper/main.tex`, `FINAL_STATUS.md`, and
the root `README.md` of the final release.
