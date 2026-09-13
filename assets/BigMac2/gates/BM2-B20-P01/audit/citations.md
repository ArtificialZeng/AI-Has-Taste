# Fresh citation and claim-support audit

## Binding and method

Release job `bigMac-00020-p01-release-80ff7c9383b6` audited evidence snapshot
`3647bf565806d5d07c7d5aaeea1ea8148576e5430042ef81a177c2acfb6b78c6`,
manuscript snapshot
`488892484bc96d7b34bbff749318870b687f20d1f27eafaeeb7f79d6da6d1515`,
and PDF
`367e110c905d90de5c2eb099cf1b67f3b2502ecd1643be94f530c6cd495f0542`.
The advisory `citation-check-skill` v2 was explicitly invoked in its two-pass
order. Verification then used the hash-matching primary PDF and the official
arXiv record. The bounded searches and primary-text inspection were performed
on 2026-09-09.

`literature/user_bibliography_check.md` was inspected. It records that this
project has no Excel-derived bibliography and that immutable `source.md`
designates one genuinely relevant paper: Darius Dramburg, *Isomorphisms of
graded semiconnected algebras*, arXiv:2609.03288v1. The available batch-local
PDF has SHA-256
`f1dff9a9f6decb301ce097bd319c2085f553e5e92f7dddafff63e772db41816e`,
exactly the user-supplied digest. The official arXiv record was accessible and
independently confirms the author, title, identifier, September 2026 date, and
math.RA classification. No DOI is supplied or asserted.

## Pass 1: fixed extraction

No source verification was performed while fixing this list.

| ID | Extracted claim | Type | Location |
| --- | --- | --- | --- |
| C01 | Dramburg asked whether the stated quotient-dimension condition forces splitness. | Attribution/existence | Abstract; section 1 |
| C02 | Standard graded, locally finite, and semiconnected have the definitions stated. | Attribution | Section 1, first paragraph |
| C03 | A possibly ungraded ideal is split exactly when the natural degree-zero composite is an isomorphism. | Attribution | Section 1, first paragraph |
| C04 | Question 6.1 has the standard, locally finite, semiconnected, and dimension hypotheses quoted. | Attribution | Section 1; Theorem 1 |
| C05 | Over every field a three-dimensional example meets the hypotheses but is not split. | Existence/statistic | Abstract; Theorem 1 |
| C06 | The displayed basis has multiplication table (1). | Existence | Proof, page 1 |
| C07 | The grading has dimensions `2,1,0,0,...`, is standard and locally finite, and has semisimple degree zero. | Statistic/existence | Proof, pages 1--2 |
| C08 | `J=ke` is a two-sided ideal. | Existence | Proof, page 2 |
| C09 | The quotient is the dual-number algebra and has dimension 2, equal to `dim A_0`. | Statistic/existence | Proof, page 2 |
| C10 | The natural map has kernel `ke`, so it is not an isomorphism and `J` is not split. | Existence/causal | Proof, page 2 |
| C11 | The construction is characteristic-free, permits zero higher pieces, uses decomposable degree zero, and asserts no minimality. | Existence/scope | Remark 1 |
| C12 | Proposition 4.7 proves splitness for the special ideals arising from an ungraded isomorphism. | Attribution | Remark 1 |
| C13 | The proof uses no numerical or symbolic computation. | Existence | Assistance disclosure |
| C14 | The reference has the displayed author, title, year, arXiv identifier, and v1 status. | Attribution/existence | References |
| C15 | `16W50` is a relevant 2020 MSC code for the manuscript. | Classification | Page 1 metadata |

## Pass 2: sequential verification

| IDs | Status | Evidence |
| --- | --- | --- |
| C01--C04 | Verified (exact/paraphrase) | The primary PDF gives Definition 1.1 on p. 1, Definition 4.1 on p. 4, and Question 6.1 on p. 9. Its hypotheses and natural map agree with the manuscript. |
| C05--C11 | Verified at the accepted mathematical scope | The claims follow from the displayed multiplication table, quotient map, and kernel calculation. `audit/math.md` independently reconstructs each point, and `audit/math.json` accepts the unchanged evidence snapshot. The manuscript adds no minimality or priority claim. |
| C12 | Verified (paraphrase) | Proposition 4.7 on p. 6 concerns `I=phi^{-1}(B_+)` and `K=phi(A_+)` under an ungraded isomorphism and says these special ideals are split. The remark retains that restriction. |
| C13 | Verified by complete proof inspection | Every proof step is elementary symbolic prose from the displayed algebra; no computational output is used. |
| C14 | Verified (exact) | The local title page and official arXiv record agree with `references.bib` and the rendered entry. |
| C15 | Verified as appropriate classification metadata | The source paper itself lists 16W50 among its algebra classification codes; the manuscript's narrower use is consistent with its graded-algebra subject. |

The required academic-citation search templates were run for author/year/title,
the full title restricted to arXiv or Semantic Scholar, author/year/venue, and
the arXiv identifier. The official primary record was found. No DOI query was
applicable because no DOI was supplied. The manuscript makes no exhaustive
novelty or later-literature claim, so search results are not used as proof of
priority.

## Citation resolution and dependency scope

The sole BibTeX key, `Dramburg2026`, occurs in `main.aux` as cited and as
`\\bibcite{Dramburg2026}{Dra26}`. The extracted and rendered PDF contains all
three citation uses and the complete reference. No nearby claim contradicts or
strengthens the cited primary text.

The sorted `publication.json` source list is exactly
`manuscript/main.tex`, `manuscript/references.bib`. Inspection of `main.tex` and
the recorder file found no authored input, figure, local style, or other source
dependency. The other recorder inputs are system TeX files or generated
auxiliaries. The declared dependency scope is complete.

**Verdict: accept.** All citations and attributions are resolved and supported;
there is no residual citation-access limitation requiring qualified acceptance.
