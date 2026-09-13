# Final status: PROVED

Original prompt complete: **true**.  Completion date: 2026-08-29.

## Conclusion

For every integer \(n\ge9\) and every intersecting family
\(\mathcal F\subseteq\binom{[n]}4\),

\[
\delta_3(\mathcal F)\le1.
\]

This closes the full \((k,d)=(4,3)\) parameter family.  The result is sharp in
both respects:

- every full star has minimum triple degree \(1\);
- the explicit 35-edge family in `discovery/breaker/n8_literal_family.json`
  is intersecting on \([8]\) and has \(\delta_3=2\), with exact degree histogram
  \(42\times2+14\times4\).

The main proof is elementary and self-contained.  Fixing an edge \(E\), two
disjoint triples outside \(E\) immediately settle all \(n\ge10\).  For \(n=9\),
four forced witnesses \(x_e\) are first shown to be distinct; a fixed exterior
triple is then forced to carry three labels although its link has size two.
The complete proof is in `proof/main_proof.md` and `paper/main.tex`; a different
graph-counting cross-check is in `proof/independent_crosscheck.md`.

## Exact endpoint certificates

The originally requested \(n=9,10\) SAT formulations are independently
certified UNSAT:

| \(n\) | variables | clauses | LRAT SHA-256 | additions / deletions |
|---:|---:|---:|---|---:|
| 9 | 126 | 819 | `44d28573280a35b81f46000e57aa7da676b4b1f844469ea130a48289992d6c9c` | 184 / 28 |
| 10 | 210 | 2415 | `1df5a6c057fd6b4fed51dfd6512433a146b9ce322586434e09ba550123459240` | 81 / 8 |

`verification/verify_instance.py` reconstructs each ordered CNF from the
definitions without importing the discovery generator.  The LRAT wrapper
snapshots the CNF, proof, and hash-verified pinned `lrat-check.c` source;
compiles a fresh temporary checker; and executes only that checker.  It accepts
both proofs and rejects eight malformed, truncated, altered, invalid-deletion,
or cross-instance traces fail closed.

The independent witness-pair encoding is corroborating breaker evidence only;
its UNSAT statuses are not promoted to certificates.  Its literal \(n=8\)
model is independently verified from definitions.

## Literature and novelty

Gate 1 and a separate second novelty pass checked Huang--Zhang's arXiv and
published records, forward and later literature, corrections, repositories,
and public code/certificate archives.  No earlier public source resolving
\(n=9\) or \(n=10\) was found as of 2026-08-29.  This is necessarily a bounded
negative search: it cannot exclude private, unpublished, unindexed, same-day,
or differently worded work.  The paper therefore makes no categorical
priority claim.

The baseline correction is explicit: Huang--Zhang's result was an arXiv
preprint in 2024 and formally appeared in JCTA in 2026.  Their theorem covers
\(n\ge11\) here.  Gan--Han--Im's later \(d=k-1\) theorem begins at \(n\ge14\)
when \(k=4\), so it does not cover the two endpoints.

## Independent audits

- Blind proof referee: PASS, zero fatal and zero major gaps.  One harmless
  \(n<3\) definition edge case was found and repaired in the formal statement.
- Certificate referee: PASS after finding and forcing repair of an initially
  unbound persistent checker binary; final re-audit reports no fatal, major,
  or local defect in the scoped verifier.
- Citation audit: all three citations independently verified against official
  publisher/DOI/arXiv sources; 3 cited, 3 present, 0 missing, 0 unused.
- LaTeX/PDF audit: clean four-page build, no warnings or layout defects, all
  fonts embedded, exact authorized author/affiliation/emails.
- Release manifests: generated and independently reverified with the skill's
  SHA-256 manifest verifier.

## Deliverables

- Article PDF: `output/pdf/d_degree_ekr_k4d3.pdf`.
- LaTeX: `paper/main.tex`, `paper/references.bib`, regenerated
  `paper/main.bbl`.
- Source and exact-certificate bundle:
  `release/d_degree_ekr_k4d3_source_and_certificates.zip`.
- Full release hash manifest: `release/RELEASE_MANIFEST.json`.
- Proof/citation/PDF audit reports: `audit/`.

## Reproduction

Run from the project root:

```bash
python code/reproduce_hz_baseline.py
python tests/test_verify_instance.py
python tests/test_verify_lrat.py
python verification/verify_lrat.py instances/ekr_k4d3_n9.cnf certificates/ekr_k4d3_n9.lrat --n 9
python verification/verify_lrat.py instances/ekr_k4d3_n10.cnf certificates/ekr_k4d3_n10.lrat --n 10
python discovery/breaker/rerun.py
python discovery/breaker/test_verify_family.py
python /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py release/package release/package/MANIFEST.json
python /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py release release/RELEASE_MANIFEST.json
```

Clean paper build:

```bash
mkdir -p tmp/reproduction-build
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir=../tmp/reproduction-build main.tex
```

## Scope limitations and proof assistants

No classification of all equality families with \(\delta_3=1\) is claimed;
full stars are used only to prove sharpness.  No Lean, Coq, Isabelle, or other
proof assistant was used.  Consequently, there is no formalization endpoint
beyond the exact SAT/LRAT certificate statements described above.
