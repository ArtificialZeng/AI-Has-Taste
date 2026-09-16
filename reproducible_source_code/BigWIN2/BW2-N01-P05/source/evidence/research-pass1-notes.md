# Bounded research pass 1: exact counts and the terminal-marker kernel

Job `newwin-00001-p05-research-0171927ebd6e`, 2026-09-12. The original
classification and enumeration for all k remain unresolved. This dossier is
research evidence, not a manuscript or a claim of a publishable new theorem.

## Exact finite results

Let T(w) be the least nonnegative number of passes needed to sort w. The
original target is T(w)=k for k letters and length 2k+2, using the known
upper bound T(w)<=k. Let P_k count target words without adjacent equal letters.

| k | M_k | P_k | independent forward census |
|---|---:|---:|---|
| 3 | 81 | 18 | 490 admissible RGS |
| 4 | 272 | 110 | 9,450 admissible RGS |
| 5 | 672 | 342 | 190,575 admissible RGS |
| 6 | 1,403 | 818 | 4,099,095 admissible RGS |
| 7 | 2,612 | 1,667 | not performed; complete inverse census |
| 8 | 4,475 | 3,047 | not performed; complete inverse census |

The forward domain includes every RGS with all multiplicities at least two.
The only two possible profiles are (4,2,...,2) and (3,3,2,...,2). Their counts
are independently checked against

    (2k+2)! / [4! 2^(k-1) (k-1)!],
    (2k+2)! / [(3!)^2 2^(k-2) 2! (k-2)!].

Clumped letters remain clumped; each unsorted pass clumps at least one new
letter (Xia; journal Corollary 2.2). Therefore omitted profiles cannot contain
an original target. RGS generation visits every relabeling class once and
prunes only impossible minimum or maximum multiplicities.

`research-pass1.py` checks a run-stack and the first-letter recursive map on
every visited iterate. On every target and reduced orbit it additionally
checks the literal forbidden-triple stack. Sorted inputs may stop early
because sorting is preserved by further passes. Full witnesses are saved in
`research-census-k3.json` through `research-census-k6.json`.

The inverse algorithm below reproduces these four entire witness sets, not
just their cardinalities, and then computes k=7,8. All inverse witnesses are
also checked through k passes using the three maps by `research-validation.py`.
The exact numbers satisfy the previously derived bookkeeping identity
M_k=P_k+(3/2)k(k-1)(2k+1). They are finite observations; no fitted all-k formula
is asserted. In particular, a degree-four interpolation through k=3,...,7
predicts 4471 at k=8, while the census gives 4475.

## Elementary facts about a new marker

Write D_x for deletion of all copies of x. If x is clumped in a word w, then

    D_x(phi(w)) = phi(D_x(w)).                         (1)

Proof by induction on word length using first-letter segmentation. If the
first letter is x, then w=x^m u, and phi(w)=phi(u)x^m. Otherwise write
w=a s_1 a s_2 ... a s_j, allowing empty segments. Because x is clumped, all
copies of x lie in one segment. Delete x in that segment, apply the induction
hypothesis there, and apply the first-letter formula to concatenate the
outputs and the terminal a-block. This also covers a segment becoming empty.
Since clumped letters stay clumped, (1) holds through every iterate.

Consequently, for a new letter x inserted anywhere in q, with resulting word
q', one has

    T(q) <= T(q') <= T(q)+1.                           (2)

Indeed, deleting a clumped letter from a sorted word preserves sortedness,
which proves the lower bound by (1). After T(q) passes, deleting x leaves a
sorted word. Inserting one x can split at most one of its constant runs, so
at most one old letter is unclumped. One more pass clumps that letter, while
all already clumped letters stay clumped. This proves the upper bound.
These are elementary working lemmas, with no priority or novelty claim.

An exact recurrence tracks the marker's gap. Number gaps in q from 0 to |q|,
and let g(q,p) be the output gap when x is inserted at gap p. Then
g(q,0)=|q|. For p>0 let a=q_0, let l be the last index <p with q_l=a, let j
be the number of occurrences of a at indices <p, and let h be the next index
>=p with q_h=a, or |q| if there is none. The first-letter formula gives

    g(q,p) = l-j+1 + g(q[l+1:h], p-l-1).               (3)

The offset is the total length of the earlier a-free segments. The marker
belongs to the indicated segment, including at its endpoints. Thus (3) is
an induction on length with a complete base case, and

    phi(q[:p] x q[p:]) = phi(q)[:g(q,p)] x phi(q)[g(q,p):].

After the unmarked word becomes sorted, the marker adds a pass exactly when
its gap lies inside a constant run. `research-validation.py` checks (3) for
every gap of every RGS of length <=8 on at most four letters, against the
literal triple-check stack. The recurrence, not the test, is the proof.

## The original bridge and a sharper unproved assertion

For an original target w with first letter x of multiplicity m, write
phi(w)=v x^m and q=trunc(v). The existing length proof in `triage-notes.md`
gives, with r=k-1,

    q is run-free, every letter occurs at least twice,
    2r <= |q| <= 2r+1.                                (4)

For completeness, the upper bound is immediate for m>=3. If m=2, split w
at its two x's. Some other letter occurs at least three times, so one of the
two segments contains a repetition. The image of any word with a repetition
has an adjacent equal pair: if its first letter repeats this is the terminal
block; otherwise remove its unique first letter and induct on length. Thus
truncating v loses at least one position. For the lower bound, maximal sorting
time forces x to be the only clumped letter of phi(w). Each other letter of v
therefore occupies at least two runs. Truncation makes this exactly the
assertion that each letter of q occurs at least twice.

Truncation compatibility implies T(v x^m)=T(qx). Hence the proposed bridge
would follow from the following statement, which is still UNPROVED:

**B:** For every r>=3 and every q satisfying (4), T(qx)=r implies T(q)=r,
where x is a new letter appended at the right.

`terminal-marker.py` checks all run-free RGS in (4) for r=3,...,6. Every
case passes. This implies the original bridge for k=4,...,7, beyond the
forward census through k=6. The inverse census tests the whole r=7 domain
as well and selects 57 marked words. The known run-free unmarked hard count
there is 1+r(3r-5)/2=57. Unmarked hard words always remain hard after adding
x by (1), so the equal cardinalities also certify B at r=7, hence the original
bridge at k=8. This is a finite conclusion using the cited preceding-layer
count, not an infinite induction.

A potentially more structural sufficient assertion is also UNPROVED:

**B2:** For every r>=3, if q is run-free, uses r letters, every letter occurs
at least twice, and at least two letters occur exactly twice, then
T(qx)=r implies T(q)=r.

B2 implies B because (4) leaves at least r-1>=2 letters occurring twice.
`two-double-marker.py` found no counterexample over all such q at r=3 and
lengths 6,...,16; r=4 and lengths 8,...,13; and r=5, length 14 (969,391 words).
For r=3 this actually covers every length: with two letters occurring twice,
run-freeness limits the third letter to at most five occurrences, so |q|<=9.
The r>=4 ranges do not exhaust B2. Its infinite proof and its literature
novelty have not been established; it is not proposed as a conjecture note.

The unrestricted version of B is FALSE even at r=3. An exact counterexample
outside (4) is q=01201202, with new marker 3:

    q    -> 21212000 -> 11000222            (sorted in two passes),
    q3   -> 212132000 -> 131000222           (unsorted after two),
                         -> 322200011      (sorted after three).

The orbits are in `terminal-marker.json` and were checked with all three maps.
There are also r=4 counterexamples at length 11. Thus commutation with deletion
does not justify deleting the marker from a sorting-time assertion. This is
an exact counterexample to an unrestricted subsidiary assertion, not a
disproof of the original problem or of the cited paper's restricted theorems.

## Complete inverse enumeration for each tested k

For a fixed output t, let Inv(t) contain its exact labeled preimages. If
t is empty, Inv(t)={()}. Otherwise let a be its last letter and m the length
of its terminal a-run. If a occurs before that run, Inv(t) is empty: the
first input letter must be the last output letter, and all of it must be in
the terminal block. In the remaining case write t=p a^m. Then

    Inv(t) = disjoint union over p=t_1 ... t_m of
             {a s_1 ... a s_m : s_i in Inv(t_i)}.       (5)

Empty t_i and s_i are allowed. Necessity and sufficiency are precisely the
first-letter formula. Disjointness follows because the occurrences of a in
an input uniquely delimit the s_i; their images fix the output cut positions.
Recursion strictly decreases length. A useful shortcut is that a run-free
output has a preimage only if all its letters are distinct, in which case
its unique preimage is its reverse; the repetition argument above proves this.

For k fixed, enumerate every q in (4), retaining exactly those with
T(qx)=r. For m in {2,3,4}, expand q's runs by a total of
d=2k+2-m-|q| positions, omitting negative d. For each resulting v, use (5)
on v x^m and standardize its preimages as RGS. This gives exactly the original
target set. Necessity is (4) and truncation; sufficiency is T(vx^m)=r, so its
preimage needs r+1=k passes. There are no duplicate descriptions: w uniquely
fixes m, its first output, its canonical q, and all run lengths. Relabeling
according to q makes one representation before final RGS standardization.

This is a finite inverse computation which RETAINS the marker; it does not
assume B. The exact q-domain totals for k=7 are 3655 and 72430, and for k=8
are 47844 and 1330994. They are independently checked using inclusion-exclusion
over adjacency links in fixed multiplicity profiles. For profile m_1,...,m_r,
sum over 0<=j_i<m_i the terms

    (-1)^sum(j_i) product_i binom(m_i-1,j_i)
      * (sum_i(m_i-j_i))! / product_i (m_i-j_i)!,

then divide by the factorials of the multiplicities of equal profile sizes.
Finally sum over all profiles with parts >=2. This independently counts the
run-free RGS domain. A chosen adjacency link merges two successive occurrences
of one letter, giving the inclusion-exclusion formula.

Although (5) is a valid general preimage recurrence, this computation still
selects q by its sorting time. It is not offered as the requested all-k
structural classification or as a new general fertility theorem. B would
replace that selection with the two known smaller-letter layers; evaluating
the inverse fibers uniformly would then remain necessary.

## Reproduction and next test

From the project root, run `python3 evidence/research-pass1.py 3 4 5 6`,
`python3 evidence/terminal-marker.py`, `python3 evidence/two-double-marker.py`,
`python3 evidence/inverse-census.py 3 4 5 6 7 8`, then
`python3 evidence/research-validation.py`. All mathematical tests use exact
integers and exhaustive specified domains; no randomness or floating point.

The next test is to prove or refute B2 using the explicit marker-gap recurrence
(3), targeting the claim that two double letters prevent the last-pass delay.
An adversarial finite attack should use r=5, length 15 and larger-excess
structured inputs, which have not been searched. A counterexample must retain
full marked and unmarked orbits and be checked against B's shorter length
scope before abandoning the original bridge. No proof that B2 is equivalent
to B or to the original classification is asserted.
