# Verification Report

Mode: primary-source search verification, with the accepted local proof used for mathematical scope transfer.
Document: manuscript/main.tex and manuscript/references.bib.
Release job: primary-20260914-triangular-square-roots-release-774ca875bd99. UTC verification date: 2026-09-14.

**PASS:** 27 extracted claim groups verified; 6 references and all 9 ordinary citation occurrences checked. No numerical error, unverified nearby citation, misleading attribution, hallucination or undefined citation remains. This is a release audit, not a new mathematical referee verdict.

The extraction was frozen before source verification in audit/citation-claim-ledger.json. The later corrections change only TeX syntax and headings: a direct library citation, canonical bibliography basename, plain subsection labels and a Unicode accent. Claim texts, ids, locations and key sets remain unchanged. Reports were rebound after the final clean build and manuscript freeze.

## Citation and bibliography coverage

| Key | Primary record and precise support | Retained purpose |
|---|---|---|
| MaoWang2026 | [The Narayana transformation](https://arxiv.org/html/2607.01572v1); PDF p.10: definitions of A and D; PDF p.11: D-square recurrence, initial rows, Conjecture 4.1; HTML Section 4, parsed lines 358–421; Conjecture 4.15 | Original conjunction, definitions and D-square recurrence |
| WangZhengChen2019 | [Analytic aspects of Delannoy numbers](https://www.sciencedirect.com/science/article/pii/S0012365X19301141); Publisher abstract, root-interval and density sentence; publisher bibliographic header | Closest ordinary-row interval and density result |
| ChenZhangPan2026 | [Analytic Aspects of Weighted Delannoy Numbers](https://www.mdpi.com/2227-7390/14/6/1039); Section 1, positive weights a,b,c and Theorem 1; Section 2, Lemma 1 and first characteristic-equation paragraphs of the proof of Theorem 1 | Weighted ordinary-row result and characteristic-root method |
| LiuWang2007 | [A unified approach to polynomial sequences with only real zeros](https://arxiv.org/pdf/math/0509207); Theorem 2.1 and proof, printed/PDF p.4, parsed PDF lines 160–193 | Alternating-sign method in its interlacing setting |
| SymPy2017 | [SymPy: symbolic computing in Python](https://github.com/sympy/sympy-paper); Authors’ source repository, recommended citation and BibTeX, parsed lines 225–251 | Symbolic computation software actually used |
| Zeng2026Evaluation | [Generic Characteristic-Zero Equivalence Between Derivative Bézout Inversion and Multipoint Evaluation](https://www.preprints.org/manuscript/202608.2160); Section 4, definitions preceding Theorem 4.1; parsed lines 209–219; Section 2.1, field-operation versus bit-cost paragraph; parsed lines 123–128; Primary header: author, v1, date and preprint status | Evaluation operation actually used and its bit-cost limitation |

Every entry supports a natural nearby claim. Five sources are outside the active 49-record library by DOI/title identity; the bibliography is neither library-only nor padded to a reference count. The main proof is self-contained in elementary recurrence, quadratic-root, phase and continuity arguments; no unmentioned preservation theorem or advanced computational algorithm is invoked.

The one selected library item is row 14. Its Section 4 addresses polynomial evaluation at supplied nodes, the actual operation in the exact sign checker. The manuscript explicitly makes no fast-algorithm claim, and Section 2.1 supports the bit-cost qualification. A second library paper has no additional natural use here. Selection is bound to the dynamically validated 49-record registry, the current attempt/launch and literal lines 297–299. The actual UTC date, rather than a local date, is recorded.

All six retained bibliography entries agree with primary title/author/year/version/venue metadata. The SymPy entry includes all 27 authors. No BibTeX entry was replaced, no citation key changed, and no unavailable official export was synthesized. Only manuscript/main.tex and its build README needed compatibility corrections; manuscript/references.bib is byte-identical to the writing snapshot.

The 2019 attribution is limited to its successfully received publisher-indexed abstract. Weighted Delannoy theorem and method passages were received from the indexed publisher text. Direct page openings failed; this is not called full-PDF access. The Zeng article's live primary header and Sections 2.1 and 4 were inspected. Its version-specific DOI matches the saved Crossref work data, parsed independently; a fresh API/DOI response could not be obtained. The retained raw response has status `ok`, declared source Crossref and the matching primary v1 URL; it lacks an HTTP provenance wrapper, which is not invented. See audit/citation-search-log.json and audit/release-http-attempts.json for exact access scope. None of these limits is converted into a mathematical conclusion or an exhaustive priority claim.

## Fixed claim-by-claim second pass

| Claim | Manuscript lines | Finding |
|---|---|---|
| C01 | 23–33 | Verified: Abstract retains every accepted quantifier, interval endpoint and simplicity claim, and expressly leaves the Eulerian component unresolved. |
| C02 | 49–53 | Verified: The path definition, shifted Eulerian index and conjunction match the original source verbatim in scope. |
| C03 | 55–62 | Verified: The main theorem equals the accepted statement, including n=0 and open endpoints. |
| C04 | 64–66 | Verified: Interval endpoints and density in the closure match the abstract exactly; no stronger comparison is attributed. |
| C05 | 66–70 | Verified: The source treats positive-weight ordinary rows with distinct real roots and an interval; the manuscript makes no matrix-square inference from that theorem. |
| C06 | 72–78 | Verified: All four recurrence terms, the range n>=4 and all four initial polynomials agree term by term. |
| C07 | 79–83 | Verified: The primary proof explicitly alternates signs at interlacing roots and applies the intermediate value theorem. The manuscript cites the method, without claiming its hypotheses hold here. |
| C08 | 85–89 | Verified: The claim is restricted to the inspected primary material and date. Fresh comparisons found no equivalent assertion there; the 2019 full-text access limit remains explicit. |
| C09 | 93–97 | Verified: The three last-step choices and initial paths give exactly this recurrence. |
| C10 | 98–104 | Verified: The attributed characteristic-root method occurs at the specified source passage. The displayed complex-argument identity is independently derived from the manuscript recurrence. |
| C11 | 105–112 | Verified: Finite summation of powers i+1 gives both outer factors u and v; the manuscript preserves the distinct-root domain. |
| C12 | 114–122 | Verified: The named constants and their order agree with the accepted proof. |
| C13 | 128–149 | Verified: The same arc, square-root branch and nonzero denominators are specified. No extra branch or endpoint assertion is introduced. |
| C14 | 151–166 | Verified: Equality would force u=i and the forbidden value -2; continuity selects the strict direction from the right endpoint. The manuscript preserves all these steps. |
| C15 | 168–194 | Verified: The phase branches, both limits, positive denominator and strict error-term bound are retained. |
| C16 | 196–203 | Verified: The construction uses first hitting times on a closed parametrized arc, not unproved phase monotonicity. |
| C17 | 207–221 | Verified: The endpoint map, positive derivative and strict outer-root ordering match the accepted proof. |
| C18 | 223–244 | Verified: The sine denominators are positive; theta ordering implies the strict amplitude comparison. Exponents and numerator signs match. |
| C19 | 245–253 | Verified: The strict range of j, unique angle and sign reversal from u-v<0 are preserved. |
| C20 | 257–273 | Verified: The ceiling splice includes integer thresholds, permits the empty second group and avoids sign evaluation at b. The count and monicity argument match acceptance. |
| C21 | 277–279 | Verified: Software identity and full metadata match the primary record. The three exact version strings match the frozen report and installed environment. |
| C22 | 279–289 | Verified: The 24 reported root-isolation degrees were checked in the frozen data. A fresh integer program rebuilt the products and replayed all 530 signs, orders and enclosure decisions at exactly the eleven listed degrees. |
| C23 | 291–295 | Verified: Multiplication of G_n(p/r) by positive r^n gives the displayed integer without changing sign; the replay implements this exact homogeneous sum. |
| C24 | 296–300 | Verified: The cited primary section studies the evaluation operation and its generic characteristic-zero relation to interpolation and canonical derivative Bezout inversion. The text explicitly declines a fast-complexity consequence. |
| C25 | 300–303 | Verified: The source explicitly separates field-operation count from representation and growth costs; the nearby limitation is a faithful paraphrase. |
| C26 | 305–315 | Verified: Splitting according to the signs of t+4 and t+3 makes squaring valid and preserves strictness. Every finite sample passed these exact comparisons. |
| C27 | 317–320 | Verified: All listed remaining questions are outside the accepted theorem; the full original is not reported as proved or disproved. |

## Dependency and compiled-citation checks

The sorted publication source list is exactly `manuscript/main.tex`, `manuscript/references.bib`. The full main source, canonical bibliography command, compiler recorder file and BibTeX log were inspected. Project-local recorded inputs besides main.tex are generated main.aux, main.bbl and main.out. The bibliography log names references.bib. There are no additional authored TeX inputs, figures or local custom styles; system TeX packages are external system dependencies.

The final compiler and BibTeX logs contain no unresolved citations/references, duplicate entries, missing database entries, layout warnings or fatal diagnostics. The six source keys equal the six BibTeX keys and six final auxiliary citation keys. The checker command `python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py manuscript/main.tex --aux build/main.aux` passes against the final canonical bibliography syntax. Its output is audit/bib-key-check.log. The early relative-path mismatch and a temporary checker projection were superseded by the canonical bibliography correction; the temporary projection was removed.

All six rendered final PDF pages were actually inspected. Body citations resolve to [1]–[6]; references on pages 5–6 are legible, complete and consistent with the checked records. No agents, additional Codex processes or background workers were used, as the user expressly prohibited them. No pre-publication hook was invoked; it remains runner-owned.
