# Precise interpreted statement

The frozen statement is `source.md`, preserved byte for byte. No correction or
parameter restriction is proposed. Here P_n denotes the underlying grid poset,
not the paper's separate notation for a poset of lattice points.

For each integer n>=1 let

    E_n = ({1,...,n} x {1,2}) minus {(n,2)},
    (i,r) <= (j,s) iff i<=j and r<=s.

A lower ideal I is a subset of E_n such that v in I and u<=v imply u in I.
The empty ideal and E_n itself are included. Define

    Q_n = {x in R^(E_n): x_v>=0 for every v,
           sum_(v in I) x_v <= |I| for every lower ideal I},
    supp(x) = {v in E_n: x_v != 0},
    H_n(t) = sum_(x in Q_n intersect Z^(E_n)) t^|supp(x)|.

All lattice points have weight one before the support marker is attached.
The polynomial counts the undilated polytope; it is not an Ehrhart numerator.
The full-ideal constraint bounds the total by 2n-1, so the sum is finite.
For each integer r>=0 define

    A_r(t) = sum_(j=0)^r binom(r,j) binom(r+1,j) t^j/(j+1),
    B_r(t) = sum_(j=0)^r binom(r,j)^2 t^j.

The target is the identity in Z[t]

    for every integer n>=1, H_n(t) = A_(n-1)(t) B_n(t).

Equivalently, for every such n and every 0<=k<=2n-1, the number of lattice
points with support size k equals

    sum_(j=0)^(n-1) binom(n-1,j) binom(n,j) binom(n,k-j)^2/(j+1),

with binomial coefficients outside their usual range equal to zero.
There are no extra assumptions on supports, coordinate sums, or n.

## Exact inequalities and boundary checks

Put a_i=x_(i,1), 1<=i<=n, and b_j=x_(j,2), 1<=j<=n-1.
Every ideal consists of a lower prefix of length i and an upper prefix of
length j, uniquely, where 0<=i<=n and 0<=j<=min(i,n-1). Indeed each row
must be a prefix, and inclusion of (j,2) forces (j,1). Conversely these
conditions make the subset a lower ideal. Thus the full constraint family is

    a_i,b_j>=0,
    sum_(k=1)^i a_k + sum_(k=1)^j b_k <= i+j
    for 0<=i<=n, 0<=j<=min(i,n-1).

For n=1, Q_1=[0,1], H_1=1+t, A_0=1 and B_1=1+t.
For all n the constant and degree-(2n-1) coefficients are one: the zero
vector is unique, and full support together with total<=2n-1 forces all ones.
The coefficient of t is n(n+1)/2+n(n-1)=n(3n-1)/2: a single nonzero
coordinate is bounded by its principal-ideal cardinality, i or 2j.
These checks agree with the proposed factors but do not prove the identity.

## Prior result, proposed contribution, verification route

Source status: the primary paper proposes this identity, as checked again
in `literature/research-screen.md`. A complete local proof candidate now
exists and awaits fresh mathematical review. No accepted resolution is
asserted at this stage. The live primary paper arXiv:2605.26916, Section
9.3 final paragraph, proposes exactly this factorization; its Section 5
and Section 9 definitions match the above normalization.

Nearest inspected established comparison: arXiv:2510.23903, Examples
2.3–2.4, gives B_r for total-bounded nonnegative vectors and A_r for
chain-prefix-bounded vectors; Theorem 3.1 and Remark 3.2 supply related
lattice-path/Eulerian descriptions. These describe the factors separately,
without a support-preserving decomposition of this coupled grid system.

Proposed delta: the complete uniform coefficient identity, with no change
to its original quantifiers or statistic. The proof candidate is
`evidence/research-proof.md`. It derives the half-step operators A and B
after x=1+u, y=1+v, proves [B,A]=t E for the origin projection E, and
evaluates the terminal moment by a finite-rank trace and coefficient
extraction. For S(u)=u+c+t/u and C_(n,k)=[u^k]S(u)^n it proves

    epsilon A(BA)^(n-1)1
      = sum_(k=1)^n k t^k C_(n+1,k) C_(n,k)/(n(n+1)t)
      = C_(n,0) C_(n,1)/n.

Specializing c=1+t gives B_n(t) and n A_(n-1)(t) as the two coefficients.
The apparent division by t is removable in the polynomial identity.

Available verifiers: the original two-slack transfer remains in
`evidence/triage-transfer.py` and `.md`. The new self-contained
`evidence/research-verifier.py` and `.json` compare the entire state
polynomial after the basis change and the generic (c,t) coefficient
formula for n=1..10. They independently enumerate every ambient vector
with total<=2n-1 for n=1..5, and check finite-rank traces for n=1..5 at
four exact parameter pairs, including zeros and negative weights. All
checks pass. These are finite same-context checks of the written proof,
not independent mathematical acceptance.

One next test: a fresh referee should audit the full proof, focusing on
the finite-support justification and sign of the boundary trace in
Section 2 and its connection to the rank-one logarithmic identity and
Lagrange extraction in Section 3. No mathematical gap is currently known.
