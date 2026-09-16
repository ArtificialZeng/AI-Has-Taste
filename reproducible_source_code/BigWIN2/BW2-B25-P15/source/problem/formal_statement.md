# Formal statement

Define the unique sequence \(a:\mathbb N\to\mathbb N\) by
\(a_0=1\) and \(a_{n+1}=a_n^2+2\) for every \(n\ge0\).

The source question asks either (i) to determine
\(\min\{n\in\mathbb N:n>4\text{ and }a_n\text{ is prime}\}\), if this set is
nonempty, or (ii) to prove that the set is empty. Here “prime” means a positive
integer greater than 1 having exactly two positive divisors.

The certified endpoint obtained here is narrower: every \(a_n\) with
\(5\le n\le21\) is composite. Consequently any next prime has index at least
22. This does not assert that such a prime exists.

The recurrence is over exact nonnegative integers. Index 4 is excluded by the
strict inequality in the source question. Since \(a_{n+1}>a_n\), every
displayed divisor smaller than its term is proper.
