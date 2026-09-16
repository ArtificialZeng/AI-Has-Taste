# Bounded literature and duplicate screen

Job: newwin-00001-p02-triage-ba81b5c3d443. Retrieved/inspected: 2026-09-12.

## Primary statement and nearest prior work

1. Jia Huang and Erkko Lehtonen, *Associative-commutative Spectra for Some Varieties of Groupoids*, ECA 4:4 (2024), Article S2R29. [Journal PDF](https://ecajournal.haifa.ac.il/Volume2024/ECA2024_S2A29.pdf). Independently inspected the supervisor-cached primary text at Definition 1.1 (p. 1) and Section 7 (p. 17), copied into `primary-extract.md`. The journal PDF web open returned an internal error, so it was not treated as a successful fresh download. The source table, fixed-order definition and nine reported terms all agree with source.md. The paper describes these examples as lacking a general result. Its listed identities are leads, not a proof of the recurrence.

2. [Author preprint, arXiv:2401.15786v1](https://arxiv.org/html/2401.15786v1), dated 2024-01-28. Live full HTML was inspected at Definition 1.1 (rendered lines 44–53), Table 1.2 (lines 160–189), and Section 7 (lines 824–851). The latter repeats the SC258 table and finite observation with no general formula. The [abstract/version page](https://arxiv.org/abs/2401.15786) listed only v1 at retrieval. Attempts at v2/v3 URLs failed and add no mathematical evidence. The journal's Section 7 and the live preprint agree on this target.

3. [OEIS A034943](https://oeis.org/A034943), inspected the formula and example sections (rendered lines 81–105) and linked references. The sequence b_n starts at n=0 with 1,1,1,2,5,12,... and has recurrence b_n=3b_(n-1)-2b_(n-2)+b_(n-3). Thus the conjectured a_n equals b_n for n>=1, with no index shift in n. The recorded generating function for b is (1-2z)/(1-3z+2z^2-z^3); subtracting b_0=1 yields the generating function in problem.md. This establishes which known sequence is intended; it does not identify SC258 term functions with that sequence.

## Current search scope

Live queries included `"SC258" "spectrum"`, `Huang Lehtonen associative spectra three-element groupoids Padovan`, `"SC258" Padovan recurrence`, `"SC685" "associative"`, `"associative spectrum" "Padovan"`, `"SC258" groupoid recurrence` (restricted to arxiv.org and ecajournal.haifa.ac.il), `"Padovan" "groupoids"`, and `"SC685" spectrum proof`. Inspected the relevant primary source above rather than relying on snippets. Broad SC-number searches also returned unrelated products and were not evidence. No later equivalent resolution was found in this bounded screen. This is not a guarantee about unindexed literature or priority.

Source status: **open-supported**, based on the primary paper's explicitly unresolved example; current nonresolution is supported only within the stated search scope. No known proof or disproof of the original all-n claim was verified in this job.

## Historical comparison

Independently screened the live local registry: 627 rows, hash and matches in `registry-screen.json`. Anchors included SC258/SC685/SC1594/SC1600, Padovan, bracketing, term-function, associative-spectrum, groupoid and magma. The exact matching target is this project's own intake record. Other hits concern Lie brackets, Galois computations, primitive groups or braces, with different objects and quantifiers; none is the same finite-algebra spectrum claim. The supervisor's candidate-specific desktop and dedup paragraphs were read as leads. Its two smallmac neighbors describe finite-magma identities and weakly-centred groupoids, but those original records were not retrieved in this job. The 2883-row Excel screen and unavailable live conversation history were not independently rerun. No exhaustive deduplication claim is made.

No `literature/*handoff*.md` files existed at intake.

## Suitability decision

Advance. Nearest prior result: the published nine-term observation. Proposed delta: exact all-n recurrence via coverage, separation and enumeration of pruned labeled trees, or an exact counterexample. Available verifier: full truth-table dynamic programming, already executed through n=10, plus a finite pruning-separation pilot through n=8. Remaining substantive work: all-n separation and a complete enumeration of attainable pruned trees. Finite agreement and the elementary pruning lemma alone do not qualify as a result-note or resolution-paper.
