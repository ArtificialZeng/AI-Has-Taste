# Precise interpretation

The immutable wording is in `source.md`. This file records the mathematical
reading used for subsequent work; it does not amend the source.

## Objects and definitions

- Let $p$ be a rational prime, and let $\mathbb F_p$ be the field with $p$
  elements (written additively when it is the underlying Alexander-quandle
  group).
- For $a\in\mathbb F_p\setminus\{0,1\}$, let
  $f_a:\mathbb F_p\to\mathbb F_p$ be $x\mapsto ax$. Then
  $Q_{p,a}=\operatorname{Alex}(\mathbb F_p,f_a)$ has operation
  
  \[
  x*y=ax+(1-a)y.
  \]
  
  Both $f_a$ and $1-f_a$ are invertible, so $Q_{p,a}$ is a finite latin
  Alexander quandle.
- The integral quandle ring \(\mathbb Z[Q_{p,a}]\) is the free
  \(\mathbb Z\)-module on symbols \(e_x\) for \(x\in\mathbb F_p\), with
  bilinear product \(e_xe_y=e_{ax+(1-a)y}\). A nontrivial idempotent is a
  nonzero \(u\) with \(u^2=u\) which is not one of the basis elements \(e_x\).
- A multiplicative character is a group homomorphism
  \(\chi:\mathbb F_p^\times\to\mathbb C^\times\); it is nontrivial if it is
  not identically $1$. Fix either primitive sixth root
  \(\zeta_6=e^{2\pi i/6}\). The unordered-set condition below is unchanged if
  \(\zeta_6\) is replaced by its inverse. The character is allowed to depend
  on both $p$ and $a$, and its order need not equal $6$.

## Quantified claim

Define the exact parameter count

\[
N_p=\#\left\{a\in\mathbb F_p\setminus\{0,1\}:\begin{array}{l}
\text{there exists a nontrivial multiplicative character }\chi\text{ with}\\
\chi(-1)=1\text{ and }
\{\chi(a),\chi(1-a)\}=\{\zeta_6,\zeta_6^{-1}\}
\end{array}\right\}.
\]

The source's universal assertion is precisely

\[
\forall p\;\bigl[(p\text{ prime})\wedge(p\ge 37)\wedge(p\equiv1\pmod{12})
\ \Longrightarrow\ N_p>0\bigr].
\]

For each fixed admissible pair $(p,a)$, Lemma 6.2 and Theorem 6.3 of
Elhamdadi--Ta--Virgin identify the character condition with existence of a
nontrivial idempotent in \(\mathbb Z[Q_{p,a}]\). Thus the ring and character
formulations are equivalent under the definitions above. The phrase in
`source.md` referring to "the exact count `N_p`" did not itself define the
symbol; the parameter count above is the natural reading. One may separately
count witness pairs $(a,\chi)$, but that is not called $N_p$ here.

The equivalent uniqueness phrasing adds the boundary assertion $N_{13}=0$:
$13$ is the first prime congruent to $1\pmod {12}$, while the quantified
universal assertion itself starts at $37$. No assertion is made that every
parameter $a$ works, or that one fixed character works for all primes.

## Prior result, status, and proposed delta

Retrieved 2026-09-06:

- M. Elhamdadi, L. Ta, and B. Virgin, *Fourier Analysis and Idempotents in
  Quandle Algebras*, arXiv:2609.03799v1,
  <https://arxiv.org/html/2609.03799v1>. Lemma 6.2 gives the character
  criterion and the necessary congruence; Theorem 6.3 proves its equivalence
  to a nontrivial integral idempotent; Corollary 6.4 treats primes outside
  $1\pmod {12}$. The introduction records the example $p=37,a=18$. The
  paper does not state the universal existence assertion above.
- J. Rong, F. Li, and T. Li, *Two classes of two-weight linear codes over
  finite fields*, AIMS Mathematics 8 (2023), 15317--15331,
  <https://doi.org/10.3934/math.2023783>, Section 2, defines cyclotomic
  numbers and tabulates classical order-six formulas for $p\equiv1\pmod
  {24}$, citing the earlier evaluations. This verifies that exact order-six
  cyclotomic-number machinery is available, but it does not state the present
  positivity claim and does not cover the $p\equiv13\pmod {24}$ half by the
  displayed lemma.

For a primitive root $g$ modulo $p$, take the sextic character
\(\chi_6(g)=\zeta_6\) and cyclotomic classes
\(C_i=g^i\langle g^6\rangle\). Since $p\equiv1\pmod {12}$ puts
\(-1\in C_0\), the number of parameters witnessed by this single character is

\[
(1,5)_6+(5,1)_6,
\qquad (i,j)_6:=\#\{x\in C_i:1+x\in C_j\}.
\]

This is a sufficient subcount of $N_p$. The nearest prior result is therefore
the fixed-parameter character criterion plus classical evaluation/bounds for
order-six cyclotomic numbers. The proposed delta is strict positivity of this
subcount for every prime $p\ge37$, $p\equiv1\pmod {12}$. A bounded
verification route is to expand the count into Jacobi sums, prove an explicit
$p/18-O(\sqrt p)$ lower bound, and exactly enumerate the finitely many primes
below the resulting threshold.

## Triage status

Source status: **new-question / status-uncertain**, not a source-attributed open
problem. Suitability: **advance**. The target is precise, the cyclotomic
reduction is nontrivial but standardly verifiable, and an exact finite checker
is available. No novelty or resolution is claimed at triage.
