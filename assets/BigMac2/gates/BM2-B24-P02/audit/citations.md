# Fresh citation and dependency audit

**Verdict: ACCEPT.** This review used the available `citation-check-skill` as
an advisory two-pass check and was completed on 2026-09-09. It is bound to
evidence snapshot `b2d23954f6d5891b916d9e20169010ea5ff36baf3d2dfde3987fd931199d1d82`,
manuscript digest
`a26950c1092c7e912eefd41eecf4991199319f4ffb9193cfbb32e698cb9349be`,
and PDF digest
`d72ea2216e7a5780f2e82b744acf6d9ea358cc709e74644858d419d084a961cf`.

## Pass 1: fixed claim extraction

The extraction scope is every externally checkable or citation-bearing claim
in the article; definitions and descriptions of the article's own method are
excluded under the skill's extraction rules. Mathematical assertions are
listed for traceability but remain governed by the accepted mathematical
review rather than by bibliographic metadata.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | Nonconstant fixed steps can improve gradient descent on smooth convex objectives. | Existence/comparative | p. 1, context paragraph |
| C02 | Das Gupta, Van Parys, and Ryu report the two-step pair `(1.414214,1.876768)` and value `0.065946`. | Attribution/statistic | p. 1, context paragraph |
| C03 | Grimmer, Shu, and Wang give the corresponding radical schedule, a tight fixed-schedule objective guarantee, and a general minimax conjecture for basic schedules. | Attribution/existence | pp. 1--2, context paragraph |
| C04 | Jung, Cho, and Yun use the same dimension-free performance measure and prove general schedule lower bounds. | Attribution/existence | pp. 1--2, context paragraph |
| C05 | The displayed pair attains the exact minimax value over all positive ordered two-step schedules. | Mathematical existence/statistic | Theorem 1, p. 2 |
| C06 | Four one-dimensional witnesses give the global lower bound and six interpolation multipliers plus a rank-one PSD residual give the matching upper bound. | Mathematical existence | pp. 3--5 |

This list was fixed before the verification pass below.

## Pass 2: source verification

| ID | Status | Evidence and exact support |
|---|---|---|
| C01 | Verified (paraphrase) | The abstracts and introductions of Grimmer--Shu--Wang and Jung--Cho--Yun explicitly describe faster guarantees from nonconstant fixed schedules; the article makes no broader quantitative claim here. |
| C02 | Verified (exact) | `literature/2203.07305.pdf`, printed pp. 34--35: Table 11 gives `0.065946` for `N=2`, and Table 12 gives `1.414214`, `1.876768`. The first page identifies arXiv:2203.07305v5, the title, the three authors, and the 2023 version date. |
| C03 | Verified (paraphrase) | `literature/2410.16249v2.pdf`: Definition 1 and Lemma 1 on printed p. 4 define the dimension-free tight `f`-composable objective guarantee; the basic `f`-composable table on printed p. 10 displays `[sqrt(2),(3+sqrt(9+8sqrt(2)))/4]` with the matching rate; Section 3.2.2 and Conjecture 1 on printed p. 12 state the basic/minimax conjecture. |
| C04 | Verified (paraphrase) | `literature/2609.04032v1.pdf`: Equation (1) on printed p. 1 is the same supremal final-gap performance measure (with an arbitrary finite horizon), and Theorem 3.3 on printed p. 7 is a lower bound for every positive finite schedule. |
| C05 | Verified by accepted mathematical audit | `audit/math.md` reconstructs both inequalities at the full frozen scope, and the accepted record `audit/math.json` is bound to the unchanged evidence snapshot. Citations are contextual and are not used as proof. |
| C06 | Verified by accepted mathematical audit | `audit/math.md`, together with the frozen exact evidence, checks the four admissible witnesses, the full positive-quadrant partition, all six positive multipliers, and the rank-one coefficient identity. |

The local primary-source hashes equal the hashes frozen in `source.md`:
`2203.07305.pdf` =
`6e660372e6874d0a65bf7de46798ddd9ce5def84b747770904b82df2ff6d263a`,
`2410.16249v2.pdf` =
`c75a6ee85b829d59ec83b28eb347fb2d05d7aad78887b50f8391cd1e49053f70`,
and `2609.04032v1.pdf` =
`862b892efb97c0d818f37339c4cbeeff259763bc62681ea761efd32570f6bcc0`.
The corresponding official arXiv records were also found by title, author/year,
and arXiv-identifier searches on 2026-09-09. Author, title, year, and version in
`manuscript/references.bib` agree with the local first pages and the rendered
bibliography. No cited passage contradicts the nearby prose, and no
unrestricted priority or uniqueness claim is made.

## Dependency and rendered-reference scope

`publication.json` lists exactly `manuscript/article.tex` and
`manuscript/references.bib`. Inspection of the TeX source and recorder output
found no authored `\input`, imported figure, local style, or other manuscript
dependency. All three citation keys are defined and used; the final `.bbl`,
compiler log, extracted PDF text, and rendered reference page resolve all three
entries without placeholders.

`literature/user_bibliography_check.md` was explicitly checked and is absent.
Accordingly, no workbook metadata was invented or treated as missing evidence;
the three genuinely relevant references were instead verified from the fixed
local primary PDFs and accessible arXiv records. This unavailable optional
cross-check leaves no cited record or nearby claim unverified in the present
manuscript.
