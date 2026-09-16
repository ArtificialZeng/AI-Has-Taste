# Triage validation evidence

Date: 2026-09-06  
Job: `win-00040-p03-triage-98375b7c1de0`

## Primary-source inspection

- Inspected https://arxiv.org/html/2608.14909v1.
- Equation (2) / Section 4.4 equation (16) matches the frozen inequality after
  setting \(d=4\).
- Section 4.4 defines normalized simplex volume as
  \(d!\operatorname{vol}(\operatorname{conv}S)\), equivalently an absolute
  augmented determinant.
- The paper proves \(d=3\) in Sections 5--6 and states in Section 7.5 that
  \(d\ge4\) remains open. It identifies \(d=4\) with geometric dimension
  \(n=5\).
- The live record lists authors Gennadiy Averkov, Katherina von Dichter, and
  Ivan Soprunov. This conflicts with the author names in the frozen source.
- Exact-title/equivalent-language searches restricted to arXiv on 2026-09-06
  returned the same record and no separate settlement of \(d=4\). This was a
  limited status screen, not an exhaustive novelty audit.

## Exact finite sanity check

All \(\binom{16}{5}=4368\) five-vertex subsets were enumerated, and each
normalized volume was evaluated by the integer Leibniz determinant formula.
The exact distribution was
\[
\operatorname{Vol}=0:1360,\quad 1:2672,\quad 2:320,\quad 3:16,
\]
so \(\sum_S\operatorname{Vol}(S)=3360\). At the all-ones vector,
\[
B=8^8=16{,}777{,}216,
\qquad A T^3=3360\cdot16^3=13{,}762{,}560,
\]
and hence \(H_4=3{,}014{,}656>0\). This validates the normalization at one
point; it is not evidence of global nonnegativity.

## Exploratory floating-point screen

A fixed-seed screen used 24 L-BFGS-B restarts in log-coordinates, normalized by
\(\sum_vx_v=1\). The largest observed ratio \(A(x)T(x)^3/B(x)\) was
approximately \(0.999999845945\), near a boundary equality and below one.
This is only floating-point evidence. It neither proves the claim nor rules out
a counterexample. A failed attempt to invoke the absent `python` executable was
operational only; the screen was then run with available `python3`.

