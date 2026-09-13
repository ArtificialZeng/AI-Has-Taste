# Citation audit

Search date: 2026-08-30.  Main source: `paper/main.tex`; bibliography:
`paper/references.bib`.  Six distinct citation keys occur in nine citation
commands.  The audit was performed serially by the main Codex session because
the user expressly prohibited subagents.

| Key | Manuscript claim | Official/primary record checked | Metadata/result | Action | Uncertainty |
|---|---|---|---|---|---|
| `Yuster2004` | conjectured exact formula; verified range (n\le8); cyclic three-part upper bound | Elsevier/ScienceDirect DOI 10.1016/j.disc.2004.07.005; arXiv:math/0304180 full text; University of Haifa CRIS | Raphael Yuster; exact title; *Discrete Mathematics* 287(1--3), 187--191 (2004); Section 4 explicitly contains all three cited claims | retained key; corrected DOI, issue, pages and arXiv id | none |
| `KabiyaYuster2008` | notation and (41/300) asymptotic bound | University of Haifa CRIS official record and author-hosted full preprint; DOI 10.1007/s00026-008-0352-3 | Mohamad Kabiya and Raphael Yuster; *Annals of Combinatorics* 12(3), 291--306 (2008); abstract and Theorem 1.2 support the claim | retained key; metadata synchronized | none |
| `Kirtchakov2026` | public certified determination of (\nu_3(9),\nu_3(10)) | raw GitHub note, artifact directories, dated sweep record, Half Ounce library; repository provenance identifies Zenodo DOI 10.5281/zenodo.21816010 | Daniel Kirtchakov; draft dated 2026-08-05; theorem and artifact claims match manuscript wording | retained key; entered as `@misc` with GitHub URL and DOI | Zenodo landing page redirect could not be opened in the web sandbox; DOI and title are corroborated by the public repository and author library |
| `McKayPiperno2014` | nauty framework and canonical-labeling methods | Elsevier DOI 10.1016/j.jsc.2013.09.003; arXiv:1301.1493; McKay official publication page | Brendan D. McKay and Adolfo Piperno; *Journal of Symbolic Computation* 60, 94--112 (2014) | retained key; metadata synchronized | paper supports nauty framework, while the exact `gentourng` 2.9.3 executable/version is separately hashed in the certificate |
| `OEISA000568` | unlabeled tournament class count sequence | live official OEIS A000568 | sequence line contains 191536, 9733056, 903753248; entry gives Davis formula and references | retained key; access date recorded | none |
| `Davis1954` | Burnside/Davis formula for tournament counts | Springer DOI 10.1007/BF02478368 corroborated by the *Bulletin of Mathematical Biophysics* bibliography and later indexed literature | Robert L. Davis; “Structures of dominance relations”; vol. 16(2), 131--140 (1954) | retained key; DOI and issue added | no publisher-exported BibTeX could be fetched through the sandbox, but metadata agree across the DOI-linked bibliography, OEIS, and later indexed citation |

## Mechanical citation surface

Command:

```text
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py paper/main.tex
```

Result before PDF build: `cited=6 bib=6 missing=0 unused=0`.  No custom cite
macros or indirect bibliography resources are present.  No citation keys were
renamed.

Official BibTeX content negotiation at the Crossref API was blocked by the web
sandbox's URL-safety layer.  Consequently the bibliography uses minimal
source-verified fields rather than claiming byte-for-byte publisher exports.
This is disclosed rather than silently inventing unavailable fields.

## Final build gate

After the complete independent order-11 Certifier and sweep comparison
passed, the manuscript was cleaned and rebuilt through BibTeX to a stable
seven-page PDF.  Final results:

- `audit_latex.py`: `cited=6 bib=6 missing=0 unused=0`;
- independent key checker with `paper/main.aux`: six cited keys and six
  `bibcite` keys, no mismatch;
- strict `main.log`/`main.blg` scan: no undefined citation/reference,
  missing database entry, BibTeX warning, repeated entry, overfull/underfull
  box, PDF-string warning, or LaTeX fatal condition;
- citation-check two-pass report: all 30 frozen manuscript claims verified,
  with zero numerical errors, unverified items, hallucinations, or misleading
  claims (`audit/CITATION_VERIFICATION.md`).

Final citation status: **PASS**.
