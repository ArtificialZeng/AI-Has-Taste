# Citation and claim audit

**Verdict:** accept  
**Mode:** two-pass search verification plus accepted exact project evidence  
**Search/verification date:** 2026-09-07  
**Audited snapshot:** mathematical `5a3f365e...e383bf`; manuscript
`0da93670...db508`; PDF `24846609...2177`.

## Two-pass procedure

Pass 1 extracted and froze 15 claims in
`audit/citation-claim-ledger.json` before any source verification. A later
metadata-only six-line insertion shifted line numbers without changing claim
text or citation pairs; the ledger records this offset. Pass 2 checked those
same 15 identifiers, without re-extraction. The three citation-bearing claims
were checked against the cited primary records and exact source passages. The
original mathematical claims were checked for exact agreement with the
accepted claim, referee report, frozen certificate, and two exact logs.

The bibliography skill's default delegation was not used because this job
explicitly prohibited agents and background workers. Each key was therefore
verified serially under the same per-reference protocol.

## Summary

| Metric | Count |
|---|---:|
| Frozen claims | 15 |
| Verified/supported | 15 |
| Citation-bearing claims | 3 |
| Citation not found | 0 |
| Numerical error | 0 |
| Misquoted, misleading, or hallucinated | 0 |
| Unverified | 0 |

## Claim verification ledger (pass 2)

| ID | Final location | Verification source and exact locator | Status |
|---|---|---|---|
| C01 | lines 35--43 | `audit/math.md`, Verdict and Reconstruction; primary and replay logs | Verified, exact |
| C02 | lines 55--57 | Ai et al., official arXiv abstract and Theorem 1.1: the one-sided out-degree-square maximum is defined and identified with the finite palette extremum for self-converse tournaments | Verified, paraphrase |
| C03 | lines 65--73 | Iľkovič, PDF p.4, Conjecture 3.3 and preceding sentence; PDF p.13, conclusion. Full-text search found no order-seven certificate or equality census | Verified, exact/paraphrase |
| C04 | lines 75--84 | `claim.json`; `audit/math.md`, accepted finite statement | Verified, exact |
| C05 | lines 88--95 | Elementary degree calculation in manuscript; `audit/math.md`, lower-bound reconstruction | Verified, exact |
| C06 | lines 107--110 | `evidence/reg5_m7_certificate.md`, Encoding and completeness; primary log (`possible_arcs=42`, exact domain size) | Verified, exact |
| C07 | lines 112--129 | Certificate lines 18--24 and primary log exact counters | Verified, exact |
| C08 | lines 131--140 | Certificate lines 26--32; both logs report 504 labeled masks | Verified, exact |
| C09 | lines 142--145 | Primary log: 6,937,603 strict candidates, zero strict free, 105 equality free | Verified, exact |
| C10 | lines 149--160 | Replay log: 2,647 degree vectors and 6,937,603 checked/containing | Verified, exact |
| C11 | lines 162--166 | Replay log: 105 masks, all score 186, free, and `T_4(7)`; the text expressly limits what the replay verifies | Verified, exact |
| C12 | lines 166--169 | Zeng et al., official Preprints.org v1, abstract and §§3, 4, 6: exhaustive finite searches, integer predicates, independent re-enumeration and a separate exact implementation | Verified, paraphrase |
| C13 | lines 173--187 | Replay log and accepted referee report, Equality classification | Verified, exact |
| C14 | lines 198--206 | Both released programs/logs; accepted report, Remaining limitations | Verified, exact |
| C15 | lines 208--213 | First-party computational disclosure, project job/evidence record, and absence of any proof-assistant artifact in the frozen evidence | Verified as workflow disclosure |

## Citation-by-citation primary-source audit

| Key | Official record | Nearby support | Metadata/action | Verdict |
|---|---|---|---|---|
| `AiEtAl2026` | Jiangdong Ai, Bin Chen, Ming Chen, Zilong Yan, Tianxiao Zhao, *Finite palette endpoints and degree-square Turán problems*, arXiv:2606.03520v1, <https://arxiv.org/abs/2606.03520> | Official abstract and Theorem 1.1 support the definition and self-converse palette identity at lines 55--57 | Authors, year, identifier and subject verified. The stale title and nonexistent v2 in the draft BibTeX were corrected to the official title and v1; key retained | Verified |
| `Ilkovic2026` | Daniel Iľkovič, *L2 Turán Problems for Small Tournaments and Stability*, arXiv:2609.05042v1, <https://arxiv.org/abs/2609.05042> | Frozen PDF p.4, immediately before and in Conjecture 3.3, reports small-order exact values and states the all-order `Reg5` formula; p.13 says a formal exact `Reg5` result remains future work | Author, title, submission date 4 Sep 2026, arXiv ID and v1 verified; no change | Verified |
| `ZengEtAl2026` | Zijian Zeng, Houde Liu, Kuru Ratnavelu, Ong Seng Huat, *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*, Preprints.org v1, <https://www.preprints.org/manuscript/202608.1658> | Abstract and §§3, 4, 6 support the narrowly worded comparison to exhaustive exact search plus separately organized replay | Official title/authors, version 1, Aug 2026, and DOI `10.20944/preprints202608.1658.v1` verified; key retained | Verified |

## Coverage and necessity audit

The bibliography is not library-only. `Ilkovic2026` is the primary source of
the problem and closest stated prior result; `AiEtAl2026` is the natural
primary source for the degree-square/palette definition and identity on which
the context sentence relies. `ZengEtAl2026` is the one genuinely relevant
active user-library record and supports a direct methodological comparison.
Each has an ordinary body-flow `\cite{FinalKey}`. No citation is decorative.

No additional reference is naturally required: the finite theorem, pruning
bound, generating-function count, forbidden-mask construction, equality count,
and replay are fully stated and proved from released project evidence rather
than imported nontrivial theorems. Adding another user-library exact-search
paper would duplicate C12 rather than cover a missing dependency.

## Mechanical bibliography audit

The final source has three cite keys and the canonical bibliography has exactly
those three entries. The final `.aux` has the same three keys; there are no
missing or unused entries, duplicate entries, undefined citations, or key
changes. The final `.bbl` displays all three verified records. The log scan is
clean. The original `source.md` remains byte-identical at SHA-256
`b71158a55cdb4fa03de594447a51ba4e88261de47df066fe822dc14354abf8b6`.
