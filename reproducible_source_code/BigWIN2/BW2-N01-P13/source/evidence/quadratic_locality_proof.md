# A proposed computer-assisted proof of quadratic positivity

Job: `newwin-00001-p13-research-75edfb64efc5`.
Scope: the full frozen statement in `source.md`, interpreted in `problem.md`.
This is a proof dossier for a fresh referee, not an acceptance or manuscript.

Write z=t-1. For a square board B of size n, put

    C[a,n](B;t) = [x^a] H(B;x+1,t),  a=0,1,2,

where coefficient extraction refers to the unique polynomial residue. We propose
to prove C[2,n](B;t) has nonnegative coefficients for every n and B. The argument
reduces this infinite assertion to exact tests on all square boards of size at
most four. In particular, this reduction is stronger than testing n<=4 alone.
For the auxiliary empty board set H_0=1, so C[1,0]=C[2,0]=0.

## 1. Balanced restriction convolution and locality

For families f,g of functions of square boards, define

    (f*g)_n(B) = sum_{R,C subset [n], |R|=|C|}
                    f_|R|(B[R,C]) g_{n-|R|}(B[R^c,C^c]).

Rows and columns of restrictions retain their induced order. This is associative
and commutative: either parenthesization sums over the same ordered partitions
of rows and columns into matching block sizes. Its identity has value 1 at the
empty board and zero in positive sizes.

Let h_n(B;t)=per(J+z B), the classical hit polynomial; h_0=1. Its convolution
inverse is h^{-1}_n=(-1)^n h_n. Indeed, for every full permutation, selecting k
of its n row/column pairs yields binom(n,k) splittings. Thus the degree-n
coefficient of h*h^{-1} is h_n sum_k binom(n,k)(-1)^(n-k).

Call f local of order k if f=h*A for a family A supported in sizes <=k.
We allow coefficients in Q(z) for this definition. Its kernel A=h^{-1}*f is
unique. Consequently it can be computed recursively by

    A_n(B) = f_n(B) - sum_{j<n} sum_{|R|=|C|=j}
                          A_j(B[R,C]) h_{n-j}(B[R^c,C^c]).             (1)

Let E multiply a size-n function by n, and let L=z d/dz. Both are derivations
of convolution. We have Eh=h*U and Lh=h*V, with kernels supported at size one:

    U_1([b])=1+zb,       V_1([b])=zb,       b in {0,1}.

The first identity marks one of the n edges of a full permutation. The second
marks and differentiates one of its weights. Therefore, if f=h*A is local of
order k,

    Ef=h*(U*A+EA),       Lf=h*(V*A+LA)

are local of order at most k+1. Multiplication by a scalar in Q(z) does not
increase order. A polynomial of total degree d in the commuting operators E,L
raises locality by at most d. Scalar factors depending on z below are applied
after these polynomial operators; they are not commuted through L.

## 2. Locality of the transformed q-rook residues

Write M_i(B,x+1)=sum_{a=0}^2 R[a,i](B)x^a modulo x^3 and set

    F[a,n](B;z)=sum_i R[a,i](B)(n-i)! z^i.

We show F[a] is local of order at most 2a for a=0,1,2.

The exact-support diagonal action has the following established consequence
(Chen--Selover, equation (3.2)). A connected support component with r rows,
c columns and rank D contributes

    x^e O_D(G,x+1),       e=r+c-D-1 >= max(r,c)-1.

Ranks and exponents add over components. A component of defect zero is exactly
a single edge of rank one, with orbit polynomial 1. All other components have
defect at least one. Components with more than three rows or columns can be
discarded modulo x^3. For the remaining components the orbit counts are
polynomials, as stated and used in Remark 2.3 and Theorem 3.12 of that paper.

Fix a collection G of k nonedge components, including a possible rank for each.
Let r,c be its total numbers of row and column vertices, D its total rank, and
e=r+c-D-k its total defect. Its contribution to R[a,i] is a fixed integer
weight times the number of embeddings of G accompanied by i-D disjoint edges.
Here an embedding means an actual labelled support with ranks specified on its
components, counted once; it does not mean all isomorphisms from a labelled
representative, which would introduce an automorphism factor.
The weight is a coefficient in the product of the orbit polynomials. It is zero
unless e<=a. Since k<=e,

    s=r+c-D=e+k <= 2a.                                      (2)

The case with no nonedge components has r=c=D=0 and weight 1 only at a=0.

For a fixed embedding of G in B, its contribution to F[a,n], apart from its
constant weight, is

    z^D sum_j r_j(B outside the rows and columns of G)
                      (n-D-j)! z^j.                        (3)

Here r_j denotes an ordinary matching number. Choose any D of G's rows and
D of G's columns and delete them. On the remaining n-D rows and columns form
a weighted matrix W as follows: its entry is 1+z B_ij when both vertices are
outside G, and it is 1 otherwise. Then (3) equals z^D per(W), by the ordinary
rook expansion of a permanent. The retained r-D rows and c-D columns of G are
called dummy vertices. The deleted rows/columns need not be a matching of G;
they are only labels removed in this auxiliary permanent construction.

In a permutation contributing to per(W), let u be the number of edges joining
a dummy row to a dummy column. Form a patch by taking every vertex of G and
every outside vertex joined by the permutation to a dummy vertex. Its row and
column counts are both

    r+(c-D-u)=c+(r-D-u)=s-u <= s.                             (4)

Every permutation edge incident with a dummy vertex has weight 1. All remaining
edges form an unrestricted weighted permutation on the complementary rows and
columns, contributing their classical hit polynomial. The core embedding and
the partial permutation touching dummy vertices depend only on the board in
the patch. Hence (3), summed over core embeddings, is a convolution h*A with
A supported in sizes <=s. To make the construction invariant under arbitrary
row and column relabeling, one may average over all binom(r,D)binom(c,D)
choices of deleted vertices; each choice gives the same permanent value. The
resulting rational local functions still give the exact identity.

This proves the asserted locality by (2). In particular F[0]=h, F[1] has order
at most two, and F[2] has order at most four. Signed orbit coefficients do not
affect this locality argument.

## 3. Locality of the ambient hit weights

For integers n>=i>=0 set m=n-i, N=n(n-1)/2 and

    A(m)=m(m-1)/4,
    B(m)=m(m-1)(m-2)(9m+13)/288,
    I(i)=i(i-1)/2,
    J(i)=i(i-1)(i+1)/6,
    K(i)=i(i-1)(i-2)(3i-1)/24,
    a(n,i)=N+A(m),
    b(n,i)=N(N-1)/2+N A(m)+B(m).

Straight multiplication of the finite products gives

    [m]!_(1+x) = m! (1+A(m)x+B(m)x^2) modulo x^3,

and the coefficient of x^0,x^1,x^2, respectively, in

    (1+x)^N [m]!_(1+x) product_{j=0}^{i-1}(t(1+x)^(-j)-1)

is

    m! z^i,
    m! (a(n,i)z^i - t I(i)z^(i-1)),
    m! (b(n,i)z^i + t(J(i)-a(n,i)I(i))z^(i-1)
                              + t^2 K(i)z^(i-2)).           (5)

Terms with negative powers have zero multiplying polynomials at the relevant
small values of i; equations can also be read in Q(z). These identities use
sum j=i(i-1)/2, sum j(j+1)/2=J(i), and sum_{j<k}jk=K(i).

Since L acts on z^i with eigenvalue i, the original hit transform and (5) give

    C[2] = F[2] + (a(E,L)-(t/z)I(L)) F[1]
         + (b(E,L)+(t/z)(J(L)-a(E,L)I(L))
                                      +(t^2/z^2)K(L)) h.   (6)

The first operator has total degree at most two in E,L; the second at most
four. By Sections 1--2, every term in (6) is local of order at most four.
Thus the quadratic kernel defined by (1) vanishes identically for every n>4,
every board, and every t. This is an algebraic statement, not extrapolation
from finite testing.
Although the locality proof used Q(z), the unique kernels in (1) are integer
polynomials in t, because C[2] and h are. Thus no singular specialization at
z=0 is needed, and the conclusion holds as a polynomial identity.

## 4. The finite certificate and the conclusion

For a=2 compute (1) on all 2^(n^2) labelled boards at n=1,2,3,4. No symmetry
quotient is used for boards. `research_n4.py` computes all exact residues using
the connected orbit table and a subset zeta transform. `research_local_kernels.py`
then performs the recursion (1). The resulting finite observations are:

| n | boards | coefficients tested | minimum | maximum | negative |
|---|---:|---:|---:|---:|---:|
| 1 | 2 | 4 | 0 | 0 | 0 |
| 2 | 16 | 48 | 0 | 1 | 0 |
| 3 | 512 | 2048 | 0 | 41 | 0 |
| 4 | 65536 | 327680 | 0 | 162 | 0 |

`research_local_kernel_results.json` reports these checks; the entire kernel
table is `research_local_kernel_tables.json.gz`. The orbit reconstruction has
the degree and polynomiality justification in `triage_reduction.md`: spanning
tree normalization leaves beta=|E|-r-c+1<=4 nonzero parameters, so each orbit
polynomial has degree at most beta. beta+1 exact field counts determine it;
additional fields can independently check the data. The complete connected
graph enumeration, normalization, rank counting and transform are reproducible
from the listed scripts. The board bit index is i*n+j with zero-based indices.

There is a second complete evaluation in `research_verify.py --exhaustive-local`.
It uses connected-core embeddings with matching dynamic programming, the
explicit weight formula (5), and the direct inverse h^{-1}, rather than the
all-support zeta transform and recursive kernel extraction. It agrees on all
329,780 quadratic coefficients and all 329,780 kernel coefficients at n<=4;
see `research_independent_n4_results.json`. The orbit table was also reconstructed
separately using ranks from minors, a BFS tree, Newton interpolation, and exact
fields of sizes 2,3,4,5,7,8; see `research_verification_results.json`. The
extension fields use u^2+u+1 and u^3+u+1. Finally, a different connected-core
evaluator agrees with (7) on the recorded extra boards of sizes 5--8, including
the Fano board and its complement. These are same-worker algorithm checks;
they are not a fresh mathematical referee audit or the proof of locality.

Since C[2]=h*K[2] and K[2] is zero above size four, (1) is equivalently the
universal identity

    C[2,n](B;t)=sum_{k=2}^{min(4,n)} sum_{|R|=|C|=k}
                  K[2,k](B[R,C];t) h_{n-k}(B[R^c,C^c];t).  (7)

The finite certificate makes each K[2,k] coefficientwise nonnegative, while
each h is a weighted-permutation hit polynomial and is coefficientwise
nonnegative. Therefore every coefficient of C[2,n](B;t) is nonnegative, which
is precisely the original quadratic-residue claim.

## Dependencies and verification boundary

External: Chen--Selover equation (3.2), the small-board orbit polynomiality
stated in Remark 2.3 / used in Theorem 3.12, and Corollary 3.13 for residue
existence. All are in the copied primary journal text in `evidence/external/`.
The finite certificate depends on exact graph/rank enumeration and polynomial
reconstruction, not numerical fitting or all-board polynomiality in general.
The locality argument and finite positivity both require fresh referee review.
No known mathematical gap is being deliberately left in (1)--(7); the most
critical review point is the dummy-permutation decomposition (3)--(4).
