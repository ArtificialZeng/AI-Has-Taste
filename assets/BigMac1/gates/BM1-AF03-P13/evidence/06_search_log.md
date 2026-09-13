# Search log

All searches were run on 2026-08-29 (Asia/Shanghai).  Primary records and
downloaded source archives are retained under `literature/sources/` and API
responses under `literature/metadata/`.

## Pass 1 — frozen questions

1. What is the literal Conjecture 5.1, and which arXiv version contains it?
2. What do “length” and \(n\) mean, what is the order-polytope dimension, and
   what symmetry/factorization is proved?
3. What is the current arXiv version and formal journal/DOI status?
4. Does Braun–Jal close only \(h^*\)-real-rootedness or also the Ehrhart disk?
5. Is there a later proof/counterexample of the disk statement or length-10
   finite endpoint?
6. Is source code or a certificate for the reported length-9 computation
   public?

## Pass 2 — records and queries

| Time / channel | Query or endpoint | Result used |
|---|---|---|
| arXiv | `https://arxiv.org/abs/2411.18695` | v1 2024-11-27; latest v2 2026-02-27; v2 accepted for Discrete Mathematics. |
| arXiv source | `https://export.arxiv.org/e-print/2411.18695v1` | Literal Conj. 5.1 and author report “length up to 9”; internal notation/sign inconsistency. |
| arXiv source/PDF | `https://export.arxiv.org/e-print/2411.18695v2` and `https://arxiv.org/pdf/2411.18695v2` | Current definitions and Theorem 2.9; Section 5, Conjecture 5.1, and the “length up to 9” sentence are retained. |
| Crossref | `https://api.crossref.org/works/10.1016/j.disc.2026.115072` | Journal, volume 349, issue 9, article 115072, September 2026 metadata. |
| eScholarship | title search and item `6n85w7mx` | Author manuscript and DOI link. |
| arXiv | `https://arxiv.org/abs/2607.00922` and v1 source | Braun–Jal v1, 2026-07-01; Theorem 4.1 proves \(h^*\)-real-rootedness only. |
| Semantic Scholar API | `paper/ARXIV:2411.18695/citations?...` | One located citing item: Braun–Jal arXiv:2607.00922. |
| Crossref metadata | DOI record `is-referenced-by-count` | Count 0 at query time; metadata count is not exhaustive. |
| Web | `"2411.18695" cited by`; `"Ehrhart" "generalized snake" roots disk`; `"Order polytopes of generalized snake posets" Ehrhart roots`; DOI exact query | No later disk proof/counterexample found; Braun–Jal and mirrors found. |
| Web / GitHub | `site:github.com "2411.18695"`; exact title; example polynomial; `generalized snake poset Ehrhart` | No project-specific computation repository found.  SymCat bibliographic source found but no disk result/code. |
| arXiv code links / archives | “Code, Data, Media” links and both TeX archives | No code/certificate bundled; source cites Sage computations. |

## Scope warnings

* Google Scholar itself was not scraped; arXiv links to it, while Semantic
  Scholar, OpenAlex/Crossref, arXiv, DOI/title queries, and public web search
  were checked.
* Search-engine snippets and MathDB are discovery aids only, not evidence for
  mathematical correctness.
* “No public code/result found” is database- and query-bounded.  It will be
  rerun with result-specific polynomial/word fingerprints in novelty pass 2.

## Post-result novelty pass — 2026-08-29

This pass was performed only after the exact length-9 and length-10 witnesses
were known.  The searches used mathematical fingerprints that would be hard to
match accidentally:

| Channel | Query family | Result |
|---|---|---|
| Web | `"LRLRLRLRLR" Ehrhart`, `"LRLRLRLRL" Ehrhart`, with and without `generalized snake` | No matching proof, counterexample, code, or certificate located. |
| Web | `"23924096" "70801492" Ehrhart`; `"385y^5" "25789" "923223"` | No matching mathematical result located. |
| Web | `"5741" "1132460" "121839662" Ehrhart`; `"LRLRLRLRL" "root"` | No matching mathematical result located. |
| Web | `"generalized snake poset" counterexample Ehrhart disk`; exact title plus `counterexample`, `roots`, or `Conjecture 5.1` | The original paper, bibliographic mirrors, and Braun--Jal were returned; no disk resolution located. |
| arXiv / Semantic Scholar / Crossref / OpenAlex | original title, arXiv id, DOI, author combinations, citing-work records | No additional citing work asserting a disk proof/counterexample was located. |
| GitHub/web code search | arXiv id, exact title, both witness words, and distinctive coefficient tuples | No source repository or prior certificate located. |

The negative result is bounded by these services and the lock date.  It
supports only the wording “no earlier result was located in the recorded
searches through 2026-08-29”; it does not establish absolute priority.
