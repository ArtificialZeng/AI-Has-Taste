# Verification report

**PASS.** Search verification and fresh primary-passage replay, with a separate
frozen extraction pass. Job: `primary-20260913-level-rook-fibres-release-8051a1494029`.
Actual verification date: **2026-09-12 UTC** (13 September in Asia/Shanghai).
Citation attempt 1; launch `ec286e12-fc71-4d29-8f1e-d383f62a5779`.

The ledger contains 40 claim records: 13 citation-bearing claims using 12 distinct
references, and 27 mathematical, finite-verification, scope or assistance records.
All 13 citation claims are supported; no missing reference, numerical mismatch,
misquotation or unsupported strengthening remains. The 27 internal records trace
to the displayed proof, the accepted mathematical dossier or the freshly rerun
exact supplement. This release audit does not constitute a new mathematical
acceptance or external peer review.

## Two-stage audit and source coverage

I first read the whole canonical manuscript and extracted its claims, locations
and direct citation keys into `audit/citation-claim-ledger.json`. I then checked
the fixed citation claims C01--C13 in order against the original passages below,
checking identity and version separately from nearby support. Independent source
retrieval requests were batched; semantic review was performed by this worker.
No agents, additional model processes or background research workers were used,
as the job expressly forbids delegation. The user explicitly required this
noninteractive two-stage procedure, so no extraction-confirmation question was
asked. Search templates and primary responses are saved under `audit/sources/`.

There are no indirect cite macros, hidden conditionals, `nocite`-only references,
or externally included TeX chapters. The ordinary body-flow key set exactly equals
the ledger union and the 12 BibTeX/auxiliary keys. Every publication source listed
in `publication.json` was inspected: the two canonical scholarly sources, build
script, supplement README, counter, verifier and exact verification record.
The verifier imports the packaged counter and otherwise uses the standard
library. The counter differs from the frozen implementation only in its module
description; the verifier's mathematical routines are unchanged from the accepted
independent verifier, with standalone import/provenance handling. Standard TeX
packages and fonts are installation dependencies, not omitted authored sources.

The bibliography has one genuinely relevant active-library reference and eleven
non-library references. Its coverage includes the problem origin, normalization,
closest rook formula, structured-capacity and bounded-poset predecessors,
interpolation methodology, bit-model distinctions and the Ehrhart verification
oracle. None is retained merely to fill a quota. No extra citation is needed for
the elementary binomial identities or determinant argument proved in the text.

## Claim-to-source checks

| Claim | Key | Original passage and exact supported scope | Verification |
|---|---|---|---|
| C01 | Barrese2021 | Section 3, paragraph introducing column-height notation: adding zero-height columns preserves the shape. [Primary text](https://arxiv.org/html/1812.00533v2). | Supported paraphrase; the convention prevents padded representations from creating an infinite count. |
| C02 | BLRS2016 | Definition 4 and its following paragraph define reversed level totals, the singleton image and involution on singleton boards. [Author's journal PDF](https://users.math.msu.edu/users/bsagan/Papers/Old/bom-ejc.pdf). | Supported paraphrase; also replayed from the frozen arXiv PDF. |
| C03 | BLRS2016 | Section 6.2, journal p.33 / PDF page 21 explicitly asks about all boards mapping to a fixed singleton. | Supported attribution; the manuscript says the arbitrary-level problem remains unresolved **here**, not that a global open-status theorem was proved. |
| C04 | BLRS2014 | Theorem 5.2, journal p.145 / author PDF page 17 including its cover, counts singleton members of an equivalence class. [Journal copy](https://users.math.msu.edu/users/bsagan/Papers/Old/mrp-jct.pdf). | Exact class distinction; frozen arXiv printed p.15 independently replayed. |
| C05 | BJY2007 | Equation (1) and Section 2.1 define one common capacity n; the matrix B(n) has indices 0 through n and counts paths by its powers. [Original text](https://arxiv.org/html/math/0606163). | Supported paraphrase; matrix size is numeric-capacity dependent. |
| C06 | JYZ2026 | Equations (1)--(4) and Theorem 1.1: common-capacity blocks compress to q+1 height states. [Version 1](https://arxiv.org/html/2607.22008v1). | Supported paraphrase; fresh late-source comparison detailed below. |
| C07 | JWZ2026 | Section 2.1, equations (27)--(30), Proposition 2.1: capacities s,s+1 and two matrices of order s+2. [Version 1](https://arxiv.org/html/2607.14887v1). | Supported paraphrase; no arbitrary-capacity theorem attributed. |
| C08 | CK2024 | Section 3, definition on printed pp.9--10 and Theorem 4, integer alternating sequences in [1,k] with prescribed endpoints; abstract and introduction describe weighted/tableau extensions. [Original v2 text](https://arxiv.org/pdf/2012.03878). | Supported paraphrase; no exhaustive claim about all possible specializations. |
| C09 | JS2014 | Theorem 2.6 and proof, printed p.5: integral order-preserving markings, marked minima/maxima, piecewise polynomiality via a subdivision. [Original text](https://arxiv.org/pdf/1206.4066). | Hypotheses agree with attached lower/upper markers. The displayed theorem does not itself bound variable-poset computation time. |
| C10 | AB2020 | Theorem 3.14, Corollary 3.15 and Remark 3.16, printed pp.10--11: decomposition over all linear extensions for a poset and restriction. [Original text](https://arxiv.org/pdf/1904.06630). | Supported paraphrase. Calling an expansion efficient to program does not state a polynomial bound on its number of terms. |
| C11 | ZVB2020 | Sections 4.1--4.3, Proposition 4.1 and Algorithm 1, PDF pp.5--6: real-variable pieces reconstructed using d+1 distinct samples and interpolation. [PMLR original](https://proceedings.mlr.press/v115/zeng20a/zeng20a.pdf). | Supported methodological attribution; the new counter instead performs discrete sums with its own size proof. |
| C12 | Zeng2026 | Version 1, Section 2.1, paragraph on field-operation versus bit models, live HTML lines 123--128. [Primary text](https://www.preprints.org/manuscript/202608.2160/v1). | Supported paraphrase: element representation and growth require separate charges. No Bézout equivalence/lower bound is imported. |
| C13 | BR2015 | Theorem 3.8, printed p.68 / updated author PDF page 84: integral convex d-polytopes have degree-d Ehrhart polynomial. [Author text](https://matthbeck.github.io/papers/ccdnew.pdf). | Applied to a bounded integral polytope; the article proves unimodularity and P(kb)=kP(b), and allows lower-dimensional cases. |

## Bibliographic identity and version checks

Every retained title, author list, year, venue and supplied DOI agrees with the
identified primary record. The structured audit table in
`audit/citation-source-verification.json` records the source, original/final title,
claim locators and disposition for every key.

* BLRS2016: European Journal of Combinatorics 57 (2016), 13--35,
  DOI 10.1016/j.ejc.2016.03.005; primary journal copy and publisher record.
* BLRS2014: Journal of Combinatorial Theory, Series A 124 (2014), 130--165,
  DOI 10.1016/j.jcta.2014.01.006; author-hosted publisher PDF title page.
* Barrese2021: Electronic Journal of Combinatorics 28(4) (2021), P4.13,
  DOI 10.37236/8435; journal's [primary record](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v28i4p13).
* BJY2007: Discrete Applied Mathematics 155(11) (2007), 1481--1496,
  DOI 10.1016/j.dam.2007.04.001; the [publisher search record](https://www.sciencedirect.com/science/article/pii/S0166218X07000728)
  supplies reported publication fields; arXiv supplies the actual argument.
* JYZ2026 and JWZ2026 are separate arXiv v1 preprints, respectively submitted
  24 July and 16 July 2026; the middle authors are Shuai Yang and Suzhen Wen.
* CK2024: the [arXiv primary record](https://arxiv.org/abs/2012.03878)
  reports European Journal of Combinatorics 121 (2024), 103840. The text read is
  v2, 7 March 2023. No unverified DOI was added.
* JS2014: [SIAM record](https://epubs.siam.org/doi/10.1137/130944849),
  28(3) (2014), 1540--1558, DOI 10.1137/130944849.
* AB2020: [publisher record](https://www.sciencedirect.com/science/article/pii/S0195669820300068),
  European Journal of Combinatorics 86 (2020), 103085,
  DOI 10.1016/j.ejc.2020.103085; authors also confirmed in original arXiv text.
* ZVB2020: [PMLR record and exported BibTeX](https://proceedings.mlr.press/v115/zeng20a.html),
  PMLR 115 (2020), 175--185, 35th UAI conference; 2020 is the proceedings
  publication year. Existing core fields match the original export.
* Zeng2026: Zijian Zeng, Preprints.org version 1, posted 31 August 2026,
  DOI 10.20944/preprints202608.2160.v1; explicitly a preprint, not peer reviewed.
* BR2015: Beck and Robins, second edition, Springer, 2015, confirmed by
  the [author's book page](https://matthbeck.github.io/ccd.html).

A few direct publisher/DOI requests returned access errors. These were not treated
as mathematical findings or missing papers: primary publisher search records,
author-hosted journal PDFs and original arXiv passages supplied the required
metadata and exact support. Before any unavailability assessment, both Crossref
capture globs were enumerated; neither matched any file. No fabricated download
or invented metadata was substituted. Recompiled arXiv title dates are not taken
as submission/version dates. Existing correct BibTeX entries were retained;
JYZ2026 was added from its primary record. No citation key was renamed and no
unrelated entry was deleted.

## Late-source and library disposition

Both supervisor handoffs were read before editing. No bibliography-revision or
fast-completion handoff existed. The late source-update Markdown hash matches
its handoff, and its original PDF was copied into `audit/sources/` with SHA256
`a3a0c578545679e1c3216c6d5d54d60f72848b55e61f6cd743d465a48e96a235`.
Definitions (1)--(4), Theorems 1.1--1.6 and Section 4, printed p.17, were read
against the live primary text. For block size one and common capacity q, its
path count equals the uniform specialization of the manuscript's count (the
terminal bound is redundant except in the one-coordinate convention). Its
recursion and transfer dimension still depend on numeric q; its Ehrhart results
concern scalar dilations. Problem 5 separately asks about periodic/finite-alphabet
capacities. No stated theorem or demonstrated direct reduction there supplies
the accepted arbitrary-individual-capacity binary-input bound. The amendment
acknowledges this actual predecessor while preserving qualified novelty and
the original all-m unresolved status. The previous referee did **not** read this
paper; no such read is attributed to that referee.

The active registry's 49 titles and the nearest methodological entry were read.
Row 14 is the selected paper because polynomial evaluation/interpolation and
coefficient growth are directly relevant to the explicit bit-bound argument.
The exact nearby citation sentence uses `\cite{Zeng2026}` in ordinary body flow.
Its version, DOI and Section 2.1 support were freshly checked; registry metadata
was only a lead. `audit/user-bibliography-selection.json` has the dynamic active
registry/workbook binding, the exact runner-issued attempt and launch, and UTC
date 2026-09-12. The actual installed selection validator passes.

## Scope, finite values and final repairs

The complete theorem, bijection, interpolation normalization and conservative
operation/bit bounds agree with the accepted frozen result-note. The illustrative
three-preimage example and empty cases agree with the formulas. The finite table
has exact values 5,461 capacity vectors; 7,338 shapes in 1,866 fibres; 400 seeded
vectors and 74,587 interval values; 16 large dilations with the listed lengths and
scales. A fresh run of the standalone verifier produces exactly the packaged
JSON. The table is explicitly implementation evidence rather than proof or
priority evidence. AI assistance and separate model review are accurately
disclosed without claiming peer review or formal certification.

The installed gate rejected custom floor/ceiling macros because their replacement
tokens fall outside its supported grammar. Both were expanded literally at every
use; no mathematical content, line count or citation sentence changed. A clean
rebuild and refreeze followed. Normalized extracted PDF text before/after that
repair is identical. The original extracted claim identities and meanings were
retained, contexts/bindings refreshed, and the exact same source locators replayed.
The installed ledger and selection validators pass; the runner-owned
`pre_publish_hook` itself was never invoked. All 14 mathematical snapshot inputs,
`source.md`, `claim.json` and `checkpoint.md` remain byte-for-byte unchanged.

Final mechanical check: 12 TeX citations, 12 bibliography entries and 12 aux keys;
zero missing or unused keys, unresolved citations, duplicate entries or final
TeX/BibTeX warnings. See `audit/bib-key-check.txt`, `audit/build.md` and
`audit/visual.md`. Release digest bindings are in `audit/citations.json`.
