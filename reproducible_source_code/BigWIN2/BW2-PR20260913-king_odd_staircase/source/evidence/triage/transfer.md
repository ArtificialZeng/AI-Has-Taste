# Exact reduction and corrected next test

This is a triage derivation, not an accepted contribution or a claim of novelty.
Write D_k=D^k_{r,r} and B_k(j)=G(D_k[0,j]), 0<=j<r. The shape is
self-conjugate, and exchanging rows and columns preserves all three moves.
Consequently G(D_k[i,0])=B_k(i).

Directly deleting complete blocks gives D_k[r,0]=D_k[0,r]=D_{k-1} for
k>=2, and D_k[r,r]=D_{k-2} for k>=3. At k=1 these destinations are all
empty; at k=2 only the diagonal destination is empty. These are identities
of partitions, not single legal King moves. For example D_2=( (2r)^r,r^r ).

To obtain the first r-by-r square of SG values for k>=2, prescribe its south
edge A(r,j)=B_{k-1}(j) and east edge A(i,r)=B_{k-1}(i), for i,j<r.
The southeast corner A(r,r) is B_{k-2}(0) when k>=3, and absent when k=2.
For k=1 all these external boundary cells are absent. Fill the square
backwards by A(i,j)=mex{A(i+1,j),A(i,j+1),A(i+1,j+1)}, omitting absent
neighbors. Then B_k(j)=A(0,j). Each prescribed cell corresponds to exactly
the named subpartition; composition of deletions proves this reduction.
Every interior cell exists, and all successors lie inside the square or on
the prescribed edges. Backward induction therefore proves the transfer.

For fixed r, (B_k,B_{k-1}(0)) is a deterministic state for k>=2 with at most
4^(r+1) possibilities. This elementary finite-state bound only ensures
eventual periodicity for each fixed r. It does not establish the proposed
root period r+2 or any uniform formula.

The first finite test is `boundary-test.py` / `.json`: 108 boundary words
agree with independently filled full boards, and 90 individual boundary
values agree with a recursive partition-tuple evaluator. All empty options
are excluded. No floating point is used. The naive boundary period r+2 is
false: r=3 has B_1=(0,3,0) and B_6=(0,2,0). This is a counterexample to
that stronger boundary assertion only, not to the original conjecture.

## Frozen replacement ansatz (unproved)

Let r be positive odd, p=r+2, t=1+((k-1) mod p),
h=floor((k-1)/p) mod 2, a=3-h, b=2+h. For 0<=j<r define W(r,k,j):

- If j=0 and t=p, set W=2.
- Otherwise, if j<p-t, set W=(t+1) mod 2 for even j, and W=a for odd j.
- Otherwise set W=b for even j, and W=t mod 2 for odd j.

The hypothesis is B_k(j)=W(r,k,j). The special root rule in the first
case matters in the second phase: simply swapping 2 and 3 everywhere is
incorrect. This ansatz has period dividing 2(r+2); its root has exactly
the originally conjectured values. `phase-holdout.py` freezes the formula
before evaluation on new r=33,35,47,63. Results are recorded separately in
`phase-holdout.json`; finite success does not prove the hypothesis.

Next decisive test: derive a piecewise formula for the square interior
produced from these W boundary words, and prove the mex identities uniformly
for every odd r, including phase transitions t=p to t=1 and the k=2 absent
corner. Failure should yield an exact boundary entry and a corrected target.
The period-r+2 boundary family from the intake lead must not be retried.
