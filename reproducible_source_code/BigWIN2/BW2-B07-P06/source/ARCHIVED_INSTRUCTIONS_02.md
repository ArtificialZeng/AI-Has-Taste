# Reproducible computations

## Environment

- Python 3.10.12
- NetworkX 3.4.2
- Ubuntu nauty package 2.7r3+ds-1
- Ubuntu libnauty2 package 2.7r3+ds-1
- Ubuntu libcliquer1 package 1.21-3

The three Ubuntu packages are frozen under tools/nauty_pkg/ and extracted
under tools/nauty_pkg/root/. Nothing is installed system-wide.

Set

    export LD_LIBRARY_PATH="$PWD/tools/nauty_pkg/root/usr/lib:$PWD/tools/nauty_pkg/root/usr/lib/x86_64-linux-gnu"
    export GENG="$PWD/tools/nauty_pkg/root/usr/bin/nauty-geng"

from the project root.

## Fast core tests

    python3 tests/test_exact_csf.py
    python3 tests/test_degree_transform.py

The first test compares three mathematical decompositions: direct
spanning-edge-subset enumeration, vertex-weighted deletion--contraction, and
proper-coloring dynamic programming. The second computes both sides of the
new degree transform from exact integers.

The companion edge-transform test is:

    python3 tests/test_edge_transform.py

An exhaustive small-order transform regression is:

    for n in 3 4 5 6 7 8 9 10; do
      "$GENG" -q -c "$n" "$n:$n"
    done | python3 tests/check_degree_transform_stream.py

It checks all 1,040 non-isomorphic connected unicyclic graphs in those
orders.

Replace the final checker by `tests/check_edge_transform_stream.py` to run
the same 1,040-graph regression for the two-vertex-component transform.

## Discovery scan

For a fixed order n:

    "$GENG" -q -c 17 17:17 |
      python3 src/csf_hash_search.py --target-only \
        --candidate-file experiments/run_n17/candidates.json

The discovery program uses fixed exact modular evaluations. It emits any pair
whose evaluation values agree but whose structural data differ. Such a pair
is only a candidate and must be exactified with both full-CSF programs.

Use order 18 in both occurrences of `17` for the order-18 scan.  Adding
`--target-only` excludes triangle-unicyclic graphs only when the order is
even, exactly matching the conjecture's stated domain.

## Independent finite verifier

    "$GENG" -q -c 17 17:17 |
      python3 src/verify_finite_stream.py --target-only \
        --output experiments/verify_n17/result.json

This verifier intentionally uses NetworkX graph6 parsing, NetworkX cycle
bases, recursive rooted-tree messages, matrix traces, and unrelated moduli
and evaluation points. It imports none of the discovery parser/evaluator.

The identity
\[
X_G(x_1,\ldots,x_q)=
\operatorname{tr}(D_0B D_1B\cdots D_{c-1}B),
\quad B=J-I,
\]
is evaluated exactly modulo the stated primes. Equal CSFs must have equal
values at every specialization and modulo every prime. Therefore distinct
signatures rigorously imply distinct CSFs; no probabilistic inference is
used in that direction. A signature collision is never called CSF equality.

## Full exactification of a graph6 pair

    python3 src/csf_subset.py GRAPH6
    python3 src/csf_delete_contract.py GRAPH6

The resulting integer dictionaries are the coefficients in the power-sum
basis. Equality must hold in both implementations before a pair is certified
as equal-CSF.
