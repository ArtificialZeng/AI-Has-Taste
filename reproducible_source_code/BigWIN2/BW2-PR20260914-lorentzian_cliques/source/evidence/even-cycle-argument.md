# Structural lead: a fixed target for every even cycle

Triage derivation, not independently refereed or novelty-certified.
Job: primary-20260914-lorentzian-cliques-triage-a33a3dbf435e.

For every integer k>=2 let F=C_(2k) and

    A = [[0,1,1],[1,0,1],[1,1,1]].

This is K3 with a loop on spin 3. Its eigenvalues are -1 and 1±sqrt(2),
so it is admissible. Let f=Z_(F,A), and beta=(k-1,k-1,0).
Direct counting gives

    Hessian(partial^beta f) = 2(k!)^2 M_k,
    M_k = [[0,1,1],[1,0,1],[1,1,6(k-1)/k]].

The vector (1,-1,0) has eigenvalue -1. The determinant is
2-6(k-1)/k = -4+6/k < 0, and the trace is positive. Hence M_k has two
positive eigenvalues and one negative eigenvalue. The required derivative
condition fails, supporting the original conjecture on all even cycles.

## Counting justification

Write c_(a,b,c) for the ordinary coefficient of x1^a x2^b x3^c.
Since the independence number of C_(2k) is k, c_(k+1,k-1,0)=0 and its
color-reversal counterpart is zero. There are two proper 2-colorings, so
c_(k,k,0)=2. The only independent k-sets of an even cycle are its two
bipartition classes. Choosing one class for color 1 and one of the remaining
k vertices for color 3 gives c_(k,k-1,1)=2k; reverse colors for its counterpart.

To count c_(k-1,k-1,2), choose the two vertices colored 3. For adjacent pairs,
there are 2k choices, and the remaining even path has two balanced colorings:
contribution 4k. For nonadjacent opposite-parity pairs there are k^2-2k
choices. The remaining two paths both have even order, giving four balanced
colorings: contribution 4(k^2-2k). For same-parity pairs there are k(k-1)
choices. Both paths have odd order; exactly two of the four choices of their
color orientations balance the total colors: contribution 2k(k-1).
The sum is 6k(k-1). These cases include k=2.

For each Hessian entry the full derivative multi-index is beta+e_i+e_j;
multiply the corresponding ordinary coefficient by the product of its
coordinate factorials. This gives exactly the displayed Hessian.

`cycles.py` checks these counts and Hessians by labeled assignment enumeration
for k=2,3,4,5. That finite check is separate from the all-k counting argument.

## Bounded continuation

A larger structural question is suggested. If F is connected bipartite on
2k vertices and its only maximum independent sets are its two size-k
bipartition classes, the same derivative has the displayed first two rows
and columns, while M_33=c_(k-1,k-1,2)/k^2. Thus this derivative fails whenever
that coefficient exceeds 2k^2. Derive a graph-theoretic formula using the
components of F after deletion of two vertices; test whether a natural
separator hypothesis ensures strict inequality. The complete bipartite graph
K_(k,k) has coefficient exactly 2k^2 and is a necessary boundary case, so
this derivative alone must not be asserted to settle all bipartite graphs.

Novelty remains provisional. The inspected source papers do not state this
even-cycle certificate; targeted searches found no inspected equivalent.
An independent proof and literature audit is required before any candidate.
