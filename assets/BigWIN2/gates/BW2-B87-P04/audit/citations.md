# Citation audit

Verdict: **accept**.

This release audit used two non-interactive stages.  First, the nine substantive
claim/citation pairs in `manuscript/main.tex` were frozen in
`audit/citation-claim-ledger.json`, with locations and direct keys.  Second,
each claim was checked against the cited primary record and the bibliography
metadata was checked against publisher, repository, or DOI records.  The
ordinary body-flow key set is exactly
`BradenEtAl2026`, `MeurerEtAl2017`, `Sinclair2026`, `Whitney1935`, and
`Zeng2026Whiskered`; it is also exactly the union of the ledger keys.  Both
publication inputs, `manuscript/main.tex` and `manuscript/references.bib`, were
audited.

## Claim-level verification

| Claim | Direct source locator | Finding |
|---|---|---|
| C01 | Hassler Whitney, *On the Abstract Properties of Linear Dependence*, AJM 57(3) (1935), pp. 509--533, DOI [10.2307/2371182](https://doi.org/10.2307/2371182); the original abstract reproduced in the [Whitney bibliography](https://celebratio.org/Whitney_H/article/219/) | Verified.  The paper introduces the term matroid and treats abstract dependence; graphic/cycle dependence is part of its motivating framework. |
| C02 | Braden--Huh--Matherne--Proudfoot--Wang, [arXiv:2010.06088](https://arxiv.org/abs/2010.06088), especially Section 5, “Modules over the graded Möbius algebra”; DOI [10.1090/jams/1083](https://doi.org/10.1090/jams/1083) | Verified.  The cited paper studies graded modules over the graded Möbius algebra in combinatorial Hodge theory. |
| C03 | Sinclair, [arXiv:2608.18519v1](https://arxiv.org/abs/2608.18519v1), abstract and introductory definitions | Verified.  The source defines the canonical radial lowering operator and the Hilbert series of the jointly generated graded cyclic module. |
| C04 | Sinclair, [HTML text](https://arxiv.org/html/2608.18519v1), Question 6.3 | Verified.  Question 6.3 names direct sum, deletion, contraction, and duality, and says that simple Hilbert-series formulas fail. |
| C05 | Sinclair, Example 3.2 and full-text comparison in [arXiv:2608.18519v1](https://arxiv.org/abs/2608.18519v1) | Verified within the manuscript's explicitly narrow comparison.  Example 3.2 gives the `K_5` value; the paper contains neither this coloop-extension computation nor this through-five-vertices classification.  The manuscript makes no global priority claim. |
| C06 | Sinclair, [HTML text](https://arxiv.org/html/2608.18519v1), Proposition 2.4 | Verified.  Proposition 2.4 gives the flat-cover lowering formulas; the manuscript accurately labels its formulas as the rescaled specialization to a simple graphic matroid. |
| C07 | Meurer et al., [PeerJ Computer Science 3:e103](https://peerj.com/articles/cs-103/), DOI [10.7717/peerj-cs.103](https://doi.org/10.7717/peerj-cs.103) | Verified.  The source identifies SymPy as the Python symbolic-computation system.  The project replay evidence, rather than the citation, establishes what this particular checker computes. |
| C08 | Zijian Zeng, SSRN 7385138, DOI [10.2139/ssrn.7385138](https://doi.org/10.2139/ssrn.7385138), abstract | Verified.  The abstract reports 6,021 graph-isomorphism classes, canonical exhaustive enumeration, exact integer arithmetic, and an independent verifier reconstructing multiplication matrices.  This directly supports the manuscript's limited “related in spirit” method comparison. |
| C09 | Sinclair, [HTML text](https://arxiv.org/html/2608.18519v1), Example 3.2 | Verified.  The displayed Hilbert series has coefficient vector `(1,11,25,10,1)`. |

## Record and coverage audit

All five bibliography records exist.  Titles, author lists, years, venues or
repository type, page or article numbers, arXiv identifiers, and DOI strings
were checked against the primary pages above.  The in-press JAMS status for
Braden et al. is consistent with the AMS record and DOI.  The SSRN record is
correctly represented as an online working paper rather than a journal article.

The bibliography is neither library-only nor padded.  Whitney supplies the
problem's historical matroid context; Braden et al. supplies the modern graded
Möbius/Hodge context; Sinclair is the problem source, closest comparison, and
formula source; Meurer et al. documents the named exact-computation software;
and Zeng is the single genuinely relevant active user-library method analogue.
Four references are non-library primary or method sources in ordinary body
flow.  A second library item was rejected because it would not support another
natural nearby claim.  No retained citation is decorative.

The clean Biber build resolves all five direct citation keys, has no missing or
unused bibliography entry, and contains no undefined-citation diagnostic.
The audit is limited to the finite classification and methodological claims
actually made in the manuscript; it does not assert priority or exhaustive
literature coverage beyond that scope.  Verification date: 2026-09-11 UTC.
