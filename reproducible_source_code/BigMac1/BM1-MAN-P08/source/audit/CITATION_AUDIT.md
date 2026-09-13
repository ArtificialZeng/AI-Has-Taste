# Citation audit

Audit date: 2026-08-22.  Five cited records were checked against publisher,
DOI/Crossref, arXiv, or official journal sources.  The final source has five
citation keys, five bibliography entries, no missing entry, and no unused
entry.

| Key | Work | Authoritative record | Action / uncertainty |
|---|---|---|---|
| `Poonen_1992` | Poonen, *Union-closed families* | ScienceDirect and DOI 10.1016/0097-3165(92)90068-6 | DOI metadata used. Publisher issue 2 overrides an issue-1 typo in the author's CV. Supports both the 1979 attribution and the exact weighting characterization. |
| `Pulaj_2024` | Pulaj--Wood, *Local Configurations in Union-Closed Families* | DOI 10.1080/10586458.2024.2410964; arXiv:2301.01331v2 | Crossref online-first year 2024 retained. The assigned print issue is 34(4), 2025. Attribution in the text is restricted to the seeds actually proved by these authors. |
| `Alweiss_2024` | Alweiss--Huang--Sellke, improved lower bound | EJC article P3.35; DOI 10.37236/12232 | DOI metadata used; publisher-confirmed article number P3.35 added to eliminate a missing-pages warning. Text says exact closed-form guarantee, not optimal universal constant. |
| `Yu_2023` | Yu, *Dimension-Free Bounds for the Union-Closed Sets Conjecture* | Entropy 25(5), 767; DOI 10.3390/e25050767 | DOI metadata used. Text explicitly calls 0.38234 author-reported numerical output, not an independent interval certificate. |
| `VuckovicZivkovic2017TwelveElement` | Vučković--Živković, 12-element case | IPSI official article/PDF and Živković publication list | No official BibTeX export or DOI exists. Entry is source-derived from the official metadata; the page range 65--71 is confirmed by the author list and issue sequence. |

No citation key was renamed from a pre-existing populated bibliography; the
initial file contained only a placeholder.  The final checks were:

```sh
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py \
  paper/main.tex --aux paper/main.aux
rg -n "Citation .* undefined|There were undefined|I didn't find a database entry|Warning--|Repeated entry|LaTeX Error|Fatal error" \
  paper/main.log paper/main.blg
```

Both checks passed with no finding.  The only metadata caveat is the documented
2024 online-first versus 2025 print-year choice for Pulaj--Wood; it does not
affect the cited mathematical claims.
