# bigMac-00027-p02 — exact three-neighbor percolation number of the `8 x 8` torus

## Immutable source statement

Let `G=C_8 square C_8`.  Starting from an initially infected set `S`, at each
step infect every uninfected vertex having at least three infected neighbors;
infection is permanent.  Let `t_3(8,8)` be the minimum cardinality of an `S`
whose closure is all 64 vertices.

Determine the exact value of `t_3(8,8)`, which the cited source bounds by

\[
22\le t_3(8,8)\le23.
\]

For the value 22, give an explicit 22-vertex set and an exact infection trace.
For the value 23, combine an explicit 23-set with a proof-producing exhaustive
certificate excluding every 22-set.  Solver success, floating-point output, or
an uncheckable symmetry assumption is not a negative certificate.  This target
does not ask for the source's full two-parameter Question 4.3.

## Source and status boundary

- Primary source: Alexander Clifton and Noah Kravitz Shaw, *Three-neighbor
  bootstrap percolation on grids and tori*, arXiv:2608.06133v1, Theorems
  1.6--1.8, Theorem 3.1, and Question 4.3, PDF pp.3, 23, and 38.
- Local primary PDF: `batches/literature/bigMac-27/2608.06133v1.pdf`, SHA-256
  `d5e8b1a28649cafea12d4b47fead8a692abb9ee1634a556cbd779d59276073e6`.
- The general perimeter lower bound gives 22 and the source's remaining-case
  construction gives 23.  The source singles out `8 x 10`, not `8 x 8`, as a
  known strict case.  The `8 x 8` value remains status-uncertain until current
  bootstrap-percolation literature and supplementary data are checked.
