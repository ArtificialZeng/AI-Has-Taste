# Exact adjacent-XOR reduction

All XOR operations below use infinite-width two's-complement integers.

## Lemma Z1

For every \(n\geq2\),

\[
a_n=0
\quad\Longleftrightarrow\quad
a_{n-2}\mathbin{\mathrm{XOR}}a_{n-1}=n. \tag{Z1}
\]

Proof.  Put \(x=a_{n-2}\) and \(y=a_{n-1}\).  The recurrence says

\[
a_n=(y\mathbin{\mathrm{XOR}}n)-x.
\]

Thus \(a_n=0\) if and only if \(y\mathbin{\mathrm{XOR}}n=x\).
Bitwise XOR by a fixed infinite bit string is an involution, so this is
equivalent to \(n=y\mathbin{\mathrm{XOR}}x\), which is (Z1).

## Exact consequences

If \(a_n=0\), then \(a_{n-2}\) and \(a_{n-1}\) have the same sign: their
infinite sign bits agree because their XOR is the nonnegative integer \(n\).
They agree at every bit position strictly above the highest set bit of \(n\),
and Lemma E1 applied to
\(a_{n-2}=a_{n-1}\mathbin{\mathrm{XOR}}n\) gives

\[
|a_{n-1}-a_{n-2}|\leq n. \tag{Z2}
\]

Equivalently, if \(e=a_{n-1}-a_{n-2}\), then a zero requires

\[
\frac{e+n}{2}=a_{n-1}\mathbin{\mathrm{AND}}n,
\]

so \(e+n\) is even, \(-n\leq e\leq n\), and \((e+n)/2\) is a submask of
\(n\).  These are exact necessary filters, but (Z1) remains an equivalent
reformulation rather than a resolution of the original tail problem.

## Scope

The eight known zeros satisfy (Z1) by direct evaluation.  Excluding every
later hit of the diagonal
\(a_{n-2}\mathbin{\mathrm{XOR}}a_{n-1}=n\) is still open.  No numerical
search, including a search that uses (Z1) as its zero test, proves this
universal exclusion.
