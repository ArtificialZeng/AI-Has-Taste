# Proof dossier: boundary classification with two missing sums

All arithmetic below is in \(\mathbb F_p\), where \(p\ge 11\) is prime and
\(3\le \ell\le (p-3)/2\). Thus \(2\ell\le p-3\). This dossier proves the
claim interpreted in `problem.md`; it does not assert novelty.

## 1. Affine normalization and the forced set

For a simultaneous affine map \(z\mapsto uz+v\), \(u\ne0\), one has

\[
(uA+v)\mathbin{\dotplus}(uB+v)
=u(A\mathbin{\dotplus}B)+2v,
\]

because the map preserves the inequality of the two summands. If the two
missing sums are distinct elements \(s,t\), take
\(u=2/(t-s)\) and \(2v=-us\). This sends their unordered set to
\(\{0,2\}\).

Now suppose the missing sums are \(0,2\), and put
\(C=\mathbb F_p\setminus A\). For \(y\in B\setminus\{0\}\), the summands
\(-y\) and \(y\) are distinct. Since their sum 0 is missing, \(-y\notin A\).
Similarly, for \(y\in B\setminus\{1\}\), the summands \(2-y\) and \(y\)
are distinct, so \(2-y\notin A\). Hence

\[
U(B):=((-B)\setminus\{0\})\cup((2-B)\setminus\{1\})\subseteq C. \tag{1}
\]

Since \(|C|=\ell\), this gives \(|U(B)|\le\ell\).

## 2. Endpoint-corrected cyclic-run lemma

**Lemma.** Let \(X\subsetneq\mathbb F_p\) be nonempty, \(|X|=\ell\), and

\[
V=(X\setminus\{0\})\cup((X+2)\setminus\{1\}).
\]

If \(|V|\le\ell\), then, for unique nonnegative \(a,b\) with
\(a+b=\ell\),

\[
X=\{2j:0\le j<a\}\cup\{-1-2j:0\le j<b\}, \tag{2}
\]

and

\[
V=\{2j:1\le j\le a\}\cup\{-1-2j:0\le j<b\},\qquad |V|=\ell. \tag{3}
\]

Here uniqueness is as an ordered pair; the range bound is part of the
hypotheses.

**Proof.** Addition by 2 is a single cycle on \(\mathbb F_p\). Decompose
\(X\) into its maximal cyclic \(+2\)-runs, and let their number be \(r\).
Because \(X\) is nonempty and proper, \(r\ge1\), and

\[
|X\cup(X+2)|=\ell+r. \tag{4}
\]

Deleting 0 from the first copy of \(X\) actually removes a point from this
union precisely when \(0\in X\) and \(-2\notin X\), i.e. precisely when 0
is a run start. Let the indicator of this event be \(\delta_0\). Deleting 1
from \(X+2\) actually removes a point precisely when \(-1\in X\) and
\(1\notin X\), i.e. when \(-1\) is a run end. Let that indicator be
\(\delta_1\). The two points are distinct, so the exact endpoint-corrected
count is

\[
|V|=\ell+r-\delta_0-\delta_1. \tag{5}
\]

Thus \(r\le\delta_0+\delta_1\le2\).

If \(r=1\), the unique run either starts at 0 or ends at \(-1\). In the
first case it is \(\{0,2,\ldots,2(\ell-1)\}\); in the second it is
\(\{-1,-3,\ldots,-1-2(\ell-1)\}\). Both endpoint events cannot occur:
a run of length \(m\le\ell\) starting at 0 and ending at \(-1\) would give
\(2(m-1)\equiv-1\pmod p\), whereas
\(1\le2m-1\le2\ell-1\le p-4\).

If \(r=2\), (5) forces \(\delta_0=\delta_1=1\). The run starting at 0 and
the run ending at \(-1\) are distinct by the same congruence and bound.
If their lengths are \(a,b\), they are all the runs, so \(a+b=\ell\), and
(2) follows. This also includes the one-run cases by allowing \(a=0\) or
\(b=0\).

For (2), direct shifting and deletion gives

\[
(X\setminus\{0\})\cup((X+2)\setminus\{1\})
=\{2j:1\le j\le a\}\cup\{-1-2j:0\le j<b\}.
\]

There is no collision between the displayed pieces: a collision would make
\(p\) divide \(2(i+j)+1\) with \(1\le i\le a\), \(0\le j<b\), but
\(3\le2(i+j)+1\le2\ell-1\le p-4\). Each piece is internally injective as
well. Thus (3) has size \(a+b=\ell\). This collision bound, together with
the congruence excluding a run from 0 through \(-1\), is the required
no-wrap argument. Uniqueness follows from the unique cyclic-run
decomposition: \(a\) is the length of the run starting at 0, or 0 if there
is none. \(\square\)

Apply the lemma to \(X=-B\). Then \(V=U(B)\), and negating (2) gives

\[
B=\{-2j:0\le j<a\}\cup\{1+2j:0\le j<b\}=B_{a,b}. \tag{6}
\]

Equation (3) says \(U(B)=C_{a,b}\). In view of (1), both this set and
\(C\) have size \(\ell\), so \(C=C_{a,b}\), and hence \(A=A_{a,b}\).

## 3. Direct converse

First, the two pieces of \(B_{a,b}\) cannot collide: a collision would give
\(p=2(i+j)+1\) for some \(0\le i<a\), \(0\le j<b\), while the right side
is at most \(2\ell-3\). The analogous possible collision in \(C_{a,b}\)
has right side at most \(2\ell-1\). Thus
\(|B_{a,b}|=|C_{a,b}|=\ell\), and \(|A_{a,b}|=p-\ell\).

The calculation (3) gives \(U(B_{a,b})=C_{a,b}\), so the argument behind
(1), read in reverse, shows that neither 0 nor 2 has an allowed
representation.

It remains to exhibit a representation for every other residue. Suppose
first that \(a,b>0\). Since \(0,1\in B_{a,b}\), every
\(s\notin C_{a,b}\cup\{0\}\) is represented as \(s=s+0\). For
\(s=2i\in C_{a,b}\), \(2\le i\le a\), use

\[
s=(2i-1)+1.
\]

The first summand is outside \(C_{a,b}\) and differs from 1. For
\(s=-1-2j\in C_{a,b}\), \(0\le j<b\), use

\[
s=(-2j-2)+1.
\]

Again the first summand is outside \(C_{a,b}\) and differs from 1. The
positive-odd/negative-even assertions here are legitimate modulo \(p\).
Indeed, a congruence \(2i-1\equiv-1-2k\) would make \(p\) divide
\(2(i+k)\), which lies strictly between 0 and \(p\). A congruence
\(-2j-2\equiv2i'\) would similarly make \(p\) divide
\(2(i'+j+1)\in[2,2\ell]\). Congruence with the negative-odd piece would
make \(p\) divide the nonzero integer \(2(k-j)-1\), whose absolute value is
less than \(p\). Finally, \(-2j-2\not\equiv1\), since
\(3\le2j+3\le2b+1\le2\ell-1<p\).

If \(a=\ell,b=0\), residues outside \(C_{\ell,0}\cup\{0\}\) are again
represented using 0. For \(s=2i\), \(2\le i\le\ell\), put
\(j=\ell-i+1\) and use

\[
s=2(\ell+1)+(-2j).
\]

Here \(-2j\in B_{\ell,0}\), while
\(2\ell+2\le p-1\) is outside \(C_{\ell,0}\). The two summands cannot be
equal modulo \(p\): their positive difference is even and strictly below
\(2p\), so it is neither \(p\) nor \(2p\). Finally, the map
\(z\mapsto1-z\) carries the case \((a,b)=(\ell,0)\) to
\((0,\ell)\) and sends sums by \(s\mapsto2-s\), so it supplies the remaining
endpoint case. Therefore the restricted sumset is exactly
\(\mathbb F_p\setminus\{0,2\}\).

## 4. Affine equivalence and class count

Suppose an affine map \(z\mapsto uz+v\) sends one displayed ordered pair to
another. Since both have missing set \(\{0,2\}\), its induced map on sums
must preserve that set:

\[
\{2v,2u+2v\}=\{0,2\}.
\]

Consequently either \((u,v)=(1,0)\), giving the identity, or
\((u,v)=(-1,1)\), giving \(z\mapsto1-z\). In the identity case the
run decomposition in the lemma recovers the same ordered \((a,b)\). Directly,

\[
1-B_{a,b}=B_{b,a},\qquad 1-C_{a,b}=C_{b,a}.
\]

Thus two representatives are affinely equivalent exactly when their
parameters agree up to \((a,b)\leftrightarrow(b,a)\). The \(\ell+1\)
ordered decompositions \(a+b=\ell\) consequently have
\(\lfloor\ell/2\rfloor+1\) affine orbits.

## Gap list

Empty for the mathematical classification. The exact novelty/overlap status
relative to the inaccessible full Liu--Qian article remains a separate
literature question and is not used in the proof.
