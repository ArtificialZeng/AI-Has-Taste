# bigMac-00027-p03 — the proposed five-letter good cyclic morphism

## Immutable source statement

On the alphabet `Z/5Z`, define the 14-uniform morphism `h` by

\[
h(0)=01213101314310,
\qquad h(r)=h(0)+r\pmod5
\]

letterwise.  Let `w=h^omega(0)` be its one-sided fixed point.  Decide whether
`w` is good: for every pair of adjacent nonempty finite factors `x,y` of `w`,

\[
\frac{\Psi(x)}{|x|}\ne\frac{\Psi(y)}{|y|},
\]

where `Psi` is the five-coordinate Parikh vector.  Equivalently, decide whether
`w` avoids weak abelian squares, or whether the associated standard-basis walk
in `N^5` has no three distinct collinear vertices.

A disproof must give the exact start position, lengths, factor text (or a
digest-bound reproducible prefix), and Parikh vectors of a violating `xy`.  A
proof must reduce all factor lengths and alignments, not infer universality
from a long finite prefix.

## Source and status boundary

- Primary source: Jeffrey Shallit, *Avoiding Three Collinear Points in a
  Unit-Step Lattice Walk*, arXiv:2609.05780v1, Proposition 1, Theorem 5, and
  Section 5, PDF pp.2, 6--8.
- Local primary PDF: `batches/literature/bigMac-27/2609.05780v1.pdf`, SHA-256
  `7b3b9e7193c9ddcf4bcb6efe3f32118bb8dfd05836ab0521a0134ffb803d8288`.
- The source proves a 16-letter construction and lists this five-letter
  morphism as a proposed smaller construction that the author could not prove.
  The exact current status remains status-uncertain pending a fresh search for
  subsequent computations or independent proofs.
