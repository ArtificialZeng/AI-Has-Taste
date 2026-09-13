# Search log

## Pass 1: frozen claims (2026-08-30, Asia/Shanghai)

Before searching, the following potentially project-changing claims were
frozen: (i) exact original formula and attribution; (ii) (n\le8) historical
range; (iii) bibliographic status and best asymptotic theorem; (iv) exact
scope and certification status of the August 2026 (n=9,10) note; (v)
whether (n=11) has since been determined; (vi) public code and canonical
class counts.

## Pass 2: primary and database searches

Search date: 2026-08-30.  All “not found” statements below are limited to the
listed sources and query spellings.

| Time/order | Source or database | Query/action | Result |
|---|---|---|---|
| 1 | Yuster author preprint | opened `https://arxiv.org/abs/math/0304180` and author PDF record | original 2004 paper located; conjecture, old finite range, and construction confirmed |
| 2 | Elsevier/ScienceDirect + DBLP volume record | exact title “The number of edge-disjoint transitive triples in a tournament” | formal metadata and DOI 10.1016/j.disc.2004.07.005 confirmed |
| 3 | Springer/Haifa CRIS + EBSCO search result | exact title “Packing transitive triples in a tournament” | formal metadata, abstract, pages, and DOI 10.1007/s00026-008-0352-3 confirmed |
| 4 | author-hosted KY08 PDF | read title, definitions, abstract, conjecture and finite/asymptotic discussion | (41/300) asymptotic bound and Conjecture 1.1 confirmed |
| 5 | Open Problem Garden live entry | title and formula search | entry still records only Yuster 2004 and Kabiya--Yuster 2008; no later resolution displayed |
| 6 | GitHub `05oz/certify` | opened repository, `tt3-paper/note.md`, `tt3-scripts/`, `tt3-certificates/`, dated sweep record | public draft and artifact layout for (n=9,10) confirmed; note explicitly says (n=11) not started on 2026-08-05 |
| 7 | Zenodo | followed repository's Part C DOI 10.5281/zenodo.21816010 | DOI exists in repository metadata; web sandbox redirect prevented inspecting deposit page |
| 8 | general web search | `Yuster arc-disjoint transitive triples tournament packing conjecture nu_3(n)`; `Kabiya Yuster packing transitive triples tournaments`; exact strings `nu_3(10)`, `nu_3(11)` | found original papers and 2026 note; no (n=11) result |
| 9 | general web search, Unicode variants | `"ν₃(11)" tournament`; `"nu_3(11)" "transitive" tournament`; `"arc-disjoint transitive triples" tournament 11`; `"Yuster's conjecture" "transitive triples"` | no determination of (\nu_3(11)) located |
| 10 | arXiv-focused search | exact paper title; title and keyword variants over transitive triples/tournament packing | original arXiv:math/0304180 located; no later paper determining order 11 located |
| 11 | scholarly-index probes | exact title against zbMATH, MathSciNet, OpenAlex, Semantic Scholar, plus DBLP/EBSCO records | exact-title web probes returned no usable record for the first four; DBLP/EBSCO and publisher/CRIS metadata did resolve |
| 12 | author publication page and citing literature | Raphael Yuster publication list; later tournament-packing title searches | later work on regular-tournament directed triangles found, but no later determination of this integral (TT_3) minimum |

## Gate 1 verdict: `NOVELTY_LOCK`

Locked at 2026-08-30: the source statement's boundary is consistent with all
located primary and public records.  The (n=9,10) result is a very recent
public computational draft with artifacts, not a located peer-reviewed
article.  No public (n=11) determination was found.  A second, post-result
priority sweep remains mandatory before any novelty claim is released.

Network note: direct `git clone` was attempted but the shell's GitHub route
was unavailable; the controlled web fetch could read the repository tree and
raw source files.  Local work therefore uses independently written programs.

## Pass 3: post-Builder priority sweep (2026-08-30)

After the complete Builder computation returned the candidate exact result,
the novelty search was repeated with result-specific strings:

- `"ν₃(11) = 15" tournament`;
- `"nu_3(11) = 15" tournament`;
- `"903,753,248" "transitive triples"`;
- `"n = 11" "arc-disjoint transitive triples" tournament`.

The only relevant hit was again Kirtchakov's August 5 note, whose Section 5
explicitly says the (n=11) computation had not been started and claims no
order-11 result.  No competing determination was located.  This is a bounded
search statement as of the stated date, not a universal priority guarantee.
The search will be cited in the release audit only after the independent full
Certifier also passes.

## Pass 4: citation-check search templates (2026-08-30)

After freezing `audit/CITATION_CLAIM_EXTRACTION.md`, the citation-check gate
ran the applicable title/author/year, full-title, venue, DOI, and arXiv query
templates for every academic reference.  Searches were kept separate from
claim extraction.  The exact query families were:

- `Yuster 2004 The number of edge-disjoint transitive triples tournament`;
  full title restricted to arXiv; author/year/venue; DOI
  `10.1016/j.disc.2004.07.005`; arXiv `math/0304180`;
- `Kabiya Yuster 2008 Packing transitive triples tournament`; full title
  restricted to arXiv; author/year/venue; DOI
  `10.1007/s00026-008-0352-3` (no arXiv identifier was found or claimed);
- `McKay Piperno 2014 Practical graph isomorphism II`; full title restricted
  to arXiv; author/year/venue; DOI `10.1016/j.jsc.2013.09.003`; arXiv
  `1301.1493`;
- `Davis 1954 Structures of dominance relations`; full title restricted to
  Springer; author/year/venue; DOI `10.1007/BF02478368` (arXiv is inapplicable
  to this 1954 article);
- Kirtchakov/title/year, full-title/arXiv, author/year/Zenodo, DOI
  `10.5281/zenodo.21816010`, and the public GitHub repository;
- exact count strings `903753248` and `903,753,248`, OEIS A000568, and
  `unlabeled tournaments order 11 Davis formula original source`.

Primary or institutional records resolved every cited work.  The result
claims and exact counts in the manuscript are separately checked against
local serialized computation outputs during citation-check Pass 2; the web
search is not used to validate the new theorem.

## Pass 5: post-certification priority sweep (2026-08-30)

Immediately after both complete exact sweeps and their 192-slice comparison
passed, a final search used the exact-result strings
`"ν₃(11) = 15" tournament`, `"nu_3(11)=15" tournament transitive triples`,
`"903753248" "arc-disjoint transitive triples"`, and the manuscript title
stem.  No relevant mathematical result was returned.  Together with Pass 3
and the August 5 note's explicit statement that order 11 had not been
started, this supports the bounded claim that no earlier public determination
was located as of 2026-08-30.  It is not asserted as an absolute priority
theorem.
