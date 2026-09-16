# Frozen source problem: Gilbreath valid-extension width at most nine

Canonical id: win-00084-p10
Frozen on: 2026-09-09 (Asia/Shanghai)
Primary source: Leila Muney, Holes in Valid-Extension Sets of Finite
Gilbreath Sequences, arXiv:2606.23721v2, definitions on PDF pp.1--3,
Proposition 2 p.8, Proposition 18 pp.17--18, Theorem 20 pp.18--20,
Theorem 25 pp.22--24, and open question 16(5) p.29.
Local copy: batches/inbox/bigWin-84-materials/2606.23721v2.pdf,
SHA-256 e571cee5a0f3d6deca074c6b951db03587296c713e14eaed820cad6573a5d5ed.

## Definitions

For an integer sequence S=(s1,...,sn), form its difference triangle by
repeated adjacent absolute differences. It is Gilbreath when the leftmost
entry of every positive row is one. Let G_n be the strictly increasing
Gilbreath sequences of length n with (s1,s2)=(2,3), and define

  K_S={k in Z : (s1,...,sn,k) is Gilbreath}.

No increasing requirement is imposed on the appended k in this two-sided
valid-extension set.

For 1<=i<=n-1, the right anti-diagonal is e_i=s^i_{n-i}. Its reverse
preimage step is

  P_e(T)={e+t:t in T} union {e-t:t in T and e>=t}.

The second branch is not {abs(e-t):t in T}.

## Statement

Give a complete if-and-only-if classification, for every n>=3, of

> all S in G_n satisfying |K_S|<=9.

A complete answer must state explicit finite or parametric templates and prove
both necessity and sufficiency; a finite table through a bounded n is not a
classification.

## Scope and contribution boundary

The source proves the unique width-five minimizer and explicitly asks for the
stability classification through width nine. This is unrelated to the prime
Gilbreath conjecture.

The cheapest first lemma to attack is:

  if K_S is not the candidate interval C_S, then |K_S|>=10.

That lemma is a research route, not part of the frozen assertion. If it fails,
the least exact counterexample should determine a repaired classification. If
it holds, combine the source interval-completeness criterion with a bounded
classification of realizable anti-diagonals. Every computation must use the
correct ordered reverse recurrence and an independent checker.

This file is immutable. Any bounded-length census must be reported only as a
partial result unless it proves the all-n classification.
