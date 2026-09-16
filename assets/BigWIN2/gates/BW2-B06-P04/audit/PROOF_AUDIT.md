# Proof audit

Status: **PASS**

## Statement and definitions

- The source statement is preserved verbatim in `problem/source_statement.md`.
- The locked proposition in `problem/formal_statement.md` matches published
  Conjecture 6.1 at the finite parameter (n=11).
- NAC colourings are surjective; only global colour exchange is quotiented.
- “One open step” is construction-independent by the proved triangle-count
  identity.

## Mathematical dependency checks

- The opposite-colour path criterion is proved in both directions.
- The 2-tree zero lemma and one-open-step uniqueness lemma include existence,
  uniqueness, surjectivity, and preservation under later closed steps.
- Family A uses the published (2^p-1) formula and the corrected published
  characterization of the no-stable-cut class.
- A prism on six vertices is automatically induced under Laman sparsity.
- Family A and B are disjoint because 0-extension graphs are 2-degenerate.

## Finite exhaustiveness checks

- Two independent universe artifacts canonically agree on 2,039,273 classes,
  with no canonical duplicates.
- The verifier checks every serialized graph has 19 edges and all 1,815
  relevant subset inequalities.
- The certificate has exactly one accepted A/B/T/2 row per distinct graph and
  no residual or negative-search row type.
- Each of the 4,027,206 Type-2 witnesses is checked for surjectivity, support,
  the exact NAC connectivity condition, and inequivalence modulo colour swap.
- Structural tags are recomputed from the graph rather than trusted from
  discovery output.

## Independence and failure tests

Discovery uses disjoint-set connectivity; verification uses separately coded
bitset transitive closure.  Fresh generation is checked against a 2018 data
artifact, and `RUN_DISCOVERY=1` reproduced the full certificate byte for byte.
Eight corruptions covering invalid, equivalent, mismatched, duplicate,
unknown, false-header, and truncated inputs were rejected.  No decisive claim
uses floating point, randomness, timeout, finite-search failure, or failure to
find a counterexample.

## Scope

The proof establishes the complete (n=11) instance and the exact count
23,499.  It does not establish the arbitrary-order converse, and the
manuscript says so explicitly.
