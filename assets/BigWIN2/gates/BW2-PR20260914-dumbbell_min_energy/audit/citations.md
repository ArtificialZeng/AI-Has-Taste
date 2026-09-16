# Citation and claim audit — accept

Job: primary-20260914-dumbbell-min-energy-release-d0dcdbfc65d4

Manuscript digest: `684f969d232c6e203ffd7fb7ee7866b0792f2879556277493b9cc223f4180229`  
PDF digest: `2c59c283fc319ae3992c6615f0593ca4e74baabd685856808187e3403ed5eb1f`  
Frozen mathematical snapshot: `c54ee1930645183cb069fba12fb9fd382eddca737522332f05cf84b9349a0cae`

41 fixed claim units were verified: 14 citation-bearing statements, 18 local mathematical/reproducibility statements, and nine certificate rows. Eight distinct body-flow citation keys exactly equal the ledger key union. No unsupported retained claim, missing citation, decorative reference, or unresolved bibliography entry remains. The original all-odd classification remains unresolved; the accepted contribution is a result-note.

## Method and independence

Pass 1 extracted and froze the claim/citation pairs with unique ids, exact source locations and direct keys. Pass 2 independently compared those fixed statements with primary source passages and the frozen accepted mathematical evidence; source conclusions were not inferred from registry titles or prior audit verdicts. Both passes were non-interactive and serial because the user prohibited agents. The citation-check-skill and bib-reference-audit instructions were read in full. Fresh searches, publication records and passage captures are in `audit/release-sources/`; the structured source locators and claim-by-claim findings are in `citation-source-locations.json` and `citation-verification.json`. The local mathematical audit remains the accepted independent referee audit, rather than a newly invented release proof.

## Primary sources and nearby support

### Reff2012

Reff, 2012, Linear Algebra Appl. 436(9), 3165–3176; DOI 10.1016/j.laa.2011.10.021

Primary record: https://arxiv.org/abs/1110.4554

Author PDF pp. 1–2 definitions and p. 4 Lemma 2.2: Hermitian adjacency, switching and diagonal unitary conjugation.

Evidence: `audit/release-sources/Reff-primary-open.txt`, `audit/release-sources/Primary-records.json`.

### ZengLiuRatnavelu2026

Zijian Zeng, Houde Liu, Kurunathan Ratnavelu; version 1, 17 August 2026; DOI 10.20944/preprints202608.1067.v1

Primary record: https://www.preprints.org/manuscript/202608.1067/v1

Section 1 Schatten definitions and Theorem 1; Section 2 equations (7)–(18), especially exact rational comparisons (11)–(18). Exponent 3/2; matrices have radicals, while the verification inequalities are rational.

Evidence: `audit/release-sources/Zeng-passages.json`, `audit/release-sources/Zeng-bibtex-discovery.json`.

### SamantaKannan2025

Aniruddha Samanta, M. Rajesh Kannan; Linear Algebra Appl. 721 (2025), 844–866; DOI 10.1016/j.laa.2024.03.028

Primary record: https://www.sciencedirect.com/science/article/abs/pii/S0024379524001241

Author preprint arXiv:2312.17152, Theorem 4.3 p. 11 gives cycle-union/matching polynomial expansion; Section 5, Theorem 5.1 pp. 18–19 gives unicyclic bounds.

Evidence: `audit/release-sources/Samanta-precise.json`, `audit/release-sources/Publication-metadata-final.json`.

### HuangPereyra2026

Silin Huang, Kevin Pereyra; arXiv:2604.27785v2, 26 May 2026. Version-specific two-author metadata checked.

Primary record: https://arxiv.org/html/2604.27785v2

Theorem 2.10 equation (13); Lemma 4.2 equations (67)–(69); Theorem 4.6; Theorem 4.7 equations (117)–(119); Proposition 4.9 equations (138)–(145). Figure 2 discussion explicitly distinguishes the nondifferentiable half-diagonal point; frozen PDF text lines 952–954.

Evidence: `audit/release-sources/Huang-passages.json`, `audit/release-sources/Huang-kernel-cusp.json`, `audit/release-sources/Primary-records.json`.

### Lewis1996

A. S. Lewis; Math. Oper. Res. 21(3), 576–588 (1996); DOI 10.1287/moor.21.3.576

Primary record: https://pubsonline.informs.org/doi/abs/10.1287/moor.21.3.576?journalCode=moor

Official publisher abstract: differentiability of Hermitian spectral functions and formula for their Clarke generalized gradient. This directly supports only the manuscript’s broad historical statement; no unpublished or unread technical theorem is invoked.

Evidence: `audit/release-sources/Lewis-publisher-record.json`, `audit/release-sources/Lewis-primary.json`.

### MateljevicBozinGutman2010

Miodrag Mateljević, Vladimir Božin, Ivan Gutman; J. Math. Chem. 48(4), 1062–1068 (2010); DOI 10.1007/s10910-010-9725-z

Primary record: https://poincare.matf.bg.ac.rs/~miodrag/10.1007_s10910-010-9725-z.pdf

Theorem 1, printed p. 1065, equations (10)–(11): Coulson integral for polynomial energy; real-coefficient reduction. The manuscript’s real-rooted specialization and scalar integral proof also cover the zero-root case.

Evidence: `audit/release-sources/Mateljevic-theorem.json`, `audit/release-sources/Mateljevic-primary.json`.

### GonzalezEtAl1989

Laureano Gonzalez, Henri Lombardi, Tomas Recio, Marie-Françoise Roy; Publications de l’Institut de recherche mathématiques de Rennes, no. 4 (1989), 47–101. Official Numdam BibTeX checked.

Primary record: https://www.numdam.org/item/PSMIR_1989___4_47_0/

Section 1, printed pp. 52–55: signed remainder recurrence, sign variations omitting zeros, Theorem 1. With auxiliary polynomial 1 this is the ordinary Sturm root-count criterion. French source read with this specialization explicitly checked.

Evidence: `audit/release-sources/Gonzalez-theorem.json`, `audit/release-sources/Gonzalez-primary.json`.

### Meurer2017

Meurer et al. (27 authors), SymPy: symbolic computing in Python, PeerJ Computer Science 3:e103 (2017); DOI 10.7717/peerj-cs.103

Primary record: https://github.com/sympy/sympy-paper

Official author repository paper.bib/metadata and paper abstract establish software identity. Actual version 1.14.0 is independently recorded in frozen evidence/research-checks.json, not inferred from the 2017 paper.

Evidence: `audit/release-sources/Meurer-bibtex.json`, `audit/release-sources/Meurer-primary.json`.

## Coverage, selection and corrections

The active 49-entry first-sheet registry was screened; rows 2, 10, 12, 13 and 29 received closer relevance comparison. Row 2 is the one gate-bound selection: the Schatten norm is the surrounding matrix-norm context and exact rational inequalities are a directly relevant verification comparison. The nearby sentence explicitly states exponent 3/2, without importing that result into energy at exponent 1. The other seven sources cover problem origin, closest gain-graph results, Coulson integrals, spectral calculus, Sturm verification and symbolic software in ordinary body flow. The library is neither the whole bibliography nor a citation quota. Dynamic registry binding, actual UTC verification date and exact job/attempt/launch identity passed the hook-compatible selection validator; the runner-owned hook itself was not invoked.

A misleading phrase suggesting rational counterexample matrices was narrowed to certification by rational inequalities, as the primary example contains radicals. The version-specific DOI was added as an explicit BibTeX field. No keys were renamed. Existing correct author/title/year/venue fields were retained after record verification, including the 27-author SymPy record. Official Numdam and author-repository BibTeX were compared where available. Several Preprints/DOI export endpoints failed; no official export was invented. No supervisor Crossref capture existed. Those failures do not invalidate the directly accessible full primary text or its deposited version identity. The table was inlined unchanged apart from omitting default spacing, and the bibliography command normalized to canonical `references`; the build supplies its lookup directory.

The Lewis publisher abstract is sufficient for the limited broad attribution actually made; no technical theorem from unread PDF text is claimed. The version/novelty check is explicitly bounded to the inspected sources through 14 September 2026. Huang–Pereyra v2 is cited both for the known D331 energy and for the exact unqualified stationarity equations corrected here. The full global classification and normal-threshold equality case are not presented as solved.

## Reproduction and full-input coverage

The exact D335 verifier was freshly run without mutating frozen evidence or its canonical table; nine nonzero intervals and the zero root were checked, giving the certified derivative sum [407312,407321] in million-scaled units and directional derivative strictly between -8/1000 and -7/1000. Additional D331 polynomial transcriptions were checked symbolically. The 125-triple statement and software version match frozen receipts. All publication source files were inspected: `manuscript/d335-table.tex`, `manuscript/main.tex`, `manuscript/references.bib`, `manuscript/verify_d335.py`. The final auxiliary-file checker reports eight cited keys, eight entries, no missing or unused entries and no key difference. The final clean build, final page views and integrity receipts are recorded separately.
