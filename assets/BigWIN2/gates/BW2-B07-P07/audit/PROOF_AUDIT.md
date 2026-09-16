# Proof audit

Date: 2026-08-30 UTC

Endpoint: coefficientwise positivity of
\(LG(D(p,q);-x,-y)\) for every \(p,q\ge1\), implying Ishii's sign
condition for this two-block alternating 2-bridge family.

Status: PASS for the stated partial theorem; the full conjecture remains
open.

| Audit item | Result | Evidence |
|---|---|---|
| Source/formal target distinguished | pass | problem/source_statement.md, problem/formal_statement.md |
| \(D(p,q)\) is an alternating knot | pass | Kohli §2.3.2 and Remark 2.13 |
| Published recurrence transcribed exactly | pass | Kohli Cor. 2.12 and proof of Thm. 2.15 |
| Apparent denominator in \(a_2\) removed | pass | telescoping identity (3.3); independent SymPy check |
| Global signs in one-block recurrence | pass | reconstructed independently in roles/referee.md |
| Boundary \(p=1\) / split \(D(0)\) | pass | empty sums and \(LG(D(0))=0\) |
| All-\(p,q\) quantifiers | pass | symbolic finite sums; no finite extrapolation |
| Implication to Ishii pairwise signs | pass | coefficient of \(x^iy^j\) is \((-1)^{i+j}a_{ij}\) |
| Stronger hole-free/log-concavity claims excluded | pass | explicit limitations in theorem and paper |
| Independent exact certification | pass | audit/REPRODUCIBILITY_AUDIT.md |

The false diagonal sign-gauge lemma from the discovery route is excluded
from the dependency graph.  The only open major item in
proof/gap_ledger.md is extension from the proved family to all alternating
knots; it is a limitation of the partial endpoint, not a missing premise in
the theorem.
