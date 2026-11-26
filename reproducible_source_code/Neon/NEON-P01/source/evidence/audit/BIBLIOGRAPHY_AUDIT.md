# Bibliography audit

Date: 2026-11-26

Every entry in `paper/references.bib` was audited against primary bibliographic records (publisher DOI/Crossref, DBLP, Zenodo, arXiv, and cached full texts of Borwein et al. 1996 and Borwein--Maitland--Skerritt 2013 in `tmp/pdfs/literature/`). Erroneous or unverified citations (including any "Vieru 2026" draft reference) were excluded.

| Key | Manuscript use | Primary / authoritative record | Verification result | Uncertainty |
|---|---|---|---|---|
| `Korselt1899` | Korselt's criterion for Carmichael numbers | *L'Intermédiaire des Mathématiciens* 6 (1899), pp. 142--143 | Author (Alwin Korselt), title (*Problème chinois*), vol. 6, pp. 142--143, 1899 verified | none |
| `Giuga1950` | Original statement of Giuga's conjecture and 1,000-digit bound | *Ist. Lombardo Sci. Lett. Rend. Cl. Sci. Mat. Nat.* (3) 14(83) (1950), pp. 511--528 (cross-checked in BMS 2013 Ref. [9] and Borwein 1996 Ref. [3]) | Author, title, series/volume 14(83), pages 511--528, 1950 verified | none |
| `Bedocchi1985` | Historical 1,700-digit lower bound | *Riv. Mat. Univ. Parma* (4) 11 (1985), pp. 229--236 (cross-checked in Borwein 1996 Ref. [2]) | Author (Edmondo Bedocchi), title, series 4 vol. 11, pages 229--236, 1985 verified | none |
| `Agoh1995` | Equivalent Bernoulli formulation (Agoh--Giuga conjecture) | *Manuscripta Mathematica* 87 (1995), no. 4, pp. 501--510; DOI `10.1007/BF02570490` (cross-checked in BMS 2013 Ref. [1] and EuDML) | Author, title, vol. 87, issue/no. 4, pages 501--510, DOI verified | none |
| `Borwein_1996` | Characterization, normal sets, mod-4 congruence, $j_{135}=3{,}459$, Open Problem #5 | Taylor & Francis DOI `10.1080/00029890.1996.12004697`; JSTOR 2975213; local full text `tmp/pdfs/literature/borwein1996.txt` | All four authors, title, *Amer. Math. Monthly* 103(1), 1996, pp. 40--50, and Open Problem #5 (p. 48) verified verbatim | none |
| `LucaPomeranceShparlinski2009` | Counting function and residue-class characterization of Giuga numbers | *Int. J. Mod. Math.* 4 (2009), no. 1, pp. 13--18 (cross-checked in BMS 2013 Ref. [14] and author archive) | Three authors, title, vol. 4 no. 1, pages 13--18, 2009 verified; journal assigns no DOI | none |
| `DBLP:journals/int/BorweinMS13` | Depth-311 bound $j_{311}=4{,}771$ ($>10^{19{,}907}$), $L_{27,692}$ exhaustibility | DBLP record `journals/int/BorweinMS13`; official PDF `tmp/pdfs/literature/borwein2013-official.pdf` (Zenodo DOI `10.5281/zenodo.10408952`) | Three authors, title, *Integers* 13 (2013), A67, Definition 11, Theorem 10, Theorem 12, and $L_{27,692}$ discussion verified verbatim | none |
| `Mavrotheris2026` | Attribution of the mod-8 congruence $m - a \equiv 1 \pmod 8$ for odd Giuga numbers (via unimodular star lattices / van der Blij) | Zenodo record DOI `10.5281/zenodo.22085830` (August 24, 2026) | Author (Nikolaos Mavrotheris), title, date (Aug 24, 2026), Zenodo DOI verified | Preprint (not peer-reviewed); attributed cleanly as prior art for the mod-8 congruence while presenting our elementary Jacobi + $(\mathbb{Z}/16\mathbb{Z})^\times$ derivation and mod-16 lift |
| `Lopez2026` | Recent 2026 status check and idempotence characterization of Agoh--Giuga counterexamples | arXiv record `arXiv:2610.09129v2` [math.NT] (October 19, 2026) | Author (Miguel Ángel López), title, arXiv ID `2610.09129v2`, Oct 2026 date verified | Preprint (not peer-reviewed); cited strictly for recent status and alternative characterization |

Build audit summary (verified via `scripts/audit_latex.py`):
- 9 cited keys, 9 BibTeX entries, 0 missing keys, 0 unused entries, 0 undefined citations or BibTeX warnings.
