# A precise obstruction to one suffix-induction method

Research job: primary-20260914-bigdescent-logconcavity-research-ff87ce2dd87c.
Status: proved-obstruction to the method class below; no claim about failure of the original conjecture.

Let T(A,B,C)=(A+tB+tC,A,tB+C), and let R_c substitute ct for t simultaneously in all three polynomials, for a positive real c. The actual state at n=2 is (1+t,1,1).

There is no set K of triples of nonnegative-coefficient polynomials satisfying all four properties:
1. K contains (1+t,1,1).
2. K is closed under every R_c, c>0.
3. K is closed under T.
4. Every triple in K has log-concave C coefficients.

Proof. By the first two properties K contains (1+ct,1,1). Two applications of T give C=1+2t+ct^2. Its determinant at k=1 is 4-c, negative for c>4. This contradicts property 4. The rational/integer choice c=5 suffices.

In particular, a cone described solely by inequalities each homogeneous in total coefficient-index weight is closed under R_c; such a cone cannot prove all three states log-concave by one-step preservation while containing the actual states. This includes ordinary log-concavity, strong synchronization, and symmetric mixed log-concavity inequalities, also with fixed relative index shifts, if each individual inequality is homogeneous in that weight. The obstruction does not cover inequalities combining different index weights, n-dependent arguments not invariant under R_c, temporal identities, or an induction that proves only B+C log-concave without requiring C log-concave.

At n=4 in the actual orbit (c=1), A=(1,5,2), B=(1,3), C=(1,2,1). Strong synchronization of C and tB already fails at k=1: C_1 B_0-C_0 B_1=2-3=-1. Its symmetric mixed determinant is nevertheless 1. Thus replacing weak synchronization by this particular stronger hypothesis is invalid even on the actual orbit.
