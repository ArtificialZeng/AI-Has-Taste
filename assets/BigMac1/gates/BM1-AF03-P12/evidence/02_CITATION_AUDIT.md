# Citation audit

Date: 2026-08-29 (Asia/Shanghai)  
Main source: `paper/main.tex`  
Bibliography: `paper/references.bib`  
Status: **POST-FULL-DAG CITATION AND CLEAN-BUILD PASS**

Exactly two citation keys occur in the frozen manuscript.  After the
hash-bound full-DAG recheck, each key was assigned to a different independent
verifier and checked against primary official records and the cited theorem
contexts.  Neither verifier edited any file.

| Key | Official record | Claim-level result | Bibliographic action | Remaining uncertainty |
|---|---|---|---|---|
| `Sagan_2026` | Bruce E. Sagan and Chenchen Zhao, “Properties of plactic monoid centralizers,” *Semigroup Forum* 113(1) (2026), 242--262, DOI [10.1007/s00233-026-10652-4](https://doi.org/10.1007/s00233-026-10652-4) | PASS: Theorem 2.13, Proposition 2.4, Lemma 3.3, Proposition 3.6, Theorem 3.7, packed Conjecture 3.8, log-concavity Conjecture 4.6, and the reported finite range all support the manuscript's uses. | Retain the DOI-export key and entry unchanged.  The extra `@string{June = "June"}` only makes the official exporter token compile under classic BibTeX. | Springer HTML has inconsistent generated conjecture numbering; the independently checked official PDF and locally archived source control the mathematical claims. |
| `cain2017noteidentitiesplacticmonoids` | Alan J. Cain, Georg Klein, Łukasz Kubat, António Malheiro, and Jan Okniński, “A note on identities in plactic monoids and monoids of upper-triangular tropical matrices,” [arXiv:1705.04596v1](https://arxiv.org/abs/1705.04596v1) (2017) | PASS: Lemmas 5.1--5.2 support the interval-subsequence plactic homomorphism; the definitions before Proposition 5.3 support \(f_3,\pi_3,\sigma_3\); Proposition 5.3 proves that \(\Psi_3=(\phi_3,\sigma_3)\) is an embedding. | Retain the official arXiv-export key and entry unchanged.  No DOI or journal fields were invented. | The official arXiv record lists only v1 and no journal reference or DOI. |

The Cain et al. source defines `phi_n(epsilon)` as the tropical identity.
The manuscript explicitly separates the empty centralizer witness before the
finite-entry matrix argument and defines its displayed interval formula only
for nonempty words.  Thus the proof never applies a finite-entry formula to
the empty word; the full monoid convention for the cited faithful map is the
source's identity-matrix convention.  This is a recorded notational precision
point, not an unsupported mathematical or bibliographic claim, and no change
was made to the referee-frozen manuscript hash.

## Mechanical and clean-build checks

The stale auxiliary files were first removed by `latexmk -C`.  The manuscript
was then rebuilt from `main.tex` and `references.bib` with TeX Live 2026,
`latexmk` 4.88, pdfTeX 1.40.29, and BibTeX 0.99e:

```text
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py main.tex references.bib
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py main.tex --aux main.aux
latexmk -C
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Results:

- cited keys: 2;
- bibliography keys: 2;
- missing keys: 0;
- unused keys: 0;
- final `.aux` citation mismatch: 0;
- citation/BibTeX/LaTeX failure strings in final `main.log`/`main.blg`: 0;
- all warnings, including overfull/underfull boxes: 0;
- final convergence run: “Nothing to do” and “All targets are up-to-date.”

Frozen hashes at this gate:

```text
8bf92439f14394a9cd2a3a90f33e0e0686cd309dc2a602a8155ff53ef0bc0ad2  paper/main.tex
9e9cfb636c86c551529fff9f91b28943af24851ab616a74787d0c44b51f984a0  paper/references.bib
5d564735954d6ff8d72970267576af5475c40e5d5778903761d41988844ca572  paper/main.bbl
1d634d4f8dadcafbb491e2a05e8dfaf612c609999cced9b3d6ec188db9fb0f17  paper/main.pdf
```

Verdict: **PASS; no citation or bibliography blocker remains.**
