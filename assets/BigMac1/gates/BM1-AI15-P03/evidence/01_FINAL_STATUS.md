# Final status: PROVED

## Theorem

For the literal simple graph on \(\mathbb Z/n\mathbb Z\) having edges of
offsets \(1\) and \(3\), and also offset \(n/2\) when \(n\) is even, the
number \(a(n)\) of proper labelled three-colourings satisfies

\[
 a(n)=0\quad\Longleftrightarrow\quad n\in\{7,8,12,16\}
 \qquad(n\ge6).
\]

The terminal state is **PROVED**.

## Decisive evidence

The positive direction is constructive.  With \(A=01\) and \(B=21202\),
proper colourings are

\[
 A^{(n-5)/2}B\quad(n\ge9\text{ odd}),\qquad
 A^{n/2}\quad(n\equiv2\pmod4),
\]
\[
 A^3BA^2B\quad(n=20),\qquad
 A^{k-1}BA^{k-4}B\quad(n=4k\ge24).
\]

These families cover every nonexceptional \(n\ge6\).  The negative direction
encodes adjacent colour differences by signs.  Closure gives
\(2p-n\equiv0\pmod3\), while the offset-three edges forbid three consecutive
equal signs.  This run bound excludes \(n=7\).  For \(n=8,12,16\), it forces
equal numbers of the two signs; the discrete intermediate-value argument for
cyclic half-windows then produces a zero-sum diameter window, a contradiction.
The complete human proof is in `proof/builder_notes.md`.

The canonical proof does not depend on computation.  As reproducible
diagnostics, four independently structured exact verifiers reconstruct the
graph, the difference-word criterion, or the seam-correct automata from
serialized inputs.  The definition-first
referee rederived the reduction, attacked all boundary cases, checked the
remediation, and returned `PASS; unresolved items: none` in
`audit/PROOF_AUDIT.md`.

## Independent transfer-automaton route

A second exact proof route is recorded in `proof/transfer_automaton.md`.
From the graph definition it constructs a 12-state odd matrix \(O\) and a
54-state paired-window matrix \(E\).  For even \(n=2m\), the required closure
is the track-swap permutation \(P\), and the colouring/walk bijection gives

\[
 a(n)=\operatorname{tr}(O^n)\quad(n\text{ odd}),\qquad
 a(2m)=\operatorname{tr}(E^mP).
\]

The ordinary trace is provably wrong: at \(n=6\) it gives \(0\) instead of
\(42\), and at \(n=8\) it gives \(114\) instead of \(0\).  Exact integer
matrix multiplication certifies \(O^{10}>0\) and \(E^{13}>0\) entrywise.
Because neither matrix has a zero column, every later power is also strictly
positive.  Thus all odd \(n\ge11\) and all even \(n\ge26\) are positive;
\(\operatorname{tr}(O^9)=18\), and an independent direct-graph recursion for
\(6\le n\le25\) has zeros exactly at \(7,8,12,16\).

The independent automaton referee proved both implications of the
colouring/walk correspondence, reconstructed the positive powers and finite
counts, tested the \(n=6\) collision, and rejected three decisive certificate
tamperings in normal and optimized modes.  Its final verdict in
`audit/AUTOMATON_EQUIVALENCE_AUDIT.md` is `PASS; unresolved items: none`.

## Verifier integrity repair

The earlier `verification/primary_verify.py` used correctness-critical Python
`assert` statements and was therefore fail-open under `python -O` for a
tampered extension block.  This was a release-fatal implementation defect,
not a gap in the canonical colour-block proof.  Every such assertion has now
been replaced by explicit `require`/`fail` checks and strict schema validation.

`verification/test_primary_fail_closed.py` tests the valid certificate and
three attacks (bad extension block, bad zero list, and a dropped required key)
under normal, `-O`, and `-O -I`.  All 12 cells now behave correctly: the three
valid cells print PASS and the nine tampered cells exit nonzero without PASS.
The exact source/input hashes for all release verifiers are locked in
`audit/VERIFIER_HASH_LOCK.md`.

## Scope and limitations

The two-pass novelty search found no prior all-order proof or counterexample
in the recorded OEIS, arXiv, DOI/Crossref, OpenAlex, SciNet, GitHub, and exact
web-query scope through 2026-08-29.  This is a bounded search conclusion, not
a guarantee of global priority.  See `literature/claim_ledger.md` and
`literature/search_log.md`.

No proof assistant was used.  The proof is an ordinary mathematical proof
supported by exact Python diagnostics and independent human-style audits.

## Reproduction

Run from the project root:

```bash
python3 certificates/verify_builder_construction.py --max-n 10000
python3 -O -I verifier/verify_zero_set.py verifier/certificate.json
python3 -O -I verification/primary_verify.py certificates/zero_set_certificate.json
python3 -O -I verification/test_primary_fail_closed.py --output verification/primary_fail_closed_results.json
python3 -O -I verification/verify_transfer_automata.py certificates/transfer_automata_certificate.json
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py paper/main.tex paper/references.bib
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py . release/manifest.json
```

Expected result: every verification command reports `PASS`; the transfer
certificate reports threshold \(26\), and the LaTeX audit reports
`cited=4 bib=4 missing=0 unused=0`.

## Static release freeze

The release gate was reopened after an independent audit found build logs in
the source archive and rendered temporary pages in the broad-scan manifest.
The final release now uses two exact, sorted whitelists:

- `release/frozen/source_whitelist.txt`: exactly 41 source-package members;
- `release/frozen/manifest_whitelist.txt`: exactly 43 signed release files,
  adding only the final PDF and final ZIP.

Both member sets have zero `logs/`, `tmp/`, build, cache, bytecode, or TeX
auxiliary entries.  `unzip -t` passes.  The fail-closed static manifest
verifier and the skill's generic manifest verifier both pass.

From a clean extraction of the final ZIP, all four theorem verifiers passed
with byte-identical output in normal and `-O -I` modes.  The primary
fail-closed harness passed in both modes with empty unmet/vulnerability lists,
and the LaTeX audit again reported
`cited=4 bib=4 missing=0 unused=0`.

Final hashes:

| Artifact | SHA-256 |
|---|---|
| `output/source/a383733_zero_set_sources.zip` | `7961a88c13c5920ffa92edda6db1fba1f6d04b48ce000af92ee5bda28f35de57` |
| `release/manifest.json` | `e50ce5b37458a0a32ebeea447be889c7a09de38f04fa50344d07d9c2af57594e` |
| `output/pdf/a383733_zero_set_proof.pdf` | `29d3ce3524c49628d613a749d5c05673eb47b8c69749107f74e8dc8efccce83b` |
| manifest whitelist | `49c04b401f47cc25ace7bf41bb9968bb7b92bb502559f54f117a74cafcc15a9f` |

The live `TASK_STATUS.json`, `FINAL_STATUS.md`, and `research_state.json` are
outside both frozen payloads because they record the final ZIP and manifest
hashes.  Including them would make those hashes self-referential.  This
control-plane exclusion is explicit in `release/frozen/README.md`.

Static release reproduction:

```bash
python3 -O -I release/frozen/build_source_zip.py . \
  release/frozen/source_whitelist.txt \
  output/source/a383733_zero_set_sources.zip
python3 -O -I release/frozen/make_static_manifest.py . \
  release/frozen/manifest_whitelist.txt release/manifest.json \
  --label A383733-zero-set-PROVED-static-2026-08-29
python3 -O -I release/frozen/verify_static_manifest.py . \
  release/frozen/manifest_whitelist.txt release/manifest.json
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py \
  . release/manifest.json
```
