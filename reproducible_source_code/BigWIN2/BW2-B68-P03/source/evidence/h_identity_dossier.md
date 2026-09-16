# Stronger 6-section identity: conjecture and attack dossier

## Exact conjecture

Write (f_d=(q^d;q^d)_\infty) and
\[
H(q)=\sum_{m\geq0}c\phi_{18}(6m+1)q^m.
\]
The new conjecture isolated in research pass 2 is
\[
\boxed{H(q)\equiv4\frac{f_2f_3^2}{f_1f_6}
=4\sum_{k\in\mathbb Z}q^{k(3k-1)/2}\pmod {16}.} \tag{A}
\]
Identity (A) is **unproved**. A falsifier is any (m\geq0) for which
(c\phi_{18}(6m+1)) is not congruent modulo 16 to 4 when (m) is a
generalized pentagonal number and to 0 otherwise.

## Proved consequences of the proposed right side

The equality
\[
\frac{f_2f_3^2}{f_1f_6}=\sum_{k\in\mathbb Z}q^{k(3k-1)/2} \tag{B}
\]
is a Jacobi triple-product identity, not a numerical conjecture. The triple
product gives
\[
\sum_{k\in\mathbb Z}q^{k(3k-1)/2}
=f_3(-q;q^3)_\infty(-q^2;q^3)_\infty,
\]
and (1+x=(1-x^2)/(1-x)) turns the last product into
(f_2f_3^2/(f_1f_6)).

For either sign, (k(3k\pm1)/2\pmod5) lies in \(\{0,1,2\}\), by checking
the five residues of (k\pmod5). Thus (A) would give
\([q^{5n+3}]H=[q^{5n+4}]H=0\pmod {16}\). Since
(6(5n+3)+1=30n+19) and (6(5n+4)+1=30n+25), it implies both parts of
the frozen Conjecture 5.1.

## Exact finite attack

The first 100 coefficients (0\leq m\leq99) were used to recognize the
generalized-pentagonal support. The statement was then frozen and checked on
the held-out range (100\leq m\leq504), with no failure. The left side was
generated in two structurally independent ways: the finite Laurent
constant-term product and formula (3.15), using eta-product and cubic-theta
expansions. The right side was generated as the eta quotient in (B) and by
direct enumeration of (k(3k-1)/2). All four 505-byte vectors agree, with
SHA-256 `8f82367d83f74fbeb3f32cf989c7c921f707c583f7c1e90e73a4d518da310db8`.
See `computation/h_identity_mod16.py` and `h_identity_metadata.json`. This is
exact finite evidence only, not an all-orders proof.

The separate summand audit of formula (3.15) gives a smaller kernel. Numbering
the fourteen nonzero summands as in `projection_term_audit.py`, all tested
coefficients in the (6m+1) section cancel in the groups
\[
(1+2),\ (3+7),\ 4,\ 5,\ 6,\ (8+9),\ 10,\ 12,\ (11+13+14).
\]
Every group except (1+2) vanishes throughout the tested section; group
(1+2) has zero 5-sections precisely at residues 3 and 4. Two whole-series
cancellations, (4+5\equiv0) and (10+12\equiv0\pmod{16}), are formal:
their multipliers are 8, while (a(q)\equiv1\pmod2) and
(f_d^2\equiv f_{2d}\pmod2).

Moreover, summands 4, 5, 6, 10 and 12 have no odd exponents modulo 16 after
their shifts. Modulo 2 their residual eta quotients are respectively
\[
\frac{f_{48}}{f_2f_{16}},\quad
\frac{f_{48}}{f_2f_{16}},\quad
\frac{f_6f_{48}}{f_8f_{16}},\quad
\frac{f_6f_{96}}{f_8f_{16}},\quad
\frac{f_6f_{96}}{f_8f_{16}},
\]
and their shifts (q^2,q^2,q^2,q^4,q^4) are even. The remaining grouped
6-section cancellations are observations through the stated range, not
proved identities.

## Source comparison and limits

The official arXiv v1 source states only the two target progressions modulo
16 as numerical Conjecture 5.1 and leaves them open. It does not state (A).
Exact-phrase and formula searches on 2026-09-07 for the (6n+1) section, the
two progressions, and generalized-pentagonal support returned no primary
source containing (A); this is a bounded screen, not a priority claim. The
searched exact coefficient range ends at (c\phi_{18}(3025)), equivalently
(m=504). No all-orders modular certificate has been checked.

## Minimal unresolved kernel and next falsifier

It is enough to prove (A). Apply the source's 2-dissection to formula (3.15)
modulo 16, extract odd powers, then apply its 3-dissections to post-extraction
indices (0\pmod3). After deleting the five parity-supported summands, test
whether the remaining four grouped identities reduce formally to
(4f_2f_3^2/(f_1f_6)). A modular-form replacement must first specify the
shifted half-integral-weight forms, level, character, cusp holomorphy or
denominator clearing, coefficient ring and Sturm bound. The fastest
computational falsifier is to extend either exact left generator beyond 504.
