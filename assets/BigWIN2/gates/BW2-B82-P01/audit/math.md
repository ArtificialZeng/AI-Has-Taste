# Fresh mathematical referee report

Referee job: `win-00082-p01-referee-d1886b93c680`  
Frozen snapshot: `a33bb42a647e35b68db40803b7f9eaeaadc42bf7247c003fff107d6de46a6730`

## Scope checked

The submitted `resolution-paper` claim is exactly the negation of the frozen
existence statement \(\mathsf E(8,4)\): it rules out every bijection
\(e:\mathbb Z_{70}\to\binom{[8]}4\), every size-35 template, and every eight
independently chosen shifts satisfying the stated incidence identities.  Thus
the candidate does not replace the original question by a symmetric,
equally-spaced-shift, or Gray-code variant.

I checked all six snapshot hashes against the current files; each agrees with
`audit/snapshot.json`.  In the cited source PDF, Definition 1.1 has the same
independent-shift meaning used here, Lemma 2.2 states the coordinate-count
congruence used below, Theorems 1.3--1.4 cover uniformities two and three, and
Conjecture 7.1 leaves necessity in higher uniformities open.

## Reconstruction of the decisive argument

Assume an ordering exists.  Two vertices cannot have the same shift, since
their incidence supports would then agree, whereas the complete weight-four
layer contains a set including either vertex and excluding the other.  Hence
the eight shifts form a set \(S\subseteq\mathbb Z_{70}\).

At every time four vertices attend, so
\[
  1_S*1_D=4\,1_{\mathbb Z_{70}}.
\]
For distinct \(b,c\in S\), the two corresponding supports meet at exactly the
times indexed by four-sets containing both vertices, hence in
\(\binom62=15\) points.  Lemma 2.2, with \(m=8\), \(r=4\), and \(\lambda=15\),
therefore gives
\[
  15(T-8b)=0\quad(b\in S),\qquad T=\sum_{c\in S}c.
\]
Subtracting the relations for \(b,b'\) gives
\(120(b-b')=0\pmod {70}\).  The kernel of multiplication by 120 in
\(\mathbb Z_{70}\) is exactly \(7\mathbb Z_{70}\), since
\(\gcd(120,70)=10\).  No nonunit has been cancelled here.  Translating
\(S\) by \(-b_0\) and \(D\) by \(+b_0\) preserves every individual support,
so one may write
\[
  S=7A,qquad A\subseteq\mathbb Z_{10},\qquad |A|=8.
\]

Write each time uniquely as \(j+7x\), with \(0\le j<7\) and
\(x\in\mathbb Z_{10}\), and put
\(D_j=\{x:j+7x\in D\}\).  Directly from membership in \(D+7a\), the attendee
set at \(j+7x\) is
\[
  C_{j,x}=\{a\in A:x-a\in D_j\}=A\cap(x-D_j).
\]
Thus \(1_A*1_{D_j}=4\,1_{\mathbb Z_{10}}\).  Summation over \(x\) gives
\(|D_j|=5\) for every slice.

Let \(B=\mathbb Z_{10}\setminus A=\{b,b+d\}\).  Subtracting the last
convolution identity from
\(1_{\mathbb Z_{10}}*1_{D_j}=5\,1_{\mathbb Z_{10}}\) gives
\(1_B*1_{D_j}=1\).  For \(f=1_{D_j}\), this is precisely
\[
  f(z)+f(z-d)=1\qquad(z\in\mathbb Z_{10}).
\]
It forces alternation on every orbit of translation by \(d\).  Since the two
points of \(B\) are distinct, \(d\ne0\); an alternating solution exists exactly
when the order of \(d\) is even, which in \(\mathbb Z_{10}\) is exactly when
\(d\) is odd.

If \(d\ne5\), the odd element \(d\) generates \(\mathbb Z_{10}\).  The only
two templates are the parity classes.  The complement \(A\) contains four
elements of each parity, so all ten columns in a slice are only the two fixed
four-subsets of \(A\).  This contradicts injectivity of \(e\).

If \(d=5\), with \(H=\{0,5\}\), the complement \(B\) is one \(H\)-coset and
\(A\) is the union of the other four.  Every \(D_j\), and hence every
\(x-D_j\), is a transversal of the five \(H\)-cosets.  Consequently every
column chooses one point from each of the four fixed \(H\)-cosets in \(A\).
Only \(2^4=16\) different columns can occur over all seven slices, whereas a
bijection must realize all \(\binom84=70\) columns.  This is again impossible.
The cases exhaust all nonzero differences, proving nonexistence in the full
frozen scope.

## Independent checks and attacks

I ran the submitted exact verifier.  It checked all
\(\binom{10}{8}\binom{10}{5}=11{,}340\) pairs and reported 200 valid slice
pairs, split as claimed: 20 even-difference complements with no template, 20
non-antipodal odd-difference complements with two templates and two accessible
columns, and 5 antipodal complements with 32 templates and 16 accessible
columns.

I also performed a separate bit-mask enumeration organized by the two-point
complement rather than by \(A\).  For every complement and every five-set it
checked the two summands in \(1_B*1_D\) directly and reconstructed each column.
It independently returned the profile
\[
 (20;0,0),\qquad(20;2,2),\qquad(5;32,16),
\]
where each triple records the number of complements, valid templates, and
accessible columns in the relevant class.  The maximum accessible-column union
for any fixed \(A\) was 16.  This agrees with, but is not needed in place of,
the symbolic proof.

The quantifier reduction, convolution sign, normalization of both factors,
degenerate difference \(d=0\), noninvertibility modulo 70, and cross-slice
possibility were each checked explicitly.  None opens a missing case.  The
argument is finite and uses no limiting, probabilistic, or floating-point step.

## Source comparison, gaps, and verdict

Lemma 2.2 alone supplies only the torsion-coset reduction.  The candidate then
derives the seven quotient slices and completely classifies their two-point
translational tilings; that additional step is what yields the contradiction.
Relative to the cited primary source, which explicitly leaves higher
uniformities open, this is a substantive resolution of the first uncovered
middle-layer instance.  The frozen contribution makes no broader priority
claim, and this review does not certify one.

No mathematical or scope gap remains in the submitted claim.  **Verdict:
accept.**
