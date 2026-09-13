# V16 independent final submission audit

Date: 26 August 2026  
Candidate directory: `output/source_packages/common_metric_three_positivity_islands_submission_2026-08-26-v16/`  
Mode: independent, read-only, fail-closed submission audit

## Verdict

**FAIL — not submission-ready in the audited state.**

- Fatal findings: **1**
- Major findings: **0**
- Minor findings: **0**

The manuscript, its local mathematical scope, the newly packaged exact
certificate chains, the clean build, bibliography, fonts, bookmarks, and all
36 rendered pages pass the checks below. The fatal finding is a release-level
integrity failure: the top-level JSON release manifest is stale and does not
bind the v16 candidate that it accompanies. No mathematical claim is rejected
by this audit, but the directory must not be frozen, archived, or submitted
until a new manifest binds the exact final file set and a fresh independent
audit verifies it.

## Candidate identity

The primary files present at the start of the audit had these SHA-256 digests:

| file | SHA-256 |
|---|---|
| `main.tex` | `a1c132ac2f167ad5a969d3a1fcd5949d2434c61a8292837a7ed3f107ceaa018c` |
| `main.pdf` | `a3be35defe20fea1917cb3c9c91a2e86901d1c62a3ea9fcae9f1d2686f8a77be` |
| `README.md` | `bf7e2ebc349d6519500600f0c9ca9553d23cefc563a01f2930d519cbe3f05b68` |
| `references.bib` | `989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600` |
| `main.bbl` | `3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b` |
| `RELEASE_MANIFEST.sha256` | `57c9090a1251921790d40b665074a77af017b3db714d3f53add184fc45451722` |

## Fatal finding

### F-1. The top-level release manifest binds an older candidate

Running the package's advertised integrity command,

```sh
python verify_release_manifest.py
```

fails with a file-set mismatch. An independent comparison found:

- JSON manifest entries: **629**;
- actual distributed files other than the manifest: **879**;
- unbound extra files: **250**;
- missing files named by the manifest: **0**;
- manifest-named files whose current byte count or digest differs: **4**.

The four changed bound records are:

| path | manifest SHA-256 | actual SHA-256 |
|---|---|---|
| `README.md` | `16e61fa90e4278eae0b03cf02428cf59156c7643fcd7b859941af2c40d1d3870` | `bf7e2ebc349d6519500600f0c9ca9553d23cefc563a01f2930d519cbe3f05b68` |
| `main.tex` | `9fbb5fe895c1e9ff0eb7a64f50bdc6460eb6be21772eb98539b24cf2a1d14c80` | `a1c132ac2f167ad5a969d3a1fcd5949d2434c61a8292837a7ed3f107ceaa018c` |
| `main.pdf` | `7e67a93526a892dcfa4221b5dc621cbcb61b48bffaa9d40f691bf24df672a417` | `a3be35defe20fea1917cb3c9c91a2e86901d1c62a3ea9fcae9f1d2686f8a77be` |
| `make_release.py` | `2ce6caef7b1ec5e350de03889d37fa2324574c5a50b1409da102a90fd6d84147` | `b3b8b6ddf07a59483a9c630c37428ffe06095616b72701ce5189ecf6baf7b2a1` |

The 250 extras include the v16 recentered/constant-sheet source and referee
materials, their reports and attack records, `BIBLIOGRAPHY_AUDIT.md`, and
LaTeX auxiliary files. Thus the manifest neither authenticates the current
paper nor closes over the new evidence on which the paper relies. This is
fatal for a frozen submission artifact even though the nested mathematical
manifests themselves pass.

Required disposition: regenerate the JSON manifest from the intended final
file set, decide explicitly whether build auxiliaries belong in that set,
verify every path/byte count/SHA entry from a fresh extraction, and rerun an
independent final audit. This report does not modify or repair the candidate.

## Mathematical claim and scope audit

The manuscript contains exactly eight theorem environments and eight theorem
labels:

1. Theorem 3.1, the scale-cubic reduction;
2. Theorem 4.1, all-scale island;
3. Theorem 5.1, positive-`Z` moving-sheet island;
4. Theorem 6.1, affine-omega tilted continuation;
5. Theorem 7.1, inward-`Z` affine-omega sheet;
6. Theorem 8.1, recentered inward-`Z` continuation;
7. Theorem 9.1, seam-preserving constant-`Z` continuation;
8. Theorem 10.1, high-`Z` complex-phase tube.

This is exactly one scale-cubic reduction plus seven local positivity
theorems. The abstract, introduction, theorem statements, scope section,
README, and PDF agree on that count and on the local nature of the result.

Active attacks on overclaiming found no violation:

- the manuscript explicitly leaves the unrestricted complex Hermitian gate,
  the full compact ball, a common metric for all separators, arbitrary-node
  bridges, and the optimal fixed-crossing-lens constant open;
- it does not identify formula-distinct charts away from their exact seams;
- it does not infer a raw-gate negative or a maximality theorem from chart
  illegality;
- the 72-node grids are repeatedly and explicitly classified as
  falsification diagnostics, never as continuum proofs;
- no result is enlarged to arbitrary dimension, unbalanced/higher rank, or
  arbitrary normalized scale outside its stated family.

The constant-`Z` theorem is stated only on

```text
X* = 1019767/1040000 <= X <= 99/100,
Z_const = Z_rec - 2(X-X*)
        = Z_in + 2(X*-83059/100000),
0 < S <= 1/10000,
|M| <= 1/1000,
|omega|,|nu| <= 1/100.
```

The manuscript says expressly that `99/100` is merely the end of the audited
rational cell and asserts no continuation or maximality beyond it.

## Constant-`Z` certificate cross-check

The packaged source/referee artifacts have the expected independent-audit
identities:

| artifact | SHA-256 |
|---|---|
| frozen source | `a99072346ca9d92e3a5e45600d1de371b2609185bef60b2c069d2a400e1d9322` |
| source manifest | `e573ff4ab4ab1f2065ff6c40289aacd19e8629e3bbe53b177cd996c7624d7840` |
| independent referee | `4958ec0eaca83cb06b8a368b94767dd32b826094e8e99fac3b34118aa19083e3` |
| referee report | `cdf21533b5b1e921d28b4ed3d7c70ea0664356b99380469bfb7fa9609df8c12f` |
| referee results | `0c5fa7ca14cf78694250c9c41755b4092badb3a5966f707d4b702ebce5a0ff21` |
| referee manifest | `378f98ff3d854f6d013d1578c8657cfa6a27502a631f1dd052f2207fd62266b3` |

The source manifest verifies 8/8 entries and the referee manifest verifies
41/41 entries. The source record, independent referee results/report, README,
Theorem 9.1 and Appendix B.2 agree on all of the following:

- original Hermitian `Q,Q^2` reconstruction, including all 9 entries of
  `Q^2`;
- degree four in `Z` and positive reversible clearing;
- exact three-layer seam at `X=X*`: parameter tuple, cleared raw gate, and
  cleared certificate core;
- structure `32/32/1581` and bidegree `(7,4)`;
- 40/40 strict exact Bernstein controls;
- unique weakest index `(7,0)`;
- reserve

```text
336916849934297843831968152548875021542760484743285035401593929563252614799020866001627
/1047953682726912000000000000000000000000000000000000000000000000000000000000;
```

- `dZ/dX <= -1019767/520000 < 0`;
- `Z >= 143889690210214873/15857127000000000000 > 0`;
- `T <= -8425123367/286000000 < 0`, hence strict danger at the root for every
  physical `S>0`;
- full `Z`, danger, `det(C)`, both signed-`z`, positive-scale and rank-two
  legality;
- 72/72 exact nodes used only diagnostically.

The normal and byte-compilation records exit zero. All eight independent
referee attacks exit one at the intended gate: optimized Python, bad source,
bad predecessor, bad source manifest, bad normalization, dropped `Q^2`,
flipped danger sign, and dropped core coefficient.

## Recentered eight-cell chain

The eight cells in the paper and README agree exactly:

```text
[83059/100000,17/20]
[17/20,7/8]
[7/8,9/10]
[9/10,11/12]
[11/12,15/16]
[15/16,19/20]
[19/20,39/40]
[39/40,1019767/1040000].
```

There are nine new source manifests and nine new referee manifests when the
constant-`Z` cell is included, exactly the eighteen chains claimed in the
README and manuscript. Running all eighteen manifests from the packaged
`certificate_workspace/` verifies **295/295** listed files.

Each of the eight recentered reports is PASS with fatal/major/minor 0/0/0 and
agrees with the paper on `34/34/1659`, bidegree `(7,4)`, 40/40 strict
controls, unique weakest `(7,0)`, its complete reserve polynomial, the
three-layer splice, both signed lifts, full-cell legality, and diagnostic-only
nodes. The eight reserves printed in Appendix B.1 agree digit-for-digit with
the corresponding independent reports. The terminal report independently
derives `X*=1019767/1040000`, proves `danger_base=0` there and
`T<=-4181417/143000<0`, and correctly classifies the obstruction immediately
to the right as chart illegality rather than a negative raw gate or
maximality result.

## Authorship and disclosure

The TeX source and rendered PDF both show `Yonghua Xiong*` as the fifth
author, followed by `* Corresponding Author: Yonghua Xiong.` The five authors,
addresses and emails are present in the end matter; the PDF metadata contains
all five author names. No author or affiliation is silently omitted from the
rendered artifact.

The reproducibility section discloses exact symbolic computation and the AI
coding assistant's roles in layout transcription, package updates,
typesetting, and build checks. It states that no Lean or other proof assistant
formalizes the complex theorems in this paper, and it does not cite unrelated
formalizations as support. It also warns that final venue-specific AI,
acknowledgment, and funding language must be confirmed before submission.
That venue-policy confirmation remains an editorial pre-submission action,
not a hidden mathematical assumption.

## Bibliography

The manuscript cites exactly five keys and `references.bib` contains exactly
five records. The package bibliography audit records primary publisher/DOI
verification of every record and evaluates each claim context. The independent
mechanical gate after a clean build gives:

```text
cited_keys: 5
bib_keys: 5
missing_bib_files: 0
cited_keys_missing_from_bib: 0
bib_keys_not_cited: 0
aux_bibcite_keys: 5
cited_keys_missing_from_aux: 0
aux_keys_not_cited: 0
```

The generated `main.bbl` contains all five entries and BibTeX reports zero
warnings.

## Independent build and PDF audit

Two independent clean builds were run in two new temporary directories using
the README's deterministic environment:

```sh
SOURCE_DATE_EPOCH=1787673600 FORCE_SOURCE_DATE=1 latexmk -C main.tex
SOURCE_DATE_EPOCH=1787673600 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Both builds exit zero and produce

```text
a3be35defe20fea1917cb3c9c91a2e86901d1c62a3ea9fcae9f1d2686f8a77be  main.pdf
```

which is byte-identical to the packaged PDF. The final `.log`/`.blg` files
contain no undefined citation/reference, missing database, duplicate entry,
LaTeX/package warning, overfull box, or underfull box.

PDF structural checks:

- 36 pages, US Letter, PDF 1.7, not encrypted;
- deterministic creation and modification date: 26 August 2026 00:00 CST;
- title and all five authors present in metadata;
- 32 listed font resources, all embedded and subsetted, with Unicode mapping;
- 23 bookmark records, covering sections, appendices, and references;
- text extraction succeeds on the document;
- all 36 pages render successfully.

Every rendered page was inspected. No clipped text, overlap, missing glyph,
blank page, broken link color, malformed equation/table, or unreadable end
matter was observed. Long exact integers in Appendices B.1--B.2 wrap within
the text block, and the corresponding-author marker, addresses and emails are
visible on the final page.

## Final disposition

Mathematical/certificate scope: **PASS**.  
Build/bibliography/PDF presentation: **PASS**.  
Nested recentered and constant-`Z` manifest chains: **PASS**.  
Top-level release integrity: **FAIL**.

Accordingly the audited directory is **not submission-ready**. The only
fatal defect found is mechanical and repairable, but it must be repaired by
producing a newly frozen candidate and then independently re-auditing that
new byte set. This audit intentionally made no change to the candidate,
`main.pdf`, any certificate, or any manifest.
