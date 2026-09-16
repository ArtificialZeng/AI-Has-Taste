# Precise problem statement

## Frozen source and interpretation

The immutable source is `source.md` (SHA256
`1f08092a9e4c6295f754d087f37122c35cefeae8728989351eb3e6644018dfcb`).
The assertion below is the universal odd-length analogue of Shoji's
Proposition 4.3 described in Remark 4.5; it is not a quotation that changes or
extends the frozen assertion.

## Objects and conventions

- Let \(F_0=0,F_1=1,F_{r+1}=F_r+F_{r-1}\).
- For each \(n\in\mathbb Z_{\ge 1}\), put \(j=2n+1\) and let
  \[
  L_n=\mathcal C(\underbrace{1,1,\ldots,1}_{j\text{ entries}})
  \]
  be the unoriented rational (two-bridge) link represented by the all-positive
  Conway normal form used in Shoji's Figure 5. With the standard simple
  continued-fraction convention, its Schubert fraction is
  \[
  [1,\ldots,1]=\frac{F_{j+1}}{F_j}
  =\frac{F_{2n+2}}{F_{2n+1}}.
  \]
  This arithmetic description fixes the same all-one family independently of
  a drawing convention. The family contains knots and two-component links;
  neither case is excluded.
- For an unoriented link \(L\), its Brandt--Lickorish--Millett--Ho
  \(Q\)-polynomial \(Q_L(x)\in\mathbb Z[x^{\pm1}]\) is determined by
  \[
  Q_{L_+}(x)+Q_{L_-}(x)
    =x\bigl(Q_{L_0}(x)+Q_{L_\infty}(x)\bigr),
  \qquad Q_U(x)=1,
  \]
  where the four diagrams agree outside the indicated skein disk and \(U\) is
  the unknot.
- For nonzero \(Q_{L_n}\), define
  \(e_n=\min\{k:[x^k]Q_{L_n}(x)\ne0\}\) and
  \(P_n(x)=x^{-e_n}Q_{L_n}(x)\in\mathbb Z[x]\). Then \(P_n(0)\ne0\).
  Multiplication by a Laurent monomial does not change the nonzero zero set,
  so Shoji's Laurent-polynomial definition of real stability is precisely the
  assertion that every complex zero of \(P_n\) is real.

## Quantified claim

Prove or disprove
\[
\boxed{\quad
  \forall n\in\mathbb Z_{\ge1}\;\forall z\in\mathbb C,
  \quad P_n(z)=0\Longrightarrow z\in\mathbb R.
\quad}
\]

A disproof requires one exact \(n\ge1\) and a rigorously certified nonreal zero
(or an exact real-root count smaller than \(\deg P_n\)). A proof must cover all
\(n\), including both component types. Finite numerical root plots or finitely
many exact checks do not prove the universal assertion.

## Scope boundaries and nearest result

The claim concerns exactly \(2n+1\) positive unit entries. It does not concern
the one-entry case \(n=0\), arbitrary odd coefficients, negative signs, general
two-bridge links, or the transformed Laurent polynomial
\(\widetilde Q_L(z)=Q_L(z+z^{-1})\).

Shoji's Proposition 4.3 proves real stability for the separate family with
exactly \(2n\) unit entries. Its proof obtains a third-order recurrence for that
even subsequence and then a Chebyshev/trigonometric sign-interlacing formula.
Remark 4.5 says only that the \(2n+1\)-entry analogue was verified for a few
small values and that a complete proof was not then available. Thus the precise
delta is the odd subsequence with its own initial data; it must not be treated
as a relabeling of Proposition 4.3.

