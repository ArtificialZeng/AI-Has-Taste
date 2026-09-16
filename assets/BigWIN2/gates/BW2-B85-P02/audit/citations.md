# Fresh citation and bibliography audit

## Scope and method

This is a two-stage search-mode audit of the canonical
\`manuscript/main.tex\` and \`manuscript/references.bib\`, bound to release job
\`win-00085-p02-release-d2c2bb0d2824\`, citation attempt 2, launch
\`d684f23c-e8a7-4420-8761-b8a07c0f4262\`, and manuscript snapshot
\`1c1a3d4cddbada860f02773aa7da2ff4272ae4988cb747f72ce8a39270b138e0\`.
The extraction pass was frozen in
\`audit/citation-claim-ledger.json\`; the verification pass then checked each
source record and the exact supporting passage.  The manuscript and
bibliography did not require correction; their frozen digests remain current.

The audit used primary publisher or repository pages and inspected the actual
source text, not search snippets alone.  Web searches used the required
author/year/title, full-title, author/venue, and DOI or arXiv-identifier forms.
The release worker performed the checks directly because this bounded job
explicitly prohibited subagents.

## Frozen claim-to-source verification

| Claim | Direct keys | Primary location inspected | Status | Confidence |
|---|---|---|---|---|
| CIT-01: Sun introduced \(s_r(n)\) with exactly \(n\) selected positions. | \`Sun2026ZeroSum\` | arXiv:2606.18234v5, Definition 1.3, HTML lines 94--110 | Verified | paraphrase |
| CIT-02: Sun's lower bound and the upper bound from \(s(\mathbb Z_n^2)=4n-3\), with the latter supplied by Kemnitz's conjecture. | \`Sun2026ZeroSum\`, \`Reiher2007Kemnitz\` | Sun v5, Theorem 1.3(ii)--(iii) and Remark 1.4, HTML lines 118--140; Reiher, p. 1 and Theorem 3.2 on p. 4 | Verified | paraphrase |
| CIT-03: Gao--Jiang--Mu's local constants permit a nonempty subsequence or one of length at most \(n\), not an exactly-four subsequence. | \`GaoJiangMu2026Local\` | arXiv:2607.11313v1, abstract and Definition 1.1, HTML lines 29--32 and 43--53 | Verified | paraphrase |
| CIT-04: the selected library paper uses independent exact-integer reconstructions for finite combinatorial certificates. | \`ZengEtAl2026FiniteCertificates\` | Preprints.org v1, Section 3 lines 155--157 and Section 6 lines 207--218 | Verified | paraphrase |

No numerical error, contradiction, omitted hypothesis, or unsupported
strengthening was found in these four citation-bearing claims.

## Publication-record audit

| Key | Record checked | Authoritative source | Metadata result | Action |
|---|---|---|---|---|
| \`Sun2026ZeroSum\` | Zhi-Wei Sun, *On zero-sum problems of new types*, arXiv:2606.18234v5, revised 2 July 2026 | https://arxiv.org/abs/2606.18234 and https://arxiv.org/html/2606.18234v5 | Author, current title, identifier, version, revision date, and subject agree | retained |
| \`GaoJiangMu2026Local\` | Weidong Gao, Xiao Jiang, Yucen Mu, *Two local zero-sum problems*, arXiv:2607.11313v1 | https://arxiv.org/abs/2607.11313 and https://arxiv.org/html/2607.11313 | Authors, title, identifier, version, submission date, and arXiv DOI agree | retained |
| \`Reiher2007Kemnitz\` | Christian Reiher, *On Kemnitz' conjecture concerning lattice-points in the plane*, *The Ramanujan Journal* 13, 333--337 (2007) | https://link.springer.com/article/10.1007/s11139-006-0256-y and https://arxiv.org/abs/1603.06161 | Author, title, journal, volume, pages, year, issue range, and DOI agree | retained |
| \`ZengEtAl2026FiniteCertificates\` | Zijian Zeng, Houde Liu, Kuru Ratnavelu, Ong Seng Huat, *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*, v1 (2026) | https://www.preprints.org/manuscript/202608.1658 | Authors, title, version, August 2026 posting, DOI identity, and methodological passage agree | retained |

The active 49-record first-sheet library was reviewed.  Row 9 is the sole
natural selection: it directly supports the finite-certificate methodology.
Adding unrelated library entries would pad the bibliography.  The bibliography
is not library-only: Sun is the problem-origin and closest-conjecture source,
Gao--Jiang--Mu is the closest later quantifier comparison, and Reiher is the
primary source for the imported Kemnitz equality.  All four entries are used
in ordinary body flow; none is decorative.

Fresh UTC-date exact-assertion searches included \`"s_1(4)"\`, \`"s_1(4)=9"\`,
\`"s_1(n)=2n+1"\`, and \`"2606.18234" "s_1(4)"\`; candidate records were
checked against the live arXiv primary record.  The searches located Sun's
conjecture but no later primary source resolving this exact
case.  This bounded negative search is not a priority claim.

## Mechanical consistency

\`check_bib_keys.py manuscript/main.tex --aux manuscript/main.aux\` found four
body citation keys, four BibTeX entries, and four AUX bibliography keys, with
no missing, unused, or stale key.  The final \`main.log\` and \`main.blg\`
contain no undefined citation, missing database entry, repeated entry, LaTeX
error, fatal error, emergency stop, undefined control sequence, or runaway
argument.  No citation key changed and no BibTeX replacement was required.

**Verdict: ACCEPT.**  Citation existence, claim support, metadata, bibliography
coverage, ordinary-flow use, and build consistency all pass for the current
snapshot.
