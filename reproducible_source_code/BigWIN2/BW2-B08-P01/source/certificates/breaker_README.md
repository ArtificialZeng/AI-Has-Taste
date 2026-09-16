# Breaker certificate for the n=8, alpha=3 stratum

This is a finite exact computation, not by itself a proof of the complete
eight-vertex theorem.  It must be combined with the separately proved
structural reduction covering `alpha >= 4`.

## Result

`nauty-geng 8` generated 12,346 unlabeled simple graphs.  Independent
re-enumeration found exactly 6,021 with independence number 3.  For every one
of those graphs the integer inclusion matrix representing
`A(w(G))_4 -> A(w(G))_5` has a serialized nonzero integer right-kernel vector.
Thus this map is not injective over characteristic zero for every graph in the
stratum.  No WLP counterexample was found; more strongly, every tested graph
has a directly checkable failure witness.

## Reproduction

Run from the project root:

    bash experiments/breaker_run.sh

The run uses eight deterministic shards indexed by the original zero-based
`geng` line number modulo 8.  `breaker_merge_shards.py` independently scans
the graph list, recomputes alpha, and requires exact equality of the ordered
`(geng_index, graph6)` list; this rejects missing or duplicate records.

`breaker_verify_certificates.py` does not import FLINT or SymPy.  It parses
each graph6 string, reconstructs all independent-set bases of the whiskered
graph, checks the Hilbert dimensions and the injective side of the dimension
comparison, and verifies every sparse integer matrix-vector product is zero.

The vector coordinates use the following deterministic basis order. Original
vertex masks `x` run increasingly from 0 to 255. For each independent `x`,
the permitted leaf masks `y` run through the standard descending submask
sequence of the complement of `x`. The combined masks `x | (y << 8)` are
then grouped, without further sorting, by their cardinality. Thus a degree-4
coordinate is the corresponding entry of this ordered list.

Main certificate: `certificates/breaker_n8_alpha3_kernels.jsonl`.

## Trust boundary and limitations

Generation relies on nauty's canonical unlabeled enumeration.  The exact
kernel witnesses no longer rely on FLINT after serialization, but completeness
of the universe relies on `geng` plus the expected count 12,346.  NetworkX is
used by both discovery and verifier for graph6 parsing; graph6 parsing is not
yet independently reimplemented.  The structural theorem for `alpha >= 4`
and the mathematical identification of the inclusion matrix with
multiplication by the all-ones Lefschetz form are outside this certificate.
