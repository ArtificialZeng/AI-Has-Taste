# Research candidate: nonexistence of a cyclic incidence ordering for \((8,4)\)

Provenance: `win-00082-p01-research-946a888524c6`  
Date: 2026-09-09

## Exact claim

The existence statement \(\mathsf E(8,4)\) in `source.md` is false.  In other
words, there do not exist a bijection
\(e:\mathbb Z_{70}\to\binom{[8]}4\), a set
\(D\subseteq\mathbb Z_{70}\) of size 35, and shifts
\(s_v\in\mathbb Z_{70}\) whose incidence supports are all \(D+s_v\).

The proof uses Definition 1.1 and Lemma 2.2 of the cited primary source.  For
clarity, the part of Lemma 2.2 used below is this: if
\(S,D\subseteq G\), \(|S|=m\), \(1_S*1_D=r1_G\), and every two distinct
translates indexed by \(S\) meet in \(\lambda\) points, then, for every
\(b\in S\),
\[
  \lambda(T-mb)=0\quad\hbox{in }G,\qquad T=\sum_{c\in S}c.
\]

## Proof

Suppose such data exist.  The eight shifts are distinct: if two vertices had
the same shift, their incidence supports would agree, whereas a four-subset
containing one of the vertices and not the other occurs in the bijective list.
Let
\[
  S=\{s_v:v\in[8]\}\subseteq\mathbb Z_{70}.
\]
At every time exactly four vertices occur.  With the convolution convention
\((f*g)(t)=\sum_y f(y)g(t-y)\), this says
\[
  (1_S*1_D)(t)=\sum_{s\in S}1_D(t-s)=4.                 \tag{1}
\]
For distinct \(b,c\in S\), the supports \(D+b\) and \(D+c\) meet once for
each four-subset containing the corresponding pair of vertices, and hence
\[
  |(D+b)\cap(D+c)|=\binom62=15.                        \tag{2}
\]
Apply Lemma 2.2 with \(m=8,r=4,\lambda=15\).  For every \(b\in S\),
\[
  15(T-8b)=0\quad\text{in }\mathbb Z_{70}.
\]
Subtracting the equations for \(b,b'\in S\) gives
\[
  120(b-b')=0\pmod {70}.                               \tag{3}
\]
The kernel of multiplication by 120 on \(\mathbb Z_{70}\) is precisely
\(7\mathbb Z_{70}\): it has \(\gcd(120,70)=10\) elements, namely the
multiples of 7.  Fix \(b_0\in S\).  Replacing
\[
  S\ 	ext{by }S-b_0,qquad D\ 	ext{by }D+b_0          \tag{4}
\]
does not change any support, because
\((D+b_0)+(s-b_0)=D+s\).  Thus (3) permits us to write
\[
  S=7A,qquad A\subseteq\mathbb Z_{10},\quad |A|=8.     \tag{5}
\]
This is a consequence of the arbitrary-shift definition, not an imposed
cyclic action on the vertices.

Every \(t\in\mathbb Z_{70}\) has a unique expression
\(t=j+7x\), where \(0\leq j<7\) and \(x\in\mathbb Z_{10}\).  Define
\[
  D_j=\{x\in\mathbb Z_{10}:j+7x\in D\}.
\]
Label the vertices by their distinct elements \(a\in A\).  At time \(j+7x\),
the vertex labelled \(a\) occurs exactly when
\[
  j+7x\in D+7a
  \iff j+7(x-a)\in D
  \iff x-a\in D_j.                                    \tag{6}
\]
Consequently the attendee set in this slice is
\[
  C_{j,x}=A\cap(x-D_j),                                \tag{7}
\]
and (1) becomes
\[
  1_A*1_{D_j}=4,1_{\mathbb Z_{10}}.                   \tag{8}
\]
Summing (8) over \(x\) gives \(8|D_j|=40\), so
\(|D_j|=5\) for every \(j\).

It remains to classify (8), which is elementary.  Put
\(B=\mathbb Z_{10}\setminus A\), so \(|B|=2\).  Since
\(1_{\mathbb Z_{10}}*1_{D_j}=5\), equation (8) is equivalent to
\[
  1_B*1_{D_j}=1_{\mathbb Z_{10}}.                      \tag{9}
\]
Write \(B=\{b,b+d\}\), with \(d\ne0\).  If
\(f=1_{D_j}\), equation (9), after putting \(z=x-b\), reads
\[
  f(z)+f(z-d)=1\qquad(z\in\mathbb Z_{10}).             \tag{10}
\]
Thus \(f\) alternates around every orbit of translation by \(d\).  Such an
alternation closes up only if the order of \(d\) is even.  In
\(\mathbb Z_{10}\) this is equivalent to \(d\) being odd.

There are then exactly two cases.

1. If \(d\ne5\), then \(d\) generates \(\mathbb Z_{10}\).  Equation (10)
   has just the two parity classes as solutions \(D_j\).  The two points of
   \(B\) have opposite parity, so \(A\) contains exactly four even and four
   odd elements.  For every \(x\), the set \(x-D_j\) is a parity class;
   hence (7) is one of only two four-subsets of \(A\).  The ten meetings in
   even a single slice therefore repeat, contradicting injectivity of \(e\).

2. If \(d=5\), let \(H=\{0,5\}\).  The set \(B\) is one \(H\)-coset and
   \(A\) is the union of the other four \(H\)-cosets.  Equation (10) says
   exactly that every \(D_j\) is a transversal of the five \(H\)-cosets.
   Reflection and translation preserve that property, so every \(x-D_j\)
   is also a transversal.  Equation (7) therefore chooses one point from
   each of the four \(H\)-cosets comprising \(A\).  Across all seven slices
   and all choices of their templates, at most \(2^4=16\) distinct attendee
   sets can occur.  A bijection onto \(\binom A4\) requires 70 distinct
   attendee sets, again a contradiction.

The alternatives exhaust every two-point complement \(B\), because even
\(d\) makes (10) impossible.  Both possible odd-difference cases contradict
the defining bijection.  Hence \(\mathsf E(8,4)\) is false. \(\square\)

## Audit record

- **Support normalization:** (4) is written explicitly and preserves each
  individual support, not merely the convolution.
- **Convolution sign:** (6) derives the sign \(x-a\in D_j\) directly from
  membership in \(D+7a\); (7) follows without reflection assumptions.
- **Tiling cases:** the order of a nonzero element of \(\mathbb Z_{10}\) is
  even exactly for odd differences.  The odd cases split into the four
  generating differences (up to sign) and the antipodal difference 5.
- **Exact falsification attempt:** `evidence/research_verify_946a888524c6.py`
  independently enumerates all
  \(\binom{10}{8}\binom{10}{5}=11{,}340\) pairs \((A,D_j)\), reconstructs
  every column (7), and checks the classification above.  Its exact run finds
  200 valid pairs: 20 non-antipodal complements with 2 templates and 2
  accessible columns each, and 5 antipodal complements with 32 templates and
  16 accessible columns each.  No fixed \(A\) can access all 70 four-subsets.
- **Dependencies:** Definition 1.1 and Lemma 2.2 of the local primary-source
  PDF; all remaining steps are proved above.  The primary source was checked
  to be arXiv v1 dated 2026-09-06 and to state that necessity in higher
  uniformities remains open.  This record makes no claim of priority beyond
  that source comparison.
- **Known mathematical gaps:** none identified in this research pass.  The
  exact scope still requires a fresh mathematical referee under the workflow.

