# Precise problem specification

## Frozen source and status

The immutable statement is `source.md` (SHA-256
`ce462b0aacd55a07bf7a64e52e96110e6e6f953d4bf779163753c7cb2ce876b9`).
The source classifies the problem as **open-supported**, citing Juan Gil,
Zhenni Liang, Ayodeji Odetola, and Michael Weiner, *Points of maximal traffic
on a grid with obstruction*, arXiv:2609.01562v1 (1 September 2026), Section 7.
This triage records that status; it does not claim an independent proof of
openness or novelty.

## Definitions and domains

For integers \(m\geq 0\) and \(0\leq k\leq m\),
\[
  \binom{m}{k}=\frac{m!}{k!(m-k)!}.
\]
For each integer \(n\geq 3\), let
\[
  A_n=\{a\in\mathbb Z:1\leq a<n/2\}
     =\{1,\ldots,\lfloor (n-1)/2\rfloor\}.
\]
For \(a\in A_n\), define
\[
\begin{aligned}
  D(n)&=\frac1n\binom{2n-2}{n-1},\\
  G(n,a)&=\frac{n-2a+1}{n-a}\binom na\binom{n-2}{a-1},\\
  R_n(a)&=\frac{G(n,a)}{D(n)},\\
  \rho(n)&=\max_{a\in A_n}R_n(a).
\end{aligned}
\]
All factorial arguments are nonnegative on this domain. Moreover,
\(n-a>0\), \(D(n)>0\), and \(n-2a+1\geq2\), so every displayed ratio is
well-defined and positive. The source writes these definitions for \(n\geq2\),
but \(A_2=\varnothing\), so \(\rho(2)\) is undefined under the usual real-valued
meaning of `max`. Restricting the definition of \(\rho\) to \(n\geq3\) repairs
this harmless boundary issue without changing the target, which only concerns
\(n\geq496\).

## Frozen target and equivalent quantified form

The claim to prove or disprove is exactly
\[
  \boxed{\quad \forall n\in\mathbb Z\ (n\geq496\Longrightarrow \rho(n)<1).\quad}
\]
Because \(A_n\) is finite and nonempty for every target value of \(n\), this is
equivalent to
\[
\begin{split}
  \forall n,a\in\mathbb Z,\quad
  &n\geq496\ \text{and}\ 1\leq a\leq\lfloor(n-1)/2\rfloor\\
  &\Longrightarrow\quad
  n(n-2a+1)\binom na\binom{n-2}{a-1}
  <(n-a)\binom{2n-2}{n-1}.
\end{split}
\]
The second form follows by multiplying \(R_n(a)<1\) by the positive quantity
\((n-a)\binom{2n-2}{n-1}\). The inequality is strict: equality for even one
admissible pair \((n,a)\), as well as a value greater than one, disproves the
claim.

## Nearest supplied result and remaining scope

Inspection of the supplied primary PDF confirms the following statements in
Section 7:

- Proposition 7.2 gives the displayed \(D(n)\), \(G(n,a)\), and \(R_n(a)\)
  reduction.
- Lemma 7.3 gives, for \(2\leq a<n/2\),
  \[
    \frac{R_n(a-1)}{R_n(a)}
    =\frac{a(a-1)(n-2a+3)}{(n-a+1)^2(n-2a+1)}.
  \]
- The paper reports exact rational verification of \(\rho(n)<1\) for
  \(496\leq n\leq2000\), and Conjecture 7.4 asserts the universal range above.

Thus the unresolved numerical scope begins at \(n=2001\). A finite exact scan
beyond 2000 can produce a rigorous counterexample if it finds \(R_n(a)\geq1\),
but a scan with no such pair is only a finite observation. Floating-point
values, non-uniform asymptotics, or verification over any finite range do not
prove the universal claim.

## Triage target

Nearest prior result: the supplied paper's exact verification through 2000 and
its adjacent-ratio identity. Proposed delta: either an exact pair
\((n,a)\) with \(n\geq2001\) and \(R_n(a)\geq1\), or a uniform proof that all
admissible pairs satisfy \(R_n(a)<1\). Verification route: use the exact
adjacent-ratio recurrence to localize/scan maximizers, preserve exact integer
comparison certificates near the threshold, and require explicit uniform error
bounds for any analytic tail argument.
