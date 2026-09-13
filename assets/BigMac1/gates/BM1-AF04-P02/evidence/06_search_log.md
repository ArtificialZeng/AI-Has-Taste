# Search log

Search date: 2026-08-30 (Asia/Shanghai).  Gate 1 is a two-pass search: the
claims were frozen before the queries below.  A second novelty pass is
required after the exact value is known.

## Pass 1: frozen questions

1. Is the count of 80 classes supported by an original classification and a
   current complete database?
2. Is there exactly one anti-Pasch class?
3. Are the other 79 classes connected by Pasch switches?
4. Did any source state or encode the exact diameter?
5. What is the latest arXiv/journal work and is there reusable public code or
   a catalogue?

## Pass 2: sources and queries

| Time/order | Database or site | Query/action | Result used |
|---|---|---|---|
| 01 | TheoremDB | `sts15-pasch-switch-graph`, P2788/R1156 | Dated 2026-07-31 frontier: 79+1 known; diameter not located. Secondary research-memory record only. |
| 02 | Web search | `Steiner triple systems order 15 80 isomorphism classes classification Pasch switch graph` | Located Mathon–Phelps–Rosa catalogue, the 2011 cycle-switch paper, and DesignTheory.org. |
| 03 | PNAS/PMC + DOI | title `The Complete Enumeration of Triad Systems in 15 Elements` | Confirmed Cole–Cummings–White, 1917, DOI 10.1073/pnas.3.3.197, pp. 197–199. |
| 04 | Combinatorial Press | Mathon–Phelps–Rosa, `Small Steiner triple systems and their properties` | Confirmed Ars Combinatoria 15 (1983), 3–110 and catalogue role; no DOI located. |
| 05 | Library and Archives Canada / web | Gibbons, `Computing Techniques for the Construction and Analysis of Block Designs` | Confirmed 1976 Toronto thesis metadata and its role as the original 79-component computation; full stable copy was not obtained in this pass. |
| 06 | Author-hosted primary PDF | Grannell–Griggs–Murphy, `SWITCH2.pdf` | Read the full paper. §3 verifies 79+1. Appendix gives every 4-, 6-, and 8-cycle switch result. Full-text search found no occurrence of “diameter”. SHA-256 `83a59a7879b1d19a79ca86cb1a50e7a907f8ad7e24f8dd0ce4c86e35c80f0a37`. |
| 07 | Springer/author PDF | Kaski–Mäkinen–Östergård, title search | Confirmed *Graphs and Combinatorics* 27 (2011), 539–546, DOI 10.1007/s00373-010-0982-1. Introduction attributes 79-class Pasch connectivity to Fisher/Gibbons and points to broader switching questions. |
| 08 | Wiley + arXiv | `Cycle switching in Steiner triple systems of order 19` | Latest directly related article located: Erskine–Griggs, 2025, DOI 10.1002/jcd.21975, arXiv:2405.07750. Its endpoint concerns v=19 single-cycle-length component structure, not this diameter. |
| 09 | Springer book chapter | `Siamese Combinatorial Objects via Computer Algebra Experimentation` | Confirmed Klin–Reichard–Woldar, 2009, DOI 10.1007/978-3-642-01960-9_2; §6.3 is a corroborating description of the 80-class graph, not a located diameter source. |
| 10 | DesignTheory.org | database → t-designs → row `2,15,35,7,3,1` | Located complete compressed XML catalogue of 80 pairwise nonisomorphic STS(15)s. Stream SHA-256 `11310c7e35330e842938dbcc4bb6e59144bf40576323f22499a809364d50f2c9`; parsed 80 designs, each 35 blocks. |
| 11 | Web/public-code search | `GitHub Steiner triple system 15 representatives 80 STS15`, exact filename `t2-v15-b35-r7-k3-L1.icgsa.txt.bz2` | Located code examples consuming the DesignTheory.org file, but no public replayable Pasch-diameter computation. |
| 12 | Exact phrase searches | `"A Few Words About STS(15)" diameter`, `"Pasch-switch" graph diameter STS(15)`, `"switching cycles in Steiner triple systems" diameter` | No source stating the requested diameter was located. Results were the known switching papers and TheoremDB. |
| 13 | Related citation search | Fisher 1940; Gibbons 1976; `Switching Cycles...`; later cycle-switch literature | Confirmed provenance chain and newer v=19 work. No correction or later STS(15)-diameter paper was located. |

## Gate-1 lock

`NOVELTY_LOCK` is granted for exact computation under the bounded statement:
as of 2026-08-30, the searches above did not locate a published value for the
diameter of the 79-vertex simple quotient component.  The 1999 full switching
table is prior art and must be cited and reproduced.  No novelty wording may
survive release until the exact value is searched in a second pass.

## Second novelty pass after exact computation

Computed invariants searched: diameter 11, 258 simple edges, radius 6, two
diameter pairs in the released canonical numbering, and the notation
\(M(15,4)\).

| Time/order | Database or site | Exact query | Result |
|---|---|---|---|
| 14 | General scholarly web search | `"STS(15)" "diameter 11" Pasch switching` | No mathematical source stating this value was located; only the open TheoremDB record appeared. |
| 15 | General scholarly web search | `"M(15,4)" diameter Steiner triple system` | No relevant source stating a diameter was located. |
| 16 | General scholarly web search | `"258 edges" "Steiner triple systems" Pasch` | No relevant graph result was located. |
| 17 | General scholarly web search | `"Pasch-switch graph" 11 diameter` | No prior solution was located. |
| 18 | Publisher/arXiv metadata recheck | DOI 10.1002/jcd.21975 and arXiv:2405.07750; cited 1999/2011 papers | The 2025 endpoint remains STS(19) component structure by cycle length; it does not report the STS(15) diameter. |
| 19 | Full primary PDF recheck | Grannell–Griggs–Murphy `SWITCH2.pdf`; terms `diameter`, `radius`, graph metrics | The paper supplies switch rows and 79+1 connectivity but no diameter/radius statement. |
| 20 | Crossref and OpenAlex APIs | Exact title plus `Steiner triple system Pasch switching diameter` and the computed invariants | Bibliographic metadata for the known papers was recovered; no additional work stating diameter 11, radius 6, or 258 edges was returned. |
| 21 | Mandatory citation-template audit | First-author/year/title-prefix, full-title Semantic Scholar/arXiv, author/year/venue, DOI, and arXiv-ID queries for every cited work | All eight bibliography records were identified from primary, publisher, institutional, or official-database pages. No cited source was missing; details are in `audit/CITATION_AUDIT.md`. |

Second-pass conclusion: as of the search date, no published occurrence of
the exact value 11 or the 258-edge simple quotient was located.  The bounded
novelty statement is now: “We did not locate a prior publication stating the
diameter; the 1999 switch table contains enough data from which it could have
been computed.”
