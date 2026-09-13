# Precise reading of DM07-01

## Frozen claim and domain

The immutable original statement is `source.md` (SHA-256
`853c88405c8f85aa43a3734cbe5b6f712db56a31f58467cd1b257593ec0207fb`).
It asks for a proof or disproof of one universal assertion, with

\[
c\in\mathbb Z,qquad c>5,qquad c\ne7,qquad S_c=\{2,5,c\}.
\]

Write \(\mathbb N_0=\{0,1,2,\ldots\}\).  Under normal play with the wall
convention, define the full Sprague--Grundy sequence recursively by

\[
G_c(n)=\operatorname{mex}\{G_c(n-s):s\in S_c,\ s\le n\}
\quad(n\in\mathbb N_0),
\]

where the mex of the empty set is zero.  The sequence is *purely periodic*
when

\[
\exists p\in\mathbb Z_{>0}\ \forall n\in\mathbb N_0:\quad
G_c(n+p)=G_c(n).
\]

If this holds, its least period is
\(\lambda(c)=\min\{p>0:G_c(n+p)=G_c(n)\text{ for every }n\ge0\}\).
This is full nim-value periodicity, not merely periodicity of the binary
outcome sequence \(1_{G_c(n)=0}\).

Let \(\rho(c)\in\{0,1,\ldots,6\}\) be the canonical representative of
\(c\bmod 7\).  For \(a=2,b=5\), let
\(\Theta_7,\Theta_{c+2},\Theta_{c+5}\subseteq\mathbb Z/7\mathbb Z\) be
exactly the three admissible-angle sets of Manabe, arXiv:2609.05358v1; the
subscripts label the three candidate periods \(a+b,a+c,b+c\).  Thus these
symbols are imported source predicates, not newly chosen residue sets.

The claim to resolve is

\[
\forall c>5,\ c\ne7:\qquad
G_c\text{ is purely periodic}
\iff
\rho(c)\in\Theta_7\cup\Theta_{c+2}\cup\Theta_{c+5}.                 \tag{C}
\]

In every positive case, \(\lambda(c)\) must be the least applicable
source-constructed candidate among \(7,c+2,c+5\), after replacing a
candidate by the proper divisor prescribed by the source whenever its
constructed word is imprimitive.  This least-period clause is part of the
claim, not an optional strengthening.

## Verified fixed-shape specialization of the cited v1

Direct inspection of Lemma 14, Theorem 28, Theorem 32, and Theorem 57 in
`literature/2609.05358v1.pdf` gives

\[
\Theta_7=\{2,5\},\qquad
\Theta_{c+2}=\{1,5\},\qquad
\Theta_{c+5}=\{2,3,6\}.                                           \tag{T}
\]

Indeed, here \(\delta=3=1\cdot2+1\); Theorem 57 gives
\(\Theta_{c+2}=\{\delta-2,5\}\), while the odd-case formula of Theorem 28
gives \(C_{2,5}=\{3,6\}\) and
\(\Theta_{c+5}=C_{2,5}\sqcup\{2\}\).  Consequently `(C)` becomes

\[
G_c\text{ purely periodic}\iff \rho(c)\in\{1,2,3,5,6\},            \tag{C'}
\]

with predicted least period

\[
\lambda(c)=
\begin{cases}
c+2,&\rho(c)=1,\\
7,&\rho(c)\in\{2,5\},\\
c+5,&\rho(c)\in\{3,6\}.
\end{cases}                                                       \tag{P}
\]

No assertion is made by `(C')` for the excluded additive point \(c=7\).
Residues \(0\) and \(4\) are the negative cases.  Theorem 32 together with
Proposition 46 gives the displayed candidate itself as the least period in
this primitive, non-harmonic shape, so there is no proper-divisor exception.

## Prior result, delta, and scope

Manabe's Theorem 32 supplies the admissible-angle construction (hence the
reverse implication in `(C)`) and the associated period information.  The
cited paper presents the necessity direction as Conjecture 50 in general.
An anonymous 2009 note, *Notes on Subtraction Games*, Theorem 6.6, already
states the zero/nonzero preperiod classification for \(\{2,5,c\}\), but it
gives no proof and contains an apparent typo in two positive-case periods;
see `evidence/literature_screen.md`.  The contribution established in
`evidence/fixed_shape_proof.md` is a complete all-\(c\) proof, with exact
nim-word formulae for both non-admissible residue families.  No claim is made
that the classification had never been stated before.

Finite computation is only evidence.  A resolution must give an all-\(c\)
argument, for example a finite-state certificate indexed by the seven
residue classes plus a proof that it covers every quotient \(\lfloor c/7\rfloor\),
or an exact counterexample verified directly from the mex recurrence.

## Source status

The cited v1 PDF is locally preserved and inspected.  A focused current
literature screen is recorded in `evidence/literature_screen.md`; it is not a
claim of priority.  The frozen assertion itself is resolved by the exact
argument in `evidence/fixed_shape_proof.md`.
