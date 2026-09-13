# Complete proof of the frozen `n=3` claim

Let

\[
q=1-p,\qquad b(p)=-p\log p-q\log q,\qquad R=pq,
\]

where `b` is extended continuously to the endpoints.  We prove that the
entropy in `source.md` is concave for every pair of positive integers
`(u,v)`.

## Exhaustive collision reduction

The additive shift by 1 is irrelevant.  A support collision for the weights
`{1,u,v}` is an equality of two distinct subset sums.  Cancelling their common
terms leaves two disjoint, nonempty subsets with equal sums.  Because there
are only three positive weights, this is either equality of two weights or
equality of one weight with the sum of the other two.  Hence a collision is
possible exactly when

\[
u=1,\quad v=1,\quad u=v,\quad v=u+1,\quad\text{or}\quad u=v+1;
\]

the remaining formal relation `1=u+v` is impossible for positive `u,v`.
Resolving the intersections of these five relations gives the following
exhaustive table.  Put

\[
A=p^3,\quad B=p^2q=pR,\quad C=pq^2=qR,\quad D=q^3.
\]

| case | positive-integer parameters | nonzero atom probabilities | entropy |
|---|---|---|---|
| 1 | `(u,v)=(1,1)` | `A,3B,3C,D` | `3b-3R log 3` |
| 2 | `(u,v)=(1,2)` or `(2,1)` | `A,2B,R,2C,D` | `3b-Rb-2R log 2` |
| 3 | `u=1,v>=3`; `v=1,u>=3`; or `u=v>=2` | `A,B,2B,C,2C,D` | `3b-2R log 2` |
| 4 | `v=u+1,u>=2`; or `u=v+1,v>=2` | `A,B,B,R,C,C,D` | `3b-Rb` |
| 5 | every remaining pair | `A,B,B,B,C,C,C,D` | `3b` |

For completeness, the entropy identities in the last column follow without
approximation as follows.  Before any merging, the entropy of the three
independent Bernoulli bits is `3b`.  Merging `k` equal atoms of mass `a`
reduces entropy by `ka log k`.  Moreover, since `B=pR`, `C=qR`, and `B+C=R`,

\[
[-B\log B-C\log C]-[-R\log R]=Rb.
\]

Applying these two identities to the displayed atoms gives exactly the last
column.  Thus the table also directly checks every collision partition.

## Uniform second-derivative argument

All five profiles have the form

\[
F_{\delta,c}(p)=3b(p)-\delta Rb(p)-cR,
\]

with

\[
(\delta,c)=(0,3\log3),(1,2\log2),(0,2\log2),(1,0),(0,0)
\]

in cases 1 through 5, respectively.  On `0<p<1`, direct differentiation
gives

\[
b'=\log(q/p),\qquad b''=-\frac1R,
\]

and, because `R'=1-2p` and `R''=-2`,

\[
(Rb)''=-2b+2(1-2p)\log(q/p)-1.                 \tag{1}
\]

If `delta=0`, then

\[
F_{0,c}''=-\frac3R+2c.
\]

Here `R<=1/4`.  In cases 1, 3, and 5, respectively, use
`log 3<2`, `log 2<1`, and `c=0` to obtain `F''<0` throughout `(0,1)`.
(The strict inequalities are the standard `log x<x-1` for `x>1`.)

It remains to treat `delta=1`.  Equation (1) yields

\[
F_{1,c}''=-\frac3R+2b-2(1-2p)\log(q/p)+1+2c. \tag{2}
\]

The binary entropy satisfies `b<=log 2` (differentiate `b`, whose unique
interior maximum is at `p=1/2`).  Also `1-2p=q-p` has the same sign as
`log(q/p)`, so their product is nonnegative.  Combining these facts with
`R<=1/4`, equation (2) gives

\[
F_{1,c}''\le -11+2\log2+2c.
\]

For case 4 (`c=0`) this is less than `-9`; for case 2
(`c=2 log 2`) it is less than `-5`, again using `log 2<1`.  Thus every one of
the five exact profiles has strictly negative second derivative on `(0,1)`.

Finally, each profile is continuous on `[0,1]`, since `x log x` has its usual
continuous value 0 at `x=0`.  Concavity on each compact subinterval of
`(0,1)` follows from the second-derivative criterion, and taking limits at
either endpoint gives concavity on the full closed interval `[0,1]`.
Therefore the frozen universal claim is proved for every positive-integer
pair `(u,v)`, including all collisions and both endpoints.

