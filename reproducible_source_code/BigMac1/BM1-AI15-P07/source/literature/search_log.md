# Search log

## NOVELTY_LOCK 1 -- 2026-08-29

The claim list C01--C11 was frozen before computational discovery.  Sources
were prioritized as: original paper/author archive; DOI/publisher metadata;
formal repository records; then dated author reports.  Forum and SciNet
entries are not treated as peer-reviewed theorems.

| Time (UTC) | Database/site | Query or target | Result used |
|---|---|---|---|
| 2026-08-29 03:50 | GitHub API + Formal Conjectures | issue 887 and comments | Exact statement; issue is closed after formalization, has no comments; closure does not solve conjecture. |
| 2026-08-29 03:52 | Erdős Problems | `/699`, history, LaTeX, discussion, proof claims | Current status, accepted partial range, two proof claims, 2026 computations and reports. |
| 2026-08-29 03:57 | Crossref | bibliographic query for Ecklund--Eggleton--Erdős--Selfridge | DOI 10.1017/S1446788700011770, journal metadata, abstract, theorem scope. |
| 2026-08-29 04:00 | Google-indexed web search | exact titles; “Erdős Problem 699”; “p >= i” | Located author-archive scan `https://combinatorica.hu/~p_erdos/1978-46.pdf`, Cambridge PDF, SciNet report, and related records. |
| 2026-08-29 04:02 | Erdős Problems data repository | `data/problems.yaml`, entry 699 | Status `falsifiable`; formalized yes; OEIS N/A. |
| 2026-08-29 04:03 | Crossref/Cambridge | DOI and article page for 1978 EEES paper | Publisher metadata and primary PDF located. |

### First-pass queries

- `"Some number theoretic problems on binomial coefficients" Erdős Szekeres PDF`
- `"On the prime factorization of binomial coefficients" PDF`
- `"Erdős Problem 699" binomial coefficient`
- `site:github.com/google-deepmind/formal-conjectures/issues/887`
- bibliographic Crossref queries for the 1978 Erdős--Szekeres and EEES papers
- Erdős Problems discussion/proof-claim/history pages and linked Overleaf projects

### Frontier at lock time

- **Original problem:** open/falsifiable.
- **Published classical input:** Sylvester--Schur; EEES large-prime-part theorem.
- **Accepted 2026 partial result:** \(j\le3i/2\) or \(n=2j\).
- **Unverified stronger 2026 claim:** ineffective reduction to \(i=3\) or finitely
  many exceptional triples with \(4\le i\le1475\).
- **Computational reports:** weak form through \(10^7\) in an open-source Rust
  report; a separate \(10^5\) SciNet enumeration awaiting independent review.
- **No located weak-form counterexample or complete proof.**

The second novelty pass must repeat targeted title/citation searches after any
candidate theorem or counterexample has been exactified.

## NOVELTY_LOCK 2 -- exact endpoint search, 2026-08-29

Frozen candidate endpoint: “weak Erdős #699 holds for the complete stratum
\(i=3\), \(8\le n\le100{,}000{,}000\).”

Queries:

- `"Erdős 699" "100,000,000" i=3`
- `"Erdos 699" "100000000" binomial`
- `"i = 3" "Erdős Problem #699" computation`
- `"Erdős Problem 699" verified i=3`
- `site:github.com "erdos699" "i=3"`
- `site:github.com "erdos_699" "100000000"`
- `site:arxiv.org Erdős Szekeres binomial coefficients common prime factor i j`
- `site:doi.org Erdős Szekeres binomial coefficients common prime divisor`

Databases/pages rechecked: Erdős Problems #699 and discussion/proof claims;
GitHub-indexed repositories; arXiv; Crossref/DOI publisher results; OEIS Wiki;
MathDB; SciNet finding 76626b5c; Formal Conjectures.

Results located were: all-\(i\) exhaustive reports to \(10^7\), a separate
all-\(i\) certified report to \(10^5\), an OEIS user report to \(10^6\), and
targeted rows \(n=2^k\), \(n=3^m+1\) up to about \(1.3\times10^8\).  No prior
complete \(i=3\), all-rows endpoint at \(10^8\) was located.  This is a bounded
database/search statement, not a guarantee of absolute priority.

## NOVELTY_LOCK 3 -- final post-binding pass, 2026-08-29

The exact claim was searched once more after the certificate, strict output,
and release binder were frozen.  Queries included:

- `"Erdős Problem 699" "100000000" "i=3"`
- `"Erdos 699" "100,000,000" binomial i=3`
- `site:arxiv.org Erdős Szekeres common prime binomial coefficients i=3`
- `site:github.com erdos_699 i3 100000000`

The current Formal Conjectures issue still describes the mathematical status
as open, although the issue itself is closed after formalization.  The public
Rust repository still documents its complete all-\(i\) sweep only through
\(10^7\), plus the sparse families \(n=2^k\) and \(n=3^m+1\) to roughly
\(1.3\times10^8\).  General search and arXiv results produced no matching
complete all-row \(i=3\) endpoint at \(10^8\).  Accordingly, the release uses
only the bounded statement “not located in the recorded searches”; it does
not claim absolute priority or resolution of problem #699.
