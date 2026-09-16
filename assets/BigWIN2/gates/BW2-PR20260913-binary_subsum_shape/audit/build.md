# Clean build audit

Job: `primary-20260913-binary-subsum-shape-release-b63927b8723e`. Verdict: **accept**. Checked 2026-09-13T00:42:04.160819+00:00.

The final source was rebuilt from scratch in `manuscript/` using:

```
latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The command returned zero and converged to a nine-page PDF. The retained `audit/release-build-transcript.log` includes the expected unresolved first-pass diagnostics before BibTeX and reruns; only the final engine log is used for acceptance. `audit/release-build.log` and the final `manuscript/build/main.blg` have no undefined citations/references, BibTeX missing or repeated entries, LaTeX errors, package warnings, overfull or underfull boxes. The key checker output is retained in `audit/release-bib-check.txt`: five source, bibliography and aux keys agree exactly.

`pdfinfo` confirms the intended title and author Xiaojian Zeng, nine letter-size pages, no encryption, and no JavaScript. `pdffonts` lists 21 fonts, all embedded. The actual PDF and every page were inspected separately as recorded in the visual report. The later one-line supplementary-code comment correction did not affect TeX inputs or PDF bytes; its checker was rerun successfully and the source manifest was refrozen.

Current manuscript digest: `d06ec580b55b37058246c2ae5e7cbc8175b2b13f0432c84821dfbee48d3510f1`.
Current PDF digest: `0f292bc7d40735ca4fe719110e0e9a7f613c6095415ccb903f9ec0f7a3de280d`.
Build-log SHA256: `32a8c4124ae8cd3f3b8c1f70d2afdb791c4402ee3dc02c33daf7e70287824b00`.
