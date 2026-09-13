# BibTeX reference audit

Audit date: 2026-08-30 (Asia/Shanghai)  
Entry point: `paper/main.tex`  
Database: `paper/references.bib`

The project-level no-delegation rule and the user's serial-role contract
precluded the skill's default one-key-per-subagent workflow.  The primary
agent therefore checked all eight keys serially under the same protocol.

## Mechanical citation surface

`check_bib_keys.py` found 8 cited keys, 8 database keys, no missing database,
no missing cited key, and no unused database entry.

| Key | Current title | Authoritative record | Match | BibTeX action | Key action | Uncertainty |
|---|---|---|---|---|---|---|
| `cole1917` | The Complete Enumeration of Triad Systems in 15 Elements | PMC/PNAS, DOI 10.1073/pnas.3.3.197 | title, authors, year, venue, volume, issue, pages, DOI | retained | none | none |
| `mathon1983` | Small Steiner Triple Systems and Their Properties | Combinatorial Press, *Ars Combinatoria* 15 (1983), 3--110 | title, authors, year, venue, volume, pages | retained; added published erratum note | none | no DOI located |
| `gibbons1976` | Computing Techniques for the Construction and Analysis of Block Designs | Library and Archives Canada thesis record | title, author, degree, institution, year | retained | none | full stable thesis text not obtained |
| `grannell1999` | Switching Cycles in Steiner Triple Systems | author-hosted primary PDF and official volume page | title, authors, year, venue, volume, pages | retained | none | no DOI located |
| `kaski2011` | The Cycle Switching Graph of the Steiner Triple Systems of Order 19 Is Connected | University of Helsinki record, DOI 10.1007/s00373-010-0982-1 | exact metadata match | retained | none | none |
| `mckay2014` | Practical Graph Isomorphism, II | ANU/arXiv and DOI 10.1016/j.jsc.2013.09.003 | exact metadata match | retained | none | none |
| `designtheory` | Database of t-designs | official Queen Mary/DesignTheory.org database | title/host/URL/access date appropriate for live database | retained | none | no DOI (web database) |
| `erskine2025` | Cycle Switching in Steiner Triple Systems of Order 19 | Wiley and arXiv:2405.07750, DOI 10.1002/jcd.21975 | exact metadata match | retained | none | none |

## Sources

- Cole et al.: https://pmc.ncbi.nlm.nih.gov/articles/PMC1091209/
- Mathon et al.: https://combinatorialpress.com/ars/vol15/
- Gibbons: https://library-archives.canada.ca/eng/services/services-libraries/theses/Pages/item.aspx?idNumber=15826048
- Grannell et al.: https://grannell.net/Papers/SWITCH2.pdf
- Kaski et al.: https://researchportal.helsinki.fi/en/publications/the-cycle-switching-graph-of-the-steiner-triple-systems-of-order-/
- McKay--Piperno: https://arxiv.org/abs/1301.1493
- DesignTheory.org: https://webspace.maths.qmul.ac.uk/l.h.soicher/designtheory.org/database/t-designs/
- Erskine--Griggs: https://onlinelibrary.wiley.com/doi/10.1002/jcd.21975

## Changes

- No citation key changed.
- `paper/main.tex` was edited only to remove an unnecessary unsupported
  minimality adjective from the Pasch-trade description.
- `paper/references.bib` gained the verified Mathon--Phelps--Rosa erratum
  locator: *Ars Combinatoria* 16 (1983), 286.

Final `.aux`, `.bbl`, `.blg`, and `.log` convergence checks are recorded in
`audit/BUILD_AUDIT.md` after the clean build.
