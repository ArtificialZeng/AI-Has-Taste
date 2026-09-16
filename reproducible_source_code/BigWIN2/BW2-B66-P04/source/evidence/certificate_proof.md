# Finite proof certificate for the 12-vertex gadget claim

## Theorem

Every connected simple graph `H` on twelve vertices with distinct terminals
`s,t`, with `deg_H(s)=deg_H(t)=2`, all other degrees equal to 3, and
`dist_H(s,t)>=3`, contains a simple cycle of length 4 or 8.

## Reduction to a complete finite domain

Because `dist_H(s,t)>=3`, the pair `st` is not an edge. Add that edge and call
the resulting graph `G`. The degrees show that `G` is a connected simple cubic
graph on twelve vertices. Conversely, if an edge `st` is deleted from a
connected simple cubic 12-vertex graph `G`, and the deletion is connected with
the endpoints at distance at least 3, the resulting `(H,s,t)` satisfies every
hypothesis. Adding and deleting the marked edge are inverse operations. The
terminal order does not affect the existence or identity of a cycle, so testing
each undirected census edge once covers both ordered-terminal orientations.

Meringer's complete connected cubic census at order 12 is the copied primary
input `evidence/external/12_3_3.asc`. Its SHA-256 is
`f32e0b0a0dcaeee8b67fcd1896a261330abecd22bab3a4144463f9011732cac7`,
the hash stated in the frozen problem. It consists of 85 representatives, as
also reported by Meringer's official connected-regular-graph registry. Thus it
suffices to inspect every edge deletion of these representatives.

## Certificate and replay

`evidence/cycle_certificate.json` has one record for every eligible pair
`(graph number, deleted edge)`. Its SHA-256 is
`8ecd431c90eb70079e0e78ff71c02e763542dec50617d5c16fe2947a5860ddf0`.
Each listed cycle is normalized by starting at its least vertex and selecting
the lexicographically smaller orientation. Among all normalized 4- and
8-cycles surviving the deletion, the record contains the lexicographically
least vertex tuple.

The deterministic generator is `evidence/generate_cycle_certificate.py`.
The separate program `evidence/verify_cycle_certificate.py` does not import the
generator and uses a different cycle algorithm: it enumerates 4- and 8-element
subsets of the surviving edges and recognizes a cycle by the connected
2-regular condition. It also independently parses and validates all census
graphs, reconstructs the full edge-deletion domain, computes endpoint distances,
rejects duplicate, missing, or ineligible records, directly validates every
listed cycle, and recomputes its lexicographic minimality.

Replay from the project directory with Python 3:

```text
python3 evidence/verify_cycle_certificate.py \
  evidence/external/12_3_3.asc evidence/cycle_certificate.json
```

The recorded replay in `evidence/verification.txt` reports:

```text
census_graphs=85
graph_edge_pairs=1530
connected_deletions=1526
eligible_pairs=1110
all_cycles_valid_and_lexicographically_least=true
```

Consequently, every eligible edge deletion contains the certified `C4` or
`C8`. By the bijection above, every graph in the theorem does as well.

## Scope and dependencies

This is an exhaustive finite proof relative to the cited complete Meringer
census; the verifier authenticates the exact copied census and validates its
85 entries, while the external census result supplies exhaustion up to
isomorphism. No floating-point calculation, randomized test, or SAT solver is
used. The accompanying Garcia PDF is included to bind the stated surrounding
order-10 result and problem provenance, not as a logical premise of the cycle
checks. An independent from-scratch cubic census regeneration would strengthen
the audit of the external completeness dependency but is not needed if the
published official census is accepted.
