# Precise problem reading

## Frozen claim

Let \(\mathbb F_3=\mathbb Z/3\mathbb Z\). Determine whether there exists a
matrix
\[
G=[g_1,\ldots,g_{11}]\in\mathbb F_3^{6\times 11}
\]
with \(\operatorname{rank}_{\mathbb F_3}G=6\) such that, for every
\(i\in\{1,\ldots,11\}\), there are four subsets
\(R_{i,1},\ldots,R_{i,4}\subseteq\{1,ldots,11\}\) satisfying

1. \(R_{i,a}\cap R_{i,b}=\varnothing\) whenever \(a\ne b\); and
2. \(g_i\in\operatorname{span}_{\mathbb F_3}\{g_j:j\in R_{i,a}\}\) for
   every \(a\in\{1,2,3,4\}\).

The recovery sets are arbitrary subsets: they need not contain \(i\), have a
prescribed size, or cover all eleven coordinates. Coefficients in each span
may be any elements of \(\mathbb F_3\). The four-set requirement is imposed
separately for each column, not simultaneously across different columns.

Equivalently, decide which of
\[
\operatorname{ASP}(6,4,3)=11\qquad\text{or}\qquad
\operatorname{ASP}(6,4,3)=12
\]
holds, where \(\operatorname{ASP}(k,t,q)\) is the minimum length of a
rank-\(k\) matrix over \(\mathbb F_q\) satisfying the \(t\)-all-symbol PIR
property above.

## Established bounds and scope

Boruchovsky--Gruica--Niemann--Yaakobi, *Serving Every Symbol: All-Symbol PIR
and Batch Codes*, arXiv:2601.04041v2, Theorem 23, gives
\[
11\leq \operatorname{ASP}(6,4,3)\leq
\operatorname{ASB}(6,4,3)\leq12.
\]
Thus existence of the stated \(6\times11\) matrix gives the lower value, while
a complete nonexistence proof gives the upper value. The source reports an
exhaustive nonexistence computation only for the binary cell
\(\operatorname{ASP}(6,4,2)>11\); it does not settle the ternary cell.

The field is exactly \(\mathbb F_3\), the dimension/rank is exactly six, and
the length under test is exactly eleven. A result about all-symbol batch codes,
another characteristic, or only a particular construction does not settle the
claim. A positive certificate must include the matrix, a rank witness, and four
disjoint recovery sets with exact coefficients for every column. A negative
certificate must exhaust all matrices modulo explicitly justified symmetries,
with a replayable completeness certificate.

## Nearest construction to test

Equation (3) of arXiv:2601.04041v2 displays a \(6\times12\) odd-characteristic
construction \(G''\). Deleting its second copy of the final all-one parity
column gives the natural \(6\times11\) candidate \(G'\). Remark 25 proves only
that this construction fails the all-symbol batch property when \(k=6\); that
does not by itself decide its all-symbol PIR property or the existence of a
different ternary matrix.

Source PDF inspected locally on 2026-09-10; SHA-256
`64d12f7e49d474c8db407ff341cc2e8cab800a88ad8cbf078244579068933062`.
