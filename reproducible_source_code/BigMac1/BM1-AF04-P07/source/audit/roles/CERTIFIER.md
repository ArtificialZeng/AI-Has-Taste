# Certifier record

The Certifier will consume only serialized generator output or summary
records, recompute transitivity and arc-disjointness, reject malformed or
truncated inputs, and bind every accepted run to code/input hashes.

## Independent design

`code/certifier_scan.c` shares no search code with the Builder.  It calls a
triple transitive exactly when its internal outdegree multiset is
(\{0,1,2\}), creates a compatibility graph on all transitive triples, and
uses complete include/exclude maximum-clique recursion to decide whether a
15-clique exists.  The three-word candidate bitset and cardinality pruning use
only integer operations.

`code/aggregate_sweep.py` accepts a run only when every residue and status
file is present, each log consists of one exact summary line, all processes
exited zero, and counts sum to the independently fixed class total.  It records
each tournament stream's SHA-256 and hashes the generator and scanner.

The short `code/verify_minimizer.py` independently reconstructed the explicit
minimizer and checked a 15-packing, all 45 used pairs, the cyclic cross-part
orientation, and all 117 transitive triples.  Nine malformed sweep controls
and six corrupt minimizer controls were rejected.

The Builder role is closed.  The complete order-11 no-import Certifier rerun
also closed successfully: all 192 processes exited zero, their counts summed
to exactly 903,753,248, and the aggregate records 16,972,027,052 clique-search
nodes with largest single-instance count 203,790.  The Certifier certificate
is `certificates/n11_certifier_full_m192.json`.

`code/compare_sweeps.py` then matched every residue count and regenerated
input-stream SHA-256 with the Builder certificate while confirming distinct
scanner executable hashes.  The binding artifact is
`certificates/n11_sweeps_match.json`.  Its own six deliberate corruptions were
all rejected.
