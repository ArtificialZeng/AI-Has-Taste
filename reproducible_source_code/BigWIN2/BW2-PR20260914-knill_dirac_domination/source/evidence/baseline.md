# Elementary checks and their limits

These are direct arguments for triage, not novel-result claims. Matrices and
quantifiers are those in `problem.md`.

1. **Orientation.** Changing a face orientation multiplies its basis vector
by a sign. For the diagonal sign matrix (Q), (d'=QdQ) and (D'=QDQ).
The combinatorial intersection matrix does not depend on orientation.

2. **Endpoint (k=1), including disconnected complexes.** Entrywise,
(|D|+I\le L). For any real unit vector (u), the vector (v=|u|) is also
unit, and
\[
u^{\mathsf T}Du\le v^{\mathsf T}|D|v
\le v^{\mathsf T}(L-I)v\le\lambda_1(L)-1.
\]
Maximizing over (u) proves (S_1(L)\ge S_1(D)+1) for nonempty (G).
There is no entrywise analogue of this argument for higher-rank maximizing
projections: taking absolute values need not preserve their constraints.

3. **Trace and zero dimension.** The diagonals give
(S_n(L)-S_n(D)=\operatorname{tr}L-\operatorname{tr}D=n).
If every face is a singleton, (L=I,D=0), so every gap equals (k).

4. **Spectral symmetry.** For the diagonal grading
(P_{x,x}=(-1)^{|x|-1}), codimension-one incidence gives (PDP=-D).
Hence the spectrum of (D) is symmetric about zero. This does not force
the requested comparison with (L).

5. **Disjoint unions.** If (G=G_1\sqcup G_2) on disjoint vertex sets,
both matrices are direct sums. For symmetric matrices,
\[
S_k(A\oplus B)=\max_{i+j=k}\{S_i(A)+S_j(B)\},
\]
where (0\le i\le\dim A,0\le j\le\dim B). Thus if the conjecture holds
on both components it holds on their union, by using a maximizing allocation
for the Dirac sum. Any counterexample therefore has a connected counterexample
component. This reduction leaves the frozen universal assertion unchanged.

6. **Routine bounds leave a gap.** The variational formula
(S_k(A)=\max_{P=P^{\mathsf T}=P^2,\,\operatorname{tr}P=k}\operatorname{tr}(PA))
gives (S_k(L)\ge k) by choosing a coordinate projection. Fan's inequality
only yields (S_k(D)\le S_k(L)+S_k(D-L)); controlling its last term requires
extra information. Neither this bound nor the separate interlacing of the
two families of matrices proves cross-family domination. This diagnoses only
these direct applications, not an impossibility theorem for the method class.

## Reproducible tiny tests

Command from project root:
`OPENBLAS_NUM_THREADS=1 python3 evidence/tiny_complexes.py`.

For a fixed universe of (m\le4) vertices the code enumerates all subsets of
the (2^m-1) possible nonempty faces and retains exactly the nonempty families
closed under nonempty subsets. Thus it covers complexes using fewer than (m)
vertices as well, with labeled embeddings counted separately. Counts are
18 for (m=3) and 166 for (m=4); the empty complex is excluded as vacuous.
Every incidence matrix satisfies (d^2=0) exactly, grading symmetry, and
characteristic-polynomial invariance under a deterministic orientation change.

For (m=3), characteristic polynomials are computed over the integers and
SymPy isolates every real root in a rational interval of width at most
(10^{-12}). Multiplicities are expanded before ordering. Subtracting upper
Dirac partial-sum bounds from lower connection partial-sum bounds is strictly
positive for every (k) in every case. This is an exact finite computation;
the saved polynomials and intervals are inspectable certificates, not a
separate independent referee pass.

For (m=4) and the 29 structured cases, `numpy.linalg.eigvalsh` supplies
floating-point evidence only. Structured cases are skeleton dimensions
(1\le q\le\min(m-1,3)) for (3\le m\le6), and paths, cycles, and stars
for (3\le m\le8). The largest matrix has 56 faces. The minimum observed
gap is (0.9999999999999996), consistent with 1 at roundoff; none is less
than (-10^{-9}). Repeated or isomorphic examples across tiers are not
claimed as distinct isomorphism classes. No negative candidate needed an
exact negative-gap certificate. No random search was performed.
