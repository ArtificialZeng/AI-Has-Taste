# Claim ledger

| ID | Claim | Status | Source | Location | Confidence | Consequence |
|---|---|---|---|---|---|---|
| C01 | Yuster defined the minimum packing parameter and conjectured (\nu_3(n)=\lceil n(n-1)/6-n/3\rceil). | exact, verified | Yuster, *Discrete Mathematics* 287 (2004), DOI 10.1016/j.disc.2004.07.005; arXiv:math/0304180 | concluding remarks / Section 4; formula restated as KY08 Conj. 1.1 | high | fixes the target formula and attribution |
| C02 | Yuster verified the formula for (n\le 8), with (n=8) computational and smaller orders by direct argument. | exact, verified from primary arXiv text and independently reported in 2026 note | Yuster 2004; Kirtchakov draft 2026 | Yus04 Section 4; note lines 76--82 | high | establishes the pre-2026 finite frontier |
| C03 | The cyclic balanced three-part blow-up proves the upper bound (\nu_3(n)\le\lceil n(n-1)/6-n/3\rceil). | exact, verified | Yuster 2004; Kabiya--Yuster 2008 | Yus04 Section 4; KY08 Section 2.4 | high | gives (\nu_3(11)\le 15) with part sizes (4,4,3) |
| C04 | Kabiya--Yuster improved the asymptotic lower bound to (\frac{41}{300}n^2(1-o(1))). | exact, verified | Kabiya and Yuster, *Annals of Combinatorics* 12 (2008), 291--306, DOI 10.1007/s00026-008-0352-3 | abstract and main theorem | high | strongest located general asymptotic bound; far below the finite target |
| C05 | A public 2026 draft certifies (\nu_3(9)=9\) and (\nu_3(10)=12) by exhaustive canonical enumeration with per-class witnesses. | author report and publicly replayable artifact claim; publication is a draft/repository deposit, not peer review | D. Kirtchakov, GitHub `05oz/certify`, draft 2026-08-05; Zenodo Part C DOI 10.5281/zenodo.21816010 | note Theorem 1.1 and Sections 2--4 | high for the stated artifact record; formal peer-review status: none located | this is the exact baseline to reproduce before (n=11) |
| C06 | The 2026 note used 191,536 and 9,733,056 isomorphism classes at orders 9 and 10 and says order 11 was not started. | exact author report | Kirtchakov 2026 draft | note lines 41--64, 148--181 | high | order 11 has 903,753,248 known isomorphism classes and is about 93 times the order-10 enumeration |
| C07 | No public determination of (\nu_3(11)) was located as of 2026-08-30. | bounded negative search result, not a theorem; confirmed in a result-specific post-Builder pass | searches in arXiv/web, Open Problem Garden, GitHub, DBLP/EBSCO-style records; queries logged separately | `literature/search_log.md`, Passes 2 and 3 | medium-high within searched sources | supports carefully bounded novelty wording after certification |
| C08 | The original Yuster article metadata are volume 287 (2004), pages 187--191, DOI 10.1016/j.disc.2004.07.005. | exact metadata, verified | Elsevier/ScienceDirect and DBLP volume record | article record | high | bibliography anchor |
| C09 | The Kabiya--Yuster article metadata are volume 12(3) (2008), pages 291--306, DOI 10.1007/s00026-008-0352-3. | exact metadata, verified | University of Haifa CRIS / DOI record; EBSCO listing | article record | high | bibliography anchor |

## Research-result checkpoints (not literature claims)

These rows separate the evidentiary state at each checkpoint from the current
terminal state.  They do not turn project outputs into external citations.

| ID | Claim | Status | Exact evidence | Consequence |
|---|---|---|---|---|
| R01 | The Builder covered all 903,753,248 order-11 canonical classes in 192 residue streams and found a 15-packing in every class. | Builder exact pass | `certificates/n11_builder_full_m192.json` | material positive result, but insufficient by itself for a terminal theorem claim |
| R02 | At the R01 checkpoint, the independent no-import Certifier, post-certification novelty search, and submission audits were still pending. | historical checkpoint | `PROGRESS.md`; G02, G04, G05 in `proof/gap_ledger.md` | terminal status was intentionally withheld |
| R03 | The independent Certifier later covered the same 903,753,248 classes, and all 192 counts and regenerated stream digests matched the Builder. | independent exact pass | `certificates/n11_certifier_full_m192.json`; `certificates/n11_sweeps_match.json` | closes the decisive independent finite-enumeration gap, subject to the declared generator trusted base |
| R04 | The explicit cyclic 4+4+3 tournament has packing number exactly 15. | exact upper-bound certificate | `certificates/minimizer_11.json`; `code/verify_minimizer.py` | proves `nu_3(11) <= 15` |
| R05 | After R03, the final novelty, citation, proof, LaTeX, PDF, and release gates passed. | current audited state | `literature/search_log.md`; `audit/PROOF_AUDIT.md`; `audit/CITATION_VERIFICATION.md`; `audit/PDF_AUDIT.md`; `release/MANIFEST.json` | authorizes current status `CERTIFIED_FINITE_RESULT` and conclusion `nu_3(11)=15` |
