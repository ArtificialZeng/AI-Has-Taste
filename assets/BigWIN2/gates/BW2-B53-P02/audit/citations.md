# Citation and bibliography release audit

## Scope and method

Search-mode review was performed in two non-interactive stages.  The final
extraction is frozen in `audit/citation-claim-ledger-final.json` and contains
16 claims.  Verification then proceeded in claim order against the accepted
exact evidence for the new theorem and against the original publication text
for every citation.  The search date was 2026-09-06 UTC.  No subagents were
used because the runner explicitly prohibited delegation.  No
`literature/bibliography-revision-*.md` or `literature/crossref-*` captures
exist in this project.  Live shell requests failed at the WSL boundary, but
the primary publisher/arXiv records were available through the web retrieval
channel; no unavailable source was treated as verified.

## Claim verification

All 16 frozen claims passed.  Claims C01, C05--C07, C09--C10, C12--C13,
C15, and C16 agree exactly with `audit/math.md`,
`evidence/computational-proof.md`, `evidence/census-primary-summary.json`,
`evidence/census-audit.json`, and the qualifying record at
`evidence/census-primary.jsonl:2062`.  The counts are exact integers, not
rounded statistics.  Claims C02--C04, C08, C11, and C14 have the following
claim-to-source map.

| Key | Nearby claim and exact source location | Result |
|---|---|---|
| `So2006` | Divisor/gcd-class characterization; Wasin So, *Integral circulant graphs*, Theorem 7.1, publisher full text at https://doi.org/10.1016/j.disc.2005.11.006 | Verified, exact theorem statement. Metadata (author, title, journal 306(1), 153--158, 2006, DOI) matches the bibliography. |
| `KlotzSander2017` | Origin of the question; Klotz--Sander, *Uniquely colorable Cayley graphs*, p. 161, Problem 3.6, primary journal PDF at https://dlib.si/stream/URN%3ANBN%3ASI%3ADOC-UHT1IWT3/f7863ef4-930c-420a-ae51-b3b3412e52f7/PDF | Verified, exact. Metadata and DOI 10.26493/1855-3974.879.d47 match. |
| `Basic2026` | Infinite family and order-60 upper bound; Bašić, *On uniquely colorable Cayley graphs*, arXiv:2609.03184v1, p. 6, Theorem 3.1; locally preserved primary PDF `evidence/external/2609.03184.pdf` | Verified, exact. The theorem states the family for primes p at least 5, unique 3-colorability, and clique number 2. |
| `ZengEtAl2026` | Analogous exact finite certificate design; Preprints.org v1, abstract and Sections 3, 4, and 6 at https://www.preprints.org/manuscript/202608.1658 | Verified, paraphrase. The source explicitly reports exhaustive graph certificates and separately implemented exact verification. Registry row 9 and final DOI metadata match the primary record. |
| `Brelaz1979` | Historical source for saturation-degree ordering; Brélaz, *New methods to color the vertices of a graph*, pp. 251--256, ACM DOI https://doi.org/10.1145/359094.359101 | Verified, paraphrase limited to the method origin. The manuscript separately proves its own first-use symmetry handling. |
| `DavisLogemannLoveland1962` | Historical source for unit propagation and binary splitting in DPLL; Davis--Logemann--Loveland, *A machine program for theorem-proving*, pp. 394--397, ACM DOI https://doi.org/10.1145/368273.368557 | Verified, paraphrase limited to the method origin. The manuscript separately specifies and justifies its CNF and blocking rule. |

The closest prior mathematical result is `Basic2026`; the manuscript claims
only the exact minimum and classification not asserted there.  `So2006` and
`KlotzSander2017` supply the natural definition/origin sources, while the two
algorithm papers supply the named nontrivial methods.  The user-library paper
is retained for a direct methodological comparison that its text supports.
No retained citation is decorative, and an Excel-only bibliography is not
used.

## Mechanical bibliography audit

The canonical bibliography is `manuscript/references.bib`; all six entries
are cited in ordinary body flow.  The read-only key checker reports six cited
keys, six BibTeX keys, no missing files, no missing or unused keys, and exact
agreement with `main.aux`.  The final log scan finds no undefined citation,
missing database entry, repeated entry, BibTeX warning, LaTeX error, or fatal
diagnostic.  No key was renamed.  The final bibliography adds the primary
Brélaz and Davis--Logemann--Loveland method records.

## User-library coverage

Registry row 9 is the single genuinely close item among the active 49-record
first sheet and is cited directly as `\cite{ZengEtAl2026}`.  A second
user-library citation was not added: other graph papers in the registry concern
different mathematical results and would not support an additional claim in
this concise manuscript.  The exact runner binding and claim-level evidence
are recorded in `audit/user-bibliography-selection.json`.

**Verdict: accept.**
