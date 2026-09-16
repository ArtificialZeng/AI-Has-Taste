# Triage evidence

Provenance: `win-00044-p02-triage-1262df62dacf`  
Retrieval/check date: 2026-09-06

## Source integrity and inspected literature

- `source.md` had SHA-256
  `ab0704f0de5fc5c2317404c3924ee9a21b70a52a90eff2f2f38c063473b2cbe9`
  before editing other project files.
- The project-local path `bigWin-44-materials/2609.03346.pdf` named by the
  source was absent.  No conclusion depends on that access failure.  The
  primary online v1 was inspected at
  <https://arxiv.org/abs/2609.03346> and
  <https://arxiv.org/pdf/2609.03346>.
- Chen--Chen, arXiv:2609.03346v1: Conjecture 1.3 is on PDF p.2; Theorem 2.7
  on pp.6--7 treats even `k=2r` only for `r>=4`; Theorem 3.5 on pp.9--10
  treats odd `k>=7`.  The arXiv record says v1 was submitted 2026-09-03.
- Czabarka--Singgih--Sz\'ekely, doi:10.1016/j.jctb.2021.06.001, was inspected
  in the authors' journal PDF at
  <https://homepages.uc.edu/~singgih/CounterExample-JCTB.pdf>.
  Conjecture 2 on printed p.40 is the general statement; the preceding text
  says that even `k=2r` is identical to part (ii) of the Erd\H{o}s et al.
  conjecture.
- Erd\H{o}s--Pach--Pollack--Tuza,
  doi:10.1016/0095-8956(89)90066-X, *JCTB* 47 (1989), 73--79, is the original
  source.  The exact odd-clique conjecture was cross-checked against the 2021
  paper and the authoritative problem-list entry
  <https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/DiameterOfKrFreeGraph.html>.
- Exact searches for `K7-free`, `6-colorable`, diameter, minimum degree, and
  the coefficient `8/3` located the 2026 preprint but no resolution of its
  `k=6` boundary.  This bounded negative search is not a novelty proof.

## Cheapest construction test

Specialize the definitions preceding Chen--Chen Theorem 2.7 to `r=3` and
choose `delta=40m`.  Then
\[
\tau=5,\quad d=8,\quad \lambda=5m,\quad a_1=a_3=8m,
\quad\eta=35m-5,\quad z=11m-5,\quad y=3m-4.
\]
The nominal 13-layer period has total weight `S=195m-1`.  Were it admissible,
its per-period excess over the frozen coefficient would be exactly
\[
13-\frac{8S}{3(40m)}=\frac1{15m}>0,
\]
so periodic repetition would give a disproof for the fixed degree `40m`.

The unmodified specialization is not admissible.  For every `m>=2`,
\[
g=\left\lceil\frac{35m-5}{11m-5}\right\rceil=4,
\]
because `eta-3z=2m+10>0` and `4z-eta=9m-15>=0`.  Its exceptional consecutive
layers therefore contain `3+4=7` mutually adjacent base vertices, producing
a `K_7` in the base graph (and hence in the blow-up).

There is also an exact obstruction to repairing this fixed architecture only
by deleting edges in that 7-vertex clique.  With all layer totals unchanged,
weighted degree constraints cap each of the three `E`-class weights by `y`
and each of the four `F`-class weights by `z`.  If a missing edge is internal
to `E`, its endpoint weights have sum at most `y`, forcing
`a_1<=2y`, contrary to `8m>6m-8`.  If internal to `F`, it forces
`eta<=3z`, contrary to `eta-3z=2m+10`.  If it joins weights `e` and `f` across
`E,F`, then `e+f<=y`; meanwhile the other classes force
`e>=a_1-2y=2m+8` and `f>=eta-3z=2m+10`, again impossible.  Additional edge
deletions only strengthen these degree constraints.  This rules out only the
fixed layer totals/topology, not other `K_7`-free constructions.

