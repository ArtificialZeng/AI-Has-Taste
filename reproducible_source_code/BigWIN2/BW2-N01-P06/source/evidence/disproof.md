# A finite disproof of the 54321 recurrence

Research candidate; proposer job `newwin-00001-p06-research-8a0fdffcb5e5`.
This is a proof and certificate dossier for fresh review, not an accepted
manuscript or a fresh referee report.

Let C_n be the permutations of {1,...,n} avoiding the classical subsequence
patterns 312 and 54321, whose composition squares avoid 132. Put a_n=|C_n|,
with a_0=1, and let b_n count the members of C_n ending in 1, for n>=1.
These are exactly the definitions frozen in `source.md` and `problem.md`.

**Claim submitted for review.** The proposed recurrence is false. Its first
failure in its stated range n>=6 is n=11, where

    a_11 = 1265,
    a_10 + a_9 + a_8 + a_7 + 10 = 655 + 338 + 174 + 89 + 10 = 1266.

The proof consists of an elementary direct-sum reduction and a complete exact
finite classification. The finite computation is part of the proof, with its
domain completeness established below; it is not a numerical extrapolation.

## 1. Direct-sum reduction

For permutations u in S_r and v in S_s, u direct-sum v is the concatenation
of u with the entries of v increased by r. Write delta_j=(j,j-1,...,1).

If a 312-avoiding permutation pi has 1 in position k, every entry before 1
is smaller than every entry after it: otherwise x,1,y with x>y would be 312.
Consequently its first k entries are exactly {1,...,k}, and it has the unique
form pi=rho direct-sum tau with rho ending in 1. Squaring preserves a direct
sum. The patterns 312 and 54321 cannot cross a direct-sum boundary, so their
avoidance is equivalent to avoidance within each summand.

If pi is in C_n and tau is nonempty, tau^2 must be increasing. An inversion
in tau^2, preceded by any entry of rho^2, would be a 132 occurrence. Thus tau
is an involution. Conversely, rho^2 avoiding 132 and tau^2 being increasing
ensure that rho^2 direct-sum tau^2 avoids 132: a mixed occurrence would need
an inversion in the right summand. This also covers an empty tau.

Every 312-avoiding involution tau is a direct sum of decreasing permutations.
Indeed, if 1 occurs in position j, the preceding minimum-element argument
isolates a block on {1,...,j}. The involution condition gives tau(1)=j.
Any ascent among the entries between this j and 1 would form a 312 together
with the first entry j. Therefore this entire block is delta_j. Its suffix
is again a 312-avoiding involution; induction proves the assertion. Conversely
every such direct sum is an involution avoiding 312. It avoids 54321 exactly
when every decreasing block has size at most four.

We have proved a bijection between C_n, n>=1, and pairs consisting of a
member counted by b_k and a composition of n-k with parts in {1,2,3,4}.
The empty composition is permitted. If t_0=1 and

    t_m = sum_{j=1}^{min(4,m)} t_(m-j)  (m>=1),

then

    a_n = sum_{k=1}^n b_k t_(n-k)  (n>=1).                 (1)

There is also a direct form useful for the proposed recurrence. A member of
C_n not ending in 1 has a nonempty layered suffix. Remove its last decreasing
block delta_j, where 1<=j<=4. The remainder is a nonempty member of C_(n-j).
Conversely appending delta_j to any nonempty member of C_(n-j) gives a member
of C_n not ending in 1. These cases are disjoint: the final decreasing run
has length exactly j, since the preceding direct-sum boundary is an ascent.
Thus, for every n>=1,

    a_n = b_n + sum_{j=1}^{min(4,n-1)} a_(n-j).           (2)

In particular for n>=5,

    a_n - a_(n-1) - a_(n-2) - a_(n-3) - a_(n-4) = b_n.  (3)

The source recurrence is therefore equivalent, at each n>=6, to b_n=n-1.
This reduction adapts the method in the proof of Archer--Bourne Theorem 4.2;
its full argument is supplied here, and no novelty is claimed for the method.

## 2. Complete finite domain for the endpoint census

A permutation pi of length n ending in 1 can be written uniquely as

    pi=(alpha_1+1,...,alpha_(n-1)+1,1),  alpha in S_(n-1).

It avoids 312 exactly when alpha does: a terminal minimum cannot participate
in a 312 occurrence. It avoids 54321 exactly when alpha avoids 4321. A
four-term descent in alpha extends by the terminal 1; conversely any
five-term descent in pi supplies a four-term descent in alpha, whether or
not it uses the terminal 1. Hence the complete classical endpoint domain at
n=11 is a shifted copy of Av_10(312,4321).

Here is an independent scalar count of that domain. Let f_h(m) count
312-avoiders of length m whose longest decreasing subsequence has length at
most h. Set f_h(0)=1, and f_0(m)=0 for m>0. The position of 1 gives the unique
decomposition

    (alpha+1),1,(beta+k+1),  |alpha|=k, |beta|=m-1-k.

Its longest decreasing subsequence has length
max(LDS(alpha)+1,LDS(beta)), with LDS(empty)=0: decreasing subsequences cannot
cross the direct-sum boundary after 1. Both subpermutations must avoid 312,
and these conditions suffice, by the minimum-element argument above. Thus

    f_h(m) = sum_{k=0}^{m-1} f_(h-1)(k) f_h(m-1-k).      (4)

Equation (4) and the base values give, for h=3 and m=0,...,10,

    1, 1, 2, 5, 13, 34, 89, 233, 610, 1597, 4181.

This integer calculation counts exactly Av_m(312,4321). It requires neither
the source conjecture nor a square-avoidance assumption.

`endpoint_exhaustive.py` visits *every* permutation of {2,...,n}, appends 1,
and applies direct index inequalities. It runs for each n=1,...,11, with no
symmetry quotient or recursive generation. At n=11 it visits all 10!=3,628,800
tuples; 16,796 avoid 312, and 4,181 also avoid the classical descending
restriction. For each of these 4,181, `endpoint_classical_n11.json` records
the permutation, its square, and either a triple of one-based indices forming
132 in the square, or null for an accepted square.

The separate `verify_endpoint_certificate.py` imports no census implementation.
It recomputes (4), checks that all 4,181 recorded permutations are distinct
bijections ending in 1, and checks their original 312 and 54321 avoidance by
generic relative ranks of subsequences. Their verified number equals the
complete domain size from (4), so no classical endpoint can be missing.
The checker then recomputes every square, validates all 4,172 exclusion
triples, and checks all triples in each of the nine accepted squares. This
is an exact certificate of exhaustiveness and both inclusion and exclusion;
a success flag alone is not the argument.

## 3. The nine members and the recurrence failure

The complete list at length 11, in lexicographic order, is as follows. Each
entry uses one-line notation; 10 and 11 are individual values.

| pi | pi^2 |
| --- | --- |
| (2,3,4,5,6,7,8,9,10,11,1) | (3,4,5,6,7,8,9,10,11,1,2) |
| (2,4,3,5,6,7,8,9,10,11,1) | (4,5,3,6,7,8,9,10,11,1,2) |
| (2,5,4,3,6,7,8,9,10,11,1) | (5,6,3,4,7,8,9,10,11,1,2) |
| (2,5,4,7,6,3,8,9,10,11,1) | (5,6,7,8,3,4,9,10,11,1,2) |
| (2,5,4,7,6,9,8,3,10,11,1) | (5,6,7,8,9,10,3,4,11,1,2) |
| (4,3,5,6,7,8,9,10,11,2,1) | (6,5,7,8,9,10,11,2,1,3,4) |
| (4,3,5,7,6,9,8,11,10,2,1) | (7,5,6,8,9,10,11,1,2,3,4) |
| (4,3,6,5,8,7,10,9,2,11,1) | (5,6,7,8,9,10,11,2,3,1,4) |
| (4,3,6,7,5,8,9,10,11,2,1) | (7,6,8,9,5,10,11,2,1,3,4) |

As a useful partition of the certificate, first entries 2,3,4 have respectively
1,597, 1,597, 987 classical endpoints, and respectively 5,0,4 accepted squares.
The exhaustive check for n=1,...,11 gives

    (b_1,...,b_11) = (1,1,2,3,3,5,6,7,8,9,9).

All these smaller endpoint lists are included in `endpoint_exhaustive.json`.
Substituting in (1), or iterating (2), gives

    (a_0,...,a_11) = (1,1,2,5,11,22,45,89,174,338,655,1265).

Thus all six prescribed initial values are correct, and b_n=n-1 for
6<=n<=10. But b_11=9 rather than 10. Equation (3) proves that n=11 is the first
recurrence failure in the stated range, with the numerical discrepancy given
at the start. A single failed instance disproves the universally quantified
original claim. No assertion about a corrected recurrence for larger n is made.

## 4. Reproduction, scope, and source

Run from the project directory using ordinary Python 3 and its standard library:

    python3 evidence/endpoint_exhaustive.py
    python3 evidence/verify_endpoint_certificate.py

These commands use the archived triage/insertion data only for comparisons
*after* independently constructing the endpoint lists and counts. The latter
are not generated by the conjectured recurrence. To reproduce the older full
class enumerations too, run `triage_count.py`, `insertion_verify.py`, and
`compare_enumerations.py` in `evidence/`, in that order, from the project root.
They use respectively minimum-element recursion and maximum insertion; both
agree with the endpoint-based counts and on the complete C_11 set. The first
method's n=12 calculation is not needed for, or included in, the claim's scope.

All decisive arithmetic and comparisons are exact integers. No random tests,
floating-point tolerances, search cutoff, unexecuted C++ program, or proposed
all-n formula is part of this certificate. The endpoint census and certificate
checker were authored and executed in this research worker; the older two
enumerators were supplied from triage. Multiple algorithms and a separate
checker do not constitute a fresh referee or a formal proof-assistant check.

The exact conjecture is in [Archer--Bourne, Section 5, second paragraph and
displayed equation](https://arxiv.org/html/2505.05218v3#S5). Their Theorem 4.2
treats the adjacent restriction 4321. The complete primary HTML, including
both passages, is frozen as `evidence/external/archer-bourne-v3.html` and was
compared with the decisive live source passages on 2026-09-12. The bounded
current literature comparison and its limitations are recorded in
`literature/research-literature.md`. No equivalent disproof was found in that
search; priority is not established by absence of a search result.

Known mathematical gaps in this computer-assisted argument: none identified
by this worker. Remaining audit tasks: independently inspect the decomposition
and completeness proof, rerun the certificate, and assess source scope and
the bounded novelty claim. No manuscript or output PDF has been created.
