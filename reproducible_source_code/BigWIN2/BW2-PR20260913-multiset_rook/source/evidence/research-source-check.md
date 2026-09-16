# Source-definition audit for the fixed counterexample

Job: primary-20260913-multiset-rook-research-14de8ccf88cc.
Date: 2026-09-13 UTC. Research check, not the required referee report.

The full archived AJQ primary HTML was parsed directly with Python's
standard HTML parser, selecting the following element IDs and retaining
the mathematical `alttext`. Selected prose and formulas were read in full.
Only illustrative rook-diagram macros in Section 3.3 were omitted from
the displayed extraction; the complete archived file retains them.

| Primary element | Checked content | Effect on this witness |
| --- | --- | --- |
| `S1.p1` | Nondecreasing row lengths; left justification; first row shortest, numbered from top | lambda=(3,3,3,3,4,4) has the required orientation |
| `Thmtheorem5` | Word ascents compare strictly increasing adjacent letters | Comparisons in positions 1 through 5; no sentinel |
| `Thmtheorem8` | Root alternation and permitted degree difference 0 or 1 | Degree 3 then 4 forces minroot(R1)<=minroot(R3) |
| `Thmtheorem9` | Every earlier/later pair is required | The pair R3,R1 suffices even though it is nonadjacent |
| `Thmtheorem12` and Section 2 context | The established rook result is in the nonattacking setting | Repeated positive content is outside that distinct-letter result |
| `S3.SS3`, introductory definition | Prescribed content, one rook per row, several allowed per column, row upper bounds | All six-letter words obey the original multiset hypotheses |
| `S3.SS3`, Examples 25/26 | lambda=22233 and alpha=(2,2,1) are admissible | A staircase lower bound is not imposed in this multiset definition |
| `S3.SS3`, equations (10)--(12) | Total and first-entry ascent refinements | No shifted exponent, sentinel or normalization is substituted |
| `S3.SS3`, Lemma 27 | Prepending a row changes content by the chosen first letter | Earlier joint-content induction is unnecessary for the direct disproof |
| `S3.SS3`, Conjecture 28, equation (14) | Total real-rootedness followed by descending refinement interlacing | The frozen original is the conjunction; its interlacing conjunct fails |
| `S3.SS3`, following paragraph and Remark 29 | Rectangular results are attributed to earlier work; the displayed non-real-rooted example uses a skew shape | Those claims are distinct from the non-skew witness here |

The source's precise meaning of an interlacing **sequence** is decisive.
The proof does not replace the all-pairs condition with an adjacent-pair
condition or assume interlacing is transitive. It uses the direct condition
R3 preceq R1. Both polynomials are nonzero and have positive leading
coefficient, so conventions for zero polynomials play no part.

Independent computational calibration also reproduces Example 26 from the
primary text: exactly 12 legal words and polynomial 3t+8t^2+t^3. This is
a convention check, not the proof of the six-letter result.

The live [AJQ arXiv record](https://arxiv.org/abs/2502.05939) was inspected
on this date and lists only v1, dated 2025-02-09. The live
[v1 HTML](https://arxiv.org/html/2502.05939v1#S3.SS3) is accessible. The local
complete v1 capture is identical to the copy placed under `evidence/external/`:

- Source file: `literature/ajq-2502.05939v1.html`.
- Frozen-input copy: `evidence/external/ajq-2502.05939v1.html`.
- SHA256 of each: `af09cd6949d991dfc7467dfb19704f0a2cc6842d05e0317f3bdfb69d40854f8a`.
- Immutable `source.md` SHA256: `2a88f14a8f18991b1253ef13abad929e8b00f48326545c52911ef89a6707f18f`.

Enumerating `literature/*handoff*.md` found no handoff files. The source
locators and these summaries do not replace the complete primary capture
in the candidate evidence list. No source file was modified.
