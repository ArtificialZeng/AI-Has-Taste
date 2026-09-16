# Exact finite resolution dossier

Provenance: `win-00082-p11-research-c81fb15b21eb` (research pass 1,
2026-09-09).

## Claim proved by the certificate

Let (T=(t_0<\cdots<t_4)) have a rank-one mass-at-most-three zero
profile whose primitive generator has mass three.  Then (M_3(T)\leq 33).
In fact, among all such profiles the largest exact minimum is 33.  Modulo
sign, the only directions with exact minimum 33 are

\[
 (1,-3,0,0,2)\quad\hbox{and}\quad(2,0,0,-3,1),
\]

which are reversals of one another.  This last classification is stronger
than the frozen universal bound.

The result is a candidate for fresh mathematical review, not a substitute
for that review.  All computations below use exact integers.

## Complete reduction to a finite domain

For a nonzero balanced row (a\in\mathbb Z^5) of mass at most three,
every coordinate lies in ([-3,3]).  Thus exhaustive traversal of that
coefficient box is complete.  Identifying (a) with (-a) by requiring its
first nonzero coordinate to be positive gives exactly 235 nonzero short rows
modulo sign (470 with both orientations).  Of these, exactly 160 are
primitive and have mass exactly three.

Write (g_j=t_j-t_{j-1}>0) and (A_j=\sum_{i=j}^4a_i).  Balance gives

\[
 a\mathbin\cdot T=\sum_{j=1}^4 A_jg_j.
\]

Consequently a direction can meet the strict-order cone only if its tail
sums contain both signs.  This condition is also sufficient: if
(P=\sum_{A_j>0}A_j) and (N=-\sum_{A_j<0}A_j), take (g_j=N) when
(A_j>0), (g_j=P) when (A_j<0), and (g_j=1) when (A_j=0).
All gaps are positive and the displayed dot product is zero.  The exhaustive
test leaves exactly 65 feasible primitive mass-three directions modulo sign.

If (T) satisfies the frozen hypotheses with primitive generator
(\delta), then

\[
 Z_3(T)=\{0,\delta,-\delta\},
\]

because every integral row in its one-dimensional rational span is an
integer multiple of the primitive row, and every nontrivial multiple other
than the two signs has mass at least six.  Hence it is enough to construct,
for each of the 65 directions, one increasing integer tuple whose complete
short zero profile is exactly that singleton modulo sign.

## Complete integer-model census

Translation normalizes every candidate integer alphabet to
(S=(0<s_1<s_2<s_3<s_4)).  For each exact diameter (D=s_4\leq33), the
producer visits all choices

\[
 1\leq s_1<s_2<s_3<D.
\]

Thus it visits

\[
 \sum_{D=4}^{33}\binom{D-1}{3}=\binom{33}{4}=40{,}920
\]

tuples.  It evaluates every one of the 235 canonical short rows on every
tuple.  A tuple is retained for direction (\delta) precisely when the
complete set of vanishing canonical rows is the singleton (\{\delta\}).
Diameters are traversed first, so the first retained tuple for a direction is
an exact minimum, not just an upper-bound witness.

All 65 feasible directions are covered.  Their largest minimum diameter is
33, attained only by the two reversal-related directions displayed above.
The certificate contains the 65 directions, their tail sums, constructive
positive-gap witnesses, minimum models, and the number of exact-profile
models through the cutoff.

The independent checker does not import the producer.  It regenerates the
235 rows as differences of unordered multisets of lengths one, two, and
three; regenerates primitive mass-three directions from pairs of disjoint
weak compositions of three; repeats all 40,920 model checks; and obtains the
same minimum model and model count for every direction.

It follows that every qualifying real (T) has the same zero profile as one
of the certified integer models of diameter at most 33, proving the frozen
universal bound.

## Sharpness from the relation-free four-letter core

For the cluster direction (\delta=(1,-3,0,0,2)), translate an integer
model to begin at zero.  The required relation forces
(-3s_1+2s_4=0), hence

\[
 S=(0,2c,2c+a,2c+b,3c),\qquad 0<a<b<c,
\]

for integers (a,b,c).  Put (U=(0,a,b,c)).  A balanced relation among
the last four letters of (S) is unchanged after translating them by
(-2c), so it is exactly a relation on (U).

Conversely, consider a reduced relation of mass (p\leq3) on (S) that
uses the first zero.  Orient it so that (z\geq1) zero terms occur on one
side.  The other terms all lie in ([2c,3c]), so equality of the two sides
requires

\[
 3c(p-z)\geq2cp,
\]

or (p\geq3z).  Therefore (p=3,z=1), and equality throughout forces the
two remaining terms on the zero side to be (3c) and all three terms on the
other side to be (2c).  This is precisely
(0+2s_4=3s_1).  Hence (S) has exactly the cluster profile if and only if
(U) is relation-free through mass three.

Because (U) begins at zero, relation-freeness is equivalent to all 20
unordered three-term sums from (U) being distinct: a shorter balanced
relation can be padded with zeros on both sides.  The exact core census
visits all

\[
 \sum_{c=3}^{11}\binom{c-1}{2}=\binom{11}{3}=165
\]

integer cores.  None with (c\leq10) is relation-free, while at (c=11)
the four relation-free cores are

\[
 (0,1,7,11),\ (0,1,8,11),\ (0,3,10,11),\ (0,4,10,11).
\]

Thus the cluster profile has exact minimum (3\cdot11=33), independently
recovering the sharp lower value.  The first core gives the model
((0,22,23,29,33)).

## Replay commands and artifacts

Run from the project root:

```sh
python3 evidence/enumerate_mass3.py --output evidence/mass3_certificates.json
python3 evidence/check_mass3_certificate.py --output evidence/mass3_audit.json
sha256sum evidence/enumerate_mass3.py evidence/mass3_certificates.json \
  evidence/check_mass3_certificate.py evidence/mass3_audit.json
```

At freeze time the producer/certificate hashes are respectively
`2760807640d5f5cc0bc68eaed87962aedef1fbb7de06a0cfe0dac72358efd2ca` and
`4168327f7cb36d5143777cd3ac1181811ea2c3b3187a27f8655eef78c9102505`.
The checker/audit hashes are respectively
`b2f53831abd6281e6d7c8957f31084348da983719802b72c2fc628adb4d32e7f` and
`484ffef747b49a55112edffa525cb8a232430c7e4872f263f4f6fd775c268e64`.

The literature boundary and its indexing limitation are recorded in
`literature/triage.md`.  No claim of global priority is inferred from a
finite literature search.
