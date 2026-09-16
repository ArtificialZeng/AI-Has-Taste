# BW2-PR20260914-dumbbell_min_energy — Singular energy minima and fixed-product structure for all-odd complex unit gain dumbbells

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-dumbbell_min_energy_Singular_energy_minima_and_fixed_product_structure_for_all_odd_complex_unit_gain_dumbb.pdf) · [LaTeX entry / 入口](source/manuscript/main.tex) · [Sources, data and proof / 复现材料](source/) · [Gate records / 历史门控](../../../assets/BigWIN2/gates/BW2-PR20260914-dumbbell_min_energy/)

Original ID / 原始编号: `primary-20260914-dumbbell-min-energy`. Origin / 来源: primary-20260914.

## Accepted scope / 已接受范围

Partial-result note; parent problem not fully solved / 部分结果札记；母题未完整解决.

For every odd r,s&gt;=3 and odd ell&gt;=1, use the frozen graph and normalized gain real parts alpha,beta of problem.md, and put L=(ell-1)/2, N=r+s+ell-1, H=(s+L)alpha+(r+L)beta. The Hermitian characteristic polynomial satisfies P(0)=(-1)^(N/2)(1-4alpha beta) and P_x(0)=-2(-1)^(N/2)H. Thus its zero eigenvalue exists exactly on alpha beta=1/4 and is simple throughout that locus in the closed square. At each interior point q of that locus, with Z,W,X,Y the source Lemma 4.2 polynomials, A=Z-alpha beta W, B=alpha X+beta Y, C=A^2+B^2, I_alpha=integral_0^infinity(-beta WA+XB)/(t^2 C)dt, and I_beta=integral_0^infinity(-alpha WA+YB)/(t^2 C)dt, one has E(q+h)=E(q)+(2/pi)(I_alpha h_alpha+I_beta h_beta)+2&#124;beta h_alpha+alpha h_beta&#124;/&#124;H&#124;+O(&#124;&#124;h&#124;&#124;^2). Therefore a necessary condition for an interior singular local minimum is alpha I_alpha=beta I_beta and &#124;alpha I_alpha+beta I_beta&#124;&lt;=pi/(2&#124;H&#124;); together with strict inequality these conditions suffice for a strict local minimum. Equality in the normal bound is unclassified. Away from the singular locus the usual necessary interior conditions I_alpha=I_beta=0 hold. For every 0&lt;p&lt;1 the energy on alpha beta=p in the positive square is strictly convex in u=(1/2)log(alpha/beta), hence has a unique constrained minimum; at p=1 the curve is a singleton. When r=s the constrained minimum is (sqrt(p),sqrt(p)). When r&lt;s its coordinates satisfy alpha&lt;beta for p&lt;1, and X(t)/Y(t)&gt;(s+L)/(r+L) for all t&gt;0. In particular, if p&gt;=(r+L)/(s+L) the constrained minimum is exactly (p,1); if s+L&gt;=4(r+L), the unique positive singular-curve minimum is (1/4,1) and there is no interior singular local minimum. Exchange of cycles and simultaneous negation give the corresponding statements. These constrained endpoint minima are not asserted to minimize the full square. For D_(3,3,1), the full-square minima are exactly (+1/2,+1/2) and (-1/2,-1/2), with eight oriented cycle-gain switching lifts and common energy 2+sqrt(13)+sqrt(5); the source equation (117) integrals at the positive minimizer are strictly positive, while its diagonal derivative jump is 4/3. For D_(3,3,5), exact root intervals put the directional energy derivative at (1/2,1/2) along (-1,-1) strictly between -8/1000 and -7/1000, so this singular point is not a local minimum. Complete arguments and all scope exclusions are in evidence/singular-branch.md. The full original all-odd global minimum/equality classification remains unresolved.

The unchanged PDF retains its original authorship. This package reuses historical independent review and release evidence; it is not a new mathematical audit, journal acceptance, or a claim about a wider parent problem.

PDF保持原始字节及署名。本次核对配套文件，不重新审稿，不将部分结果或猜想包装成原题全解。

## Restore exact inputs / 还原精确输入

From this package directory / 在当前包目录执行:

```sh
python3 ../prepare.py --restore BW2-PR20260914-dumbbell_min_energy
```

No large input needs restoration.

Restoration verifies stored and original digests and refuses to overwrite modified data. Large restored files are excluded from Git; compressed copies are the distributed originals.

## Rebuild the manuscript / 重编译

```sh
python3 ../build.py BW2-PR20260914-dumbbell_min_energy
```

The helper uses a disposable copy and retains build output outside the archive. Requires `latexmk` and the TeX packages declared by the source. Build status during packaging: **pass**. A regenerated PDF is not a replacement for the historical released PDF.

Recorded build working directory / 已核验编译目录: `latex-parent`. The helper applies this automatically.

## Reproduction programs and proof / 程序与证明

Run programs from the `source/` directory unless their original instructions specify a subdirectory. Inspect their arguments first: discovery searches and full certificates can be long-running. Prefer a disposable copy; original programs may regenerate result files.

- `evidence/recovery_checks.py`
- `evidence/research_checks.py`
- `evidence/research_diagnostics.py`
- `evidence/triage_checks.py`

Bounded replay status in this packaging task: **not-rerun**. Not rerun means archived but not re-executed here; it does not mean the historical proof failed. A short test does not certify assertions outside its encoded finite range.



## Dependencies and limitations / 依赖与限制

- numpy
- scipy
- sympy

- Asset selection is a packaging recommendation, not a rerun of the proof or citation audit.
- Do not copy external literature PDFs, downloaded web pages, third-party archives, jobs, logs, prompts, or private operational metadata.
- Review absolute paths and third-party attribution markers before publishing. Import names are inferred dependencies, not a tested environment lock.
- The original question is unresolved; the released artifact is a partial result or unproved conjecture, according to its frozen claim.
- {'path': '/home/ailab/4math-open-problems/projects/primary-20260914-dumbbell-min-energy/evidence/triage_checks.py', 'indicators': ['absolute-local-path']}
- External reference literature is not redistributed. Consult the bibliography and archived source URLs.

`package.json` records every distributed scientific input, its original relative path, digest, and compression. External literature, account/configuration files, agent transcripts, installed environments and unrelated third-party binaries are not included. Bibliographic references remain in the LaTeX sources.
