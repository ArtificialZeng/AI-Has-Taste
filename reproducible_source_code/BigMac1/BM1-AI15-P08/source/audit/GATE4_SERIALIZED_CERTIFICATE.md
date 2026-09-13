# Gate 4 serialized-certificate audit

Audit date: 2026-08-29 (Asia/Shanghai)  
Scope: `certificates/low_degree_identities.json`,
`certificates/low_degree_certificate_manifest.json`,
`tests/verify_serialized_low_degree_certificate.py`, and
`tests/gate4_serialized_tamper_matrix.py`.

## Verdict

**PASS after repair.**  The earlier serialized verifier pinned the canonical
certificate digest and label inventory, but its parser did not reject every
extra field.  Moreover, changing a certificate together with the digest
constant inside the same verifier was not an independently rooted release
binding.  That earlier state must not be cited by itself as a frozen
fail-closed certificate.

The repaired layer now has all of the following:

1. an exact schema and exact field sets at the certificate root, conjugation,
   group, definitions, check-item, and kind-specific nested levels;
2. a separate JSON manifest whose own SHA-256 is pinned by the verifier;
3. the canonical certificate path and SHA-256 pinned by both manifest and
   verifier;
4. frozen hashes for the formal statement, builder proof/checker, independent
   referee report/checker, and manuscript proof;
5. an outer release manifest that binds the verifier, certificate manifest,
   matrix driver, and this audit without creating a self-hash cycle.

The serialized layer is supporting exact evidence.  It is not the sole proof:
the analytic proof, independent human-style referee reconstruction, and the
hard-coded standard-library referee checker remain independently decisive.

## Hash chain

```text
92a5280a7380c140ad758b9d2f346adf3ba4072393890c778056cd50acde8720  certificates/low_degree_identities.json
a6a5ad4f655b315cf3def4e8f37d4bf89e993a63d0efbb3e3b7007fa480753c3  certificates/low_degree_certificate_manifest.json
5244545747cd200b07c87730b0188927e7193da2bf73d760dc4c8d62f7f81153  tests/verify_serialized_low_degree_certificate.py
43fb7d56d563667f2153d6392eec7a776ce860bcc2e58fdb3f4666108a73f384  tests/gate4_serialized_tamper_matrix.py
```

The certificate manifest freezes these independently meaningful inputs:

```text
c0cc95ed9411c7ee5751aa37969bb2315440839b3219a3ff166980e7bf88a2be  problem/formal_statement.md
126ec4120fd2984a300d35805f074fa932a37b79bf555925f53b12c1d34001df  proof/builder_notes.md
fd8e983f79b22ec2dd2be056e2ae4515f9a46e8321ac89bd6c73f6c5d1775a99  src/builder_symbolic_checks.py
4e171752e1dc030ffe2856d22b915e37bcbf2f8ed62ed667003bcf2962dd3fd3  audit/referee_low_degree.md
e8e37c700e625342a46bcf15778237f2bc182a66e60c4399166c51750564d3a4  tests/referee_low_degree_identities.py
ca929d47781190a84937445afecf5bfa63888e02476316a7b3694395642d86d4  paper/main.tex
```

A preliminary design also froze `audit/PROOF_AUDIT.md`, which itself froze
the serialized verifier.  Independent review correctly rejected that design
as a circular/stale binding.  The final manifest removes that edge.  The
outer source manifest freezes the Gate 4 verifier and audit instead.

## Strict schema

`exact_keys(...)` rejects missing and additional keys.  It is applied to:

- the manifest root, certificate descriptor, and each frozen artifact;
- the certificate root and conjugation object;
- every group and its exact definition-name set;
- every check item; and
- the nested expected-coefficient map for `schur_coefficients`.

The group names/order, variable inventory/order, conjugation metadata,
definition inventories, check labels/order/kinds, and the complete eleven
check inventory are fixed.  Duplicate JSON keys and duplicate labels remain
explicit failures.  The verifier contains no `assert` or `__debug__`
dependency.

## Independent 5 by 4 matrix

An independent agent ran the current files from
`/var/folders/kh/3l44w5_56q36j9p6cyg1fgy00000gq/T/gate4_independent_external_cwd_s4rli5mn`
with `/opt/homebrew/bin/python3` (CPython 3.14.7).  No project working
directory or third-party package was used.

| Case | normal | `-O` | `-I` | `-O -I` | Gate exercised |
|---|---:|---:|---:|---:|---|
| genuine | 0 | 0 | 0 | 0 | all 11 exact checks and all frozen hashes |
| badhash | 1 | 1 | 1 | 1 | canonical certificate digest |
| extra-field | 1 | 1 | 1 | 1 | exact root field set |
| drop-check | 1 | 1 | 1 | 1 | exact per-group and global inventory |
| change-expression | 1 | 1 | 1 | 1 | exact identity recomputation |

The independent referee additionally obtained exit 1 in all four modes for:

- a synchronized rewrite of both input and expected expressions to a true
  tautology: rejected by the canonical certificate digest;
- a self-consistent expression rewrite plus a copied manifest whose
  certificate digest was synchronized: rejected by the pinned manifest
  digest;
- a manifest trailing-newline mutation: rejected by the pinned manifest
  digest; and
- extra nested fields at each schema level listed above.

The checked-in matrix driver independently reproduced 24/24 expected outcomes
(the requested 20 cells plus an in-memory changed-expression residual test in
all four modes):

```bash
/opt/homebrew/bin/python3 tests/gate4_serialized_tamper_matrix.py
```

## Scope and proof-assistant disclosure

This repair changes no mathematical statement, proof, coefficient, or
literature claim.  It does not touch Q4-U or Q5-U and performs no numerical
search.  No proof assistant was used.
