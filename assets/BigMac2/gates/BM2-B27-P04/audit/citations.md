# Fresh citation and claim-support audit

Audit date: 2026-09-09. Release job: `bigMac-00027-p04-release-f90b63d4e5db`.
The requested citation-check skill was applied as an advisory two-pass check,
supplemented by inspection of the manuscript, extracted PDF text, bibliography,
accepted mathematical report, and accessible primary records. The extraction
below was fixed before verification. Because this was a bounded noninteractive
release job, the pass boundary was recorded here rather than paused for input.

## Pass 1: fixed claim extraction

- C01 | The order-eight classification consists of four classes with reduced
  nullities 7, 4, 6, 4, and all admit generating $\mathbb F_2^3$-magic maps |
  existence/statistic | abstract and Theorem 1.
- C02 | The classification used eleven feasible regular classes, all $8!$
  labelings per representative, exact row reduction, and independent coverage |
  statistic/existence | abstract and Section 3.
- C03 | Batal introduced the stated notions and reduced-adjacency criterion and
  proved the regular case for at most two generators, hence cube-free order |
  attribution | Section 1.
- C04 | Batal's result does not cover the order-eight group $\mathbb F_2^3$ |
  comparative/existence | Section 1.
- C05 | The closest inspected prior work is Batal's framework; the paper claims
  only a bounded comparison, not general priority | ranking/attribution |
  Section 1.
- C06 | The two user-workbook papers use canonical or symmetry-reduced finite
  enumeration, exact arithmetic, and independently checkable verification, but
  do not prove a distance-magic result | attribution/comparative | Section 1.
- C07 | Generating $\mathbb F_2^3$-magic maps are equivalent to reduced binary
  nullity at least two | existence | Lemma 2.
- C08 | Ordinary distance-magic regularity forces even degree, leaving degrees
  0, 2, 4, 6 | statistic/causal | Section 3.
- C09 | The degree-wise representative and labeled counts are
  $(1,1),(3,3507),(6,19355),(1,105)$ | statistic | Section 3.
- C10 | `geng` generated the unlabeled representatives | attribution/existence |
  Section 3.
- C11 | The eleven-row table gives exact labeling counts and reduced ranks and
  nullities | statistic | Section 3.
- C12 | The displayed part-labelings have constants 9, 18, and 27 as stated |
  statistic | Section 3.
- C13 | The independent verifiers repeat 443520 labeling tests, check binary
  ranks and row operations, and use exact rather than floating-point arithmetic |
  statistic/existence | Section 4.

## Pass 2: verification

- C01, C02, C07--C09, and C11--C13: verified exactly against the accepted
  mathematical reconstruction in `audit/math.md` and the frozen certificate
  evidence named by `claim.json`. The manuscript neither enlarges the accepted
  theorem nor converts computation into proof.
- C03: verified against the official arXiv record for Ahmet Batal,
  arXiv:2609.05934v1. Its abstract states the generating and affinely generating
  criteria, the generating group-distance-magic conjecture, the two-generator
  regular theorem, and the cube-free consequence. Author, title, identifier,
  version, and 5 September 2026 submission date agree with `references.bib`.
- C04: verified as a direct scope comparison: $\mathbb F_2^3$ needs three
  generators and order eight is not cube-free. The manuscript also proves the
  needed specialization directly, so no unsupported dependence remains.
- C05: acceptable bounded novelty language. It says “closest inspected” and
  expressly disclaims priority beyond the comparison; it makes no global
  firstness or literature-exhaustion claim.
- C06: verified against the official Preprints.org abstract for DOI
  10.20944/preprints202608.1658.v1 and the SSRN paper record for DOI
  10.2139/ssrn.7385138. Their abstracts support the narrow methodological
  comparison and concern ternary finite geometry and whiskered-graph Lefschetz
  questions, respectively, not distance-magic graphs.
- C10: McKay and Piperno's primary arXiv record confirms the title, authors,
  nauty/Traces program context, and the journal metadata in the bibliography;
  the local frozen producer record establishes this run of `geng`. Independent
  orbit and labeled-recursion coverage means the theorem does not rely solely
  on the generator's class count.

## Bibliography and dependency findings

All four citation keys used by `article.tex` are defined in
`references.bib`, appear in the generated bibliography, and are resolved in
the extracted and rendered PDF. No citation is contradicted, misleading, or
used to support the new theorem. The two user-selected records were retained
with `metadata_basis=user_designated_workbook`, specifically the workbook and
rows documented in `literature/user_bibliography_check.md`; bounded external
refresh also located matching official abstract pages. The DOI resolver's
403/safe-URL behavior did not override those authoritative records.

The publication dependency scope is complete: the manuscript imports no local
authored file beyond `manuscript/article.tex` and
`manuscript/references.bib`. System LaTeX packages are outside the required
source list. Verdict: **accept**.
