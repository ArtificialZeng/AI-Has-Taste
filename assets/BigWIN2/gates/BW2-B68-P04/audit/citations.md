# Verification Report

**Mode:** Search verification and frozen accepted-proof scope comparison.
**Document:** manuscript/main.tex and manuscript/references.bib.
**Release job:** win-00068-p04-release-8022f2ea8df8.
**Citation attempt:** 7; launch 7d2fa8cf-75e9-4ed1-af49-e35e25f004b1.
**Date:** 2026-09-08 UTC.
**Overall status:** PASS within the stated scope.

| Metric | Count |
|---|---:|
| Frozen substantive claim blocks | 21 |
| Verified | 21 |
| Bibliography entries | 7 |
| Natural non-library sources | 6 |
| Selected active-library sources | 1 |
| Unsupported claims, numerical errors, undefined citations | 0 |

Pass 1 read the entire repaired manuscript and froze the 21 claim blocks before formal attempt-7 verification. Pass 2 then checked those fixed IDs in order against primary texts freshly opened on 2026-09-08 and the accepted mathematical audit. No interactive questions or delegated agents were used, as expressly requested. Definitions and assistance-process descriptions were excluded as directed by the citation skill; all substantive mathematical assertions were included.

| ID | TeX lines | Direct keys | Verification and exact location |
|---|---|---|---|
| C01 | 32-45 | Own accepted proof | Abstract matches the accepted finite-curvature domain, complete cell treatment, global forward dynamics, equilibrium list and sorted limit trichotomy. audit/math.md: Scope reconstructed; Exhaustive dynamics. |
| C02 | 50-53 | LinLuYau2011, Ollivier2009 | Ollivier defines transportation-based curvature; Lin, Lu and Yau define the limit as idleness tends to one. Ollivier Definitions 2-3, PDF p.5; Lin-Lu-Yau Section 2 following Lemma 2.2, author PDF p.6. |
| C03 | 54-57 | BaiLinLuWangYau2024 | The earlier graph flow uses induced endpoint distance and removes an edge exceeding that distance. Bai et al. equation (4), Definition 3 and Section 3 exit condition (I), publisher PDF pp.2,4,8-9. |
| C04 | 58-61 | BaiHua2026 | The dated tree paper provides the inverse-weight definitions and normalized flow, and states the cycle question. Bai-Hua v1 Introduction final paragraph before Main results; Section 2 equations (2.1)-(2.2), curvature definition and (2.5)-(2.8). |
| C05 | 63-67 | Own accepted proof | The manuscript confines its theorem to the literal triangle problem and derives cyclic transport rather than using a tree theorem. source.md and audit/math.md: Scope reconstructed; Transport calculation. |
| C06 | 106-128 | Own accepted proof | Substitution gives the three imbalances and their zero sum. The two epsilon bounds ensure the first source and second sink signs. audit/math.md: Transport calculation; evidence/verify_edge12_lp.py. |
| C07 | 134-156 | BaiLinLuWangYau2024 | The source supplies the finite coupling primal and Lipschitz dual; this manuscript supplies and checks its own two feasible witness pairs. Bai et al. Section 2 Definitions 1-2 and following dual formula, publisher PDF p.4; audit/math.md: Transport calculation. |
| C08 | 158-179 | Own accepted proof | The two branches, branch difference, min/max formula and six weak ordering chambers agree with the accepted certificates. audit/math.md: Transport calculation; evidence/verify_edge12_lp.py. |
| C09 | 181-196 | Own accepted proof | The tied-edge substitution yields the finite formula. A longer edge gives limiting transport cost 1-a and positive numerator (2a-1)/a. audit/math.md: Transport calculation. |
| C10 | 200-213 | Own accepted proof | The ordered curvature formulas and zero simplex-sum derivative match the accepted exact chamber identities. audit/math.md: ODE and boundary audit; evidence/verify_chamber_dynamics.py. |
| C11 | 215-223 | Own accepted proof | Every pair sum is at least 1/2 on the compact closure, so the displayed min/max expression admits a locally Lipschitz neighborhood extension. audit/math.md: ODE and boundary audit. |
| C12 | 224-226 | Teschl2012 | The cited results give local classical uniqueness for a locally Lipschitz field on an open set and continuation from compact containment. The manuscript proves those hypotheses. Teschl Theorem 2.2, printed p.38 (PDF p.49); Corollary 2.15, printed p.52 (PDF p.63). |
| C13 | 228-252 | Own accepted proof | Permutation equivariance and the exact geodesic-wall identity give invariant walls; bounded exponential coordinate multipliers preserve positivity and permit continuation. audit/math.md: ODE and boundary audit; evidence/verify_chamber_dynamics.py. |
| C14 | 257-263 | Own accepted proof | The proposition restates the accepted well-posed region and invariant strata without assigning inverse-weight measures at zero. claim.json; audit/math.md: ODE and boundary audit. |
| C15 | 268-292 | Own accepted proof | Exact log-ratio, largest-coordinate and median equilibrium factors are reproduced by the frozen chamber script, yielding exactly four labelled equilibria. audit/math.md: Exhaustive dynamics; evidence/verify_chamber_dynamics.py. |
| C16 | 295-297 | Own accepted proof | An initial label permutation and invariant equality walls preserve the weak ordering. audit/math.md: ODE and boundary audit. |
| C17 | 299-312 | Own accepted proof | On the equal-minima median the exact scalar field is negative for 1/4<s<1/3; the lower limiting zero is 1/4, including its fixed endpoint. audit/math.md: Exhaustive dynamics; evidence/verify_chamber_dynamics.py. |
| C18 | 314-327 | Own accepted proof | The ratio has a strictly positive lower derivative bound if bounded. Its divergence and b<=1/2 force c to zero; the two remaining upper bounds force the displayed limit. audit/math.md: Exhaustive dynamics. |
| C19 | 333-348 | Own accepted proof | The final theorem matches all three accepted sorted cases, their labelled permutations and singleton omega limits, with degeneration only at infinite time. claim.json and audit/math.md: Exhaustive dynamics. |
| C20 | 353-360 | 10.7717/peerj-cs.103 | The software paper explains exact rational simplification and factorization. Both local scripts were read and replayed; the analytical arguments remain separate. SymPy authors repository simplification.tex, paragraph on factor and table entries factor/cancel; audit/attempt2-script-replay.json. |
| C21 | 362-368 | ZengTuza2026 | The selected preprint explicitly separates finite reduction from paired feasible cover/packing certificates checked by an independent verifier. The comparison concerns this verification design only. Zeng v1 Introduction immediately following Theorem 1, HTML lines 114-115; Section 4 Exact verification, line 229. |

## Bibliography coverage and correctness

Seven retained works support actual uses: curvature origins (Ollivier; Lin-Lu-Yau), the preceding general graph flow and finite transport formulation (Bai et al.), the inverse-weight tree problem origin (Bai-Hua), ODE existence and continuation (Teschl), symbolic verification (SymPy), and the concrete paired-certificate comparison (Zeng). No additional mathematical method is imported without its natural source. The present explicit primal/dual witnesses need no black-box LP solver citation. No bibliography quota or decorative reference was used.

The active 49-entry first-sheet registry was read, all titles screened, and candidate abstracts for rows 9, 15, 20, 30 and 48 compared. Row 30 is the best fit for the specific paired feasible-witness design discussed in Section 5; its v1 full text, author, posting date and nearby support were independently inspected. It is the sole gate-bound minimum selection. Six non-library sources provide the subject and method bibliography. Selection metadata, literal citation context and the current registry/workbook digests are in user-bibliography-selection.json.

The complete publication source dependency set is main.tex and references.bib. Direct body keys, ledger union, bibliography keys and auxiliary keys agree exactly. There are no hidden conditionals, inert citation macros, comments carrying citations, nocite uses, TeX includes or figures. Standard installed TeX packages and the plain bibliography style are build dependencies.

No TeX or BibTeX entries or keys were changed in this attempt. Existing verified entries were retained. SymPy agrees with its authors' supplied BibTeX; the other entries were checked against the original journal, author or versioned preprint records. Teschl's volume 140 and ISBN are confirmed by the author-owned book record. No source field was invented and no failed export was replaced with guessed BibTeX.

See attempt7-source-verification.md and attempt7-mandatory-searches.md for original URLs, precise passages, record checks and the complete applicable query suite. The cycle statement is attributed to Bai-Hua v1, not asserted as an unrestricted current open-status theorem. The bounded current title/topic search found no equivalent literal triangle classification in the consulted results; it is not proof of priority. The accepted mathematics and every frozen file remain unchanged.

## Build and access checks

The forced-clean latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex build converged to a six-page PDF. The gated final log `audit/build.log` and converged BibTeX log contain no undefined citations/references, missing entries, repeated entries, fatal errors or box warnings. The bibliography checker resolves all seven keys; both frozen SymPy scripts replay successfully. Build and direct six-page image review are recorded separately.

All needed original substantive passages were obtained through browser tools. Author, journal, publisher, and versioned-preprint texts and records supplied the relevant support. Before treating any endpoint as unavailable, `literature/bibliography-revision-*.md` and `literature/crossref-*.json`/`*.md` were enumerated. No matching revision or Crossref capture exists; `literature/` contains only the earlier operational timeout handoff. No endpoint failure or time budget was interpreted as a mathematical result.
