# Citation and bibliography audit

## Verdict

Accept. The extraction pass froze 18 material claims in
`audit/citation-claim-ledger.json`; the verification pass then checked only that
ledger and recorded all exact source locations and results separately. All 18
claims pass. The seven citation-bearing claim instances resolve to four real
sources, and every retained citation supports its nearby statement.

After that check, a metadata-only `hyperref` option was added to populate the
PDF title and author; it changed no claim text, line number, citation, or
bibliography entry. The claim ledger was rebound to the final manuscript
snapshot, and build, metadata, and page checks were repeated on the final PDF.

The audit was performed serially because the job explicitly prohibited agents
and other workers. Search verification used the mandatory author/title/venue/
identifier query patterns, official arXiv records, the published Journal of
Integer Sequences record, the primary Preprints.org record, and exact passages
in the two frozen arXiv PDFs. No `literature/bibliography-revision-*.md` or
`literature/crossref-*.json`/`.md` files existed when enumerated before review.

## Per-reference findings

| Key | Bibliographic identity | Nearby support | Result |
|---|---|---|---|
| `KutinSmithline2026` | Kutin--Smithline, arXiv:2408.00903v3 | game origin, multicolor rules, CircularShift, Lemma 4.4, Conjecture 4.5, and the disclosed Definition 4.3 discrepancy | Verified |
| `Hiveley2025` | Hiveley, arXiv:2506.23452v2; published as JIS 29 (2026), Article 26.1.7 | experimental study of monochrome Permutation Wordle strategies | Verified |
| `KutinSmithlineVatter2026` | Kutin--Smithline--Vatter, arXiv:2609.01874v1 | monochrome strong optimality including non-permutation guesses; multicolor conjecture and work in preparation | Verified |
| `ZengEtAl2026FiniteCertificates` | Zeng--Liu--Ratnavelu--Huat, Preprints.org v1, DOI 10.20944/preprints202608.1658.v1 | independent finite-domain reconstruction and discovery/certification separation | Verified |

No BibTeX replacement or key change was required: the author, title, year or
consulted version, venue/type, DOI, and URL fields agree with authoritative
records. The Hiveley entry deliberately identifies the cited arXiv version;
the audit also verified its later journal reference. The Zeng et al. item is an
ordinary direct body citation and is bound to citation attempt 1 and launch ID
`36be15ba-4093-4016-83f8-cbfa36d5ffe0` in
`audit/user-bibliography-selection.json`.

## Coverage and scope

The bibliography is not user-library-only: Kutin--Smithline supplies the
problem origin and multicolor rule, Kutin--Smithline--Vatter supplies the
closest strong monochrome theorem and current conjectural comparison, Hiveley
supplies the cited experimental work, and the selected library paper supplies
only the narrow certificate-method comparison. None is decorative. The paper
makes no general multicolor theorem or unqualified priority claim, and it
preserves the accepted warning about the inconsistent displayed update cases.

Mechanical TeX/BibTeX consistency and final build/log results are recorded in
the build audit. There are four used bibliography keys, no missing database
entry, no unused entry, no duplicate key, and no unresolved citation.
