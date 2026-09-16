# A modulo-32 obstruction for the rational moment system

## Claim

There is no tuple \((x_1,\ldots,x_{18})\in\mathbb Q^{18}\) satisfying

\[
 \sum x_j^2=9,\qquad \sum x_j^4=\frac{27}{4},\qquad
 \sum x_j^6=\frac{45}{8}.
\]

## Proof

Suppose such a tuple exists.  Choose integers \(a_1,\ldots,a_{18}\) and a
positive common denominator \(D\) such that \(x_j=a_j/D\) and
\(\gcd(D,a_1,\ldots,a_{18})=1\).  Clearing denominators gives

\[
 S_2:=\sum a_j^2=9D^2,\qquad
 S_4:=\sum a_j^4=\frac{27D^4}{4},\qquad
 S_6:=\sum a_j^6=\frac{45D^6}{8}. \tag{1}
\]

The integer \(D\) is even: if it were odd, the middle identity in (1),
after multiplication by 4, would have an even left side and an odd right
side.  Put \(k=v_2(D)\geq 1\), and write \(D=2^k d\) with \(d\) odd.
Primitivity implies that at least one \(a_j\) is odd.

Let \(O\) be the number of odd \(a_j\).  For an odd integer \(a\), define
\(p(a)\in\mathbb Z/4\mathbb Z\) by

\[
 a^2\equiv 1+8p(a)\pmod {32}.
\]

Then

\[
 a^4\equiv1+16p(a),\qquad
 a^6\equiv1-8p(a)\pmod {32}. \tag{2}
\]

Indeed, these follow by squaring and multiplying \(1+8p(a)\), with all
terms of degree at least two reduced modulo 32.  Put
\(P=\sum_{a_j\text{ odd}}p(a_j)\in\mathbb Z/4\mathbb Z\).  Also let \(E\)
and \(F\) count indices with \(v_2(a_j)=1\) and \(v_2(a_j)=2\),
respectively.  An integer of 2-adic valuation 1 contributes
\((4,16,0)\) to \((a^2,a^4,a^6)\) modulo 32; one of valuation 2 contributes
\((16,0,0)\); and one of valuation at least 3 contributes \((0,0,0)\).
Consequently,

\[
\begin{aligned}
 S_2&\equiv O+8P+4E+16F,\\
 S_4&\equiv O+16P+16E,\\
 S_6&\equiv O-8P
\end{aligned}\pmod {32}. \tag{3}
\]

If \(k=1\), the right sides of (1) are respectively congruent to
\((4,12,8)\) modulo 32.  The fourth-power identity modulo 16 gives
\(O\equiv12\pmod {16}\), hence \(O=12\), because \(1\leq O\leq18\).
But the sixth-power identity modulo 8 gives \(O\equiv0\pmod8\), a
contradiction.

Now suppose \(k\geq2\).  Both \(S_4\) and \(S_6\) are 0 modulo 32.
The fourth-power identity modulo 16 gives \(O\equiv0\pmod {16}\), so
\(O=16\).  The last congruence in (3) then gives
\(P\equiv2\pmod4\).  Substitution in the middle congruence in (3) forces
\(E\) to be odd.  There are only two even \(a_j\), so \(E=1\).  The other
even \(a_j\) has valuation 2 or at least 3, and hence \(F\in\{0,1\}\).
The first congruence in (3) therefore yields

\[
 S_2\equiv4+16F\in\{4,20\}\pmod {32}. \tag{4}
\]

On the other hand, (1) gives \(S_2\equiv16\pmod {32}\) if \(k=2\), and
\(S_2\equiv0\pmod {32}\) if \(k\geq3\).  Both alternatives contradict
(4).  Thus every possible value of \(k\) is excluded, proving the claim.

## Consequence for the earlier unit-pair search

There is also a shorter obstruction specific to that ansatz.  If rational
\(a,b\) satisfy \(a^2+b^2=1\), clear denominators primitively to obtain a
primitive integer Pythagorean triple.  Its hypotenuse is odd (otherwise the
two legs would both be even).  Thus \((ab)^2\) has odd reduced denominator.
A finite sum of such numbers has odd reduced denominator and cannot equal
\(9/8\).  Hence the nine-unit-circle-pair construction is impossible without
any height or pair-type restriction.

