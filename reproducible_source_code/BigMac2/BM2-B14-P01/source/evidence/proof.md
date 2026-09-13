# Exact invertibility probability: proof submitted for fresh review

Research provenance: `bigMac-00014-p01-research-09c4ecbfdfab`.
This is a mathematical evidence dossier, not a manuscript or an audit verdict.
The original statement is `source.md`; scope is fixed in `problem.md`.

## Statement

For every integer N >= 2, let A be uniform among N by N binary matrices
with all row and column sums equal to two; diagonal ones are allowed.
Set p_N = P(det A != 0), and define formal power series

\[
D(z)=e^{-z/2}(1-z)^{-1/2},\qquad
H(z)=e^{-z/2}(1+z)^{1/4}(1-z)^{-1/4}.
\]

Then, writing d_N=[z^N]D and h_N=[z^N]H,

\[
p_N=h_N/d_N. \tag{1}
\]

This holds for every N >= 2, with d_N>0. In particular p_2=p_4=0,
p_3=1, and 0<p_N<1 for every N>=5. As N tends to infinity through
all integers,

\[
\begin{split}
p_N={}& C_0N^{-1/4}
       +(-1)^{N+1}C_1\bigl(N^{-3/4}+N^{-7/4}\bigr)
       +O(N^{-9/4}),\\
C_0={}&\frac{2^{1/4}\sqrt\pi}{\Gamma(1/4)},\qquad
C_1=\frac{e\sqrt\pi}{2^{9/4}\Gamma(3/4)}>0.
\end{split}\tag{2}
\]

In particular the two-term expansion is
C_0 N^(-1/4) + (-1)^(N+1) C_1 N^(-3/4) + O(N^(-7/4)),
which implies both asymptotic requirements in `problem.md`.

## 1. Why the conditioned Ewens construction is uniform

Associate to a binary matrix A its simple bipartite graph with row vertices
and column vertices. All vertices have degree two, so every component is
an even cycle, of length 2k with k>=2. Let c(A) be its number of components.
Each component has exactly two alternating perfect matchings. Consequently
the whole graph has exactly 2^c(A) ordered decompositions A=P+R into disjoint
permutation matrices: choose which alternating matching belongs to P on
each component; the other matching is R. This accounts for every
decomposition, since each vertex must receive one edge of each color.

For such a decomposition put Q=P^(-1)R, so A=P(I+Q). Disjointness of P and R
is equivalent to Q having no fixed point: their columns coincide in a row
exactly when the corresponding relative permutation fixes an index.
Conversely every pair (P,Q) with Q fixed-point-free produces a binary
matrix with the specified row and column sums.

Following alternately an R edge and the inverse of a P edge around a
bipartite component of length 2k visits exactly its k column vertices.
Thus the relative permutation has one k-cycle on that component, and
c(Q)=c(A). The statement is unaffected by which conventional orientation
is used for permutation matrices.

Let Z_N = sum over fixed-point-free q in S_N of 2^(-c(q)). This is positive
for every N>=2, since an N-cycle is admissible. Independently choose P
uniformly and Q with mass 2^(-c(Q))/Z_N. The probability assigned to A is

\[
\sum_{P(I+Q)=A}\frac{2^{-c(Q)}}{N!Z_N}
=\frac{2^{c(A)}2^{-c(A)}}{N!Z_N}
=\frac1{N!Z_N}.
\]

It is constant on the entire matrix set. This proves the part of
He--Huang Lemma 6.2 needed here, including its normalization, and identifies
the law of Q as Ewens_N(1/2) conditioned on no fixed points. The above
proof is included so that no probabilistic representation is assumed.

## 2. The determinant criterion

This reduction is already explicit in Li--Lin--Rodman (1999), Theorem 3.1
and its proof; it is reproduced here for completeness, not claimed as new.

After simultaneous permutation of its rows and columns, Q is block
diagonal with cycle blocks C_k. The characteristic polynomial of C_k is
x^k-1: its eigenvectors are the geometric progressions corresponding to
the k distinct roots of unity. At x=-1 this gives

\[
\det(I+C_k)=1-(-1)^k.
\]

Therefore det(P(I+Q)) is nonzero if and only if every cycle length is odd.
Since fixed points were excluded, the allowed lengths are exactly
3,5,7,... . On this event |det A|=2^c(Q). No assertion about eigenvalues
of A following those of Q is needed: P is invertible and determinants
are multiplicative.

## 3. Weighted coefficient identity and all small sizes

For nonnegative integers m_1,...,m_N with sum k m_k=N, the number of
permutations with m_k cycles of length k is

\[
\frac{N!}{\prod_{k=1}^N k^{m_k}m_k!}.
\]

Indeed order the labels, divide by rotations within each cycle, and
divide by permutations of cycles of equal length. Weighting each cycle
by 1/2 and summing over allowed lengths L gives

\[
\frac1{N!}\sum_{q:\,\text{cycle lengths in }L}2^{-c(q)}
=[z^N]\prod_{k\in L}\sum_{m\ge0}\frac{(z^k/(2k))^m}{m!}
=[z^N]\exp\left(\frac12\sum_{k\in L}\frac{z^k}{k}\right). \tag{3}
\]

Take L={2,3,...} for D and L={3,5,...} for H. The formal identities
sum_{k>=1} z^k/k=-log(1-z) and
sum_{k>=1 odd} z^k/k=(log(1+z)-log(1-z))/2 give exactly D and H above.
The ratio of the two weighted sums is the probability in (1).
The same fiber calculation gives the integer counts

\[
|\mathcal M_{N,2}|=(N!)^2d_N,\quad
|\{A\in\mathcal M_{N,2}:\det A\ne0\}|=(N!)^2h_N. \tag{4}
\]

For a finite expression, sum the products
prod_{k=2}^N 1/((2k)^(m_k) m_k!) over sum k m_k=N, allowing only odd k
in the numerator. This is an all-N finite formula.
An alternative exact evaluation uses d_0=h_0=1, d_1=h_1=h_2=0 and

\[
2n d_n=2(n-1)d_{n-1}+d_{n-2}\quad(n\ge2),
\]
\[
2n h_n=2(n-2)h_{n-2}+h_{n-3}\quad(n\ge3). \tag{5}
\]

These follow by differentiating D and H:
2(1-z)D'=zD and 2(1-z^2)H'=z^2H.

No sum of odd integers >=3 equals 2 or 4; 3 itself is allowed. Every
fixed-point-free permutation on three points is a 3-cycle. Thus the
three exceptional values stated above follow. For odd N>=5 a single
N-cycle gives h_N>0; for even N>=6, the lengths 3 and N-3 do so.
For even N a single even N-cycle gives a singular matrix, and for odd
N>=5 the cycle lengths 2 and N-2 do so. Their positive Ewens weights
prove p_N<1 for N>=5. The case N=1 is outside the question (the matrix
set is empty); the formal zero denominator at N=1 is never divided by.

## 4. A coefficient estimate with an explicit remainder justification

For any fixed real noninteger beta, the generalized binomial identity
and the first gamma-ratio expansion from Stirling's formula give

\[
[z^n](1-z)^\beta
=\frac{\Gamma(n-\beta)}{\Gamma(-\beta)\Gamma(n+1)}
=\frac{n^{-\beta-1}}{\Gamma(-\beta)}
 \left(1+\frac{\beta(\beta+1)}{2n}+O(n^{-2})\right). \tag{6}
\]

Replacing z by -z multiplies the coefficient by (-1)^n.
All powers use their analytic branches defined by the value 1 at z=0.

Here is a direct justification for adding the two singularity
contributions and for the error bounds used below. It avoids needing
an unstated multi-singularity transfer theorem. If an analytic function
in the open unit disk extends to a C^3 function on the circle, its
nth Taylor coefficient is O(n^(-3)). To see this, use its Fourier
coefficient formula on the boundary and integrate by parts three times;
the integral of the absolute value of the third derivative is finite.
The boundary Fourier formula follows by radial limits and continuity.

Expand each analytic multiplier at each relevant singularity through
degree three and subtract the corresponding four fractional-power
terms from the function globally. For D the remaining local power at
1 is (1-z)^(7/2) times an analytic function. For H the remaining local
powers are (1-z)^(15/4) at 1 and (1+z)^(17/4) at -1, each times an
analytic function. A term subtracted at one point is analytic near
the other point. All three remaining fractional powers have exponent
strictly greater than three. They and their first three derivatives
along the unit circle extend continuously through the relevant point.
Away from these points the original functions and the subtracted
terms are analytic in a neighborhood of the circle. Thus the global
remainders have coefficients O(n^(-3)).

The degree-two and degree-three subtracted terms can now be bounded
individually using (6). For D they are O(n^(-5/2)) and O(n^(-7/2));
for H at 1 they are O(n^(-11/4)) and O(n^(-15/4)); and for H at -1
they are O(n^(-13/4)) and O(n^(-17/4)). Consequently retaining only
degrees zero and one incurs O(n^(-5/2)) for D and O(n^(-11/4)) for H.
There are no other singularities on the unit circle.

## 5. Both singularities and division

Write t=1-z and s=1+z. Direct Taylor expansion gives

\[
D(z)=e^{-1/2}t^{-1/2}(1+t/2+O(t^2)),
\]
\[
H(z)=e^{-1/2}2^{1/4}t^{-1/4}(1+3t/8+O(t^2))\quad(z\to1),
\]
\[
H(z)=e^{1/2}2^{-1/4}s^{1/4}(1-3s/8+O(s^2))\quad(z\to-1).
\]

For instance the analytic multipliers for H are
exp(t/2)(1-t/2)^(1/4) and exp(-s/2)(1-s/2)^(-1/4).
Using (6) and the remainder argument just given, set

\[
a=\frac{e^{-1/2}2^{1/4}}{\Gamma(1/4)},\quad
b=\frac{e^{1/2}2^{-1/4}}{\Gamma(-1/4)},\quad
c=\frac{e^{-1/2}}{\sqrt\pi}.
\]

Then

\[
d_N=cN^{-1/2}\left(1-\frac{3}{8N}+O(N^{-2})\right), \tag{7}
\]
\[
h_N=aN^{-3/4}\left(1-\frac{3}{8N}\right)
 +(-1)^N bN^{-5/4}\left(1+\frac{5}{8N}\right)
 +O(N^{-11/4}). \tag{8}
\]

For explicit sign and correction checks, the relative first corrections
are, respectively,

\[
-\tfrac18+\tfrac12(-\tfrac12)=-\tfrac38,
\quad -\tfrac{3}{32}+\tfrac38(-\tfrac34)=-\tfrac38,
\quad \tfrac{5}{32}-\tfrac38(-\tfrac54)=\tfrac58.
\]

The gamma factors in these corrections use Gamma(x+1)=x Gamma(x).
Since c>0 and d_N>0, division of (8) by (7) is justified. The first
corrections from z=1 cancel, so there is no N^(-5/4) nonoscillating
term in the probability. The relative correction from -1 after
division is (5/8)+(3/8)=1. The absolute remainder is O(N^(-9/4)):
the numerator remainder O(N^(-11/4)) is divided by order N^(-1/2),
and denominator truncation contributes O(N^(-9/4)) to the leading
term and O(N^(-11/4)) to the alternating term. Finally

\[
\frac ac=C_0,\qquad
\frac bc=\frac{e\sqrt\pi\,2^{-1/4}}{\Gamma(-1/4)}=-C_1,
\]

because Gamma(-1/4)=-4 Gamma(3/4). This proves (2) with the indicated
parity sign and hence the full frozen original problem.

## Dependencies, evidence, and gaps

External mathematical tools: elementary cycle decomposition, the
generalized binomial identity, Stirling's gamma-ratio expansion to first
order, and Fourier integration by parts. The needed uniform representation
and remainder argument are proved above; no spectral limit is used.
Flajolet--Odlyzko (1990), Section 5.1, supplies a primary reference for
the classical Darboux principle, but not the specific probability formula.

`evidence/verify_exact.py` and `evidence/exact_checks.json` give exact
finite consistency checks with fully stated coverage. The separate
`evidence/verify_asymptotics.py` and `evidence/asymptotic_checks.json`
verify local coefficient algebra exactly and label numerical asymptotic
diagnostics as uncertified floating point. Finite checks
are not the proof of the all-N claims. The derivation was prepared by
the research worker with deterministic Python assistance. No fresh
mathematical audit has yet occurred. Known mathematical gaps: none in
the argument submitted above; this remains a claim for independent review.
Literature and priority limitations are separately recorded in
`literature/research_comparison.md` and do not constitute proof gaps.
