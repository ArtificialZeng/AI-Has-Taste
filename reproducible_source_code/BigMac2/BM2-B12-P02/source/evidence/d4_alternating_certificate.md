# Exact certificate for the `D_4` alternating normal form

This file uses the letter convention

`a=σ'_0`, `b=σ_0`, `c=σ_1`, `d=σ_2`.

All claims below are exact. The companion verifier
`evidence/verify_d4_alternating.py` uses integer root matrices and exhaustively
enumerates the relevant finite Coxeter and parabolic groups; it contains no
floating-point or randomized step.

## Tail lemma used

For a finite Coxeter group `W`, let `underline(w)` denote the simple lift of
`w` to its positive Artin monoid. If `J` is a set of simple reflections and
the parabolic decomposition is

`w = w^J w_J`, with `w_J in W_J`, length additive, and with `w^J` having no
right descent in `J`, then

`τ_J(underline(w)) = underline(w_J)`.

Indeed, the displayed length-additive factorization lifts to the monoid. A
right divisor of a simple element is simple. Thus any right divisor belonging
to the parabolic monoid is the lift of a parabolic weak-order suffix of `w`;
the standard parabolic decomposition makes every such suffix a right divisor
of `w_J`. Hence `underline(w_J)` is the greatest, not merely a maximal,
parabolic right divisor. In the four instances below, the verifier also
checks this last assertion directly: it enumerates every element of `W_J`,
selects all length-additive right suffixes, and verifies that each right-divides
the proposed tail.

## The simple lift and its four maximal tails

Use the `D_4` simple roots

`α_b=e_1-e_2`, `α_c=e_2-e_3`, `α_d=e_3-e_4`, and `α_a=e_3+e_4`.

The source word is

`bacbacdcbacd`.

Its successive Coxeter lengths are exactly `1,2,...,12`, and its root matrix
is `-I_4`. Since `D_4` has twelve positive roots, this is the longest element
`w_0`, so the source word is a reduced representative of the simple element
`Δ`. The word

`dbcabcdcbaca = (db)(ca)(bcdcb)(aca)`

is another reduced word with the same matrix. Matsumoto's theorem therefore
identifies their positive lifts using only the defining Artin braid relations.

Starting on the right, the exact parabolic decompositions are:

| step | `J` | element before | maximal tail | residual | lengths before = residual + tail |
|---:|:---:|:---|:---|:---|:---:|
| 1 | `{a,c}` | `dbcabcdcbaca` | `aca` | `dbcabcdcb` | `12=9+3` |
| 2 | `{b,c,d}` | `dbcabcdcb` | `bcdcb` | `dbca` | `9=4+5` |
| 3 | `{a,c}` | `dbca` | `ca` | `db` | `4=2+2` |
| 4 | `{b,c,d}` | `db` | `db` | `1` | `2=0+2` |

The residual at each row has no right descent in the indicated `J`. An exact
root certificate is:

- after step 1: `a -> e_2-e_3`, `c -> e_3+e_4`;
- after step 2: `b -> e_2-e_4`, `c -> e_3+e_4`, `d -> e_1-e_3`;
- after step 3: `a -> e_3+e_4`, `c -> e_1-e_4`;
- after step 4 the residual is the identity.

Every displayed image is a positive `D_4` root. For additional finite
greatestness checks, the numbers of parabolic right suffixes at steps 1--4 are
respectively `6,12,3,4`; their length histograms are respectively

`(1,2,2,1)`, `(1,2,3,3,2,1)`, `(1,1,1)`, and `(1,2,1)`.

The tail lemma now gives the complete alternating normal form

`[Δ] = (db, ca, bcdcb, aca)`,

or, in the source's notation,

`[Δ] = (σ_2σ_0, σ_1σ'_0, σ_0σ_1σ_2σ_1σ_0, σ'_0σ_1σ'_0)`.

## The left-divisor set and Condition A

The leftmost factor is the simple element `db=bd`. Its Coxeter left descent
set is exactly `{b,d}`: the verifier checks `ell(s db)<ell(db)` precisely for
`s=b,d`, and not for `s=a,c`. Therefore

`L*(Δ,S) = {σ_0,σ_2}`.

As recorded in `problem.md`, `Δ` is central, so `Φ_Δ` is the identity, while
`S_1^perp` is empty. Hence

`Φ_Δ(S_2 boxminus S_1)={σ_0,σ_2}=L*(Δ,S)`.

For completeness, the stipulated Corollary 4.7 implication now gives Condition
A for the base `Δ`:

`dpt(Δ^m)-1 = m(dpt(Δ)-1)` for every integer `m>=1`.

Applying this once with `m=pt` and once with `m=p` yields, for arbitrary
integers `p,t>=1`,

`dpt(Δ^(pt))-1 = pt(dpt(Δ)-1)
                 = t(dpt(Δ^p)-1)`.

Thus the frozen all-powers assertion follows; no finite extrapolation in `p`
or `t` is used.

The immutable `source.md` SHA-256 checked by the verifier is
`68c77ce76e18be01e19e9c878d344f7d933fcdb187acd250853f21610efae2ff`.
