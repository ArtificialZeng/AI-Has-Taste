# Independent uncancelled-product audit at degree 5

All equalities below are in the quotient ring
\(\mathbb Z[q]/(q^6)\). Write

\[
 N_m=(1-q^{2m})^8,
 \qquad D_m=(1-q^m)^{-16}.
\]

The binomial and negative-binomial formulas give

\[
N_m=\sum_{j=0}^{\lfloor5/(2m)\rfloor}(-1)^j{8\choose j}q^{2mj},
\qquad
D_m=\sum_{j=0}^{\lfloor5/m\rfloor}{15+j\choose15}q^{mj}.
\]

Thus factors with denominator index \(m\ge6\), and numerator index
\(m\ge3\), are exactly \(1\) modulo \(q^6\). The complete list of
nonidentity factors is

\[
\begin{array}{c|l}
N_1&1-8q^2+28q^4\\
D_1&1+16q+136q^2+816q^3+3876q^4+15504q^5\\
N_2&1-8q^4\\
D_2&1+16q^2+136q^4\\
D_3&1+16q^3\\
D_4&1+16q^4\\
D_5&1+16q^5.
\end{array}
\]

This keeps the numerator and denominator Euler factors separate; no use is
made of the cancellation \((1-q^{2m})/(1-q^m)=1+q^m\).

## Exhaustive convolution ledger

For a coefficient vector \([c_0,\ldots,c_5]\), multiplication by the next
factor uses \(c'_k=\sum_{i+j=k}c_i h_j\). Here are all nonzero summands that
change or initially create a coefficient. Coefficients declared unchanged
have only the summand \(c_k\cdot1\); hence no convolution summand is omitted.

Starting from \(N_1=[1,0,-8,0,28,0]\), multiplication by \(D_1\) gives

\[
\begin{array}{c|l|r}
k&[q^k](N_1D_1)&\text{value}\\ \hline
0&1&1\\
1&16&16\\
2&136-8&128\\
3&816-8\cdot16&688\\
4&3876-8\cdot136+28&2816\\
5&15504-8\cdot816+28\cdot16&9424.
\end{array}
\]

Successive multiplication by \(N_2\) changes only degrees 4 and 5:

\[
[1,16,128,688,\,2816-8,\,9424-8\cdot16]
 =[1,16,128,688,2808,9296].
\]

Multiplication by \(D_2\) has the full ledger

\[
\begin{array}{c|l|r}
0&1&1\\
1&16&16\\
2&128+16&144\\
3&688+16\cdot16&944\\
4&2808+16\cdot128+136&4992\\
5&9296+16\cdot688+136\cdot16&22480.
\end{array}
\]

Multiplication by \(D_3\) leaves degrees 0, 1, and 2 unchanged and gives

\[
\begin{array}{c|l|r}
3&944+16&960\\
4&4992+16\cdot16&5248\\
5&22480+16\cdot144&24784.
\end{array}
\]

Multiplication by \(D_4\) leaves degrees 0 through 3 unchanged and gives

\[
[q^4]=5248+16=5264,\qquad
[q^5]=24784+16\cdot16=25040.
\]

Finally, multiplication by \(D_5\) leaves degrees 0 through 4 unchanged and
gives

\[
[q^5]=25040+16=25056.
\]

The omitted \(N_3,N_4,N_5\) are each the identity modulo \(q^6\), as are all
remaining relevant numerator and denominator factors described above. It
follows exactly—not numerically—that

\[
\prod_{m\ge1}(1-q^{2m})^8(1-q^m)^{-16}
=1+16q+144q^2+960q^3+5264q^4+25056q^5+O(q^6).
\]

In particular \(b(5)=25056=5\cdot5011+1\). The frozen claim includes
\(n=1\), so this exact coefficient is a counterexample and the universal
congruence is false.

`evidence/research_b5_independent.py` reproduces every factor, every partial
coefficient vector, and every nonzero summand in each convolution using sparse
integer dictionaries and a locally implemented multiplicative binomial
routine. Its asserted final vector is
`[1, 16, 144, 960, 5264, 25056]`.
