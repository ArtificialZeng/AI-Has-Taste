# Build audit

Verdict: **ACCEPT**. Job: `primary-20260914-stirling-transition-release-4805c41c0f1c`. UTC date: 2026-09-14.

After the final TeX formatting repairs, the generated `manuscript/build` directory was removed and the following command completed with exit code 0 from `manuscript/`:

```sh
latexmk -pdf -outdir=build -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The actual clean-build transcript is `audit/release-build-transcript.log`. The final compiler and bibliography logs are `manuscript/build/main.log` and `manuscript/build/main.blg`. Both were inspected and scanned: no fatal error, undefined reference/citation, database omission, duplicate entry, package/LaTeX warning, overfull box or underfull box remains. Temporary first-pass label warnings in the full transcript resolved on convergence.

The read-only skill checker command
`python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py manuscript/main.tex --aux manuscript/build/main.aux`
reports five cited keys, five bibliography keys and five resolved aux keys, with zero missing, unused or unmatched keys. The final output is saved in `audit/bib-key-check.txt`.

The PDF is a nonencrypted A4 document with five pages and extractable text. `pdfinfo` confirms the article title and Xiaojian Zeng as author, pdfTeX production, no JavaScript and no forms. Fonts are embedded Type 1 Latin Modern fonts and mathematical symbols render legibly. `audit/pdfinfo.txt` and `audit/release-pdf-text.txt` retain the metadata and extracted text. The recorder and bibliography log show no omitted local authored dependency. The supplement replay matches its declared exact results; it is not part of LaTeX execution.

The current snapshot binds the PDF digest `22f7c5bfe3776b76e3440bb37b6cc9731b836d1d817a01617f50e97b7978157d`, manuscript digest `b64176baca047430939a473ba56db928a446b305936c40617a9b3da740e3b2d3`, and unchanged research snapshot `b137208424a1f9968874146cbe4d73bed2aeb9258d7ef9df7b155c852e9275ca`. `audit/build.json` additionally binds the final compiler-log bytes. This build audit checks the artifact; mathematical correctness rests on the separate accepted mathematical review.
