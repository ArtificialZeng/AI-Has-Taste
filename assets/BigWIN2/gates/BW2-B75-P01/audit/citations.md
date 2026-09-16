# Citation and bibliography audit

**Verdict:** accept  
**Release job:** `win-00075-p01-release-2a110e7491e7`  
**Citation attempt / launch:** `4` / `b1e993d3-8a4f-458a-8444-bdb9a95d0faa`  
**Primary-source verification date (UTC):** `2026-09-08`

## Scope and method

The audit covered every ordinary body-flow citation in `manuscript/main.tex` and every entry in the canonical `manuscript/references.bib`. It used the required two-stage non-interactive procedure: first, each substantive claim/citation pair was frozen in `audit/citation-claim-ledger.json`; second, each pair was checked against a located passage in the primary publication or the cited standard monograph. The detailed locators and support determinations are preserved in `audit/citation-source-verification.json`.

Per-key verification was performed serially in this release context because the job prompt expressly prohibited agents, other Codex processes, and background workers. No source lead was accepted solely from registry metadata.

## Claim-level verification

| Claim | Key | Primary source and exact locator | Determination |
|---|---|---|---|
| Ambient seventh-degree unit-circle family and its complete root-count distribution | `XiongYan2026` | [arXiv:2609.04683v1](https://arxiv.org/abs/2609.04683v1), abstract and submission metadata | Verified exactly. The abstract states the displayed family, parameter field, unit circle, and complete frequency distribution. |
| Generic characteristic-zero reversibility and explicit positive-characteristic information loss | `Zeng2026Bezout` | [Preprints.org 202608.2160](https://www.preprints.org/manuscript/202608.2160), abstract and Section 6, Proposition 6.1 | Verified as a faithful comparison. The source states the generic characteristic-zero result and gives the family \(X^p+cX+d\), whose canonical pair is independent of \(d\). |
| Standard trace criteria and additive-character background | `LidlNiederreiter1996` | [Finite Fields, 2nd ed.](https://doi.org/10.1017/CBO9780511525926), Corollary 3.79 and Chapter 5, Section 1 | Verified. These are the cited standard locations for the characteristic-two quadratic trace criterion and finite-field characters. |
| Artin--Schreier function-field facts | `Stichtenoth2009` | [Algebraic Function Fields and Codes, 2nd ed.](https://doi.org/10.1007/978-3-540-76878-4), Chapter 3, Section 3.7, Proposition 3.7.8, pp. 127--128 | Verified. The proposition treats Artin--Schreier extensions, normalized poles, ramification, and genus. The manuscript separately supplies its smoothness and adjunction calculation. |
| Finite-extension curve point-count formula | `Weil1948` | [*Sur les courbes algébriques et les variétés qui s'en déduisent*](https://denisevellachemla.eu/Weil-courbes-varietes.pdf), Part II, Section IV, Theorem 13 and Corollary 2, pp. 58--60, and no. 22, pp. 60--61 | Verified. Combining the two displayed identities gives \(N_m=q^m+1-\sum_i\alpha_i^m\), hence the genus-one formula used in the manuscript. |

All five ledger claims passed. There were no missing publications, misquotations, misleading attributions, unsupported numerical claims, or unresolved verification items.

## Bibliography coverage and consistency

The bibliography is claim-driven rather than padded. `XiongYan2026` supplies the problem-family provenance; `LidlNiederreiter1996`, `Stichtenoth2009`, and `Weil1948` supply the non-library primary or standard-method background actually invoked; and the gate-selected user-library item `Zeng2026Bezout` supports one explicitly delimited comparison about characteristic dependence. The latter is cited in ordinary body flow and is not used as proof input. No second active-library item naturally supports a manuscript claim, as recorded in `audit/user-bibliography-selection.json`.

Mechanical extraction found exactly five ordinary body-flow citation keys and exactly the same five canonical BibTeX keys. The `.aux` file records all five, while comments, `\nocite`, verbatim material, inert macros, and hidden conditionals contribute none. There are no missing, unused, duplicate, or undefined entries; no BibTeX replacement or citation-key change was required. The compilation log contains no undefined citation/reference or BibTeX diagnostics.

**Final determination:** the nearby claims are directly supported, dependency scope is complete, bibliography coverage is natural, and the citation audit accepts the manuscript.
