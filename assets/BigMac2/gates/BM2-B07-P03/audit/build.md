# Fresh build audit

Job: `bigMac-00007-p03-release-81cefd28b28f`. Reviewed: 2026-09-08T01:29:21.569617+00:00.

Evidence snapshot: `cde79d0ffca4c534449707d908f5983ea532054c14cc11a1f03e5d6913fcb0c1`.
Manuscript digest: `01fa45de2f853484308b276235d642c8f28098bd86c264922d2333c9e4dae501`.
PDF digest: `f363137820632afdb2f4d961be62835e867bc9334e9a32269a8566997f37cd4a`.

Verdict: **accept**.

Removed only the generated `manuscript/build` directory, recreated it empty, and ran three successful pdfLaTeX passes with the argument array in `audit/release-build-command.txt`. No source or frozen mathematical evidence was edited. The engine is pdfTeX 1.40.29 (TeX Live 2026). Each pass exited zero. The final third-pass `manuscript/build/main.log` is nonempty and records a five-page PDF. Reviewed the actual compiler log and final diagnostics: no fatal error, undefined control sequence, unresolved citation or reference, rerun warning, missing character, font substitution warning, overfull box or underfull box remains. The package-description phrase “Providing info/warning/error messages” is informational package identification, not a diagnostic.

`pdfinfo` and `pdftotext -layout` succeed. The PDF has a valid header, 5 letter-size pages, no encryption and nonempty text. Title, author Xiaojian Zeng, subject and keywords are correct. The 15 font entries reported by `pdffonts` are embedded subset Type 1 fonts with Unicode mappings. Supporting outputs are `audit/release-pdfinfo.txt`, `audit/release-pdffonts.txt`, and `manuscript/build/main.txt`.

The recorder has one authored project dependency, `manuscript/main.tex`; other project inputs are generated `.aux` and `.out`. All citation and cross-reference keys resolve. The inline bibliography needs no BibTeX pass. Detailed source/data/supplement checks are in `audit/release-content-check.md`.

The fresh PDF differs in its build-time bytes from the writer's PDF; `freeze-manuscript` was rerun successfully, preserving the unchanged source/evidence digests and binding the current PDF. All release audits refer to this current snapshot. Acceptance concerns build integrity and presentation; it adds no mathematical certification.
