# Claim ledger — frozen claim list before search

Initial cutoff: 2026-08-29; release rerun cutoff: 2026-08-30
(Asia/Shanghai).  Status values below are deliberately
`UNVERIFIED` until supported by a primary source.  “Not found” will be bounded
to the recorded databases and queries.

| ID | Claim | Type | Status | Source/location | Confidence | Consequence if false |
|---|---|---|---|---|---|---|
| C01 | Ambrus–Gárgyán's paper is published in *Advances in Mathematics* 441 (2024), article 109524, with the stated title and authors. | exact metadata | VERIFIED | Crossref DOI record; publisher VOR title page, p. 1; `sources/root/ambrus_gargyan_2024_vor.pdf` | 100% | None. |
| C02 | The formal DOI is `10.1016/j.aim.2024.109524`. | exact metadata | VERIFIED | Crossref and Elsevier/ScienceDirect records; VOR p. 1 | 100% | None. |
| C03 | arXiv:2307.03792 is the corresponding preprint; identify its latest version/date and whether it differs mathematically from the journal version. | exact metadata | VERIFIED WITH VERSION NOTE | arXiv reports v4, updated 2024-01-29, DOI linked, comment “Final version.” Principal endpoints agree with the VOR, but v1 has an incorrect displayed \(J_n(r)\) formula and v3→v4 contains proof-level corrections (including an interval endpoint and the Section 6 Hessian calculation). This was not a bytewise VOR/v4 diff. | 99% | Use only the VOR or arXiv v4; earlier versions are unsafe substitutes. |
| C04 | Conjecture 1.3 says that all locally extremal central hyperplane sections of the cube are diagonal, with “diagonal” as used in the source. | exact theorem wording | VERIFIED | VOR pp. 2–3, definition (1.2) and Conjecture 1.3 | 100% | The user's implication matches the source. |
| C05 | For every \(n\ge4\), the paper constructs non-diagonal critical central sections. | paraphrase | VERIFIED | VOR p. 3, Theorem 1.2 (indeed full-support/nonzero coordinates) | 100% | None. |
| C06 | The selected non-diagonal family used to prove Theorem 1.2 is proved to consist of saddle points. | paraphrase | VERIFIED WITH SCOPE | VOR Section 6, pp. 23–25: the selected \(v_{n,2}(\xi_n)\) has an increasing direction inherited from its one-parameter local minimum and a strict negative Hessian direction (6.1)–(6.4). The paper does **not** classify every zero of \(F_{n,2}\) or every non-diagonal critical point. | 99% | Do not broaden this to all non-diagonal critical points. |
| C07 | The literature gives a complete classification of critical directions for \(n=4\), with the sole non-diagonal orbit represented by \((1,1,2,2)/\sqrt{10}\), and the corrected literature makes it a saddle. | paraphrase | VERIFIED; INDEPENDENT BASELINE REPRODUCED | G. Ambrus, *Proc. AMS* 150 (2022), Theorem 3, DOI 10.1090/proc/15955, arXiv:2107.14778v3; AG24 v4/VOR Section 6 for the robust saddle conclusion. The 2022 proof invokes undisclosed CAS and older public copies contained erroneous ambient-Hessian conclusions. This project independently obtains the intrinsic tangent eigenvalues \(-5\sqrt{10}/12,-25\sqrt{10}/24,+5\sqrt{10}/24\); see `proof/agent_builder_report.md` and `src/builder_verify_formulas.py`. | 99% | Use the project certificate, not the old ambient-Hessian list. |
| C08 | As of the cutoff, no public work was located that completely classifies the local extrema or all critical directions for \(Q_5\), and no published non-diagonal local extremum was located. | novelty claim | NOT FOUND AFTER GATES 1–2 (DATABASE-BOUNDED) | Exact-title, exact-endpoint, algebraic-fingerprint and terminology queries in arXiv, Crossref, Semantic Scholar, OpenAlex, Google Scholar, GitHub and general web; latest versions and all citation-index hits listed in `search_log.md` were scope-checked in primary text. | 94% | “Not located” is not a proof of nonexistence; an omitted, unindexed, differently worded, or non-public result could change originality. |
| C09 | The displayed truncated-power formula in `problem/formal_statement.md` equals the central section volume, including the support-reduction convention. | exact formula | VERIFIED BY INDEPENDENT DERIVATION | Coarea gives \(\sigma(a)=\|a\|f_{\sum a_iU_i}(0)\); translating \(U_i\sim\mathrm{Unif}[-1/2,1/2]\) to \([0,a_i]\) and inclusion–exclusion gives the displayed box-spline density. Zero coordinates factor off a unit cube. A second evaluator is still required for decisive computations. | 99% | Formula may be used as a proved structural lemma after it is written out in the proof report. |
| C10 | There is public author code/data for the 2024 paper, or there is none discoverable through the recorded searches. | resource claim | NO AG24/Q5-SOLUTION CODE FOUND (BOUNDED) | Exact title, arXiv ID, author/title+code, exact radical and \(Q_5\)-endpoint searches; GitHub repository API returned zero repositories for the recorded queries, while unauthenticated code search was unavailable. Neither the VOR nor arXiv record links code/data. The located repository `RainCamel/slab_of_the_poly_norms` belongs to arXiv:2603.25643 and is explicitly scoped to that paper's at-most-four-dimensional computations, not the present \(Q_5\) result. | 88% | Baseline must be independently implemented; absence is not asserted globally. |
| C11 | No later work located as citing the 2024 article settles the \(Q_5\) classification. | novelty claim | NOT FOUND AFTER GATES 1–2 (CITATION-INDEX-BOUNDED) | Google Scholar and Semantic Scholar each exposed four citing works; OpenAlex exposed one. The latest primary versions of all four were checked. Direct search additionally found Brandenburg–De Loera–Luo–Meroni, arXiv:2603.25643v2, which cites AG24 but was absent from those cited-by lists; it stops at dimensions \(\le4\). | 97% | Citation indexes demonstrably lag; a missing or differently linked citing work could change the conclusion. |
| C12 | Signed permutations and antipodal identification reduce the search to \(a_1\ge\cdots\ge a_5\ge0\). | inference/exact reduction | PROVED | Signed permutation matrices are orthogonal symmetries of \(Q_5\) and preserve Hausdorff volume; take absolute values then sort. | 100% | None. |
| C13 | The pre-2025 claim that every diagonal section is locally extremal for \(n\ge4\) is false; for \(3\le k\le n-1\), the \(k\)-diagonal central section is not locally extremal. | post-freeze correction | VERIFIED | Ambrus–Gárgyán, *Bull. LMS* 57 (2025), Theorem 1.4, DOI 10.1112/blms.70157; Pournin erratum, DOI 10.1007/s11854-025-0384-1, explains the missing Hessian term. | 100% | **Repairs the requested classification:** in \(Q_5\), \(d_3,d_4\) are known non-extrema; diagonal local extrema are \(d_1\) (global min), \(d_2\) (global max), and \(d_5\) (strict local max). |
| C14 | The closest located 2026 chamber-method paper does not solve the requested \(Q_5\) endpoint. | frontier scope | VERIFIED WITH DATABASE BOUND | Brandenburg–De Loera–Luo–Meroni, *Critical moments of slices and slabs of the cube (and other polyhedral norms)*, arXiv:2603.25643v2 (2026-07-01). It catalogues rational formulas for the four-cube and its critical analysis there is explicitly partial; no five-cube local-extremum classification is stated. | 98% | Confirms, but cannot absolutely prove, that the present endpoint remains open. |
| C15 | No public prior result was located that classifies the full-support critical directions of \(Q_5\), up to signed permutations and antipodes, as exactly \(d_5\) and \(v_\alpha=(\alpha,\alpha,1,1,1)/\sqrt{2\alpha^2+3}\), where \(\alpha=(24+\sqrt{69})/13\). | exact-result novelty claim | NOT FOUND AFTER GATE 2 (DATABASE-BOUNDED) | Gate 2 exact theorem wording, coordinate-pattern, radical, and elimination-polynomial queries; current arXiv topic corpus and latest primary versions; Crossref/Semantic Scholar/OpenAlex/Google Scholar; public-web and GitHub queries, all detailed in `search_log.md`. | 95% | This is an originality assessment, not a mathematical premise; a prior unlocated result would affect novelty but not correctness. |
| C16 | No public prior result was located that classifies **all** locally extremal central sections of \(Q_5\), up to signed permutations and antipodes, as exactly the diagonal types \(d_1,d_2,d_5\). | exact-result novelty claim | NOT FOUND AFTER GATE 2 (DATABASE-BOUNDED) | Same Gate 2 search, supplemented by the 2025 diagonal-extremality paper/poster: it supplies the diagonal status but does not classify non-diagonal \(Q_5\) directions. | 95% | A prior unlocated complete classification would affect originality but not the project's independent proof. |

## Gate 1 decision

`NOVELTY_LOCK = LOCKED_WITH_DATABASE_BOUND` on 2026-08-29.  The exact
mathematical problem remains open in the searched primary/public record, but the source
motivation required correction C13.  Any later originality statement must repeat the
novelty search after a rigorous result is obtained.

## Gate 2 decision (exact proved endpoints)

`NOVELTY_LOCK_GATE_2 = LOCKED_WITH_DATABASE_BOUND` on 2026-08-29 for C15
and C16.  No public prior statement of either exact endpoint was located in the
recorded searches through the cutoff.  This bounded negative result supports an
originality claim only in the form “no prior result was located”; it does not establish
that no unpublished, unindexed, inaccessible, or differently phrased result exists.

## Release-phase novelty rerun

`NOVELTY_LOCK_RELEASE = LOCKED_WITH_DATABASE_BOUND` on 2026-08-30 for C08,
C11, C15, and C16.  The rerun repeated exact theorem, coordinate-pattern,
minimal-polynomial, author, citation-index, arXiv, Crossref, OpenAlex,
Semantic Scholar, public-web, and public-code queries.  No prior complete
classification of the critical or locally extremal central sections of
\(Q_5\), and no non-diagonal local extremum, was located.  The closest new
primary work remained Brandenburg--De Loera--Luo--Meroni,
arXiv:2603.25643v2 (updated 2026-07-01), whose explicit cube catalogue and
critical-point analysis stop at dimension four.  This remains a bounded
database statement: unindexed, inaccessible, unpublished, differently worded,
or later work is outside the lock.
