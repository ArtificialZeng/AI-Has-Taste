# Formal statement

## Locked definitions

Let \(\Sigma=\{0,1\}\), ordered by \(0<1\). For two words of equal length,
``<`` means the induced lexicographic order. If
\(x=x_0x_1\cdots x_7\in\Sigma^8\), its rotation by \(j\) positions is

\[
 \rho_j(x)=x_jx_{j+1}\cdots x_7x_0\cdots x_{j-1}
 \qquad (1\le j\le 7).
\]

A **binary Lyndon word of length 8** is a word \(x\in\Sigma^8\) satisfying
\(x<\rho_j(x)\) for every \(1\le j\le7\). Write

\[
 \mathcal L_8=\{x\in\Sigma^8:x<\rho_j(x)\text{ for all }1\le j\le7\}.
\]

For finite words \(u,W\), say that \(u\) is a **contiguous factor** of \(W\)
if there is an integer \(i\) with \(0\le i\le |W|-|u|\) such that
\(W_iW_{i+1}\cdots W_{i+|u|-1}=u\).

## Quantifiers and objective

Define

\[
 L_8=\min\bigl\{|W|:W\in\Sigma^*,\ 
       (\forall x\in\mathcal L_8)\ x\text{ is a contiguous factor of }W\bigr\}.
\]

The research question is to determine the exact integer \(L_8\), and to
produce both:

1. a literal word \(W\in\Sigma^{L_8}\) covering \(\mathcal L_8\); and
2. an independently checkable exact certificate that no word in
   \(\Sigma^{L_8-1}\) covers \(\mathcal L_8\).

## Normalizations

- The alphabet order is fixed as \(0<1\). Complementing every bit maps this
  convention to the opposite alphabet order but is not used silently.
- Reversal and bit-complement preserve superstring length after applying the
  same transformation to every required factor; they may be used only after
  the corresponding action on \(\mathcal L_8\) is proved.
- Leading and trailing bits are part of \(W\); cyclic wraparound is not
  allowed.

## Edge cases

- \(W\) is an ordinary finite linear word, not a cyclic word.
- Multiple occurrences and overlapping occurrences are allowed.
- Since every target has length 8, a word of length below 8 covers no target.
- The asserted cardinality \(|\mathcal L_8|=30\) will be derived exactly and
  independently enumerated; it is not taken as a definition.
- The source bounds \(49\le L_8\le94\), the claimed length-48 exclusion, the
  claimed 94-bit witness, and the claim of present open status remain source
  reports until the literature/certificate audit verifies them.

## Repair log

The source did not explicitly fix the alphabet order, rotation convention,
linear-versus-cyclic interpretation, factor indexing, or the form of the
minimum. These are fixed above without changing the intended finite problem.
