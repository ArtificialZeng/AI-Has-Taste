# Research pass 1: exact abacus enumeration and a separated product lead

All claims in this file use the beta-set convention frozen in `problem.md`.

## Exact finite parametrization

Let (A=S(\lambda^1,0)).  The nesting (A\subseteq B\subseteq A+6)
first forces (A\subseteq A+6), so (\lambda^1) is a 6-core.  On runner
(i\in\{1,\ldots,6\}), let the first gap of (A) be

\[
  g_i=i+6a_i,\qquad a_i\in\mathbb Z,\qquad \sum_{i=1}^6a_i=0.
\]

Then ((A+6)\setminus A=\{g_1,\ldots,g_6\}), and the standard abacus
size formula gives

\[
 |\lambda^1|=3\sum_i a_i^2+\sum_i i a_i.
\]

A beta set (B=S(\lambda^2,t)), for (t=1) or (3), lies between (A)
and (A+6) exactly when it is (A\cup\{g_j:j\in J\}) for a subset
(J\subseteq\{1,\ldots,6\}) of cardinality (t).  Adjoining (t) beta
numbers (x_1,\ldots,x_t) to a charge-zero beta set changes partition size
by (\sum x_i-t(t+1)/2).  Hence every object, without duplication, has

\[
 |\lambda^1|+|\lambda^2|
 =6\sum_i a_i^2+2\sum_i i a_i
   +6\sum_{j\in J}a_j+\sum_{j\in J}j-\frac{t(t+1)}2. \tag{1}
\]

This formula is implemented in `enumerate_series.py`.  Enumeration through
degree 250 is complete: on the sum-zero hyperplane, Cauchy--Schwarz gives

\[
 |\lambda^1|\ge 3\lVert a\rVert_2^2-\sqrt{35/2}\lVert a\rVert_2.
\]

Thus a coordinate outside the script's box ([-9,9]) already forces
(|\lambda^1|>250), while every counted bipartition has
(|\lambda^1|\le |\lambda^1|+|\lambda^2|).  The calculation found no zero
coefficient for either charge in degrees (0\le n\le250).

Independently, the script expands
(c_3(q)=(q^3;q^3)_\infty^3/(q;q)_\infty) by exact integer polynomial
arithmetic, and expands (\phi(q)) from its defining square sum.  It found
no mismatch in

\[
 \phi(q)c_3(q)^2=c_{6,(0,3)}(q)+2q c_{6,(0,1)}(q)
\]

through degree 250.  The full coefficients and metadata are in
`series_250.json`.

## Separated product lead for the charge `(0,1)` branch

The first 80 exact coefficients suggested the periodic Euler exponents

\[
 c_{6,(0,1)}(q)\stackrel{?}=
 \frac{(q^2;q^2)_\infty^3(q^6;q^6)_\infty^2
       (q^{12};q^{12})_\infty^2}{(q;q)_\infty^2}
 =\psi(q)^2c_3(q^2)\psi(q^6). \tag{2}
\]

After freezing (2), `check_factorization.py` compared it against a fresh
complete enumeration through degree 500.  There were no mismatches, including
the held-out range (81\le n\le500); see `factorization_500.json`.  This is
exact finite evidence, not an identity proof.

If (2) is proved, positivity of this entire branch follows quickly.  The
constant term of (\psi(q^6)) may be used, and
(\psi(q)^2=\phi(q)\psi(q^2)).  Lemma 1.5 of the source supplies a 3-core of
every square size.  It is therefore enough that every (n\ge0) have

\[
 n=x^2+y(y+1)+2z^2. \tag{3}
\]

Equivalently, (4n+1=(2x)^2+(2y+1)^2+2(2z)^2).  The classical regularity
theorem for (X^2+Y^2+2Z^2) represents every odd positive integer; for an
integer congruent to 1 modulo 4, parity forces the (Z)-coordinate even and
exactly one of (X,Y) odd, giving (3).  As a falsification check only, (3)
has no miss through 10,000 in `factorization_500.json`.

## Gap

Equation (2) remains unproved here.  Finite agreement, even on a held-out
range, is not a theorem.  No analogous simple Euler product was detected for
the `(0,3)` branch.  Consequently the original conjunction remains open.
