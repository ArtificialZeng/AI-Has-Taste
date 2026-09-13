# Proof audit

Audit date: 2026-08-29 (Asia/Shanghai)

## Verdict

**PASS for the frozen claims; not a proof of the original all-degree
problem.**  An independent referee reconstructed the normalizations,
boundary lemma, both Schur branches, the cubic center homotopy, and the
isolated zero-boundary case directly from the definitions.  The verdict is:

- complete exact proofs for \(n=1,2,3\);
- exact partial theorems for \(n=4,5\) when an endpoint coefficient has
  modulus \(A\), when a zero is off the unit circle, or when all roots are
  unimodular and \(2|a_n|\ge A\);
- exact even sparse pullbacks of the quadratic result on support
  \(\{0,n/2,n\}\), plus the elementary odd endpoint-binomial class.

The all-unimodular, non-endpoint strata \(2|a_4|<A\) and
\(2|a_5|<A\) remain major open gaps Q4-U and Q5-U.  They are excluded from
every frozen theorem.  The unrestricted Sheil-Small question remains open.

## Independent reconstruction and repairs

The full adversarial report is `audit/referee_low_degree.md`.  It found no
fatal gap.  Its local/expository repairs are grouped here into five broad
categories: phase wording, positive root separation, the unit-circle Schur
branch, exact degree/equality handling in the cubic quotient, and root-count
homotopies.  The direct post-referee diff also contains the referee's explicit
R3 zero-boundary converse, R8 stronger cubic radius, and R11 quintic
restatement.  Thus “five” is a compressed classification, not a claim of five
literal diff hunks.  The independent reconstruction and provenance limits
are recorded in `audit/BUILDER_NOTES_DIFF_AUDIT.md`.

The open gaps and their severity are serialized in `proof/gap_ledger.md`;
the logical dependencies are in `proof/proof_dag.md`.

## Exact verification

Two implementations reconstruct the displayed Schur/Laurent identities:

```bash
/opt/anaconda3/bin/python src/builder_symbolic_checks.py
/opt/homebrew/bin/python3 tests/referee_low_degree_identities.py
```

Both are fail-closed and pass from an external working directory under
normal, `-O`, `-I`, and combined `-O -I` modes.  Their injected-failure
paths exit nonzero in all four modes.  The dependency, clean-venv, command,
and hash evidence is in `audit/fail_closed_dependency.md`.

These programs verify algebraic identities; they are not proof assistants
and do not formalize the analytic/topological steps.

## Bound inputs (SHA-256)

```text
c0cc95ed9411c7ee5751aa37969bb2315440839b3219a3ff166980e7bf88a2be  problem/formal_statement.md
126ec4120fd2984a300d35805f074fa932a37b79bf555925f53b12c1d34001df  proof/builder_notes.md
4e171752e1dc030ffe2856d22b915e37bcbf2f8ed62ed667003bcf2962dd3fd3  audit/referee_low_degree.md
e8e37c700e625342a46bcf15778237f2bc182a66e60c4399166c51750564d3a4  tests/referee_low_degree_identities.py
fd8e983f79b22ec2dd2be056e2ae4515f9a46e8321ac89bd6c73f6c5d1775a99  src/builder_symbolic_checks.py
92a5280a7380c140ad758b9d2f346adf3ba4072393890c778056cd50acde8720  certificates/low_degree_identities.json
5244545747cd200b07c87730b0188927e7193da2bf73d760dc4c8d62f7f81153  tests/verify_serialized_low_degree_certificate.py
a6a5ad4f655b315cf3def4e8f37d4bf89e993a63d0efbb3e3b7007fa480753c3  certificates/low_degree_certificate_manifest.json
43fb7d56d563667f2153d6392eec7a776ce860bcc2e58fdb3f4666108a73f384  tests/gate4_serialized_tamper_matrix.py
```

The serialized layer's strict-schema and tamper-matrix audit is
`audit/GATE4_SERIALIZED_CERTIFICATE.md`.  It is supporting exact evidence;
the analytic proof, independent referee reconstruction, and hard-coded
standard-library referee checker do not depend on accepting arbitrary
serialized identities.

## Proof-assistant disclosure

No Lean, Coq, Isabelle, HOL, or other proof assistant was used.  The proof is
human mathematics with two exact symbolic identity checkers and an
independent human-style referee reconstruction.
