# Reproducing the quadratic certificate

All commands run from the project root with Python 3 and its standard library.
No external numerical library, floating-point interpolation, hidden worker,
fresh model context, or formal proof assistant was used in this research pass.

1. `python3 evidence/triage_orbits.py` reconstructs the 28 connected orbit
   classes and reproduces the inherited n<=3 checks. The reconstruction uses
   the published small-board polynomiality and the spanning-tree degree bound;
   see `triage_reduction.md` and Section 4 of `quadratic_locality_proof.md`.
2. `python3 evidence/research_n4.py` enumerates every labelled 4x4 support and
   board. Components with more than three row or column vertices are discarded
   before canonicalization. Component products give normalized rank residues;
   a subset zeta transform includes every support contained in each board.
   The exact hit transform gives the three coefficients for every hit index.
3. `python3 evidence/research_local_kernels.py` loads that data, generates sizes
   1--3 if absent, and computes the unique kernels by recursive convolution
   subtraction. It records the full integer tables and coefficient ranges.
4. `python3 evidence/research_verify.py` verifies the complete orbit graph
   census, uses determinant minors and a different spanning tree to count ranks
   over fields of sizes 2,3,4,5,7,8, and reconstructs the same polynomials using
   Newton divided differences. It also compares the proposed locality identity
   to an evaluation by connected cores and matching DP on the listed test
   cases through size eight. These larger cases are supplementary checks; the
   infinite reduction is proved algebraically in the proof dossier.
5. `python3 evidence/research_verify.py --exhaustive-local` independently
   evaluates every board of sizes 1--4 using connected cores and matching DP,
   the explicit quadratic weight formula, and the direct alternating inverse
   of the classical hit family. It compares all quadratic values and all
   kernels to the first calculation. This takes about a minute in the current
   environment. It is a different algorithm run by the same worker, not a fresh
   referee audit.

The finite certificate covers 66,066 distinct boards and 329,780 board/index
pairs across n=1,2,3,4. Both algorithms agree on every quadratic value and
kernel. The kernel coefficient ranges for n=1,2,3,4 are respectively [0,0],
[0,1], [0,41], [0,162]; no negative coefficient occurs. The recurrence and
locality theorem imply that these are all the nonzero kernel sizes needed.

`research_nN_residues.bin.gz`, N=1,2,3,4, contains a gzip-compressed binary stream
of signed little-endian int64 triples (c0,c1,c2). Board masks increase from 0
through 2^(N*N)-1; within each board d increases from 0 through N. A cell (i,j)
has bit i*N+j, with zero-based indices. The accompanying JSON gives the digest
of the uncompressed stream and all coverage checks.

`research_local_kernel_tables.json.gz` is compressed JSON. The first key is
the coefficient order (`"1"` or `"2"`); the next is the board size. Each entry
is a list indexed by board mask, whose value is the list of coefficients in t
in increasing order. Size-zero entries for orders one and two are [0].

The second evaluator's JSON also gives separate SHA256 digests for its
quadratic and kernel coefficient streams, each with one signed little-endian
int64 per board/index pair. These digests bind data, not mathematical truth.
The two finite algorithms share the orbit polynomial table, which the
determinant/extension-field path separately reconstructs. They both depend
on the cited polynomiality theorem; finite field samples alone are not used
to establish it. All mathematical acceptance remains the fresh referee's task.
