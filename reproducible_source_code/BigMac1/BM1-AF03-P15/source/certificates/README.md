# Exact orbit-flow certificates

## Frozen D9 release roles

`PRIMARY_D9_BINDING.json` is authoritative about artifact roles and hashes.
There is exactly one primary theorem certificate,
`d9_normalized_flow.json`, and one primary checker,
`verify_d9_flow.py` (whose default endpoint is D9).  The differently encoded
`discovery/d9_orbit_flow_candidate.json` and
`tests/verify_breaker_orbit_candidate.py` are cross-check-only artifacts.
They must not be substituted silently into the primary release pair.

## Mathematical encoding

A type string `positive_partition|negative_partition` denotes a
\(B_n\)-conjugacy orbit inside \(D_n\).  The negative partition must have even
length.  A serialized flow record gives:

- the total orbit-to-orbit mass \(F(C,D)\) as `numerator/denominator`;
- the lower and upper degrees of the orbit-pair cover graph;
- its exact edge count \(E(C,D)\);
- the uniform lifted edge mass \(F(C,D)/E(C,D)\).

Zero orbit flows are omitted.  Every stored rational is positive and in lowest
terms.  The checker reconstructs omitted zeros when it tests every row and
column equation.

## Independence boundary

`verify_d9_flow.py` imports no discovery code and trusts no rank size, orbit
size, adjacency, multiplicity, or cached objective from the JSON.  It
reconstructs these data by a second partition generator and the signed-cycle
cover rules, checks the rank vector both by orbit aggregation and by the type
\(D_n\) exponent product, and validates conservation with exact rational and
cleared integer arithmetic.  It fails on missing or extra JSON fields.

Conjugation by \(B_n\), not merely by \(D_n\), is the quotient action.  This
matters for even \(n\), where a signed cycle type can split into two
\(D_n\)-conjugacy classes.  Since \(D_n\triangleleft B_n\), conjugation by
\(B_n\) is still an automorphism action on the absolute order, and every
\(B_n\)-orbit-pair cover graph is biregular.

## Commands

```bash
python certificates/verify_d9_flow.py \
  --expected-n 4 certificates/d4_baseline_flow.json
python certificates/verify_d9_flow.py certificates/d9_normalized_flow.json
python tests/test_verify_d9_flow.py
```

The corruption test changes rank data, removes layers and flows, inserts an
unknown field, changes a cover multiplicity, makes a flow negative or
noncanonical, corrupts an endpoint, and attempts to pass the \(D_4\)
certificate as \(D_9\).  All are required to be rejected.
