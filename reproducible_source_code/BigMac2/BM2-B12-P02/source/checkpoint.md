# Checkpoint

Research job: `bigMac-00012-p02-research-c0f1856efc40` (pass 1,
2026-09-07). Original status on entry: unresolved.

## New decisive evidence

Write `a=σ'_0`, `b=σ_0`, `c=σ_1`, `d=σ_2`. Exact Coxeter/root calculation
gives the full alternating normal form

`[Δ]=(db,ca,bcdcb,aca)`.

The four maximal right-tail steps, from right to left, are

1. `dbcabcdcbaca=(dbcabcdcb)(aca)`, the `{a,c}`-tail is `aca`;
2. `dbcabcdcb=(dbca)(bcdcb)`, the `{b,c,d}`-tail is `bcdcb`;
3. `dbca=(db)(ca)`, the `{a,c}`-tail is `ca`;
4. `db=(1)(db)`, the `{b,c,d}`-tail is `db`.

All factorizations are Coxeter-length additive. At each step the residual has
no right descent in the applicable parabolic. The exact verifier additionally
enumerates all elements of the parabolic groups (orders 6 and 24), identifies
all parabolic right suffixes, and checks every one right-divides the displayed
tail. This certifies greatestness of each tail, rather than only exhibiting a
parabolic suffix. Both the source word and the displayed factorized word are
reduced length-12 representatives of `w_0=-I_4`, hence give the same positive
simple lift by Matsumoto's theorem.

The leftmost factor is `db=bd`; its atom left-divisors are exactly `{b,d}` by
the exact left-descent calculation. Consequently

`L*(Δ,S)={σ_0,σ_2}=Φ_Δ(S_2⊟S_1)`.

Using the Corollary 4.7 implication frozen in `problem.md`, this proves
`dpt(Δ^m)-1=m(dpt(Δ)-1)` for every `m>=1`. Substitution at `m=pt` and `m=p`
then proves Condition A for every base power `Δ^p` and every `t>=1`; this is
not a finite-power extrapolation.

Decisive artifacts:

- `evidence/d4_alternating_certificate.md` gives the proof and tail table.
- `evidence/verify_d4_alternating.py` is the reproducible exact certificate.
- The verifier checks the immutable `source.md` hash
  `68c77ce76e18be01e19e9c878d344f7d933fcdb187acd250853f21610efae2ff`.

## Obstacles and audit status

No mathematical gap is presently known within the frozen `D_4` scope. The
claim has not yet received the required fresh mathematical referee audit, so
this research pass proposes a candidate and does not certify acceptance.
The earlier literature search was limited and supports only the source-relative
open-status statement already recorded in `problem.md`; no priority claim is
made.

## One next test

Fresh referee: independently reconstruct the four parabolic decompositions
from the frozen words (preferably without trusting the supplied factorization),
check the simple-lift/parabolic-tail lemma and the Corollary 4.7 hypotheses, and
try to falsify the claimed left-descent set of `db`.
