# Exact computational resolution dossier for `s_1(4)`

Job: `win-00085-p02-research-1374d8ae701f`

## Candidate theorem

`s_1(4)=9`.

## Mathematical reduction

An integer not divisible by 4 has residue in

`A={1,2,3,5,6,7,9,10,11,13,14,15}`

modulo 16.  Four integers have sum divisible by 4 but not by 16 exactly when
their residue sum modulo 16 is in `T={4,8,12}`.  Hence all hypotheses and the
desired conclusion depend only on the input residues modulo 16.

Permutation of sequence positions changes neither multiplicities nor the
existence of a four-position selection.  A length-`k` sequence can therefore
be represented without loss by a unique multiplicity vector
`c=(c_r)_{r in A}` with nonnegative entries summing to `k`.

## Lower bound

The length-eight sequence

`(1,1,1,2,2,2,10,13)`

uses only allowed residues.  Exact bounded-submultiplicity enumeration gives
the following complete support for sums of four of its positions modulo 16:

`{0,1,2,3,5,6,7,9,10,11,13,14,15}`.

This set is disjoint from `T`, so the defining universal property fails at
length 8 and `s_1(4)>=9`.

For a direct check, let `a,b,c,d` be the selected numbers of copies of
`1,2,10,13`.  Then `a+b+c+d=4`, with `a,b<=3` and `c,d<=1`, and the sum is
`4+b+9c+12d` modulo 16.  The four possibilities for `(c,d)` give respectively
`{5,6,7}`, `{13,14,15,0}`, `{0,1,2,3}`, and `{9,10,11}` (with exactly the
allowed ranges of `b`).  Their union is the displayed support, so this lower
bound does not depend on trusting the exhaustive program.

## Upper bound and exhaustive certificate

The independent verifier `multiplicity_dp_check.py` recursively generates
weak compositions of 9 into 12 coordinates.  Its recursion selects the first
11 coordinates and forces the last, so every nonnegative vector of sum 9 has
exactly one root-to-leaf path.  The asserted and observed domain size is

`binom(9+12-1,12-1)=binom(20,9)=167,960`.

For a fixed vector `c`, let `R_{i,j}` be the set of residues modulo 16
obtainable by selecting exactly `j` terms from the first `i` residue classes,
never taking more copies than `c` permits.  Starting from
`R_{0,0}={0}`, the program applies the exact recurrence

`R_{i+1,j} = union_{0<=q<=min(c_i,j)} (R_{i,j-q}+q*r_i) mod 16`.

It stores each `R_{i,j}` as a 16-bit Boolean mask and truncates only degrees
above 4.  Induction on `i` proves that the final degree-four mask is exactly,
not approximately, the support of all valid four-submultiset sums.

The scan tested all 167,960 multiplicity vectors and found zero for which the
degree-four support misses all of `4,8,12`.  Thus every allowed length-nine
sequence has the required selection and `s_1(4)<=9`.

Combining the bounds gives `s_1(4)=9`.

## Independent implementation evidence

The research verifier does not use `itertools.combinations_with_replacement`
and does not enumerate subsets of sequence positions.  Its result agrees with
the structurally different triage implementation, which sorts residue
multisets and directly tests position quadruples:

- length 8: 75,582 total multisets and 160 avoiders in both implementations;
- length 9: 167,960 total multisets and zero avoiders in both implementations;
- the displayed witness has the same complete four-sum residue support.

The executable sources and JSON reports contain hashes, coverage counts,
outcome histograms, and exact witnesses.  These artifacts constitute a
resolution candidate for fresh referee audit; this dossier does not itself
record referee acceptance.
