# Final status: PROVED

## Conclusion

The maximum number of full base-block translation orbits in a cyclic
\(3\)-\((31,5,1)\) packing is

\[
  \boxed{M=12}.
\]

The twelve base blocks are serialized in `certificates/packing12.json` and
displayed in `paper/main.tex`. Full development gives 372 distinct blocks and
3,720 distinct triples, so it is a valid packing.

For the upper bound, the exact orbit model has 145 triple resources and 4,761
internally valid block variables. Multiplication by the units modulo 31 splits
those variables into 162 orbits with distribution `30^156,15^5,6^1`. Every
hypothetical 13-packing has a multiplier image containing one canonical
representative. A definition-level exact clique enumerator proves that none of
the 162 representative neighborhoods contains the required 12-clique. The
scopes are disjoint and cover all 4,761 variables; therefore target 13 is
impossible.

## Certificates

- Positive: `certificates/packing12.json`, SHA-256
  `23dc758771e6dce03b943a48aab50077a5ee00c36e24cde02f74aa2468f8cf45`.
- Global negative manifest:
  `certificates/negative/target13_global_fixed_cover_manifest.json`, SHA-256
  `ae259e64de1793421a7e5e4bd525fec405133f3f277074a222badf6ac5d522b3`.
- Exact enumerator source: `code/exact_clique.cpp`, SHA-256
  `ae549763147bd579353d3b91fcbad4e9afb4e2e404c97f915115d8b6e84458c9`.
- Locked enumerator binary: `experiments/exact_clique_fixed_fast`, SHA-256
  `2b0cb86d49c2ce6add774dedf98796b706d72cd0d2266b5a7aa9ce653413d30f`.
- Global exact run: 68,377,851,660 deterministic branching nodes; branch range
  251,805,613--636,752,470.

## Independent audit

- The positive verifier imports no discovery state and reconstructs every
  developed block and triple.
- The global negative verifier independently reconstructs the finite instance,
  multiplier action, branch scopes, hashes, statuses, and aggregate counts; it
  reports `VERIFIED_GLOBAL_TARGET13_UNSAT`.
- Fixed-branch and global test suites deliberately corrupt schemas, hashes,
  claims, scope/action text, results, counts, and coverage, and fail closed.
- Clean source rebuild/replays passed for the minimum-node branch and the
  unique size-six multiplier orbit.
- Two auxiliary LRAT refutations pass the official `lrat-check`; they are
  cross-checks rather than the global proof.
- Gate 2 novelty, frozen two-pass citation, BibTeX, LaTeX, metadata, source
  archive, and five-page visual PDF audits all passed. Novelty remains a
  bounded database-search statement, not a universal priority claim.

## Reproduction

From the project root:

```sh
python3 code/verify_packing_certificate.py \
  certificates/packing12.json --expected-blocks 12
python3 code/verify_global_fixed_cover.py
python3 tests/test_global_fixed_cover.py
python3 tests/test_fixed_clique_certificate.py
```

The optional `python3 code/verify_global_fixed_cover.py --rebuild-rerun`
compiles the locked source once in a temporary directory and replays all 162
exact searches. This is intentionally much slower than checking the serialized
manifests. Further commands and expected outputs are in `REPRODUCE.md`.

## Limitations and formalization status

- Timed-out, UNKNOWN, interrupted, local-search, floating-point, and optimizer
  outputs are not used as evidence.
- The proof is an exact certified finite computation with conventional
  C++/Python verifiers. **No proof assistant was used.** It is therefore not a
  Lean, Coq, Isabelle, or HOL formalization.
- The literature search cannot exclude unindexed or unpublished prior work.

## Release artifacts

- Final PDF: `output/pdf/cyclic-315-packing-M12.pdf`, SHA-256
  `1f72dfdde2bf58cc3c77795510056a563d35816fa152ab722211c4c09db37426`.
- LaTeX source archive: `output/source/cyclic-315-packing-M12-source.zip`,
  SHA-256
  `e1aba6aec4ddf17311ed15f1e78032b2729e64721f6b09e275ffabd40a2ac311`.

Author and artifact identity were checked as exactly Zijian Zeng, the specified
UCSI University affiliation, and the two authorized email addresses.
