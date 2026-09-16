# Verification report

**Mode:** Search verification with primary-source passage checking  
**Document:** `manuscript/main.tex` and `manuscript/references.bib`  
**Verified:** 2026-09-07  
**Release job:** `win-00067-p04-release-fc7f9ea98fa7`  
**Citation attempt / launch:** `2` / `6eb6c72d-4f71-439f-ad64-c2711d781293`  
**Bound manuscript digest:** `1a5c424ba6100bad286c6fd696c8a1659946c806ad9ca73ac1c3dea973451a55`  
**Bound PDF digest:** `f748baaa05f7f4e2e5afc649b0e76f791949d960c2128d2259104f3d8a235bcf`

## Summary

| Metric | Count |
|---|---:|
| Frozen citation claims | 5 |
| Verified | 5 |
| Citation not found | 0 |
| Numerical error | 0 |
| Misleading or misquoted | 0 |
| Hallucination | 0 |
| Unverified | 0 |

**Overall status: PASS.** The initial claim extraction was frozen in
`audit/citation-claim-ledger.json` before source checking. The second pass used
only those five fixed claims. All remained supported, so no citation wording,
key, or bibliography record changed during verification.

No subagents were used because the runner explicitly prohibited agents and
background workers. Each key was therefore checked serially under the same
per-citation protocol.

## Verified claims

| ID | Key | Nearby claim and exact source support | Status | Confidence |
|---|---|---|---|---|
| C01 | `Grundy1939` | Grundy, *Mathematics and Games*, *Eureka* 2 (1939), pp. 6--8, assigns nonnegative values recursively to impartial-game positions using the least excluded option value. This supports the manuscript's normal-play Sprague--Grundy recursion. | Verified | paraphrase |
| C02 | `Golomb1966` | The publisher abstract defines take-away games, treats the one-dimensional case, and describes recursive analysis by a nonlinear shift register. This exactly supports the corrected historical claim that Golomb treated one-dimensional take-away games. | Verified | paraphrase |
| C03 | `Manabe2026` | The arXiv v1 abstract states an explicit sufficient pure-periodicity criterion and the conjectured converse. Theorem 28 (PDF pp. 19--20), Theorem 32 (pp. 21--22), Conjecture 50 (p. 33), and Theorem 57 (p. 35), specialized at `(a,b)=(2,5)`, give the claimed covered and uncovered residue classes. | Verified | paraphrase |
| C04 | `Manabe2026` | Direct substitution `a+b=7`, `delta=3`, `eta=1`, `epsilon=1` in the cited results yields covered residues `1,2,3,5,6` and leaves `0,4`; Conjecture 50 on PDF p. 33 is the precise full-shape statement completed by the manuscript's accepted theorem. | Verified | interpretation (fully shown) |
| C05 | `ZengEtAl2026Certificates` | The official Preprints.org v1 page, Sections 2--6 and the computational disclosure, documents integer predicates, independent exact implementations, human-readable reductions, and that language-model output is not mathematical evidence. The manuscript explicitly limits this citation to methodological context and does not use it in the proof. | Verified | paraphrase |

## Bibliographic record audit

| Key | Audited record | Author/title/date/venue result | Authoritative source | Action |
|---|---|---|---|---|
| `Grundy1939` | Patrick M. Grundy, *Mathematics and Games*, *Eureka* 2 (1939), 6--8 | Consistent with the original scan/reprint record | https://oeis.org/A002188/a002188.pdf | Retained |
| `Golomb1966` | Solomon W. Golomb, *A Mathematical Investigation of Games of “Take-Away”*, *Journal of Combinatorial Theory* 1 (1966), 443--458 | Exact publisher metadata and DOI match | https://doi.org/10.1016/S0021-9800(66)80016-9 | Retained; nearby wording narrowed |
| `Manabe2026` | Hikaru Manabe, *Purely Periodic Three-move Subtraction Games*, arXiv:2609.05358v1 (4 September 2026) | Exact arXiv title, author, version, identifier, and scope match | https://arxiv.org/abs/2609.05358 | Retained |
| `ZengEtAl2026Certificates` | Zijian Zeng, Houde Liu, Kuru Ratnavelu, Ong Seng Huat, *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*, Preprints.org v1 (24 August 2026) | Exact official page and DOI metadata match | https://doi.org/10.20944/preprints202608.1658.v1 | Retained |

No key changed and no BibTeX record required replacement in this attempt. All four final keys
exist exactly once in the canonical bibliography and all four occur in ordinary
body flow. The final `.aux` contains the same four-key set; there are no unused
entries, missing entries, duplicate entries, or undefined citations.

## Coverage and relevance audit

The bibliography is not library-only. `Manabe2026` is the primary problem
source and closest result; `Grundy1939` directly supports the classical mex
recursion; `Golomb1966` provides primary take-away-game context; and the sole
selected active-library item, `ZengEtAl2026Certificates`, supports one narrowly
stated methodological comparison in the computational disclosure. Adding a
second active-library paper would not support a further claim naturally made by
this manuscript and would be padding. The finite mex certificate, seam tables,
and primitivity argument are self-contained and bound to the accepted
mathematical audit, so they do not depend on an uncited external method.

The active 49-entry registry and source workbook were checksum-bound in
`audit/user-bibliography-selection.json`. Before this decision, all
`literature/bibliography-revision-*.md`, `literature/crossref-*.json`, and
`literature/crossref-*.md` patterns were enumerated; none exist in this project.

## Search and passage-check method

For each academic citation, the audit ran the applicable title/author/year,
exact-title database, venue, and DOI or arXiv-identifier query forms rather than
stopping at a discovery snippet. Verification used the original Grundy scan,
Elsevier's article record for Golomb, the archived 45-page Manabe v1 PDF at
`evidence/external/2609.05358v1.pdf`, and the full official Preprints.org v1
record for the selected library item. Registry metadata was used only to locate
the selected item; the primary page supplied the claim-level verification.

Mechanical closure was checked with:

```text
python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py main.tex --aux main.aux
cited_keys: 4; bib_keys: 4; missing: 0; unused: 0; aux differences: 0
```
