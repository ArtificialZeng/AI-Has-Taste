# Precise reading

## Frozen target

Let \([n]=\{1,\ldots,n\}\) and let \(S_n\) be the set of all bijections
\(w:[n]\to[n]\).  For \(w\in S_n\), define \(G_w=\operatorname{Grid}(w)\)
to be the \(n\times n\) array whose square \((i,j)\) is black exactly when
\(j=w(i)\), and white otherwise.  Thus the convention is that the black
squares are the 1-entries of the permutation matrix of \(w\), with rows and
columns numbered in matrix order.

An *across word* is a maximal nonempty contiguous run of white squares in one
row; a *down word* is the analogous run in one column.  A complete
non-attacking rook placement on \(G_w\) is a subset \(R\) of its white squares
such that

\[
 |R\cap A|=1\quad\text{for every across word }A,
 \qquad
 |R\cap D|=1\quad\text{for every down word }D.
\]

Write \(\operatorname{RP}(G_w)\) for the finite set of these placements and
\(c(w)=|\operatorname{RP}(G_w)|\).  The quantity in the source is

\[
 r(n)=\max_{w\in S_n}c(w).
\]

The precise frozen equality claim is

\[
 \boxed{\max_{w\in S_9}c(w)=28549.}
\]

Equivalently, it consists of the two assertions

1. \(c(w)\le 28549\) for every one of the \(9!=362880\) permutations
   \(w\in S_9\); and
2. equality is attained.

The second assertion is already supplied by Lewis--Won, Proposition 3.15.  In
the usual direct-sum convention, the layered permutation of shape
\((3,1,1,1,3)\) is

\[
 w_0=321456987.
\]

Since \(S(3,1)=1\), \(S(3,2)=3\), and \(S(3,3)=1\), Proposition 3.15 gives

\[
 c(w_0)=\sum_{k=1}^{3}\bigl(S(3,k)k^3k!\bigr)^2
       =1+48^2+162^2=28549.
\]

Consequently a disproof of the numerical equality requires an explicit
\(w\in S_9\) together with an exact certificate that \(c(w)>28549\).  Merely
finding another maximizer would not disprove it.

## Exact counting interpretation

For a permutation grid there are \(2n-2\) across words and \(2n-2\) down
words.  Form the \((2n-2)\times(2n-2)\) zero-one matrix \(B_w\), with rows
indexed by across words and columns by down words, where an entry is 1 exactly
when the two words meet in a white square.  Then

\[
 c(w)=\operatorname{perm}(B_w).
\]

For an auditable integer recurrence, order the across words
\(A_1,\ldots,A_{2n-2}\).  Let \(F_i(S)\) be the number of matchings from the
first \(i\) across words onto the set \(S\) of down words.  Initialize
\(F_0(\varnothing)=1\), all other states as zero, and for every down word
\(D\notin S\) meeting \(A_{i+1}\), set

\[
 F_{i+1}(S\cup\{D\})\mathrel{+}=F_i(S).
\]

Then \(c(w)=F_{2n-2}(\{D_1,\ldots,D_{2n-2}\})\).  This is an exact
integer count, not numerical evidence.  An exhaustive proof must additionally
show that its permutation generator covers every element of \(S_9\) exactly
once, or justify any symmetry reduction completely.

## Scope and status

The claim asks only for the value of \(r(9)\).  Classification of all
maximizing permutations, proof of Lewis--Won Conjecture 3.14 for every \(n\),
and asymptotics of \(r(n)\) are outside the frozen claim.  They may be recorded
only as explicit strengthenings.

The nearest primary result is Joel Brewster Lewis and Robert Won,
*Non-attacking rook placements on crossword grids*, arXiv:2609.03081v1
(submitted 2026-09-02), especially the definitions in Section 2 and Section
3.2, Question 3.13, Conjecture 3.14, and Proposition 3.15:
https://arxiv.org/html/2609.03081v1 .  The paper reports exhaustive values only
through \(n=8\), namely \(1,1,1,5,17,73,469,3493\), and poses the general
maximization as a question/conjecture.  The exact \(n=9\) equality is therefore
an open-supported finite instance, not a theorem claimed by that source.

Literature check on 2026-09-06: exact-title, arXiv-identifier, and exact
"Conjecture 3.14" searches were run.  The arXiv record listed only v1, and no
separate primary paper resolving this four-day-old claim was found.  This is a
limited negative search result, not proof of priority or open status.  No local
historical registry was supplied for comparison.

## Triage target

Nearest prior result X: Lewis--Won prove the displayed formula for the layered
family and report a full computation through \(n=8\).  Proposed delta Y: give
a reproducible exhaustive exact determination of \(r(9)\), ideally with the
maximizers classified as a separately labelled strengthening.  Verification
route Z: enumerate all \(362880\) permutations, construct each \(16\times16\)
word-incidence matrix, compute its permanent by the integer subset recurrence
above, and independently spot-check the implementation against direct
backtracking and the published \(n\le8\) sequence.
