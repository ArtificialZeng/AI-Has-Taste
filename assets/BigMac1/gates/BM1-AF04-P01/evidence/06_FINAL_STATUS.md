# Final status: PROVED

## Conclusion

Let

\[
F(t)=\frac{1+\sqrt{1-2t}}{\sqrt{1-2t}}
e^{-1-t+\sqrt{1-2t}}-(2-t)e^{-t}
=\sum_{n\ge0}a_n\frac{t^n}{n!},
\]

with the formal square root having constant term (1).  Then for every
integer (n\ge4),

\[
\begin{aligned}
0={}&(2-n)a_n+(2n^2-8n+7)a_{n-1}
+(6n^2-18n+11)a_{n-2}\\
&+(n-1)(6n-11)a_{n-3}
+2(n-1)(n-2)a_{n-4}.
\end{aligned}
\]

The necessary initial block is
((a_0,a_1,a_2,a_3)=(0,0,1,1)).  In OEIS offset (1), the equivalent
presentation starts the recurrence at (n=5) with
((a_1,a_2,a_3,a_4)=(0,1,1,21)).  The (n=4) identity is valid after the
canonical EGF extension (a_0=F(0)=0).

## Differential equations

The proof first obtains the third-order annihilator

\[
\begin{aligned}
0={}&(4t^3-3t+1)F'''
+(12t^3+2t^2-2t-1)F''\\
&+(12t^3+6t^2+6t-15)F'
+(4t^3+4t^2+3t-18)F.
\end{aligned}
\]

An exact rational differential-operator left multiple gives

\[
\begin{aligned}
0={}&t(2t-1)F^{(5)}+(6t^2+10t-2)F^{(4)}
+(6t^2+36t+7)F^{(3)}\\
&+(2t^2+37t+35)F''+(12t+39)F'+12F,
\end{aligned}
\]

whose coefficient equation is exactly the OEIS recurrence.

## Limitations and novelty wording

The result assumes the published Krasko--Omelchenko EGF and proves its
coefficient recurrence.  It does not re-prove the combinatorial EGF, the OEIS
asymptotic, or minimality of either ODE.  Two recorded literature passes found
no independent proof of the exact recurrence, but this is a bounded database-
and-query statement, not an absolute priority claim.

## Certificate and independent audit

- Exact certificate: `certificates/annihilator_certificate.json`.
- No-import standard-library verifier: `certificates/verify_certificate.py`.
- Four corrupted certificates are rejected by `tests/test_certificate.py`.
- Direct literal-EGF differentiation independently verifies both ODEs.
- Exhaustive perfect-matching enumeration independently matches (n=1,ldots,7).
- Builder, Breaker, Certifier, and Referee records were produced serially.
- Citation audit: 12/12 frozen claims verified.
- LaTeX audit: 2 cited, 2 defined, 0 missing, 0 unused.
- Clean build: pass with no final warnings or box overflows.
- PDF: 4 pages inspected; metadata, embedded fonts, author identity, affiliation,
  emails, equations, table, references, and whitespace pass.
- Release manifest: `manifests/release_manifest.json`, generated from the stable
  `release_manifest_root` staging tree and verified with the skill's independent
  checker after all final artifacts were frozen.  The staging tree and manifest
  contain no `logs/` entry.  The live research log remains preserved in the
  project tree but is deliberately outside the release freeze root.

## Reproduction

```bash
python3 certificates/verify_certificate.py certificates/annihilator_certificate.json
python3 tests/test_certificate.py
python3 tests/enumerate_small.py
python tests/direct_symbolic_check.py
python src/derive_annihilator.py
python /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py paper/main.tex paper/references.bib
(cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex)
python /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py /Users/mac/Documents/ChatGPT/ai15-fourth-batch-2026-08-30/01_a278992_dfinite_recurrence/release_manifest_root /Users/mac/Documents/ChatGPT/ai15-fourth-batch-2026-08-30/01_a278992_dfinite_recurrence/manifests/release_manifest.json
```

No Lean, Coq, Isabelle, or other proof assistant was used.
