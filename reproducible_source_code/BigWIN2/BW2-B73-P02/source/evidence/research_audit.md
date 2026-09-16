# Independent research audit of the sharp threshold

Date: 2026-09-08.  Job: `win-00073-p02-research-479cdddb82ca`.

This audit uses the canonical representatives `0,...,p-1` for elements of
`F_p`.  It is independent of the coefficient-expansion and pair-enumeration
loops in `verify_small_primes.py`; that script remains the exact machine replay
of equations (4)--(5).

## 1. Coefficient/digit extraction

Put `e=(p-1)/2` and

`(x^3+A*x+B)^e = sum_k c_k x^k`.

If a monomial contributing to `c_(p-1)` chooses `i` copies of `x^3`, `j`
copies of `A*x`, and `k` copies of `B`, then

`i+j+k=e`, `3i+j=p-1`,

and its contribution is `e!/(i!j!k!)*A^j*B^k`.  Applying this formula gives:

| `(p,A,B)` | `e` | contributing `(i,j,k)` | exact coefficient `c_(p-1)` | `c_(p-1) mod p` |
|---|---:|---|---:|---:|
| `(5,1,1)` | 2 | `(1,1,0)` | `2!/(1!1!)*1 = 2` | 2 |
| `(7,0,1)` | 3 | `(2,0,1)` (all `j>0` terms vanish) | `3!/(2!1!)*1 = 3` | 3 |
| `(11,1,3)` | 5 | `(3,1,1)` | `5!/(3!1!1!)*1*3 = 60` | 5 |
| `(13,0,4)` | 6 | `(4,0,2)` (all `j>0` terms vanish) | `6!/(4!2!)*4^2 = 240` | 6 |

These are also the literal equation-(4) digits, not merely congruent values.
Indeed, with `w=p^2`, evaluating the polynomial at `2^w` gives

`(2^(3w)+A*2^w+B)^e = sum_k c_k 2^(wk)`.

All coefficients are nonnegative, and their sum is respectively
`3^2=9`, `2^3=8`, `5^5=3125`, and `5^6=15625`; each is less than the
corresponding base `2^w`.  There is therefore no carry between base-`2^w`
digits.  Division by `2^(w(p-1))` and reduction modulo `2^w` extracts exactly
the displayed coefficient.  Thus the four exact extracted digits are
`2,3,60,240`, and the outer reductions modulo `p` give

`r = 2,3,5,6`.

The direct big-integer evaluation in `verify_small_primes.py` independently
returns those same four digits.

## 2. Direct affine point counts

For `t in F_p`, the number of `y` satisfying `y^2=t` is 1 for `t=0`, 2
for a nonzero quadratic residue, and 0 otherwise.  The following tables list
`f(x)=x^3+A*x+B mod p` for every `x`; hence they are complete enumerations of
the affine counts.

| `(p,A,B)` | nonzero square residues | `f(0),...,f(p-1)` | zero / nonzero-square / nonsquare inputs | `N` |
|---|---|---|---|---:|
| `(5,1,1)` | `{1,4}` | `1,3,1,1,4` | `0 / 4 / 1` | `0+2*4=8` |
| `(7,0,1)` | `{1,2,4}` | `1,2,2,0,2,0,0` | `3 / 4 / 0` | `3+2*4=11` |
| `(11,1,3)` | `{1,3,4,5,9}` | `3,5,2,0,5,1,5,1,6,4,1` | `1 / 8 / 2` | `1+2*8=17` |
| `(13,0,4)` | `{1,3,4,9,10,12}` | `4,5,12,5,3,12,12,9,9,5,3,9,3` | `0 / 10 / 3` | `0+2*10=20` |

For all four rows `r^2 <= 4p`.  Consequently the indicator term in equation
(5) is zero and `Nhat=p-r`, giving respectively `3,4,6,7`.  These differ from
the complete affine counts `8,11,17,20` in every row.

Finally,

`4A^3+27B^2 mod p = 1,6,5,3`,

respectively, so all four witnesses are nonsingular (though nonsingularity is
not needed to refute a universally quantified formula).

## 3. Upper range and hypothesis match

The live primary source is Bogdan Dumitru and Mihai Prunescu, *Short arithmetic
terms express the cardinality of elliptic curves in Weierstrass normal form
over finite fields*, arXiv:2609.05371v1 (2026-09-04), especially Lemmas 4--6
and Theorem 3:

<https://arxiv.org/html/2609.05371v1#S5.Thmthm3>.

Theorem 3 has exactly the hypotheses needed here: `p>=17` is prime; `A,B` are
arbitrary natural numbers and are reduced modulo `p`; equation (4) has
`w=p^2`, exponent `floor(p/2)`, the same division and the same two remainders;
equation (5) uses the same truncated subtraction; and `N` counts affine pairs
in `(Z/pZ)^2`.  It explicitly covers repeated-root (singular) cubics.  Taking
the canonical natural representatives of arbitrary `A,B in F_p` therefore
proves `P(p)` for every prime `p>=17`.

For completeness, the source proof obtains `r = a_p mod p`, where `a_p=p-N`,
and Lemma 6 gives `|a_p|<=2 sqrt(p)` in both the singular and nonsingular
cases.  When `p>=17`, `p-2 sqrt(p)>2 sqrt(p)`, so exactly one of `r` and
`r-p` lies in that interval; the test `r^2<=4p` selects it and yields equation
(5).  This also confirms why the theorem's stated lower bound is relevant.

The primes `5,7,11,13` are the complete list of primes with `3<p<17`, and the
tables above disprove `P(p)` at each one.  Combined with Theorem 3, this proves
the frozen biconditional for every odd prime `p>3`.

Targeted web searches of arXiv by identifier, exact title, formula fragments,
and the phrase “threshold 17” on 2026-09-08 found the cited v1 paper but no
separate primary source stating this sharp-threshold corollary.  This is a
bounded comparison, not a claim of priority.  The author attribution in
`source.md` is bibliographically wrong; the linked paper's live v1 record names
Dumitru and Prunescu.  The title, formulas, theorem number, and mathematical
content match the linked source.
