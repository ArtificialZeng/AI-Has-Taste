# BW2-PR20260914-arbor_ehrhart_words — An Ehrhart–word identity for arbor polytopes

[Final PDF / 最终稿](../../../pdfs/BigWIN2/BW2-PR20260914-arbor_ehrhart_words_An_Ehrhart_word_identity_for_arbor_polytopes.pdf) · [LaTeX](source/manuscript/main.tex) · [Code, data and proof / 复现材料](source/) · [Historical release evidence / 门控记录](../../../assets/BigWIN2/gates/BW2-PR20260914-arbor_ehrhart_words/)

Origin / 原始编号: `primary-20260914-arbor-ehrhart-words`. primary-20260914.

## Accepted scope / 已接受范围

For every integer n>=1, every partition of [n] into nonempty blocks B_v, and every rooted tree tau on those blocks, let D_v be the union of descendant blocks including B_v and N_v=|D_v|. Set Q_tau={x in R^n: x_i>=0 for all i and sum_{i in D_v} x_i<=N_v for every v}. Let W_tau be all length-n words over [n] with at least N_v occurrences of letters from D_v for every v, and des(w)=|{j:1<=j<n, w_j>w_{j+1}}|. With sum_{m>=0}|m Q_tau intersect Z^n| t^m=h*(Q_tau,t)/(1-t)^(n+1), one has h*(Q_tau,t)=sum_{w in W_tau} t^(n-1-des(w)). Equivalently, for every integer m>=0, |m Q_tau intersect Z^n|=sum_{a in A_tau} product_{i=1}^n binom(m+1,a_i), where A_tau={a in Z_{≥0}^n:sum_i a_i=n and sum_{i in D_v} a_i>=N_v for every v}, and binom(m+1,a_i)=0 when a_i>m+1. No restriction on block labels, sizes, depth, or branching is imposed.

Branch: `resolution-paper`. Frozen original statement: `proved`. This records the prior internal review; it is not external peer review or a new priority claim. The PDF is unchanged.

## Verify and rebuild / 校验与编译

```sh
python3 ../prepare.py --verify
python3 ../build.py BW2-PR20260914-arbor_ehrhart_words
```

Requires Python 3.10+, latexmk and the TeX packages declared by the manuscript. The builder works in a disposable copy and does not replace the released PDF. `package.json` binds every source/data file to its original digest.

## Reproduction / 复现

- `source/evidence/research_checks.py`
- `source/evidence/triage_recursion.py`
- `source/evidence/desk_calibration.py`

Inspect each program before running it. Run from `source/` unless its own documentation says otherwise; some programs overwrite their output files, so use a disposable copy. The exact finite checks do not replace the general proof. This packaging pass replayed evidence/research_checks.py in a disposable directory: all recorded exact output bytes match. The tested ranges are 264 local identities, 225 operator identities, 80,011 subset objects, 17,065 word tests and three direct cases. The general proof is not established by these finite tests.

Dependencies and external-source access limitations are recorded in `package.json`. Downloaded third-party papers, credentials, installed environments and agent transcripts are deliberately excluded. Bibliographic metadata remains in the LaTeX/BibTeX files.

配套源码与数据保持原相对路径；打包不改变数学主张，也不把有限测试表述成一般性证明。外部文献访问的历史限制仍然有效。


## Packaging check results / 本次检查

Clean LaTeX rebuild: pass, six pages, no final warnings. Bibliography and extracted text match the frozen release; all six rendered pages match the original exactly and were visually inspected. Rebuilt PDF metadata differs, so the original released PDF is retained.
