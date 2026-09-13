# Gate 1 claim ledger (NOVELTY_LOCK)

Audit cutoff: **2026-08-29, Asia/Shanghai**. This ledger freezes and checks
only the source/novelty claims needed to decide whether the proposed $n=5$
project has the advertised boundary. Mathematical claims below are supported
only by primary sources: the author's papers/preprints and official publisher,
DOI, arXiv, university, and repository records.

## Frozen claims and dispositions

| ID | Frozen claim | Claim type | Gate-1 disposition | Primary evidence and exact location | Confidence | Consequence |
|---|---|---|---|---|---:|---|
| C01 | Lentfer defines $B_n^{(1,2)}$, and Conjecture 3.2 says that it is a basis of $R_n^{(1,2)}$. | exact | **verified** | Published paper, Definition 3.1 and Conjecture 3.2, journal p. 717 (PDF p. 8); arXiv v3 PDF p. 7; v3 TeX definition lines 619--621 and conjecture lines 706--708. Exact conjecture sentence: “The set $B_n^{(1,2)}$ is a basis for $R_n^{(1,2)}$.” | 100% | Fixes the target statement. |
| C02 | The paper proves $\lvert B_n^{(1,2)}\rvert=2^{n-1}n!$. | exact | **verified** | Theorem 3.7, journal p. 719 (published PDF p. 10); arXiv v3 PDF p. 7 and TeX lines 739--768. | 100% | Hence $\lvert B_5^{(1,2)}\rvert=2^4 5!=1920$, by exact integer arithmetic. |
| C03 | The source says the basis conjecture has been verified for $n\le4$. | author report | **verified as an author report, not as an independently certified computation** | Remark 3.3, journal p. 717 (published PDF p. 8); latest arXiv v3 PDF p. 7 and TeX lines 710--712. Exact sentence: “The conjecture has been verified for $n\leq 4$.” The paper supplies no computation certificate or code for this sentence. | 100% that the author reports it; no Gate-1 assessment of the computation itself | The last claimed baseline in the source is $n=4$. It must still be reproduced independently before relying on the implementation. |
| C04 | Canonical publication metadata are John Lentfer, *A conjectural basis for the $(1,2)$-bosonic-fermionic coinvariant ring*, *Algebraic Combinatorics* 8 (2025), no. 3, 711--743, DOI 10.5802/alco.424. | exact metadata | **verified** | Official journal record and DOI/Crossref CSL record. Journal record also gives received 2024-08-09, revised 2025-02-19, accepted 2025-02-24, and published online 2025-06-26. | 100% | Use this as the canonical bibliographic citation. |
| C05 | As of the cutoff there is no public proof/disproof of $n=5$ or of the full conjecture. | global novelty/absence claim | **not established globally; no solution found in the recorded search scope** | Strongest positive frontier evidence: Jiang--Lentfer, arXiv:2608.02881v1 (submitted 2026-08-03), Table 1, PDF p. 3, marks the $(k,j)=(1,2)$ dimension $2^{n-1}n!$ with a dagger and says daggered entries are conjectural. TeX lines 221--244. Lentfer, arXiv:2505.14885v2 (revised 2026-06-23), PDF p. 10, says all $k+j\ge3$ Frobenius-series cases remain open. Exact-title, exact-topic, author, citing-paper, publisher/DOI, and code searches found no proof/disproof. “Not found” is limited to those sources and queries. | 95% for the scoped conclusion; 0% for any impossible-to-certify all-public-literature absence claim | Gate 1 permits the $n=5$ result to be reported with the stated novelty qualification. The contractual final pre-release search was completed after the exact result was available. |
| C06 | The 2025 publication is the latest relevant manuscript and there is no correction/erratum affecting Conjecture 3.2. | version claim | **first clause false; target statement unaffected in located versions** | arXiv identifies **v3, 2026-04-07**, as the latest version and labels it “Final version”; v1 2024-06-28, v2 2024-11-13. v3 still has the same Conjecture 3.2, Remark 3.3, and Theorem 3.7. Compared with v2, v3 repairs wording/base-case details in Theorem 3.7's proof and adjusts Figure 3; the target statements do not change. The official publisher page has no correction/corrigendum link, and the DOI record has empty relation and no update-to/updated-by entry. This is only a scoped no-erratum finding. | 100% on version history and unchanged target statements; 95% on scoped no-erratum search | Work from arXiv v3 plus the version of record, not from v1/v2 alone. Do not describe the 2025 PDF as the latest manuscript. |
| C07 | Public source code exists that implements the same quotient and reproduces $n\le4$. | code-availability claim | **not found in the recorded scope** | No code/repository URL or computational appendix occurs in the published PDF or any arXiv v1--v3 source. The author's official research page links only journal/arXiv records for this paper and has no code link. GitHub repository API searches for exact topic and arXiv ID returned total_count 0; exact-title/domain web discovery searches returned no repository. GitHub repository search does not search all file contents, so this is not a global nonexistence claim. | 95% for “no paper-linked or metadata-matching public repository found” | Baselines and exact verifier must be implemented independently; no external code may be treated as a certified reference. |
| C08 | $n=5$ is the first unverified dimension. | inference | **verified only as an inference from the audited author reports/frontier, not as a quotation** | C03 gives every $n\le4$; C05 gives no located later extension and, more strongly, the 2026-08-03 primary frontier still labels even the general dimension formula conjectural. Thus the least positive integer not covered by the author report is 5. | 95% (novelty-limited) | Correct project wording: “$n=5$ is the first dimension not covered by the author's $n\le4$ verification, and no later settlement was found in the recorded searches.” |
| C09 | Later primary literature still treats relevant $R_n^{(1,2)}$ data as conjectural. | exact later-literature claim | **verified** | (i) Lentfer, arXiv:2501.09920v2 (2026-04-07), PDF p. 15 / TeX lines 778--787, calls the hook characters of $R_n^{(1,2)}$ conjectural and states Theorem 8.4 conditionally. (ii) Jiang--Lentfer, arXiv:2608.02881v1 (2026-08-03), Table 1, PDF p. 3, marks $\dim R_n^{(1,2)}=2^{n-1}n!$ conjectural. | 100% | This is strong contemporaneous primary evidence that the target was not known to those authors by 2026-08-03; it is not a proof of worldwide absence. |
| C10 | A 2026 Lentfer dissertation may supersede the paper. | unverified source lead | **bibliographic lead located; thesis text not publicly located in the audited official sources** | Jiang--Lentfer arXiv:2608.02881v1 bibliography cites John Lentfer, *Combinatorics of Bosonic-Fermionic Coinvariant Rings*, PhD thesis, UC Berkeley, 2026, but gives no URL. The UC Berkeley department publication searches returned no Lentfer/title match; the official author page links no thesis. | 90% that the dissertation exists as cited; 0% on uninspected contents | Its unavailability in the final pre-release pass is an explicit residual limitation, not evidence that it contains no solution. |

## Theorem frontier frozen for this project

1. **Established in the audited source:** Definition 3.1 constructs
   $B_n^{(1,2)}$; Theorem 3.7 proves its cardinality $2^{n-1}n!$ for general
   $n$.
2. **Author-reported finite verification:** Remark 3.3 says Conjecture 3.2 was
   verified for $n\le4$, without a public certificate or implementation in
   the paper package.
3. **Still conjectural in the newest directly relevant primary frontier
   found:** Jiang--Lentfer (2026-08-03) marks
   $\dim R_n^{(1,2)}=2^{n-1}n!$ conjectural. A basis theorem would imply that
   dimension formula, so the general basis conjecture is not presented there
   as settled.
4. **Current finite target:** $n=5$, with 1920 candidate monomials, is the
   first case beyond the source's reported verification. Whether the basis
   statement holds at $n=5$ is not decided by Gate 1.

## Mandatory wording correction to the project boundary

Do **not** state without qualification that “$n=5$ is the first open
dimension” as a globally certified fact. State instead:

> Lentfer's latest arXiv version (v3, 2026-04-07) still reports verification
> only for $n\le4$, and a 2026-08-03 primary paper still marks the associated
> general dimension formula conjectural. No settlement of $n=5$ was found
> in the explicitly recorded searches; hence $n=5$ is the first case beyond
> the published author-reported baseline.

## Final pre-release Gate-1 verdict after the exact $n=5$ result

**NOVELTY_LOCK: FINAL PRE-RELEASE PASS COMPLETE; PASS, QUALIFIED.** After the
exact $n=5$ theorem and its certificates were reported available, a fresh
search on 2026-08-29 at 18:17--18:22 Asia/Shanghai found no newer arXiv
version, publisher/DOI correction, later public settlement, or
paper-linked/exact-metadata public repository. The exact F01--F18 queries,
results, raw paths, and hashes are recorded in
<code>literature/search_log.md</code>. The earlier P01--P08 pass is retained
there as an intermediate provenance check and is not counted as the
contractual result-after novelty pass.

This final lock does not certify worldwide absence. In particular, the cited
2026 Lentfer dissertation remains uninspected and authenticated GitHub
repository-content search was unavailable. Those limitations qualify the
novelty claim but do not leave an additional novelty pass outstanding for this
release.
