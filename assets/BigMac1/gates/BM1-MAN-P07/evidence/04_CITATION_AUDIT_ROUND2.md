# Citation audit, editorial round 2

Audit date: 2026-08-22.

The revised manuscript cites eleven records.  The seven inherited records
were already checked individually in `BIB_AGENT_A.md`, `BIB_AGENT_B.md`, and
`CITATION_AUDIT.md`.  The four newly introduced records were checked against
official or primary sources in `BIB_ROUND2_AGENT_LIT.md` and
`BIB_ROUND2_AGENT_PROOF.md`.

| Key in the revised manuscript | Work | Authoritative source | Claim support | Result |
|---|---|---|---|---|
| `Lehmer1932EulerTotient` | Lehmer, *On Euler's totient function* | AMS/DOI and original paper | Original problem | verified |
| `CohenHagis1980PrimeFactors` | Cohen--Hagis (1980) | zbMATH and later primary attribution | Historical 14-factor and size bounds | verified with recorded provenance limitation |
| `Wong1997NormalFamilies` | Wong, M.Sc. thesis (1997) | LAC catalog and thesis PDF | \(\omega(n)\ge15\), normal-family and Dirichlet extension precedent | verified |
| `Renze2004ComputationalEvidence` | Renze notebook (2004) | Wolfram Library Archive | Later computation and method precedent | verified |
| `Pinch2006Note` | Pinch ANTS VII poster (2006) | Official conference poster | \(n>10^{30}\) and independent computation | verified |
| `BurcsiCzirbuszFarkas2011` | Burcsi--Czirbusz--Farkas (2011) | Journal PDF and DOI | Computational precedent and the conditional \(3\mid n\) bound | verified |
| `GrytczukWojtowicz2003` | Grytczuk--W\'ojtowicz (2003) | Project Euclid/DOI and article | Published record of the conditional \(k\ge3\), \(\omega(n)\ge1991\) bound | verified |
| `Tarnauceanu2024Generalizing` | T\u{a}rn\u{a}uceanu (2024 issue) | EMS Press and DOI | Open status | verified; online-first date recorded separately |
| `Apostol_1976` | Apostol (1976), Dirichlet chapter | Springer chapter and DOI | Dirichlet's theorem for reduced progressions | verified; official BibTeX used |
| `AlRasasiEchiGhanmi2013` | Al-Rasasi--Echi--Ghanmi (2013) | Official journal PDF | Related Korselt-set infinitude theorem | verified; no DOI or official BibTeX located |
| `McNew_2016` | McNew--Wright (2016) | DOI/Crossref and author preprint | Related non-Carmichael radimichael infinitude | verified; official DOI BibTeX used |

Round-2 key changes made to follow official exports:

- `Apostol1976Dirichlet` -> `Apostol_1976`;
- `McNewWright2016` -> `McNew_2016`.

There are no unresolved work-identity or proposition-support blockers.
MathSciNet's full topic search remained unavailable without institutional
login; this affects only an absolute priority claim, which the manuscript
does not make.

One mechanical repair was made to the raw Crossref block for McNew--Wright:
the exported `month=Sept` uses a BibTeX string that is undefined in the
standard style, so it was changed to `month={September}`.  All identity fields
remain those of the official export.
