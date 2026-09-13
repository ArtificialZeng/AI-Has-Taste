# Fresh citation and claim-to-source audit

Date: 2026-09-09  
Release job: `bigMac-00023-p06-release-71cb8b727e7d`  
Method: `$citation-check-skill` v2 used as an advisory two-pass audit, with primary-source web/local inspection and frozen-evidence checks.  
Document: `manuscript/main.tex` and the freshly built `manuscript/main.pdf`.

## Pass separation and scope

Pass 1 was completed and fixed before verification in
`audit/citation-claims.md`; pass 2 used exactly claims C01--C20 from that
file. The authored dependency list was checked against the TeX/BibTeX build:
`publication.json`, `manuscript/main.tex`, and `manuscript/references.bib`
account for all authored inputs. The `.fls` file contains no other authored
project input; its other local inputs are generated `.aux`, `.bbl`, and `.out`
files. The extracted PDF contains four resolved bibliography entries, and the
final `.aux` maps every cited key to a bibliography item.

`literature/user_bibliography_check.md` is not present, and a project search
found no Excel workbook. Thus no user-workbook record was available to inspect
or to identify as the source of a citation. This absence is already disclosed
in `publication.json`. It does not make any of the four actually cited records
unverified: all four were checked against primary records/text. Metadata basis
is the cited primary records plus the frozen local Basic PDF, not a
user-designated workbook.

## Bibliographic records and nearby attributions

The required author/year/title, full-title, venue, DOI, and (where applicable)
arXiv-ID searches were run on 2026-09-09. Online checks were bounded after the
primary records and relevant passages were obtained.

| Key | Metadata and source-text check | Nearby manuscript claim | Result |
|---|---|---|---|
| `Basic2026` | arXiv `2609.03184v1`, submitted 2026-09-02, title *On uniquely colorable Cayley graphs*, author Milan Bašić. The frozen eight-page PDF `literature/2609.03184v1.pdf` has the exact source hash. Its §2 (printed p. 2) gives the arbitrary divisor-set `ICG_n(D)` description; §5 (printed p. 7) says the full perfect integral-circulant classification remains open after the unitary case. | Usual divisor-set description and the broader open direction. | Verified, exact/paraphrase. |
| `ChudnovskyEtAl2006` | Maria Chudnovsky, Neil Robertson, Paul Seymour, Robin Thomas, *The Strong Perfect Graph Theorem*, *Annals of Mathematics* 164(1), 51--229 (2006), DOI `10.4007/annals.2006.164.51`. The official Annals abstract defines Berge graphs by absence of odd holes and their complements and states that the paper proves perfect iff Berge. | Perfect iff neither graph nor complement contains an induced odd cycle of length at least five. | Verified, paraphrase with the same hypotheses. |
| `KlotzSander2007` | Walter Klotz and Torsten Sander, *Some Properties of Unitary Cayley Graphs*, *Electronic Journal of Combinatorics* 14, R45 (2007), DOI `10.37236/963`. The official journal PDF states at Theorem 12 (printed p. 7) that `X_n=ICG_n({1})` is perfect iff `n` is even or `n` is odd with at most two distinct prime divisors. | The unitary `D={1}` subfamily has a perfectness classification. | Verified, exact scope. |
| `So2006` | Wasin So, *Integral Circulant Graphs*, *Discrete Mathematics* 306(1), 153--158 (2006), DOI `10.1016/j.disc.2005.11.006`. The publisher record gives the same metadata. Theorem 7.1 gives the union-of-gcd-classes characterization; §7 says spectra for all possible symbols below 100 were computed before Conjecture 7.3. | Divisor-set description; prior sub-100 enumeration was spectral and is not asserted to be a perfectness census. | Verified, exact/paraphrase. |

Primary pages used online were the arXiv record, the official Annals article
page, the official EJC PDF/citation record, and the publisher's So article
record and §7 text. The Basic claim-support passages were additionally checked
in the frozen local PDF rather than inferred from its DOI or abstract.

## Fixed-claim verification results

| IDs | Evidence checked | Status |
|---|---|---|
| C01, C12 | `claim.json`, `evidence/n32_manifest.json`, and a direct parser comparison of every manuscript table mask. There are exactly 539 records, 415 perfect and 124 imperfect; row counts are 6, 6, 54, 6, 52 and every mask matches. | Verified, exact. |
| C02, C03 | Frozen manifest certificate fields, accepted `audit/math.md`, and the manuscript's explicit translation/completeness proof; SPGT checked above. No stronger scope than the accepted `n<=32` statement was introduced. | Verified. |
| C04, C17, C18 | `evidence/n32_replay.json` reports 539 coverage and adjacency checks and 124 verified witnesses; `evidence/n32_networkx_crosscheck.json` reports NetworkX 3.4.2, 539 records, 1,602,322 cycles, no mismatches. | Verified, exact. |
| C05 | Abstract and limitations retain `33<=n<=64` and unbounded `n` as unproved. This agrees with `claim.json`, `source.md`, and Basic §5. | Verified. |
| C06--C10 | Original-source checks in the preceding table. | Verified. |
| C11 | The sentence reports only a bounded negative search and explicitly disclaims priority. It matches `evidence/primary-source-collision-screen.md`; it is not presented as proof that no prior result exists. | Verified as a bounded-process statement. |
| C13 | Manifest includes `n=1` and both extreme masks; the complement identity follows directly from the strict-divisor partition and is proved in the text. | Verified. |
| C14 | Manifest summary and witnesses give 2,789,071 states; sides 105/19; lengths 86/36/2. | Verified, exact. |
| C15 | Manifest record `(n,dmask)=(12,6)` has `D={2,3}` and graph-side cycle `[0,2,4,1,3]`. | Verified, exact. |
| C16 | Manifest canonicalization states translations, multiplication by units, rotations, and reversal; the prose correctly says this affects presentation only. | Verified. |
| C19 | Manifest summary gives 329 structurally covered perfect records and residue 86 across exactly the seven listed classes. | Verified, exact. |
| C20 | Manifest runtime is CPython 3.13.5; the NetworkX record is 3.4.2; the named programs and JSON outputs exist. | Verified, exact. |

No numerical error, contradicted attribution, misleading strengthening,
undefined citation, unsupported novelty assertion, or removable citation was
found. All four citations are relevant; Klotz--Sander and So are especially
material comparisons with the claimed finite perfectness census. The missing
optional user bibliography-check file is disclosed without fabricating an
Excel-list provenance.

**Verdict: accept.**

