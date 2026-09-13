# Final status: `PROVED`

Modulo signed coordinate permutations, the locally extremal central sections
of \(Q_5\) are exactly
\[
d_1=(1,0,0,0,0),\qquad
d_2=(1,1,0,0,0)/\sqrt2,\qquad
d_5=(1,1,1,1,1)/\sqrt5.
\]
The unique non-diagonal full-support critical orbit is represented by
\((\alpha,\alpha,1,1,1)\), where
\(\alpha=(24+\sqrt{69})/13\), and is a saddle.  The support-four
non-diagonal orbit \((1,1,2,2,0)/\sqrt{10}\) is also a saddle.  Thus every
locally extremal central section of \(Q_5\) is diagonal.

The exact audit covers the six full-support chamber closures, all pair and
singleton walls, and supports one through four.  The primary master run is
23/23 PASS.  The independent no-project-import verifier reconstructs 17
hash-bound inputs and is PASS; its 10/10 semantic mutations and 4/4 parser
attacks are rejected.  The final hostile referee verdict is PASS with fatal 0,
major 0, local 0, and expository 0.  Complete hashes are recorded in
`audit/R_M1_REPAIR_HASHES.md` and the machine verdict is
`audit/independent_referee/hostile_referee_verdict.json`.

Reproduction commands:

```text
/opt/anaconda3/bin/python3 src/verify_all.py
/opt/anaconda3/bin/python3 audit/independent_referee/independent_verifier.py
/opt/anaconda3/bin/python3 audit/independent_referee/mutation_tests.py
/opt/anaconda3/bin/python3 audit/independent_referee/test_parser_failclosed.py
```

No Lean, Coq, Isabelle, or other interactive proof assistant was used.  The
decisive computation uses exact integer/rational/algebraic arithmetic,
Bernstein certificates, Sturm chains, and Singular ideal computations.  No
formalization endpoint is claimed.

## Submission release

The release-delta verdict is PASS and submission-gate PASS, with
fatal/major/local/expository 0/0/0/0.  All publication gates are complete:
second database-bounded novelty search, 5/5 citation-key and 11/11 claim
audit, two clean byte-identical builds, zero final undefined
citation/reference/error findings, 101/101 archive-manifest verification,
clean extraction/rebuild, and pagewise visual inspection of all 8 PDF pages.

- PDF: release/Q5_central_sections_Zijian_Zeng.pdf
  - SHA-256: 183ff0236e53de460de80a9c97ace776aba06eb681bd79315ab344827a55d7eb
- Source ZIP: release/Q5_central_sections_Zijian_Zeng_source.zip
  - SHA-256: dbbbbe24fe08d770c06f95b9b6cc3275e6eba459ce030026b043a921fb57284f
- Archive rebuild log: release/archive_rebuild.log
  - SHA-256: 88f91648c89e9862423064efc99ad06d53f2fad87e1ebeda001b0bc13c552863

The release is **submission-ready**.
