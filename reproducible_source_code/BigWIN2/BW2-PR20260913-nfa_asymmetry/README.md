# BW2-PR20260913-nfa_asymmetry — Exact directional NFA separation for binary words with one marker

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260913-nfa_asymmetry_Exact_directional_NFA_separation_for_binary_words_with_one_marker.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260913-nfa_asymmetry/)

Original ID / 原始编号: `primary-20260913-nfa-asymmetry`. Origin / 来源: primary.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

Use epsilon-free NFAs over {0,1} with a finite nonempty state set, one initial state, an arbitrary accepting subset, and possibly missing transitions. Let nsep(w,x) be the minimum state count of an NFA accepting w and rejecting x, with unrestricted behavior on all other words. For every integer q&gt;=3, the maximum of nsep(0^a 1 0^b,0^c 1 0^d), over all nonnegative integers a,b,c,d satisfying a+b=c+d, a!=c, and nsep(0^c 1 0^d,0^a 1 0^b)&lt;=q, equals (q-1)^2+2. All word lengths are allowed and the maximum is attained. Consequently the unrestricted A(q) from source.md is at least (q-1)^2+2; its asymptotic growth remains unresolved.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260913-nfa_asymmetry
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260913-nfa_asymmetry
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/research-checks.py`
- `evidence/triage-structural-check.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- No third-party Python import detected by static inspection; this is not a tested environment lock.

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260913-nfa-asymmetry/evidence/triage-registry-screen.json', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
