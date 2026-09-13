# Builder/R route: exact (B_n)-orbit flow for \(\operatorname{Abs}(D_9)\)

Date: 2026-08-29 (Asia/Shanghai)  
Role: independent proof builder / structural reduction  
Scope: this note and `discovery/` only

## 1. Endpoint actually established by this route

Subject to the standard Carter identity

\[
\ell_T(w)=\operatorname{codim}\operatorname{Fix}(w)
\]

for real reflection groups, the serialized certificate
`discovery/d9_orbit_flow_candidate.json`, together with the independent verifier
`discovery/verify_orbit_flow.py`, proves the finite statement

\[
\operatorname{Abs}(D_9)\text{ admits a normalized flow with unit vertex weights.}
\]

The certificate contains 150 (B_9)-orbits and 284 positive rational
orbit-pair flows.  It was reconstructed and checked using exact integer and
rational arithmetic.  This is a finite (D_9) result, not an induction proof
for all (D_n).

## 2. Definitions rebuilt from the source

Let (W=D_n=G(2,2,n)) be the group of signed permutations (w) of
\(\{\pm1,\ldots,\pm n\}\) satisfying (w(-i)=-w(i)) and having an even
number of negative entries among (w(1),\ldots,w(n)).  Its reflections are

\[
t_{ij}^{\delta}: i\mapsto \delta j,\quad j\mapsto \delta i,
\qquad \delta\in\{+1,-1\},\quad 1\le i<j\le n,
\]

with the forced images of (-i,-j).  Thus (D_n) has (n(n-1))
reflections.

For (T) this reflection set, define

\[
\ell_T(w)=\min\{k:w=t_1\cdots t_k,\ t_i\in T\}.
\]

The absolute order is

\[
u\le_T v\quad\Longleftrightarrow\quad
\ell_T(u)+\ell_T(u^{-1}v)=\ell_T(v).
\]

It is ranked by \(\ell_T\), and (u\lessdot v) exactly when
\(v=ut\) for a (t\in T) and
\(\ell_T(v)=\ell_T(u)+1\).

For a finite ranked poset (P=\bigsqcup_r P_r) with unit vertex weights, a
normalized flow is a family (f_r(x,y)\in\mathbb R_{\ge0}), supported on
covers (x\lessdot y), satisfying

\[
\sum_{y:x\lessdot y}f_r(x,y)=\frac1{|P_r|},\qquad
\sum_{x:x\lessdot y}f_r(x,y)=\frac1{|P_{r+1}|}.
\]

The equations for different adjacent rank pairs are independent.

## 3. Why quotienting by (B_n), rather than (D_n), is exact

Let (B_n=G(2,1,n)).  The parity-of-sign map (B_n\to\{\pm1\}) has
kernel (D_n), so (D_n\triangleleft B_n).  Conjugation by any (g\in B_n)
therefore maps (D_n) to itself.  It also permutes the roots
\(e_i\pm e_j\), hence permutes the (D_n)-reflection set (T).  It follows
that

\[
w\longmapsto gwg^{-1}
\]

preserves reflection length, absolute order, ranks, and covers.  Thus (B_n)
is a legitimate subgroup of \(\operatorname{Aut}(\operatorname{Abs}(D_n))\),
even though it is larger than (D_n).  Gaetz--Gao Proposition 3.6 applies to
any automorphism group, not only inner automorphisms from (W).

This choice also removes the familiar splitting of some (B_n)-classes into
\(D_n\)-conjugacy classes.  The orbit quotient used here is by the actual
\(B_n\)-action, so no split-class convention is being silently assumed.

For completeness, let (O,O') be (B_n)-orbits in consecutive ranks.  The
induced cover graph between (O) and (O') is biregular: transitivity gives
constant upper degree (d^+_{O,O'}) on (O) and constant lower degree
\(d^-_{O,O'}\) on (O'), with

\[
|O|d^+_{O,O'}=|O'|d^-_{O,O'}=:E_{O,O'}.
\]

If a quotient flow has value (F(O,O')), put
\(F(O,O')/E_{O,O'}\) on every individual cover in this bipartite graph.
Then each (x\in O\) receives row contribution (F(O,O')/|O|), and each
\(y\in O'\) receives column contribution (F(O,O')/|O'|).  Consequently
the quotient equations below lift exactly to the unit-weight equations on
the full poset.  Conversely, summing a full flow over each orbit pair gives a
quotient flow.  This proves strict equivalence, not merely necessity.

## 4. Signed cycle types, sizes, and ranks

A signed cycle is positive or negative according as the product of its edge
signs is (+1) or (-1).  A (B_n)-conjugacy class is indexed by a
bipartition

\[
(\lambda,\mu),\qquad |\lambda|+|\mu|=n,
\]

where \(\lambda\) lists positive-cycle lengths and \(\mu\) lists
negative-cycle lengths.  Such a class is contained in (D_n) exactly when
\(\ell(\mu)\) is even.  These are therefore exactly the quotient nodes.

Writing

\[
z_\lambda=\prod_{j\ge1}j^{m_j(\lambda)}m_j(\lambda)!,
\]

the orbit size is

\[
c(\lambda,\mu)=
\frac{2^n n!}
{2^{\ell(\lambda)+\ell(\mu)}z_\lambda z_\mu}.
\tag{4.1}
\]

This follows from the standard signed-cycle centralizer order in (B_n).
Because the full (B_n)-class lies in (D_n), no extra factor of two occurs.

A positive signed cycle has a one-dimensional fixed space and a negative
signed cycle has none.  Carter's identity hence gives

\[
\rho(\lambda,\mu)=\ell_T(w)=n-\ell(\lambda).
\tag{4.2}
\]

The program also independently checks that the sum of (4.1) over all allowed
types is (2^{n-1}n!), and that the rank totals equal the coefficients of

\[
(1+(n-1)q)\prod_{i=1}^{n-1}(1+(2i-1)q).
\tag{4.3}
\]

## 5. Exact cover support on the quotient

Right multiplication by (t_{ij}^{\delta}) either joins two signed cycles or
splits one.  Joining multiplies their cycle signs; after splitting, the two
new cycle signs multiply to the old sign.  Equation (4.2) says an upward cover
must reduce the number of positive cycles by exactly one.  Exhausting the
possibilities gives precisely the following three operations:

1. (P_a+P_b\longrightarrow P_{a+b}) (merge two positive cycles);
2. (P_a+N_b\longrightarrow N_{a+b}) (merge a positive and a negative cycle);
3. (P_{a+b}\longrightarrow N_a+N_b) (split a positive cycle into two
   negative cycles), for (a,b\ge1).

Here are the exact source-side reflection multiplicities, which are useful
both for checking the transition support and for writing the lifted flow.
Let $m_a^+$ and $m_b^-$ denote the multiplicities of parts $a$ in
$\lambda$ and $b$ in $\mu$, respectively.  For a fixed source type
$A=(\lambda,\mu)$, the number $d^+_{A,B}$ of reflections taking any fixed
$w\in A$ to the indicated target type $B$ is:

\[
d^+_{A,B}=
\begin{cases}
2ab\,m_a^+m_b^+,&P_a+P_b\to P_{a+b},\ a\ne b,\\
a^2m_a^+(m_a^+-1),&P_a+P_a\to P_{2a},\\
2ab\,m_a^+m_b^-,&P_a+N_b\to N_{a+b},\\
(a+b)m_{a+b}^+,&P_{a+b}\to N_a+N_b,\ a<b,\\
a\,m_{2a}^+,&P_{2a}\to N_a+N_a.
\end{cases}
\tag{5.1}
\]

For the first two kinds, select the source cycles and then one of the $2ab$
signed transpositions joining their supports.  For a positive cycle of length
$c=a+b$, an unordered cut at cyclic distances $a,b$ has $c$ choices if
$a<b$ and $c/2=a$ choices if $a=b$; for each cut exactly one of the two sign
choices produces two negative cycles.  This gives the last two lines.
Different source-cycle choices leading to a fixed target type are exactly the
choices counted in (5.1).

Consequently the number of individual covers between the two orbit nodes is

\[
E_{A,B}=c(A)d^+_{A,B}.
\tag{5.2}
\]

The group action proves equally that $E_{A,B}=c(B)d^-_{A,B}$, where
$d^-_{A,B}$ is the lower degree at a target vertex.  Thus a quotient amount
$F(A,B)$ lifts explicitly by putting $F(A,B)/E_{A,B}$ on each of these
individual covers.  Formula (5.2), rather than a tacit assumption that there
is only one cover in an orbit pair, is the multiplicity used by the lifting
argument.

The other sign possibilities go down one rank:
\(N+N\to P\), (P\to P+P\), and (N\to P+N\).  Every listed schematic
operation is realized by at least one (D_n)-reflection; the canonical
representative evaluator in the independent verifier checks realizability
directly rather than trusting this transition list.

As a separate small-(n) audit, `discovery/bruteforce_transition_check.py`
does not import the quotient constructor.  It enumerates every even signed
permutation and all (n(n-1)) reflections.  The recorded runs were:

```text
{'n': 4, 'elements': 192, 'reflections': 12, 'upward_directed_edges': 1152,
 'orbit_types': 11, 'transition_support_verified': True,
 'transition_multiplicities_verified': True,
 'class_sizes_verified': True}
{'n': 5, 'elements': 1920, 'reflections': 20,
 'upward_directed_edges': 19200, 'orbit_types': 18,
 'transition_support_verified': True,
 'transition_multiplicities_verified': True,
 'class_sizes_verified': True}
```

Thus both formula (4.1) and the entire cover-support rule were checked against
an independent element-level model in two nontrivial cases.

## 6. The exact transportation problems

Let \({\cal O}_r\) be the set of types with
\(n-\ell(\lambda)=r\), and put

\[
N_r=\sum_{A\in{\cal O}_r}c(A)=|\operatorname{Abs}(D_n)_r|.
\]

For every allowed quotient cover (A\to B), introduce
\(F_r(A,B)\in\mathbb Q_{\ge0}\).  The complete quotient normalized-flow
system is

\[
\sum_{B:A\to B}F_r(A,B)=\frac{c(A)}{N_r}
\quad(A\in{\cal O}_r),
\tag{6.1}
\]

\[
\sum_{A:A\to B}F_r(A,B)=\frac{c(B)}{N_{r+1}}
\quad(B\in{\cal O}_{r+1}).
\tag{6.2}
\]

This formulation uses one variable per *orbit pair with a cover*, not one
variable per individual cover and not one variable per finer edge orbit.
Section 3 proves that this is sufficient because every orbit-pair induced
graph is biregular.

For exact construction, set

\[
L_r=\operatorname{lcm}(N_r,N_{r+1}),\qquad
s_A=L_r\frac{c(A)}{N_r},\qquad
d_B=L_r\frac{c(B)}{N_{r+1}}.
\]

All these quantities are integers, and
\(\sum_As_A=L_r=\sum_Bd_B\).  A source--left--right--sink network with
source capacities (s_A), sink capacities (d_B), and allowed support arcs
therefore has an integral maximum flow.  A flow of value (L_r) gives the
exact rational solution \(F_r(A,B)=m_{A,B}/L_r\).  No floating-point LP is
used anywhere in this route.

## 7. Baseline (D_8) reconstruction

The constructor found and serialized an exact solution for the last published
baseline (D_8):

- orbit count: 95;
- rank sizes:
  \([1,56,1316,16856,127694,578984,1505524,1984584,945945]\);
- positive orbit flows: 172;
- all eight adjacent-rank maximum flows equal their exact target (L_r).

Independent-verifier output:

```json
{"input_sha256":"2b1c573972e7f8b7ff310f5093b77001379083f3e25838acc614b83afebbb2c8",
 "n":8,"orbits":95,"positive_orbit_flows":172,"rank_pairs":8,
 "status":"VERIFIED"}
```

This is a fresh reconstruction, not an import of Gaetz--Gao's unpublished
Sage output.

## 8. Exact (D_9) result

For (D_9), the exact rank sizes are

\[
\begin{split}
(N_0,\ldots,N_9)={}&(1,72,2220,38304,405174,2702448,\\
&11228300,27491616,34812945,16216200).
\end{split}
\]

They sum to (92{,}897{,}280=2^8\,9!=|D_9|).  There are 150 quotient
nodes, distributed by rank as

\[
(1,1,3,5,11,17,29,35,34,14).
\]

The nine transport instances have the following exact construction summary.

| ranks | allowed orbit-pair edges | positive flows | (L_r\) = exact max flow |
|---:|---:|---:|---:|
| 0--1 | 1 | 1 | 72 |
| 1--2 | 3 | 3 | 13,320 |
| 2--3 | 9 | 7 | 7,086,240 |
| 3--4 | 22 | 15 | 369,518,688 |
| 4--5 | 50 | 27 | 26,070,515,856 |
| 5--6 | 97 | 45 | 7,585,974,219,600 |
| 6--7 | 156 | 65 | 1,641,936,765,600 |
| 7--8 | 175 | 72 | 106,340,457,307,680 |
| 8--9 | 96 | 49 | 12,545,192,860,200 |

The independent verifier:

- parses only the serialized JSON;
- rebuilds the exhaustive set of bipartitions;
- recomputes all class sizes, ranks, rank sizes, and group order;
- constructs a canonical signed permutation for every source type;
- multiplies it by every one of the 72 (D_9)-reflections to verify every
  claimed positive flow edge is a genuine upward cover;
- checks all equations (6.1)--(6.2) with `fractions.Fraction`;
- reconstructs each orbit-pair edge count and the uniform per-edge lift, then
  checks the lifted row and column equation for every orbit class;
- rejects missing or unknown fields and noncanonical fractions;
- prints both input and verifier SHA-256 hashes.

Recorded output:

```json
{"input_sha256":"1139852c155f754f6b998b15bf3fcd0f42942351a609e283615cb7599002beca",
 "n":9,"orbits":150,"positive_orbit_flows":284,"rank_pairs":9,
 "status":"VERIFIED",
 "verifier_sha256":"5b8cd92a7837018e2e6b46a3f31094c579f23ea338e10a96eee388bec20a5535"}
```

The mutation suite changed a flow amount, inserted an unknown endpoint, set a
zero denominator, removed a flow, and duplicated a type.  All five corrupted
inputs were rejected.

## 9. Attempted (D_n\to D_{n+1}) pattern and remaining gap

The structural quotient and integer-flow constructor are uniform in (n), but
the present project endpoint and release scope are exactly (D_9).  Exploratory
outputs above (n=9) were removed after the scope was frozen and are neither
evidence nor deliverables for this project.

The most obvious embedding sends

\[
(\lambda,\mu)\longmapsto(\lambda\cup\{1\},\mu),
\]

corresponding to adding a positive fixed point.  The particular sparse
integral max flows returned by the deterministic solver do **not** restrict to
rankwise scalar multiples of the (D_n) flow: already from (D_8) to (D_9),
the ratios vary among embedded edges from rank (1) onward.  This kills the
naive "append a fixed point and rescale" reading of the computed certificate.
It does not rule out a different, deliberately selected family of flows.

The precise unclosed induction problem is now:

> Prove the weighted Hall inequalities for every subset of every adjacent-rank
> bipartite graph on the allowed bipartitions, or give a closed nonnegative
> formula satisfying (6.1)--(6.2) that is compatible with adding a letter.

No such all-(n) Hall proof or compatible closed formula was obtained in this
route.  Therefore the only theorem endpoint claimed here is the independently
verified finite result for (D_9) (plus the reconstructed (D_8) baseline).

## 10. Reproduction commands and hashes

From the project root:

```bash
python3 discovery/orbit_lp.py 8 --output discovery/d8_orbit_flow_candidate.json
python3 discovery/orbit_lp.py 9 --output discovery/d9_orbit_flow_candidate.json
python3 discovery/bruteforce_transition_check.py 4
python3 discovery/bruteforce_transition_check.py 5
python3 discovery/verify_orbit_flow.py discovery/d8_orbit_flow_candidate.json
python3 discovery/verify_orbit_flow.py discovery/d9_orbit_flow_candidate.json
python3 discovery/test_verifier_rejects.py discovery/d9_orbit_flow_candidate.json
```

SHA-256 at the recorded milestone:

```text
65bef4c9074767b7c9e26fda5e5851791e77198c0c4d0fcbf04866609d039271  discovery/orbit_lp.py
05ab0a8b4c8a5ff729f4da8e11207672b51e7cbe39b0ed694a5f2f0eb2760c1f  discovery/bruteforce_transition_check.py
5b8cd92a7837018e2e6b46a3f31094c579f23ea338e10a96eee388bec20a5535  discovery/verify_orbit_flow.py
0f4c849454f14471a25e2a6da5382cb6930d5d18b46c469af9cddcbe2c7e5035  discovery/test_verifier_rejects.py
2b1c573972e7f8b7ff310f5093b77001379083f3e25838acc614b83afebbb2c8  discovery/d8_orbit_flow_candidate.json
1139852c155f754f6b998b15bf3fcd0f42942351a609e283615cb7599002beca  discovery/d9_orbit_flow_candidate.json
```

Python standard library only was used.  No Lean, Coq, Isabelle, or other proof
assistant was used in this builder route.

## 11. Explicit assumptions and audit cautions

1. The human proof uses the standard real-reflection-group identity
   \(\ell_T(w)=\operatorname{codim}\operatorname{Fix}(w)\).  The rank formula
   is also cross-checked computationally in small (n), but the manuscript
   should cite the exact primary theorem/location.
2. Formula (4.1) is the standard (B_n) signed-cycle centralizer formula.  It
   is exhaustively cross-checked for (D_4,D_5), but the manuscript should cite
   a primary source or include its short centralizer derivation.
3. The certificate proves existence; the sparse flow returned by Dinic is not
   canonical and carries no evident representation-theoretic meaning.
4. The verifier checks quotient flows and actual cover realizability.  The
   lift to all individual edges is represented by the biregularity proof in
   Section 3 rather than by serializing all full-poset edge weights.
5. The all-(n) conjecture remains outside this route's proved endpoint.
