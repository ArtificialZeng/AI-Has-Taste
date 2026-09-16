# Conditional Schur positivity with four free event positions

Job: primary-20260914-bigdescent-logconcavity-research-5c6b908e3ed6.
Research theorem with a complete matrix reduction and two deterministic
certificate implementations. It has not received a fresh mathematical referee.

## Exact statement

For n>=1 let a_n(S) count binary words w of length n ending in 1 whose event
set E(w) is exactly S. An event position is the ending position of a factor
10 or 011, and hence belongs to {2,...,n}. Unattainable sets have count zero.
Let J be any subset of {2,...,n} of size m<=4, and let S be any subset of its
complement. Define

    H_(S,J)(x,y) = sum_(T subset J) a_n(S union T)
                     a_n(S union (J minus T)) x^|T| y^(m-|T|).

Then H_(S,J) is Schur-positive in two variables. Equivalently, with

    h_j = sum_(T subset J, |T|=j) a_n(S union T)
                                      a_n(S union (J minus T)),

we have h_j>=h_(j-1) for 1<=j<=floor(m/2); symmetry gives h_j=h_(m-j).
All other event indicators are fixed: those in S are present, those outside
S union J are absent. The statement includes zero-count configurations and
has no bound on n, the spacing of J, or |S|.

In the full pair-profile notation, all profiles with at most four entries
equal to 1 are therefore Schur-positive: their polynomial is
(xy)^|S| H_(S,J). This is an infinite family at unbounded total degree.

## A matrix theorem sufficient for the statement

Use column vectors and the following matrices and boundary rays:

    P = ((1,0,0),(1,0,0),(0,0,1)),
    Q = ((0,1,1),(0,0,0),(0,1,0)),
    O = ((1,0,0),(0,1,0),(1,0,1),(0,1,1)),
    I = ((1,0,0),(1,1,0),(1,0,1),(1,1,1)).

Write cone(O) for nonnegative linear combinations of the output row rays,
and cone(I) for nonnegative linear combinations of the input column rays.
For any l in cone(O), r in cone(I), m<=4, and arbitrary products M_i of P,Q
(empty products allowed), put

    A_T = l U_1 M_1 U_2 ... M_(m-1) U_m r,

where U_i=Q if i belongs to T and P otherwise. For m=0 put A_empty=l r.
The matrix theorem is that sum_T A_T A_(complement T) x^|T| y^(m-|T|)
is Schur-positive.

To connect this to words, suffix states are A=ending 0, B=ending 01,
C=ending 1 but not 01. Appending an event-free letter acts by P and
appending a letter creating an event acts by Q. The initial vector is
v=(1,0,1)^T and the acceptance row is u^T=(0,1,1). Therefore the count of
an exact event set is u^T U_n ... U_2 v. Splitting this product at the
positions in J gives the displayed A_T, with the order of J reversed to
match matrix multiplication. Cardinalities and complements do not depend
on this reversal.

The cones are invariant under the required multiplications. Their exact
descriptions are

    cone(O) = {(a,b,c): a,b,c>=0 and c<=a+b},
    cone(I) = {(a,b,c)^T: a,b,c>=0 and b<=a, c<=a}.

For the first description choose c=c1+c2 with 0<=c1<=a, 0<=c2<=b,
then use (a-c1)o0+(b-c2)o1+c1 o2+c2 o3. For the second choose
max(0,b+c-a)<=d<=min(b,c) and use
(a-b-c+d)i0+(b-d)i1+(c-d)i2+d i3. These formulas also prove that
the inequalities describe the listed cones exactly. The maps are

    (a,b,c)P=(a+b,0,c),  (a,b,c)Q=(0,a+c,a),
    P(a,b,c)^T=(a,a,c)^T, Q(a,b,c)^T=(b+c,0,b)^T.

They preserve the displayed inequalities. In particular, the exterior
products give permitted l and r since u^T=o3 and v=i2.

## Exhausting all gap words

Direct multiplication gives P^2=P and

    Q^2 = e0 e1^T,
    e0=(1,0,0)^T in cone(I), e1^T=(0,1,0) in cone(O).

First delete repeated P's from each gap word. If a gap contains QQ, write
M=A Q^2 B=(A e0)(e1^T B)=a b^T. Its factors belong to cone(I) and cone(O)
by invariance, even when one is zero. Every remaining nonempty gap word
alternates P and Q. The identities

    PQPQP=PQP+P, QPQPQ=QPQ+Q,
    (PQ)^3=(PQ)^2+PQ, (QP)^3=(QP)^2+QP

show, by their Fibonacci recurrence and initial two words, that it belongs
to one of four separate nonnegative families. Including the empty word,
the five families are

    cone(Id), cone(P,PQP), cone(Q,QPQ),
    cone(PQ,(PQ)^2), cone(QP,(QP)^2).               (1)

These are sufficient supersets of the alternating words; the families are
kept separate, and different gaps may use different families.

If a gap M_i=a b^T has rank one as above, then A_T factors into a left and
a right count on disjoint groups of selected positions. Consequently its
pair polynomial is the product of the corresponding two pair polynomials,
with valid new boundaries a and b^T. Both groups have fewer selected
positions. For m=0 the pair polynomial is (l r)^2; for m=1 it is
(l P r)(l Q r)(x+y). Both are Schur-positive. Strong induction on m handles
every gap containing QQ once the five-family cases in (1) are certified.

For completeness, products preserve two-variable Schur positivity because

    s_(a,b) s_(c,d)
      = sum_(i=0)^min(a-b,c-d) s_(a+c-i,b+d+i)

for a>=b, c>=d. This identity follows by multiplying the finite geometric
sums s_(a,b)=(xy)^b sum_(j=0)^(a-b) x^j y^(a-b-j).

## The finite algebraic certificate

Independently expand l and r in their four rays and each gap in its own
one- or two-generator family in (1). Every A_T is multilinear in these
m+1 parameter groups. Every h_j, and hence every Schur coefficient
delta_j=h_j-h_(j-1) (h_-1=0), has degree two in each group.

The script multi_singleton_certificate.py multiplies the exact integer
coefficient tables of A_T and A_(complement T). It lists every quadratic
parameter monomial, including zeros, in the lexicographic Cartesian product
of unordered index pairs for output, input, gap1, ..., gap_(m-1).
For a gap with d generators there are d(d+1)/2 quadratic monomials.
Summing over its five families gives 1+4*3=13 possibilities. Thus complete
coverage for a fixed m and every Schur row has exactly

    (floor(m/2)+1)*10*10*13^(m-1)

coefficient positions, independently of which coefficients are nonzero.
The serialized certificate contains:

| m | gap-family combinations | all coefficient positions | negative |
|---|---:|---:|---:|
| 2 | 5 | 2,600 | 0 |
| 3 | 25 | 33,800 | 0 |
| 4 | 125 | 659,100 | 0 |

Every listed coefficient is an integer >=0. This proves each delta_j is
nonnegative for all nonnegative real parameters, rather than just testing
sample parameter values. Together with the complete gap reduction and
rank-one induction, it proves the matrix theorem and the word theorem.

The separate implementation pass3_audit.py imports none of the generating
script. It extracts quadratic parameters directly from tensor products:
for a distinct parameter pair (a,b), the coefficient of M tensor M is
M_a tensor M_b+M_b tensor M_a; for a repeated pair it is M_a tensor M_a.
It multiplies these 9-state matrices between
R=x Q tensor P+y P tensor Q and evaluates the polarized boundary tensors.
Arbitrary-precision integer operations match all 695,500 coefficients,
including symmetry and zeros. It independently checks cone preservation
and the explicit rank-one factorization. Direct binary-word enumeration
also checks all 72,447 configurations with <=4 free sites through n=11,
including 152,573 Schur coefficient positions. The finite word check is a
check of interpretation, not the proof of unbounded n.

## Consequences and boundaries

For fixed S and J with |J|<=4, put

    G(t;z)=sum_(T subset J) a_n(S union T) t^|T| product_(i in T) z_i
           =sum_k g_k(z)t^k.

Then every g_k(z)^2-g_(k-1)(z)g_(k+1)(z) is coefficientwise nonnegative.
Indeed, each occurring monomial in this difference has exponents 0,1,2;
fix its common-event positions (exponent 2) in both words and regard its
singly occupied positions (exponent 1) as the new J. Their number is <=4,
and the requested coefficient is the middle Schur difference of the
corresponding H, multiplied by no further negative factor. This also proves
ordinary LC after any nonnegative assignment of the z_i. If no word
satisfies the fixed outside indicators, all relevant counts are zero;
the argument never divides by the probability of a conditioning event.

The same proof covers arbitrary m when rank-one gap cuts split the selected
positions into components of size at most four: factor at all such cuts
and apply the theorem to each component. This gives Schur-positive profiles
at unbounded singleton count as well as unbounded common-event count.

For m=2 the inequality reads a_empty a_12<=2 a_1 a_2, and the factor 2
is sharp. At n=4, S=empty, J={2,4}, the four counts are (2,1,1,1), from
{0001,1111}, {1001}, {0011}, {1011}, respectively. Thus the binomially
normalized antipodal-pairs inequality and ordinary conditional negative
correlation fail on this model. Neither is used in the proof.

The three-position extension is not a consequence of just imposing the
sharp two-position bound on every face of a general Boolean weight.
For example, on subsets of {1,2,3}, give the empty and full sets weight 2
and all other sets weight 1. On each of its six two-dimensional faces,
AD=2BC; but its three-position pair coefficients are (4,3,3,4), giving
Schur coefficient -1. This exact generic-weight counterexample is also
checked in pass3_audit.py. It lies outside the word model, and clarifies
why additional matrix structure is needed for the new extension.

The original problem includes all 21 source pattern families at every k;
it is unresolved here. Even the unrestricted exceptional-class polynomial
allows arbitrarily many free positions without rank-one cuts, and is not
settled by this theorem. The four-position cutoff is a proved range, not
a claimed optimal cutoff. No all-m polynomial certificate or preservation
theorem is asserted.

Known mathematical gaps in the stated <=4 theorem: none identified.
Fresh referee and contribution/novelty review remain outstanding. The
associated certificate must be available if this computational proof is
submitted for review; a successful audit JSON alone is not its proof.
