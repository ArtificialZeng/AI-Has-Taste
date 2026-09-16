# Citation and bibliography audit

**Verdict: accept.**  Fresh search verification for citation attempt 2 was
performed on 2026-09-09 UTC by release job
`win-00086-p03-release-6700fccf9f2a`.
The audit used two non-interleaved stages.  Pass 1 read the complete canonical
manuscript and froze the six claim/citation pairs in
`audit/citation-claim-ledger.json`.  Its key union is exactly the six ordinary
body-flow citation keys.  Pass 2 worked only from that frozen set and checked
each source's existence, metadata, exact nearby support, hypotheses and scope.

## Pass 1: frozen claims

The ledger records C01--C06 at exact `manuscript/main.tex` line intervals.
The extraction found six `\cite{...}` keys and no citation variants, custom
cite macros, `\nocite`, hidden conditionals, commented citations or inert
citations.  The canonical bibliography contains exactly the same six keys.

## Pass 2: source verification

| Claim | Key | Exact primary evidence and result |
|---|---|---|
| C01 | `HuczynskaKlawuhnPaterson2026` | **Verified (exact).**  arXiv:2510.04675v2, Example 2.11 (HTML lines 282--284; PDF p.9) states that (x^4\in\mathbb F_{11}[x]) is projectively equivalent to (x^8) and observes only EA inequivalence.  Definition 2.14 (HTML lines 335--337; PDF p.13) gives affine graph equivalence, and Open Problem 4 (HTML lines 1280--1283; PDF p.34) asks for a projectively equivalent but non-CCZ-equivalent pair.  The arXiv record and publisher/institutional record agree on the final title, authors, 2026 journal publication, volume 114, article 102828 and DOI.  Sources: <https://arxiv.org/html/2510.04675v2>, <https://doi.org/10.1016/j.ffa.2026.102828>. |
| C02 | `CarletCharpinZinoviev1998` | **Verified (paraphrase).**  The primary paper exists with the stated authors, title, journal, volume 15(2), pages 125--156, year and DOI.  Huczynska--Klawuhn--Paterson v2 explicitly calls CCZ equivalence the notion introduced by Carlet, Charpin and Zinoviev immediately before Definition 2.14.  Springer metadata matches the BibTeX entry.  Sources: <https://link.springer.com/article/10.1023/A:1008344232130>, <https://arxiv.org/html/2510.04675v2>. |
| C03 | `Dempwolff2018` | **Verified (exact).**  The official Springer abstract states the iff classification with (0\le a<n), either \(\ell\equiv p^a k\pmod{p^n-1}\) or \(k\ell\equiv p^a\pmod{p^n-1}\).  Substitution (p=11,n=1,k=4,\ell=8) gives the manuscript's exact residues (8\ne4\) and (32\equiv2\ne1\pmod {10}).  Springer metadata matches author, title, volume 86, pages 665--692, issue year 2018 and DOI.  Source: <https://link.springer.com/article/10.1007/s10623-017-0350-8>. |
| C04 | `Dempwolff2022Correction` | **Verified (exact).**  The correction's author-posted first page, lines 61--65 of the live text extraction, says that it corrects the proof of Lemma 2.13 and that validity of the main result, Theorem 1.1, is unaffected.  The official Springer record matches author, title, volume 90, pages 473--475, issue year 2022 and DOI.  Sources: <https://doi.org/10.1007/s10623-021-00979-0>, <https://link.springer.com/article/10.1007/s10623-021-00979-0>. |
| C05 | `Kaleyski2021` | **Verified with scope qualification (exact).**  The primary IACR author preprint defines the differential spectrum on printed p.8 (PDF index 7, lines 546--548) and states its CCZ invariance on printed p.8 and again in Section 3.1 on printed p.12 (PDF index 11, lines 696--701).  That paper treats vectorial Boolean functions; the manuscript does not transfer an unstated binary theorem to odd characteristic, but immediately supplies its own general affine-difference proof and incorporates the ten vertical entries.  Springer metadata matches author, title, volume 13, pages 995--1023, year and DOI.  Sources: <https://eprint.iacr.org/2021/300.pdf>, <https://link.springer.com/article/10.1007/s12095-021-00541-8>. |
| C06 | `ZengLiuRatnavelu2026` | **Verified (paraphrase).**  The official Preprints.org v1 page lists the three authors, title, posting dates and DOI.  Its Data Availability Statement explicitly separates the algebraic proof from an exact-arithmetic companion verifier checking finite identities.  The local citation is deliberately limited to this verification practice and disclaims use as a CCZ source.  Source: <https://www.preprints.org/manuscript/202608.1194>. |

All six statuses are verified; there are no numerical errors, hallucinations,
misleading claims, missing citations or unverified retained references.  No
BibTeX or citation-key replacement is required.  The one selected user-library
record is row 8; its live primary record supports its literal nearby sentence.
The other five citations are natural non-library sources in ordinary body flow,
covering problem origin, foundational equivalence, closest prior
classification/correction and the standard spectrum method.  This is a normal
scholarly bibliography rather than a user-library-only list, and no reference is
decorative.

The publication dependency list was also checked.  The independent Python
checker and the complete certificate are stable corroborating inputs, not
bibliographic authorities; the checker reproduced the certificate and the two
histograms exactly.  Targeted current searches for the exact pair, the primary
identifier and Open Problem 4 found no post-v2 primary resolution other than
the cited prior classification route.  This bounded negative search is recorded
only as a limitation and not as evidence of priority.

Mechanical checks found six cited keys, six BibTeX entries, no missing or
unused entries, and exact agreement with the final `.aux` citation set.  The
active hook-compatible user-library validator accepted the attempt-2 job,
launch, registry, literal citation context, nearby-claim substring, ordinary
body-flow citation, and canonical bibliography bindings.  The release
build/log audit records the converged BibTeX build separately.
