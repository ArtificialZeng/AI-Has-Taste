# Citation audit

Audit date: **2026-08-29**.  Scope: every item cited by `paper/main.tex`.
There are four cited keys, four database entries, no missing key, and no
uncited entry.  Because the bibliography is small, the main agent audited the
records serially rather than delegating them.

| Key | Existence and metadata | Claim supported | Resolution |
|---|---|---|---|
| `ErdosSzekeres1978` | Original three-page author-archive scan inspected; title, authors, journal, volume, issue, year, and pp. 97--99 agree with the scan, Erdős's publication list, MR 80e:10010, and Zbl 0401.10003.  No DOI was located. | The literal weak conjecture and the distinction from the stronger strict inequality. | Manual BibTeX retained with stable author-archive URL. |
| `Ecklund_1978` | DOI `10.1017/S1446788700011770` resolved to the Cambridge article; DOI content-negotiation BibTeX and publisher PDF agree on title, author list, journal, volume 26, issue 3, year 1978, and pp. 257--269. | The published large-prime-part theorem cited as classical context. | Official DOI BibTeX retained. |
| `Bloom699` | The current Erdős Problems entry #699 was inspected, including its dated history and proof-claim links. | Current open status and the reported ranges \(j\le3i/2\), \(n=2j\). | Custom web entry, access date pinned. |
| `Lu2026` | Repository README and pinned commit `7d030640beeb6bd64b4703fb2e252576a8ab56bb` inspected; GitHub account metadata identifies Cong Lu. | Public exact-arithmetic report through \(n=10^7\) and selected larger families. | Custom repository entry with commit-pinned URL. |

The prose distinguishes primary theorems from dated author/site reports.  In
particular, neither the current Erdős Problems page nor the Rust repository is
presented as a peer-reviewed proof.  The two novelty locks record the queries
and use the bounded phrase “not located in the recorded searches,” not an
absolute priority claim.

Mechanical cross-checks:

```bash
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py \
  paper/main.tex --aux paper/main.aux
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py \
  paper/main.tex paper/references.bib
```

Result: **pass**; cited 4, database 4, missing 0, unused 0, and AUX keys
consistent.
