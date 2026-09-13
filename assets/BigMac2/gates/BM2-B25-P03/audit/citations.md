# Fresh citation and claim-support audit

Audit date: 2026-09-09. Release job:
`bigMac-00025-p03-release-3e0a1365b5bd`.

The requested `citation-check-skill` was applied as an advisory two-pass
audit. Pass 1 fixed the claims below from the complete authored manuscript and
the text extracted from the three-page PDF; no verification was done while
forming this list. Pass 2 then checked that fixed list against the accepted
mathematical snapshot, the listed computational sources, the rendered PDF,
and the two cited primary records.

## Pass 1: fixed claim extraction

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | Every `4+5` partition of the additive group $\mathbb F_3^2$ has the stated four-edge cross-part matching. | existence | abstract; Theorem 1 |
| C02 | The eight nonzero vectors form the four displayed antipodal directions. | existence/count | Section 1, display (1) |
| C03 | Afifurrahman--Primaskun--Putri--Wijaya pose the general cross-part problem as Open Problem 2. | attribution | Section 1 |
| C04 | Yip--Yoo--Yu prove the same-part statement for every odd-order finite abelian group and say their method does not seem to extend directly to the cross-part variant. | attribution | Section 1 |
| C05 | Four disjoint cross edges are equivalent to an injection from the four-element part into its complement, and the four-direction predicate is equivalent to the oriented-difference condition. | existence/equivalence | Section 2; Lemma 2 |
| C06 | There are exactly $\binom94=126$ four-subsets, $5P_4=120$ injections per subset, and 15,120 candidates in total. | statistic | Section 2 |
| C07 | The exhaustive program retains one witness for every four-subset and counts every accepted injection. | existence | Section 3 |
| C08 | Exactly 54 subsets have 8 valid injections, 72 have 12, the minimum is 8, and 126 witnesses are serialized. | statistic | Table 1 |
| C09 | The separate checker validates all 126 witnesses and independently re-enumerates 15,120 injections, reproducing the 54/72 distribution. | existence/statistic | Section 3 |
| C10 | The finite computation uses integer arithmetic and no randomness, floating point, symmetry assumption, or extrapolation. | existence | Sections 2--3 |
| C11 | Both programs require only the Python 3.12 standard library. | existence | Section 4 |
| C12 | The result is limited to $\mathbb F_3^2$ and does not address larger odd-order groups. | scope | abstract; Sections 1 and 4 |
| C13 | An OpenAI language model assisted with development, checking, and exposition, but model output is not mathematical evidence. | attribution/scope | assistance disclosure |
| C14 | The Afifurrahman et al. record has the authors, title, journal, volume/article number, year, and DOI printed in reference [1]. | citation metadata | References |
| C15 | The Yip--Yoo--Yu record is arXiv:2601.12250v3, dated 1 September 2026, with the title and three authors printed in reference [2]. | citation metadata | References |

Method descriptions that merely tell the reader how to run the programs were
not separately extracted, consistently with the skill's extraction rules.

## Pass 2: verification of the fixed claims

| IDs | Evidence and result | Status |
|---|---|---|
| C01--C02, C05 | The accepted referee report reconstructs the injection reduction, the four antipodal classes, and the equivalence to the frozen multiset condition; it independently checks all 126 certificate witnesses. The manuscript does not strengthen that accepted scope. | verified, exact |
| C06--C10 | `evidence/exhaustive_certificate.json` and `evidence/independent_verification.json` contain the exact stated values. During this release audit both programs were rerun with `/Users/mac/4prove-or-disprove-math/.research-venv/bin/python`; the regenerated certificate and independent report were byte-identical to the frozen files, with SHA-256 values `cf3589e80b12bdf59e737e073cb690a0f01d99fb9ba4b6b4e2258c18f73d449e` and `d5268ca8d0e5f11cf42ed85881311b50507245b2b31bfb6204164b84435b035b`. | verified, exact |
| C11 | Direct inspection shows that both programs import only `argparse`, `hashlib`, `itertools`, `json`, `pathlib`, and `__future__`, all in the Python standard library. | verified, exact |
| C12 | The abstract, comparison paragraph, theorem, and closing scope paragraph all retain the accepted $\mathbb F_3^2$, `4+5` boundary and expressly disclaim larger-group scope and priority. | verified, exact |
| C13 | This is an author disclosure rather than an externally sourced claim; it is precise and does not treat model output as evidence. | verified as disclosed scope |
| C03, C14 | Springer Nature's version of record for DOI `10.1007/s40590-025-00772-2` confirms the four authors, exact title, journal, volume 31, article 82, publication year 2025, and DOI. Its Section 5, page 9, states Open Problem 2 for a balanced partition of an odd-order finite abelian group and cross edges whose signed differences cover the nonidentity elements. This supports the manuscript's narrower contextual paraphrase. | verified, paraphrase/metadata exact |
| C04, C15 | The primary arXiv v3 HTML identifies Chi Hoi Yip, Semin Yoo, and Shikang Yu, `arXiv:2601.12250v3 [math.CO]`, dated 1 September 2026. Problem 1.6 and Theorem 1.7 give the same-part result for finite abelian groups of odd order; the following paragraph identifies Afifurrahman et al.'s cross-part analogue and says the methods do not seem to extend directly. | verified, paraphrase/metadata exact |

Primary records inspected:

- Springer Nature version of record:
  `https://link.springer.com/article/10.1007/s40590-025-00772-2`.
- arXiv version 3, especially Problem 1.6, Theorem 1.7, and the following
  paragraph: `https://arxiv.org/html/2601.12250v3`.

The project-local `literature/user_bibliography_check.md` is absent, so no
workbook-derived metadata basis was available or asserted. This absence is
disclosed but leaves no citation unverified: both records and both nearby
attributions were checked against accessible primary text. The manuscript
cites two genuinely relevant papers, makes no priority or exhaustive-search
claim, and needs no prose repair.

## Dependency and rendered-reference checks

All six paths in `publication.json` were inspected. The TeX source cites only
the two keys present in `manuscript/references.bib`; `main.aux`, `main.bbl`,
and the extracted PDF resolve them as references [1] and [2.]
`manuscript/main.fls` shows no unlisted authored TeX import, local style, or
figure. The four listed computational files are the sources and exact outputs
described in the proof. Thus the declared dependency scope is complete,
there are no undefined citations, and the rendered bibliography is legible.

## Verdict

**Accept.** All extracted claims are supported at their stated scope, both
cited records and nearby attributions are verified, the bibliography is
resolved, and the comparison language is appropriately bounded.
