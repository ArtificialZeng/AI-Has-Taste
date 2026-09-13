# v17 repaired-candidate independent submission re-audit

Date: 2026-08-26  
Candidate: tmp/pdfs/v17_candidate/  
Mode: independent and read-only  
Verdict: **PASS — submission-ready candidate**  
Classification: **fatal 0 / major 0 / minor 0**

The repaired candidate passes every bounded gate requested for this fresh
audit. The two defects in the earlier frozen failed candidate are genuinely
absent: equation (78) contains a real LaTeX spacing command and prints no
literal qquad0, and the second constant-Z cell is now proved inside the
constant-Z theorem after Z_const is defined. The repair did not alter the
local theorem quantifiers or their frozen exact certificates.

This verdict applies only to the candidate bytes listed below. It does not
promote the local results to the unrestricted common-metric theorem, a
full-compact-ball theorem, an arbitrary-node bridge, or the optimal constant
of a fixed crossing lens.

## Frozen candidate and release manifest

| artifact | SHA-256 |
|---|---|
| main.tex | cfd1be699b3fba93b16288d846552ce883f2b75883a930ea527c1de87b67e6ff |
| main.pdf | 41f816165950f9d5369f0cc4583b33f396fb7bb3d3b937d8a62f8b1177611939 |
| main.bbl | 3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b |
| references.bib | 989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600 |
| README.md | c0fc9523b19569feb40c9d72cb8b6937a2ad84968c39f536338b436f084d2aea |
| RELEASE_MANIFEST.sha256 | 0d08df65797fb1c5ddfb4fc9cd9b9f77d46420a90aca00962057f71fb817530b |

Independent JSON parsing found exactly 1174 manifest records and exactly
1174 other files. Missing, extra, changed-hash, and wrong-size counts are all
zero. The package-local verifier independently returned PASS 1174/1174.

The top gate fails closed in fresh temporary copies. A changed byte in
README.md produced exit 1 at the record-mismatch gate; an unlisted file
produced exit 1 at the file-set gate and named the extra file.

## Exact certificate chains and manuscript transcription

The six primary post-v16 chains were independently parsed and replayed from
certificate_workspace:

| chain | records | manifest SHA-256 |
|---|---:|---|
| constant-Z source | 8 | e7220043d9ac01c91e72ebf4029a8c248bff77bb2225b2884b5c372c60df108d |
| constant-Z referee | 35 | 50c451f84eabfdb7832e3610c37bd347dc1419c109f64b7c7cece41e8e60eb06 |
| cap-shear source | 8 | 8d68e2cbeb9e56e86b818dfcdfb1e4ebc1ac5cc5a678ab4c3857a55cde0d2cc5 |
| cap-shear referee | 40 | 3cdbb03409be176c7d557056e3fcbd426e14563f35d81edc18b03dbd43064a9c |
| local-box source | 21 | 9655e59e124f8a8dd2aaf661a052f70c9d489c058e638c2d8212c7c6b794422d |
| local-box referee | 64 | dcd4d091a8b2b9fc714c1e79571a3f251b747777ff91721fe1f5a1f7ab9a67cd |

The final independent referee reports remain frozen at:

- constant-Z: ed2cb48240fa5a17eef9e9e76c4e547942642de1cc3997f2c23ae95818b61c45;
- cap shear: b8db0fa9bf450312c8921ca9ace147c09b451060647a9b90cb1267992144e71d;
- local box: d5560cb01f08bae6634f2b48710dacfda1e03bdd5f8752c651dc3c728586cb0a.

The three new v17 results agree with these frozen artifacts:

1. On the second constant-Z cell 99/100 <= X <= 497/500, the manuscript
   retains 32/32/1581, bidegree (7,4), 40/40 strict controls, unique weakest
   index (7,0), and exact reserve
   237983128275106868164816372024450404725835762778737426332055936856452553581744586321
   divided by
   719207337600221184000000000000000000000000000000000000000000000000000000.
   The Z, danger, determinant, both-sign and rank-two bounds, as well as the
   parameter/cleared-gate/cleared-core seams, are stated at the correct
   scope. The 72 nodes are diagnostics only.

2. The cap shear is restricted to 497/500 <= X <= 1. It retains
   48/48/2263, bidegree (7,8), 72/72 strict controls, unique weakest (7,8),
   the exact reserve
   79085602723906157917988882974367991904890648543683584180560419945180485170965315227
   divided by
   239735779200073728000000000000000000000000000000000000000000000000000000,
   three-level seam, full-cell legality, both signed lifts, and rank two.

3. The geometrically independent all-scale box is exactly Z=1/8,
   |x-5/8|<=1/1000, |y|<=1/100, both signed lifts, 0<h<=1, and lambda>0.
   Its control groups remain 1+9+50+147+324=531, all strict. The unique
   global minimum is the lambda-cubed control at (0,0,6),
   8332318460470459/15187500000000000. The exact danger reserve
   30189/62500 and det C/S=5/72 agree with the referee.

No sampled node is promoted to a theorem. CE-046/048/059/060 are not reused.
The manuscript repeatedly separates chart illegality from a negative raw
gate and from maximality. It expressly leaves open the full compact ball,
the unrestricted complex common-metric gate, arbitrary nodes and dimension,
and the optimal fixed-lens constant.

## Repair, proof order, and text structure

An exact source scan found zero bare qquad tokens. Extracted PDF text has zero
qquad0 tokens and zero unresolved placeholders. The recentered proof ends
before the definition of Z_const. The 99/100 <= X <= 497/500 legality
paragraph occurs after that definition, inside the constant-Z proof, after
its first-cell legality calculation and before its gate-sign argument. It is
absent from the recentered proof. Proof environments are balanced, labels are
unique, and every explicit reference has a defined label.

Three in-memory attacks on the independent audit script all exit 1 at the
intended structural gate: reintroducing the bare token, moving the second-cell
block before its definition, and rewriting diagnostic nodes as a proof.
These attacks do not alter candidate bytes.

## Independent builds and final logs

Two fresh temporary copies were cleaned and built serially with latexmk -C
followed by a fixed-epoch latexmk PDF build. All four command exits are zero.
Both PDFs have SHA-256
41f816165950f9d5369f0cc4583b33f396fb7bb3d3b937d8a62f8b1177611939;
they are byte-identical to each other and to the candidate PDF.

The two converged main.log files are byte-identical at
2dbe27d9406c3923132ede0c0d2a7a1498254ec0001ee183bc832b8987ef5484;
the two main.blg files are byte-identical at
a8cb88f58755e28516b9086ad725b35841ba236889f79771c2409b9fd48f0347.
They contain no undefined citation/reference, LaTeX/package warning,
multiply-defined label, overfull/underfull box, or BibTeX warning/error.
The archived full latexmk console transcripts retain normal first-pass
warnings before BibTeX and later passes; they are multi-pass transcripts, not
final TeX logs. The repair report does not mischaracterize them as
warning-free final logs.

## PDF, authors, and visual inspection

The PDF has 41 letter pages, is unencrypted PDF 1.7, and has every font
embedded. Its title, subject, fixed timestamp, and five-author metadata match
the source. The TeX author block exactly marks Yonghua Xiong with a star and
contains the corresponding-author footnote; PDF text contains the author
name and Corresponding Author: Yonghua Xiong. Affiliations and email are
present. The AI-assistance disclosure limits its role to transcription,
typesetting, build assistance, and exact symbolic computation, and the
manuscript says that no Lean proof formalizes these complex positivity
theorems.

Poppler rendered 41/41 pages at 150 dpi. All pages were inspected in contact
sheets; pages 1, 20, 24--30, 32--33, and 40--41 were additionally inspected
at original detail. There is no clipping, overlap, black square, broken
table, unreadable glyph, header/footer defect, or page-numbering defect.
Page 20 now prints correct spacing, and pages 24--25 present the constant-Z
proof in coherent order.

## Bibliography

The mechanical closure is exact: five cited keys, five BibTeX keys, five AUX
keys and five BBL keys, with no missing or unused record. No citation was
added by the repair. The context and publication data agree with the
official records:

- Beckermann--Crouzeix, A lenticular version of a von Neumann inequality,
  Archiv der Mathematik 86 (2006), 352--355,
  https://doi.org/10.1007/s00013-005-1533-5;
- Crouzeix--Delyon, Some estimates for analytic functions of strip or
  sectorial operators, Archiv der Mathematik 81 (2003), 559--566,
  https://doi.org/10.1007/s00013-003-0569-7;
- Badea--Beckermann--Crouzeix, Intersections of several disks of the Riemann
  sphere as K-spectral sets, CPAA 8 (2009), 37--54,
  https://www.aimsciences.org/article/doi/10.3934/cpaa.2009.8.37;
- Crouzeix, Bounds for Analytical Functions of Matrices, IEOT 48 (2004),
  461--477, https://doi.org/10.1007/s00020-002-1188-6;
- Crouzeix, Some Constants Related to Numerical Ranges, SIAM J. Matrix Anal.
  Appl. 37 (2016), 420--442,
  https://epubs.siam.org/doi/10.1137/15M1020411.

No BibTeX field or citation key needs changing.

## Conclusion

The fresh repaired-candidate audit found no fatal, major, or minor defect.
The exact local certificates, claim discipline, proof order, bibliography,
deterministic builds, PDF rendering, author metadata, release manifest, and
fail-closed behavior all pass. The candidate is submission-ready at the
stated local scope. This audit does not create a formal output PDF or ZIP and
does not alter the candidate.
