# Citation audit

Audit date: 2026-08-29 (Asia/Shanghai).  Mode: web-search validation against
primary sources, followed by a manuscript-level consistency check.

## Pass 1: external claim inventory

| ID | Manuscript claim | Claim form | Cited location | Disposition |
|---|---|---|---|---|
| C01 | Lentfer constructs \(B_n^{(1,2)}\) and Conjecture 3.2 says it is a basis. | paraphrase | Definition 3.1 and Conjecture 3.2, journal p. 717 | verified |
| C02 | The candidate cardinality is \(2^{n-1}n!\). | paraphrase | Theorem 3.7, journal p. 719 | verified |
| C03 | The author reports verification for \(n\le4\). | paraphrase, explicitly attributed as an author report | Remark 3.3, journal p. 717 | verified |
| C04 | The path/alpha description in the manuscript is equivalent to Definition 3.1. | mathematical restatement | Definitions 2.1, 2.3, and 3.1, journal pp. 715--717 | verified |
| C05 | \(n=5\) is the first case beyond the verification reported in that paper. | qualified inference, not a global novelty assertion | C03 plus integer ordering | verified as phrased |

## Pass 2: source validation

The following query families were checked: author/title/year; exact title on
arXiv and Semantic Scholar; author/year/journal/topic; DOI
`10.5802/alco.424`; and arXiv identifier `2406.19715`.  The decisive evidence
was taken from primary records, not search-result snippets:

- official publisher record and version of record:
  <https://alco.centre-mersenne.org/articles/10.5802/alco.424/>;
- DOI record: <https://doi.org/10.5802/alco.424>;
- latest arXiv record: <https://arxiv.org/abs/2406.19715>.

The local version-of-record PDF has SHA-256
`37f6b097ff430f9ea498ae2aaf70013e105d0b6221d642ac147103babe8768ca`.
The decisive passages were also checked in the latest arXiv v3 source.  No
claim above is supported only by a secondary index.

## BibTeX/key audit

The manuscript has one citation key, `ALCO_2025__8_3_711_0`.  Its BibTeX was
copied from the official publisher and records John Lentfer, the exact title,
*Algebraic Combinatorics* 8 (2025), no. 3, pp. 711--743, and DOI
10.5802/alco.424.  The checked source/key counts are:

```text
cited_keys: 1
bib_keys: 1
missing_in_bib: []
unused_in_bib: []
aux_missing_vs_tex: []
aux_extra_vs_tex: []
```

## Verdict

All five externally sourced manuscript claims are supported and correctly
qualified.  The single reference exists, its metadata is authoritative, and
the citation points to the relevant definitions, conjecture, remark, and
theorem.  No citation was added for the new exact computations, which are
supported by local certificates rather than external literature.

## Gate 1 NOVELTY_LOCK supplement

This supplement records the wider source/novelty audit through **2026-08-29**;
it does not alter the manuscript-level BibTeX verdict above.

### Exact source locations and version boundary

| Item | Version of record | Latest arXiv v3 |
|---|---|---|
| Definition of $B_n^{(1,2)}$ | Definition 3.1, journal p. 717 / PDF p. 8 | PDF p. 7; TeX lines 619--621 |
| Basis statement | Conjecture 3.2, journal p. 717 / PDF p. 8 | PDF p. 7; TeX lines 706--708 |
| Author-reported finite check | Remark 3.3, journal p. 717 / PDF p. 8 | PDF p. 7; TeX lines 710--712 |
| Candidate cardinality | Theorem 3.7, journal p. 719 / PDF p. 10 | PDF p. 7; TeX lines 739--768 |

The journal version of record was published online 2025-06-26. The latest
public manuscript is arXiv v3, revised 2026-04-07 and labeled “Final version”;
v1 is dated 2024-06-28 and v2 2024-11-13. The v2-to-v3 source diff repairs
induction base-case wording in Theorem 3.7's proof and adjusts Figure 3 but
does not change Conjecture 3.2, Remark 3.3, or Theorem 3.7. The DOI metadata
has no update relation, and the publisher page exposes no formal
erratum/corrigendum.

### Later primary sources

1. Lentfer, arXiv:2501.09920v2 (2026-04-07), PDF p. 15 / source lines
   778--787, still describes relevant $R_n^{(1,2)}$ hook characters as
   conjectural and restates target-paper Theorem 8.4 conditionally.
2. Lentfer, arXiv:2505.14885v2 (2026-06-23), PDF p. 10, says all
   Frobenius-series cases with $k+j\ge3$ remain open.
3. Jiang--Lentfer, arXiv:2608.02881v1 (2026-08-03), Table 1, PDF p. 3 /
   source lines 221--244, marks
   $\dim R_n^{(1,2)}=2^{n-1}n!$ conjectural and cites the target as ref. [27].
4. Corteel--Lentfer, arXiv:2608.08187v1 (2026-08-08), uses a specialization
   of the target paper's Section 6 map but concerns $R_n^{(1,1)}$, not
   Conjecture 3.2.

No inspected later primary source claims a proof, counterexample, $n=5$
certificate, or extension of Remark 3.3 beyond $n=4$.

### Public-code scope

No code/repository link appears in the publisher or arXiv v1--v3 package, and
the author's official page provides no code link for this paper. GitHub
repository metadata searches by topic, arXiv ID, exact title, and DOI returned
zero. The GitHub repository-content code API returned HTTP 401 without
authentication, so the audit does **not** claim exhaustive GitHub file-content
coverage.

### Intermediate repeat (not the contractual post-result pass)

This provenance pass ran on 2026-08-29 at approximately 18:17
Asia/Shanghai, after the preliminary Gate-1 verdict but was not anchored to
the strict mathematical result:

- the arXiv API still returned 2406.19715v3, 2608.02881v1, and 2608.08187v1;
- exact-title arXiv search returned only the target;
- publisher and DOI repeats exposed no correction/update relation;
- exact-title and DOI GitHub repository searches again returned zero;
- authenticated GitHub code search remained unavailable.

Exact P01--P08 URLs, results, raw paths, hashes, and limitations are in
<code>literature/search_log.md</code>.

### Final pre-release novelty pass after the exact $n=5$ result

A fresh pass ran on **2026-08-29 at 18:17--18:22 Asia/Shanghai**, after the
research team reported that the exact $n=5$ theorem and its certificates were
available. It rechecked the target plus two newest relevant records through
the arXiv API; the full John Lentfer arXiv author feed; exact-title and
exact-$(1,2)$ topic searches; DOI/Crossref and the official publisher; GitHub
repository metadata by exact title, DOI, and arXiv ID; the GitHub code API; and
eight exact web-discovery queries for a proof, counterexample, $R_n^{(1,2)}$
basis result, or GitHub artifact. The target remained arXiv:2406.19715v3,
Jiang--Lentfer remained 2608.02881v1, and Corteel--Lentfer remained
2608.08187v1. No primary source claiming an earlier $n=5$ or general
settlement was discovered. GitHub repository queries returned zero, while its
content-search endpoint returned HTTP 401 and therefore supplies no exhaustive
negative evidence.

Exact F01--F18 URLs/queries, results, scoped limitations, raw artifact paths,
and sha256 hashes are in <code>literature/search_log.md</code>.

### Final Gate-1 verdict

**NOVELTY_LOCK: FINAL PRE-RELEASE PASS COMPLETE; PASS, QUALIFIED.** As of the
recorded searches through 2026-08-29, $n=5$ is the first case beyond Lentfer's
author-reported $n\le4$ baseline, and no prior public settlement, correction,
or paper-linked/exact-metadata public repository was found in the audited
scope. The 2026-08-03 primary frontier still marks the associated general
dimension formula conjectural.

This is not a global absence theorem. A cited 2026 Lentfer dissertation,
*Combinatorics of Bosonic-Fermionic Coinvariant Rings*, was not publicly
located in the audited official sources and remains uninspected; authenticated
GitHub file-content search was also unavailable. Those qualifications remain,
but the contractually required result-after novelty pass is complete and no
additional repeat is outstanding for this release.
