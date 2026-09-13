# Gate 5 citation audit

Date: 2026-08-29  
Mode: source-by-source web verification, followed by LaTeX/BibTeX key audit.

## Citation inventory

The final manuscript contains three citation keys and the bibliography
contains exactly the same three keys. There are no missing or unused entries.

| Key | Claim supported | Authoritative record checked | Verdict |
|---|---|---|---|
| BandeltChepoiLaurent1998 | The \(n=3\) rectilinear case and earlier structural context | Springer DOI 10.1007/PL00009370; author-hosted published PDF; DBLP/Crossref author metadata | PASS |
| KoolenLaurentSchrijver2000 | The \(n=4\) case and positive weighted nested-cut formulation | CWI final PDF; DOI 10.1023/A:1008391712305; Crossref | PASS |
| GeXuZhou2026 | Current report that the \(p=1\) formula is known only through \(n=4\) | arXiv:2606.03987v1, submitted 2026-06-02; arXiv DOI 10.48550/arXiv.2606.03987 | PASS |

## Metadata decisions

1. **Bandelt--Chepoi--Laurent.** The Springer BibTeX export corrupts the
   first author's name as “-J. Bandelt, H.” The retained entry uses the
   printed article, DBLP, and Crossref form “Hans-Jürgen Bandelt.”
   Journal, volume 19, issue 4, pages 595--604, year 1998, and DOI agree.
2. **Koolen--Laurent--Schrijver.** Crossref, CWI, and the issue record give
   volume 21, combined issues 1--3, pages 149--164, year 2000. A single
   Springer article-export endpoint labels the issue as 1; the combined
   issue form is retained because it agrees with the formal issue and
   Crossref records.
3. **Ge--Xu--Zhou.** The manuscript cites the official arXiv record as a
   preprint and makes no journal-publication claim. The inspected version is
   v1.

## Claim-to-source check

- Bandelt--Chepoi--Laurent, Proposition 4.1, supports the
  three-dimensional upper bound; the cross-polytope gives equality.
- Koolen--Laurent--Schrijver, Proposition 8 and Theorem 9, support
  \(e(\ell_1^4)=8\). Proposition 2 is the closest prior cut-family
  framework to the present reduction.
- Ge--Xu--Zhou, Section 1.1, explicitly reports that the \(p=1\) conjecture
  is known only for \(n\le4\). This is used as a dated current-status report,
  together with the bounded secondary novelty sweep, not as a logical proof
  that no unindexed work exists.

## Mechanical checks

- LaTeX citation keys: 3.
- BibTeX entries: 3.
- Missing keys: 0.
- Unused entries: 0.
- Undefined citations after clean BibTeX build: 0.
- Duplicate entries: 0.

The mechanical key audit and final converged-log scan were rerun after the
last layout-only source edit; the same 3/3/0/0 counts and zero undefined
citations were reproduced.

Detailed queries, exact page locations, database limitations, and the final
support-\(19\) no-match sweep are recorded in
'literature/search_log.md', 'literature/claim_ledger.md', and
'literature/NOVELTY_LOCK.md'.
