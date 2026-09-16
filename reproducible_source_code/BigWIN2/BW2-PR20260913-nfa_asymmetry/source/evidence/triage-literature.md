# Literature and scope check

Job: primary-20260913-nfa-asymmetry-triage-46dc24ebd607.
Retrieval/inspection date: 2026-09-13 Asia/Shanghai (2026-09-12 UTC).

## Inspected sources

- John W. Nicol, *Further Remarks on Separating Words*, arXiv:2608.30928v1.
  [Live HTML](https://arxiv.org/html/2608.30928v1) Section 4, Section 4.1,
  Theorem 6 and its full proof were read. The definition has one initial state,
  arbitrary final subset, partial transitions, and no epsilon transitions.
  The displayed bounds are (q-1)^2+1<=A(q)<=2^q, q>=3, followed by the explicit
  open growth question. Section 4.2 concerns deterministic versus
  nondeterministic separation, not directional nsep. The
  [live submission record](https://arxiv.org/abs/2608.30928) lists only v1,
  submitted 31 August 2026. The local original PDF/HTML hashes match the frozen
  source and handoff. Source status: **open-supported** within checked coverage.

- Pavol Zajac and Matus Jokay, *Computing Indexes and Periods of All Boolean
  Matrices up to Dimension n=8*, Computing and Informatics 31 (2012), 1329-1344.
  The supplied original `literature/boolean-matrix-index-cai.pdf` was read at
  physical pp.1-3 and reference list. Theorems 1-2 on printed p.1331 explicitly
  give universal index (n-1)^2+1 and universal period as the lcm of lcms of all
  partitions of n. Reference [6] is Schwarz 1974. Use the stated theorems and
  the normal definition of eventual period; Definition 1's extracted expression
  is malformed and was not used as a formula. The
  [publisher PDF](https://www.cai.sk/ojs/index.php/cai/article/download/1310/485/3294)
  timed out in live retrieval; the byte-verified supplied PDF was accessible.

- Stefan Schwarz, *Sums of Powers of Binary Relations*, Matematicky casopis
  24(2) (1974), 161-171, Russian. The
  [DML full bibliographic record](https://www.dml.cz/handle/10338.dmlcz/126603?show=full)
  was opened and its title, author, year, pages and PDF link checked. The PDF
  request timed out; alternate host access failed. Local urllib retrieval was
  denied by the network sandbox. No original proof was read and no PDF was
  saved. This is a source-verification gap, not a mathematical obstruction.
  The [1970 Schwarz record](https://dml.cz/handle/10338.dmlcz/100989) and its
  image-only PDF were also located, but no decisive theorem was successfully
  inspected there. Do not describe either original as proof-checked.

- Demaine, Eisenstat, Shallit and Wilson, *Remarks on Separating Words*.
  The [author PDF](https://erikdemaine.org/papers/WordSep_DFCS2011/paper.pdf)
  was opened live. Its Section 6's asymmetry example and unbounded-difference
  question are prior context, with the latter already resolved by Nicol.
  Its early prefix-separation and unary-periodicity facts are consistent with
  the elementary separators used here. The supplied two-state calibration was
  not rerun or enlarged; it is not a new contribution.

## Bounded search coverage

Queries used exact/equivalent terms: `"A(q)" "nsep"`,
`"separating words" "asymmetry" nondeterministic`,
`"nondeterministic separation" "one" "quadratic"`,
`"nsep" "single" "marker"`, `"nsep" "quadratic" "Nicol"`,
`"separating words" "one-marker"`,
`"nondeterministic separation" "Schwarz"`, and
`"directional" "separation" "Nicol" automata`.
Many results were unrelated physics/communication-complexity pages; these were
discarded. No equivalent one-marker extremal formula or later resolution of
A(q) was found in the inspected primary sources. Search snippets and mirrors
were used only as leads. This is not a comprehensive priority or openness claim.

The proposed one-marker extremal quantity has status **new-question** in this
project; its novelty remains unverified. Its relevance is that it includes the
entire published family giving the quadratic directional lower bound.

## Historical comparison and handoff validation

Enumerated `literature/*handoff*.md`: only `outer-intake-handoff.md` was present;
it and the referenced admission were read. The published statement and matrix
theorem reports were checked directly, not accepted on handoff authority.

`triage-registry-screen.json` records an independent decoded keyword screen of
the current 642-row historical registry, including the current job's own row.
The six returned records were read and compared. The closest earlier record,
win-00087-p06, minimizes word length merging states in a fixed DFA family;
this project minimizes NFA state count accepting one given word and rejecting
another. They have different objects, variables, quantifiers and targets.
Other hits concern unrelated geometry, lattice walks or subtree polynomials.
The current job's own row is the exact match and was excluded as a duplicate.
The handoff's earlier 641-row hash predates that self-entry.

This worker did not independently reread the Windows Excel payloads or target
conversation. The handoff's broader exclusion claim remains attributed to the
supervisor; no complete new dual-source deduplication claim is made.
