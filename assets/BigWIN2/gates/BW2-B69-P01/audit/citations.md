# Citation and claim audit

**Verdict:** accept  
**Mode:** two-pass extraction and fresh primary-source verification  
**Verification date:** 2026-09-08  
**Release job:** `win-00069-p01-release-f4ce9d811492`  
**Citation attempt / launch:** `3` / `9177a0a5-39ad-4352-9916-8514c0ff383d`

## Two-pass procedure

Pass 1 reread the complete canonical manuscript after the rendering-preserving
TeX-parser compatibility edit and froze 21 substantive claims with their direct
citation keys in `audit/citation-claim-ledger.json`.  The citation-bearing prose
and line intervals are unchanged.  The ledger is bound to the current source,
bibliography, snapshot, attempt-3 job, and launch identity; its seven-key union
is exactly the ordinary body-flow citation surface of `manuscript/main.tex`.

Pass 2 replayed the frozen claim identifiers in order against the exact recorded
locators and freshly checked primary Annals, arXiv, Elsevier, Normaliz, PeerJ,
and Preprints.org records.  Mathematical and numerical claims without external
citations were replayed against accepted `claim.json`, `audit/math.md`, and the
frozen exact certificate reports.  The active registry record and literal nearby
manuscript context were also rechecked.  This release audit does not reinterpret
a build or audit record as a mathematical proof.  The bibliography skill's
default delegation was not used because this bounded job explicitly prohibited
agents and background workers.

## Summary

| Metric | Count |
|---|---:|
| Frozen substantive claims | 21 |
| Verified or supported | 21 |
| Ordinary body-flow citation keys | 7 |
| Citation not found | 0 |
| Numerical error | 0 |
| Misquoted, misleading, or hallucinated | 0 |
| Unverified | 0 |

## Pass-2 claim results

| IDs | Final manuscript lines | Verification source and locator | Status |
|---|---:|---|---|
| C01, C05--C06, C08--C10, C12, C14--C17, C21 | 34--49, 71--98, 131--186, 206--218, 229--277, 304--308 | Accepted `claim.json` and `audit/math.md`; exact certificate counts and reductions agree with the frozen evidence | Verified, exact/paraphrase |
| C02 | 54--55 | Brändén--Huh, Annals publisher abstract and article record | Verified, paraphrase |
| C03, C07, C11, C18 | 55--62, 111--129, 195--204, 279--286 | Bathija--Rohatgi--Soskin, arXiv v1, Definitions 5.4 and 9.1, Proposition 7.4, Conjecture 9.2 | Verified, exact/paraphrase |
| C04 | 64--69 | Huang--Huh--Soskin--Wang, arXiv v2, Conjecture 5.5; Bathija--Rohatgi--Soskin, Definitions 5.4 and 9.1 | Verified, exact/paraphrase |
| C13 | 220--228 | Bruns--Ichim publisher abstract; official Normaliz site and How-to-cite page | Verified, paraphrase |
| C19 | 288--296 | PeerJ article record and abstract; accepted project evidence for the particular use | Verified, paraphrase/exact workflow report |
| C20 | 298--302 | Official Preprints.org v1 abstract and Section 14 | Verified, exact/paraphrase |

## Citation-by-citation audit

| Key | Primary record and exact nearby support | Metadata/action | Verdict |
|---|---|---|---|
| `BrandenHuh2020` | Annals of Mathematics 192(3), 821--891, DOI `10.4007/annals.2020.192.3.4`; abstract and keywords support the broad Lorentzian/log-concavity context | All retained fields agree with the publisher | Verified |
| `BathijaRohatgiSoskin2026` | arXiv:2609.05341v1, Definitions 5.4 and 9.1, Proposition 7.4, Conjecture 9.2 | Authors, title, version, year, identifier and class agree | Verified |
| `HuangHuhSoskinWang2025` | arXiv:2510.25030v2, Conjecture 5.5 | Authors, title, version, year, identifier and class agree | Verified |
| `BrunsIchim2010` | Journal of Algebra 324(5), 1098--1113, publisher abstract, DOI `10.1016/j.jalgebra.2010.01.031` | All retained bibliographic fields agree | Verified |
| `Normaliz` | Official Normaliz home and How-to-cite pages; Hilbert-basis and rational-cone computation goals | Official authors, title and URL agree; access note is accurate | Verified |
| `MeurerEtAl2017` | PeerJ Computer Science 3:e103, publisher abstract, DOI `10.7717/peerj-cs.103` | Accurate scholarly et-al. author form; title, venue, year, article number and DOI agree | Verified |
| `Zeng2026Lens` | Official Preprints.org v1, abstract and Section 14, DOI `10.20944/preprints202608.1272.v1` | Registry row 13 and primary record agree; final key retained | Verified |

No key change or BibTeX repair was needed.  The final `.bib`, `.aux`, and body
citation sets are the same seven keys, with no missing, unused, duplicated, or
undefined entry.

## Coverage and necessity

The bibliography is not user-library-only.  `BathijaRohatgiSoskin2026` is the
primary source of the conjecture, conventions, and closest degree-four cone
result; `HuangHuhSoskinWang2025` is the primary predecessor;
`BrandenHuh2020` supplies the natural foundational context;
`BrunsIchim2010` and `Normaliz` document the nontrivial Hilbert-basis method and
software; and `MeurerEtAl2017` documents the symbolic-computation system.
`Zeng2026Lens` is the one genuinely relevant active-library record and supports
only the explicit exact-verifier methodology comparison.  Every retained key
has a direct ordinary body-flow use and a substantive nearby claim.  No
reference is decorative, and a second user-library citation would duplicate
the same limited methodological point rather than cover a missing dependency.

The bounded source search and accepted referee screen found no equivalent
single-chamber theorem in the inspected records as of 2026-09-08; this is not a
claim of priority or proof that unpublished overlap is absent.
