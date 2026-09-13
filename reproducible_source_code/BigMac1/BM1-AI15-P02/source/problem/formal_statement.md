# Formal statement

## Objects and quantifiers

For every integer \(n\ge 1\), let
\[
B_n=\{1,2,3,4\}\times\{1,2,\ldots,2n\}.
\]
A king placement is a subset \(P\subseteq B_n\). It is nonattacking when
for all distinct \((r,c),(r',c')\in P\),
\[
\max(|r-r'|,|c-c'|)>1.
\]
Partitioning the board into the \(2n\) disjoint \(2\times2\) cells
\(\{1,2\}\times\{2j-1,2j\}\) and
\(\{3,4\}\times\{2j-1,2j\}\) proves \(|P|\le 2n\), and this bound is
attained by \(\{(1,2j-1),(3,2j-1):1\le j\le n\}\). Let \(X_n\) be the set of nonattacking placements with
\(|P|=2n\).

The group used here is, by explicit convention, the rectangular Klein
four-group
\[
G=\{1,h,v,hv\},\qquad
h(r,c)=(5-r,c),\quad v(r,c)=(r,2n+1-c).
\]
This convention is retained even at \(n=2\), when the board happens to be a
square. In particular the two diagonal reflections and the two quarter
turns of the square are **not** included. (Using the full order-eight square
group at \(n=2\) gives 14 orbits, whereas the OEIS value 23 is the order-four
count.)

Define \(a(n)=|X_n/G|\). At \(n=0\), set \(B_0=\varnothing\),
\(X_0=\{\varnothing\}\), and \(a(0)=1\).

## Target theorem

Prove, for every integer \(n\ge 10\),
\[
\begin{aligned}
a(n)={}&12a(n-1)-54a(n-2)+98a(n-3)+17a(n-4)-346a(n-5)\\
&+505a(n-6)-210a(n-7)-120a(n-8)+126a(n-9)-27a(n-10).
\end{aligned}
\]
Equivalently, prove in \(\mathbb Q[[x]]\) that
\[
\sum_{n\ge0}a(n)x^n=
\frac{(1-2x)(1-6x+17x^2-18x^3-2x^4+7x^5+6x^6-3x^7)}
{(1-x)^2(1-3x)^2(1-3x+x^2)(1-x-x^2)(1-3x^2)}.
\]
Also prove that numerator and denominator are coprime over \(\mathbb Q[x]\),
so the displayed degree-ten denominator and recurrence order are minimal.

## Edge cases and conventions

- The recurrence starts at \(n=10\), exactly the OEIS condition \(n>9\).
- Placements are subsets, so kings are indistinguishable.
- “Nonequivalent” means orbit counting under the specified order-four
  action, not that every orbit has size four.
- All certificate arithmetic is over \(\mathbb Z\) or \(\mathbb Q\); no
  floating-point or finite-prefix inference is accepted as proof.
