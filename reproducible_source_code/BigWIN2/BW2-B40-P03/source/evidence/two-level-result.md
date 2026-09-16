# Exact two-level result for the four-cube inequality

Date: 2026-09-06  
Job: `win-00040-p03-research-837d53ce3818`

## The subsidiary theorem

Let (H_4=B-AT^3) be exactly as defined in `problem.md`. If the sixteen
coordinates of (x\in\mathbb R_{\geq0}^{16}) take at most two distinct
values, then

\[
H_4(x)\geq0.
\]

This does **not** settle the frozen problem for vectors taking three or more
values.

## Exact reduction and proof

Fix a subset (U\subset V=\{0,1\}^4), put (x_v=a) on (U), and put
(x_v=b) on its complement, where (a,b\geq0). Define

\[
c_j(U)=\sum_{\substack{S\in\binom V5\\|S\cap U|=j}}
\operatorname{Vol}(S),\qquad
q_F(U)=|F\cap U|,
\]

with every volume evaluated by the exact integer determinant in `problem.md`.
Then

\[
\begin{aligned}
A&=\sum_{j=0}^5c_j(U)a^jb^{5-j},\\
T^3&=(|U|a+(16-|U|)b)^3,\\
B&=\prod_F\bigl(q_F(U)a+(8-q_F(U))b\bigr).
\end{aligned}
\]

Consequently there are integers (h_0(U),\ldots,h_8(U)) such that

\[
H_4(x)=\sum_{k=0}^8h_k(U)a^kb^{8-k}.
\]

The self-contained standard-library program `two_level_certificate.py`
enumerates the (\binom{16}{5}=4368) simplices, evaluates their determinants
by the Leibniz formula, and computes these nine coefficients for all unordered
nontrivial bipartitions. Completeness is obtained by choosing from each pair
(\{U,V\setminus U\}) the unique member not containing the distinguished
vertex ((1,1,1,1)). These are exactly the nonempty masks on the remaining
fifteen vertices, hence (2^{15}-1=32767) cases. This covers every assignment
of two values; constant assignments are included by taking (a=b).

The program found (h_k(U)\geq0) in all (32767\times9=294903) positions.
Since (a^kb^{8-k}\geq0), the displayed coefficientwise expansion proves the
theorem. This is an exhaustive finite exact certificate, not an inference from
sampling or floating-point optimization.

## Reproduction record

Command:

```text
python3 evidence/two_level_certificate.py
```

Output on the stated job:

```text
volume_distribution={0: 1360, 1: 2672, 2: 320, 3: 16}
canonical_bipartitions_tested=32767
coefficients_tested=294903
negative_coefficients=0
zero_coefficients=2040
smallest_positive_coefficient=1
invariant_h_at_one=3014656
certificate_sha256=cd479d1e958d79bcd9580697f4c4fa2a932f18448174226026ecdeffcfdbbd19
certificate=PASS
```

The volume distribution is asserted in the program before the coefficient
test and agrees with the independent triage enumeration. The digest binds the
canonical stream `mask:h_0,...,h_8` for masks 1 through 32767; it is a
reproducibility aid, not a proof substitute.

## Structured numerical search beyond the theorem

The separate reproducible program `orbit_search.py` exhaustively enumerated
all set partitions of the five Hamming-weight orbits and the eight
fixed-facet-layer orbits into two and three levels. Optimization of the one- or
two-parameter values was floating point. Counts and largest observed ratios
(AT^3/B) were:

| Orbit system | Levels | Partitions | Largest observed ratio |
|---|---:|---:|---:|
| Hamming weight | 2 | 15 | 0.820312500000006 |
| Hamming weight | 3 | 25 | 0.999999997433264 |
| Fixed facet layer | 2 | 127 | 0.937499999999714 |
| Fixed facet layer | 3 | 966 | 0.999999999999886 |

Full positive optimization on the five and eight orbit parameters likewise
found no ratio above one (best approximately (0.9999999087) and (1.0),
respectively), with optima driven to boundary equality. These numerical
results neither certify a maximum nor extend the exact theorem to three-level
vectors.

## Primary-source comparison and limitation

The inspected source, arXiv:2608.14909v1, derives the hypercube inequality,
proves (d=3), and in Section 7.5 leaves (d=4) open. Searches within that
primary text found no statement about two-valued (x)-vectors. Its Section
4 reduction does use rows with two possible entries, which is a different
restriction. Limited arXiv searches on 2026-09-06 found no separate primary
source stating the subsidiary theorem above. This is a bounded comparison,
not a priority claim. The original sixteen-variable copositivity problem
remains unresolved.

Primary source: https://arxiv.org/html/2608.14909v1
