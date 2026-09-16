# Triage findings

Provenance: `win-00086-p03-triage-a8b7f5d8ddfc`  
Date: 2026-09-10 (Asia/Shanghai)

## Exact discriminating test

The matrix
\[
M=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}
\]
has determinant \(-1\ne0\) in \(\mathbb F_{11}\).  It swaps the second and
third projective coordinates.  For \(x\ne0\),
\[
 M(x:x^4:1)^{\mathsf T}=(x:1:x^4)^{\mathsf T}
   =(x^{-3}:x^{-4}:1).
\]
Putting \(u=x^{-3}\), the map \(x\mapsto u\) permutes
\(\mathbb F_{11}^{*}\), and \(u^8=x^{-24}=x^{-4}\), since exponents are
modulo 10.  Moreover, \((0:0:1)\) maps to \((0:1:0)\), and
\((0:1:0)\) maps to \((0:0:1)\).  Hence \(M(S_f)=S_g\), including the
zero and infinite points.

Exact enumeration of all ordered differences gives
\[
 \#\{w\ne0:\Delta_{\Gamma_f}(w)=k\}
   =\{0:50,\ 1:50,\ 3:20\},
\]
whereas
\[
 \#\{w\ne0:\Delta_{\Gamma_g}(w)=k\}
   =\{0:30,\ 1:70,\ 2:20\}.
\]
In particular, \(\Gamma_f\) has 20 nonzero difference vectors of
multiplicity 3, while \(\Gamma_g\) has none.  An affine graph equivalence
would send every difference \(w\) to \(Aw\) under its invertible linear
part, so it would preserve this 120-entry multiset.  The unequal multisets
therefore rule out CCZ equivalence.

`triage_exact_check.py` uses only integer arithmetic reduced modulo 11,
checks the source hash and all 12 projective points, constructs both complete
120-entry tables, asserts the two histograms above, and prints the tables.
This is exact reproducible evidence, not floating-point evidence.  It has not
yet received a fresh mathematical referee pass, so triage records an advance,
not an accepted resolution.

## Literature check

The cited arXiv v2 was inspected directly at
<https://arxiv.org/pdf/2510.04675> on 2026-09-10.  Example 2.11 proves the
projective half and states only EA inequivalence; Definition 2.14 supplies the
CCZ definition; Open Problem 4 asks for existence of projectively equivalent
but non-CCZ-equivalent polynomials.  Targeted searches of arXiv for the exact
pair, the exact equivalence language, and papers citing arXiv:2510.04675
returned no later primary resolution.  This limited search supports further
work but cannot establish novelty or priority.  No `literature/*handoff*.md`
file was present.
