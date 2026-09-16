# Precise problem and admitted subsidiary target

Job: primary-20260913-nfa-asymmetry-research-71ec4a8ef3d7. Date: 2026-09-13.
The original source is immutable; no correction to its statement is proposed.

## Definitions and quantifiers

An NFA is (Q,{0,1},delta,i,F), with Q a finite nonempty state set,
i in Q its single initial state, F any subset of Q, and delta a possibly
partial transition relation Q x {0,1} -> P(Q). There are no epsilon edges.
A word is accepted precisely when some path with that label goes from i to F.
For distinct finite binary words w,x, nsep(w,x) is the minimum |Q| of such an
NFA accepting w and rejecting x. Its behavior on all other words is unrestricted.

For each integer q>=3 define

    A(q) = max { nsep(w,x) : L>=1, w,x in {0,1}^L,
                              w!=x, nsep(x,w)<=q }.

All lengths L are included; there is no fixed length ceiling. The set is
nonempty and integer-valued. Powerset determinization of the reverse separator,
including the empty subset, and complementation give A(q)<=2^q, so a maximum
exists. Direction, equal length, binary alphabet, partial transitions and the
single initial state are part of the frozen problem.

The source asks for the growth of A(q), without conjecturing a particular
formula. The precise research reading is to determine its asymptotic order as
q tends to infinity; a genuine improvement of its bounds is partial progress,
and an exact formula would be stronger. A statement only about unequal lengths,
unambiguous NFAs, singleton recognition, or sep/nsep is a different problem.

## Nearest verified prior result

Nicol, Further Remarks on Separating Words, arXiv:2608.30928v1,
[Section 4.1, Theorem 6](https://arxiv.org/html/2608.30928v1), gives
(q-1)^2+1<=A(q)<=2^q and explicitly leaves the growth question open.
The live version record lists v1, 31 August 2026. Source status is
open-supported within the bounded literature coverage recorded in
`evidence/triage-literature.md`; no global openness or priority claim is made.
The older unbounded directional difference/ratio question is already resolved.

## Explicit subsidiary scope submitted for review

Define A_one(q) by the same maximum restricted to

    w=0^a 1 0^b, x=0^c 1 0^d,
    a,b,c,d in Z_{>=0}, a+b=c+d, a!=c.

This natural subsidiary target includes Nicol's entire quadratic lower-bound
witness family. It does not replace the original A(q). The first research pass
supplies a complete proposed proof of the sharp formula

    A_one(q) = (q-1)^2+2, for every integer q>=3.

This is a result-note candidate requiring fresh review, not an accepted theorem.
The upper bound uses the classical Boolean-matrix power index H=(q-1)^2+1,
an elementary derivation of period lcm(1,...,q), and a complete short-block/
modulus dichotomy. The lower bound strengthens Nicol's pumping argument:
a simple prefix of m-1 edges visits every state of an m-state NFA, including
a vertex on a cycle in its long zero suffix. Full arguments, dependencies,
and the owner gap record are in `evidence/one-marker-proof.md`. The new exact
diagnostics and their coverage are in `evidence/research-checks.py`,
`evidence/research-checks.json`, and `evidence/research-verification.md`.

Nearest prior result X: Nicol's quadratic family and Schwarz's classical
universal Boolean-power theorem. Proposed delta Y: the exact extremal
directional cost on all one-marker words, locating the sharp limit of that
witness class. In particular, no one-marker construction can witness
superquadratic directional cost in terms of the reverse separator size.
The all-size separator and strengthened lower witness have been checked by
the owner, and the exact theorem was compared against current primary sources.
A standalone constant improvement to the general lower bound is not the
proposed contribution scope.

The decisive original-source inputs are copied unchanged into `evidence/external/`:
Nicol's v1 PDF/HTML, Schwarz's 1974 PDF, the Zajac-Jokay PDF, and the Demaine
et al. author PDF. `evidence/external-source-manifest.json` records their hashes.
Schwarz's 1974 printed p.167 explicitly states the required index bound for
every binary relation, using the periodic-group definition on p.161 and
referring to his 1970 p.653. The 1974 statement was read and rendered; this
provides the authoritative account required by the previous next test.
The original 1970 proof was not accessed and is not described as proof-checked.
The proof dossier derives the period directly and does not use the printed
typo in Zajac-Jokay's definition. No equivalent exact one-marker formula was
found in the bounded searches recorded in `evidence/research-literature.md`;
priority and significance still require referee judgment.
No claim about general A(q)'s asymptotic order follows from the restriction.

## One next test

Have a fresh referee verify the precise formula A_one(q)=(q-1)^2+2 for all
q>=3, focusing on Schwarz's all-relations index statement, the extra-state
cycle insertion, and whether the sharp subclass theorem is a substantive
unrecorded contribution beyond Nicol's lower-bound construction.
