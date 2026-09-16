# Exact triage test and factorization route

Run `python3 evidence/triage_exact.py` from the project root. The script uses
Python integers and rational fractions, with no floating-point sign tests.
The output is `evidence/triage_exact.json`; results are replaced atomically after
each dimension. The defining double Stirling formula and the independent
face-vector conjugation B Q B^{-1} agree for every d=0,...,16. The d=0 case
is an auxiliary empty-complex convention, outside the source's requested range.
Boundary rows and the source's recurrence (21) agree throughout this range.

For d=1,...,8 every minor was enumerated with its row and column sets in
increasing order. Integer Bareiss elimination with pivot row swaps and exact
division assertions evaluated 66,186 minors in total, with zero negative minors.
The respective counts are 5, 19, 69, 251, 923, 3431, 12869, and 48619;
each equals C(2d+2,d+1)-1. The JSON records signs separately for every order.

For example,

```
H_3 = [[1, 0, 0, 0],
       [9, 8, 5, 3],
       [3, 5, 8, 9],
       [0, 0, 0, 1]].
```

For d=1,...,16 the script applies no-swap adjacent-row Neville elimination to
A=H_d^T and then to the transpose of its resulting upper-triangular matrix U.
It refuses a nonzero target with a zero denominator. A zero target is skipped,
including all forced boundary zeros. Both stages reconstruct their input
exactly by reversing the recorded row operations. The second residual is
checked to be diagonal. Every recorded multiplier is nonnegative and every
diagonal entry is positive for these 16 matrices.

To interpret the certificate: if the first-stage operations, in execution order,
are `row_i -= m row_(i-1)`, let E=I+m e_(i,i-1) be their inverses and let L
be the product of these E's in that same order. Then A=L U. Let K be the
corresponding product for the second stage, so U^T=K D. Consequently
`H_d^T=L D K^T`. Each E is a nonnegative unit bidiagonal matrix and is TN;
D is positive diagonal. Cauchy--Binet therefore explains why the recorded
factor identities certify TN of the individual tested matrices. The JSON
provides all rational multipliers and D, not only success flags.
This is finite exact evidence with reproducible certificates, not an
all-dimensional proof, independent referee acceptance, or novelty claim.

## One specific next test

Use the defining binomial sums to derive and determine the sign, for every
d>=3 and 2<=i<=d, of

```
Delta(d,i) = det H_d[{1,2},{i-1,i}].
```

This is the numerator of the next active Neville pivot, rather than an
arbitrary chosen minor family. Indeed direct summation gives, for 1<=j<=d,
`H_d(1,j)=(d+j) 2^(d-j-1)` (and H_d(1,0)=d(2^(d-1)-1)). To see it,
the s=0 terms use local coefficients ell_A(r,1)=r for r>=2 and the s=1
term supplies the missing j=1 boundary contribution. The binomial first-moment
identity then gives the displayed expression. Thus first-stage multipliers are
`m_(i,1)=(d+i)/(2(d+i-1))`, 2<=i<=d. After eliminating column 1 of H_d^T,
the entry in position (i,2) is Delta(d,i)/H_d(1,i-1).

A negative Delta would furnish an exact disproof; a uniform positive expression
would complete the next step toward a dimension-uniform factorization. Neither
outcome is asserted here. The proposed contribution remains a uniform structural
result or an exact negative minor, not a larger positive finite table.

Obstacles: the signs of general-order pivots and second-stage factors are
unproved in arbitrary d. The signed B Q B^{-1} identity alone is not a TN
factorization, and an interlacing criterion supplies at most order 2 even if
its antiprism premise were proved. No method-class impossibility is claimed.
