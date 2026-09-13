# Certificate index

The decisive lower-bound artifacts are aggregate indices over canonical
generator streams.  They do not store 903,753,248 individual packings.

- `n11_builder_full_m192.json`: strict aggregation of the Builder's 192
  residue slices.
- `n11_certifier_full_m192.json`: strict aggregation of the independently
  written compatibility-graph Certifier (created only after its full run).
- `n11_sweeps_match.json`: residue-by-residue equality of class counts and
  regenerated input-stream SHA-256 values, while requiring distinct scanner
  executable hashes (created only after both aggregate certificates pass).
- `minimizer_11.json`: literal tournament, cyclic `4+4+3` partition, and a
  15-packing proving the upper bound is attained.
- `baseline_n9_sweeps_match.json` and
  `baseline_n10_sweeps_match.json`: exact reproduction of the last known
  public finite baseline with both algorithms.

Every aggregate slice points to one strict one-line log under `logs/runs/` and
records its hash.  `code/aggregate_sweep.py` fails on a missing residue,
nonzero or malformed status, extra/malformed log line, endpoint mismatch,
role mismatch, nonpositive counters, or incorrect exact total.

The mathematical trusted base and replay commands are stated in
`audit/PROOF_AUDIT.md` and the manuscript.  A SHA-256 digest is an integrity
binding, not a substitute for the exact search or for canonical-generation
correctness.
