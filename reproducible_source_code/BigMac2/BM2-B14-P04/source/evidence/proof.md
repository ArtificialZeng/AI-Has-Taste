# Exact certificates for `rdim(B_3)=2`

Elements of $B_3$ are encoded by integers $0,\ldots,7$; the three bits of
an integer are the characteristic vector of the corresponding subset of
$[3]$. Thus $0=\varnothing$, $1=a$, $2=b$, $3=ab$, $4=c$,
$5=ac$, $6=bc$, and $7=abc$.

## Upper certificate

The three PLEs

```text
0 1 2 3 4 5 6 7
4 2 6 1 5 3
5 2
```

have total element-occurrence cost $8+6+2=16$. The exact checker verifies
directly that each is a PLE, every element and every comparable pair is
covered, and both orientations of every incomparable pair are covered.

## Lower certificate

Use one covering requirement for each element, one for co-occurrence of each
unordered comparable pair, and two (one per orientation) for each unordered
incomparable pair. There are $8+19+18=45$ requirements. Give the following
21 requirements the displayed weights and give every other requirement weight
zero. The description is symmetric under permuting $a,b,c$:

```text
weight 1/3: comparable(0,D) and comparable(D,7), for D in {3,5,6}
weight 2/3: both orientations of each pair in {1,2,4}
weight 2/3: both orientations of each pair in {3,5,6}
weight 2:   6<1, 5<2, and 3<4
```

Here $x<y$ on a line naming an orientation means that a PLE lists $x$
before $y$; it does not assert inclusion. All weights are nonnegative and
their sum is $6(1/3)+12(2/3)+3(2)=16$.

Here is a direct verification of every PLE inequality. For a PLE $M$, let
$s$ and $d$ be the numbers of its singleton and doubleton elements, let $e$
be the number of its elements among $0$ and $7$, and let $q$ count the
displayed weight-2 orientations that $M$ covers. Its covered dual weight is

\[
w(M)=\frac{ed}{3}+\frac23\binom{s}{2}
     +\frac23\binom{d}{2}+2q.
\]

We have $q\le1$. Indeed, if two distinct complementary pairs were both
reversed, say $D_i<i$ and $D_j<j$, inclusion would force
$D_i<i<D_j<j<D_i$, impossible in a linear order. Also $0\le s,d\le3$.
The endpoint term satisfies $ed/3\le e$. If $q=0$, then
$u(u-1)\le3u$ for $u=s,d$, so the remaining terms total at most $s+d$.
If $q=1$, then $s,d\ge1$, and

\[
s(4-s)+d(4-d)\ge 3+3=6,
\]

which is equivalent to
$\frac23\binom{s}{2}+\frac23\binom{d}{2}+2\le s+d$.
Thus the covered weight is at most $e+s+d=|M|$ in all cases.

The same family of inequalities is additionally checked exactly, without a
solver, by `verify_certificate.py`: it generates all 1,323 nonempty PLEs and
checks the inequality using rational arithmetic. Its domain enumeration is
exhaustive because it considers each of the $2^8-1$ nonempty induced ground
sets and recursively chooses every minimal remaining element. Every produced
order is a linear extension; conversely, the first element of any linear
extension is minimal, so induction on the ground-set size shows that every PLE
is produced, exactly once. The empty PLE also obeys the inequality $0\le0$ and
cannot help cover a requirement.

Now let $\{M_i\}$ be any local realizer. Every one of the 45 requirements is
covered. Summing its nonnegative dual weight first over requirements and then
over PLEs gives

\[
16
\le \sum_i \bigl(\hbox{weight covered by }M_i\bigr)
\le \sum_i |M_i|.
\]

Thus every local realizer has cost at least $16$. Together with the upper
certificate, the minimum cost is exactly $16$. Since $|B_3|=8$,

\[
\operatorname{rdim}(B_3)=16/8=2.
\]

## Replay

From the project directory, run:

```sh
python3 evidence/verify_certificate.py --output evidence/verification.json
```

The checker uses only the Python standard library, regenerates the PLE domain
instead of trusting a solver export, and cross-checks the recursive enumeration
against a second method that filters all 109,600 nonempty partial permutations.
It also validates the frozen `source.md` digest and writes a deterministic JSON
summary.
