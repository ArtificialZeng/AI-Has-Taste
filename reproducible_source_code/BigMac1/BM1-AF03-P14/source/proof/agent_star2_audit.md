# Adversarial audit of the ordered `star2` Bernstein no-go

## Verdict

The mathematical certificate is valid.  An independent implementation using
only Python standard-library `Fraction` arithmetic reconstructed the chamber,
the 32-subset box-spline numerator, all four critical numerators, the selected
directional combination, and both Bernstein tables.  It exactly confirmed:

* five (P)-blocks with 14 monomials each;
* all 70 (P)-coefficients positive, with minimum 16;
* nine (H)-blocks with 125 monomials each;
* all 1125 (H)-coefficients positive, with minimum 32;
* a positive constant coefficient in every block;
* Bernstein degrees 4 and 8;
* the canonical table digest
  `7ea0e1ec667bcceb0be53f4cc437fe0ffef5d146528268054d98c39b8b82d95f`;
* the certificate digest
  `fd591e360a57668ad818ba8adb8e48d5670a211da3f43528c7f3f68517310a80`.

Thus the ordered full-support `star2` chamber closure contains no critical
direction, assuming the already-derived central-section box-spline formula.

The audit initially found one release-engineering defect: the original
verifier accepted an altered `claim` field and an altered
`critical_numerators` declaration.  This did not affect its independently
reconstructed polynomial or the theorem's mathematical truth, but it violated
the requested fail-closed binding between serialized input and endpoint.  The
root verifier was then patched to check both values exactly; its expanded
mutation suite now rejects all eight corruptions.  The independent audit
verifier also rejects both mutations.

## Independent reconstruction of the chamber chart

Put (a_4=1) and introduce ordered coordinate gaps

\[
\begin{aligned}
 a_3&=1+w, & a_2&=1+w+z,\\
 a_1&=1+w+z+y, & a_0&=1+w+z+y+x,
\end{aligned}
\qquad x,y,z,w\ge0.
\]

For a high pair (ij), use the signed margin
(2(a_i+a_j)-\sum a_k); for a low pair use its negative.  Direct expansion
shows that only the following three margins are nonredundant:

\[
 m_{02}=x+z-1,qquad m_{03}=1+z-x,qquad m_{12}=1+x-z.
\]

The first is the high-(02) margin, while the latter two are the low-(03)
and low-(12) margins.  Solving these three triangle inequalities gives

\[
 u=\frac{x+z-1}{2}\ge0,qquad
 v=\frac{1+x-z}{2}\in[0,1],
\]

with inverse

\[
 x=u+v,qquad z=u+1-v.
\]

This proves that the chart is bijective, not merely sufficient.

The audit script expanded every order, pair-sign, and polygon margin in the
nonnegative domain basis (u,y,w,v,1-v).  The ten pair margins are:

| Pair | Required sign | Exact nonnegative expansion |
|---|---:|---|
| 01 | high | (2u+2y) |
| 02 | high | (2u) |
| 03 | low | (2(1-v)) |
| 04 | low | (2(1-v)+2w) |
| 12 | low | (2v) |
| 13 | low | (2u+2v+2(1-v)) |
| 14 | low | (2u+2v+2(1-v)+2w) |
| 23 | low | (2u+2v+2(1-v)+2y) |
| 24 | low | (2u+2v+2(1-v)+2y+2w) |
| 34 | low | (4u+2v+4(1-v)+2y+2w) |

The four order margins are

\[
 a_0-a_1=u+v,quad a_1-a_2=y,quad
 a_2-a_3=u+1-v,quad a_3-a_4=w.
\]

All five polygon margins (sum a_j-2a_i) were also reconstructed as
nonnegative combinations; the smallest-looking one is

\[
 \sum a_j-2a_0=2v+4(1-v)+2w\ge2.
\]

Consequently no hidden singleton wall occurs, all coordinates remain at
least 1, and the only chamber-boundary strata are exactly the advertised pair
and coordinate-equality walls.

## Independent numerator and derivative checks

At the strict rational chart point

\[
 (x,y,z,w)=(3/2,1,3/2,1),
\]

the audit enumerated all 32 subsets in

\[
 \sum_{S\subseteq[5]}(-1)^{|S|}
 \left(T-\sum_{i\in S}a_i\right)_+^4.
\]

Exactly 16 subsets are active.  Expanding their signed fourth powers agrees
coefficient-for-coefficient with the paired expression

\[
 P=T^4-\sum_i(T-a_i)^4+
 \sum_{i<j}(T-a_i-a_j)^4
 -2\sum_{ij\in\{01,02\}}(T-a_i-a_j)^4.
\]

This direct 32-subset derivation is independent of the paired-sign
reconstruction used by both the constructor and original verifier, and it
specifically tests the easy-to-miss negative high-pair branches.

With

\[
 S=\sum_i a_i^2,qquad D=a_0a_1a_2a_3,qquad
 F=\frac{\sqrt S\,P}{D},
\]

the stated critical numerator is correct:

\[
 H_q=S_qPD+2SP_qD-2SPD_q=2SPD\,\partial_q\log F.
\]

As a second derivation, the audit verified all four exact quotient-rule
identities

\[
 D\,\partial_q(SP^2)-2SP^2D_q=P H_q,
\]

which arise by differentiating (F^2=SP^2/D^2).  Thus no factor or sign in
(H_q) is inherited uncritically from the original implementation.

At any critical direction all four (H_q) vanish, so the exact linear
combination

\[
 H=-2H_x+2H_y-2H_z+H_w

\]

must vanish as well.  The audit independently used precisely this combination
before applying the chamber substitution.

## Independent Bernstein audit

For a power-basis polynomial

\[
 f(v)=\sum_{i=0}^n c_i v^i,
\]

the degree-(n) Bernstein coefficients were independently computed from

\[
 b_k=\sum_{i=0}^k\frac{\binom{k}{i}}{\binom{n}{i}}c_i.
\]

The standard-library implementation then reconstructed the original
polynomial from

\[
 \sum_{k=0}^n b_k\binom nkv^k(1-v)^{n-k}
\]

and compared its canonical sparse tables against the JSON.  Both directions
of the identity passed for (P) and (H).

Every (P)-block contains 14 strictly positive monomial coefficients, every
(H)-block contains 125, and every block contains a strictly positive
constant.  Hence for (u,y,w\ge0), each coefficient polynomial is strictly
positive.  The Bernstein weights are nonnegative and sum to one even at
(v=0,1).  It follows that (P>0) and (H>0) throughout the entire closed
chart, including every simultaneous combination of:

* (u=0), the high-(02) wall;
* (v=0), the low-(12) wall;
* (v=1), the low-(03) wall;
* (x=0), (y=0), (z=0), or (w=0), the coordinate-equality walls.

Since a fourth positive-part power is (C^3), the first derivatives used by
the critical equations agree on pair-sum walls.  Thus the closed-wall claim
does not silently use a one-sided derivative.

## Falsification attempts

The independent script used no SymPy and imported neither the constructor nor
the original verifier.  It performed the following attacks:

1. compared direct 32-subset and paired-sign polynomials exactly;
2. checked four independent (F^2) quotient-rule identities;
3. reconstructed and compared all 1195 rational coefficients;
4. reconstructed each JSON Bernstein table back to the target polynomial;
5. checked all 19 pair/order/polygon margins symbolically;
6. evaluated (P) and (H) exactly at four boundary points and 64 seeded
   rational points, including unbounded (u,y,w) values and both endpoints of
   (v).

No falsification was found.  The smallest sampled exact values were (P=22)
and (H=72); these are diagnostics only, not global lower bounds.

## Verifier audit and mutation behavior

The original verifier correctly rejects changes to the chamber graph,
direction, domain, degree, coefficient table, and margin identity.  Its
mathematical recomputation passes.

However, these two direct mutations were accepted by the original verifier:

```text
claim = "false claim"                 -> return code 0 / PASS
critical_numerators = "wrong"         -> return code 0 / PASS
```

The cause is that `src/verify_star2_bernstein.py` checks that those keys exist
but did not compare their values.  The released verifier now contains the exact checks
for

```python
payload["claim"] ==
    "the ordered full-support star2 chamber closure has no critical direction"
payload["critical_numerators"] ==
    "Hq=S_q*P*D+2*S*P_q*D-2*S*P*D_q"
```

The original behavior was a certificate-binding defect, not a counterexample
to the theorem; it has been repaired and re-tested.

The independent verifier/audit is `src/breaker_star2_audit.py`; its result is
`experiments/breaker_star2_independent_audit.json`.  It rejects altered claim,
critical declaration, graph, direction, coefficient, and missing-domain
inputs.  The mutation log is
`experiments/breaker_star2_audit_mutation_tests.json`.

Reproduction:

```bash
python src/breaker_star2_audit.py \
  results/star2_bernstein_no_go_certificate.json \
  --output experiments/breaker_star2_independent_audit.json \
  --seed 220260829 --random-checks 64
python src/breaker_star2_audit_tests.py \
  --output experiments/breaker_star2_audit_mutation_tests.json
python src/verify_star2_bernstein.py \
  results/star2_bernstein_no_go_certificate.json
python tests/test_star2_bernstein_verifier.py
```

No Lean, Coq, Isabelle, or other proof assistant was used.  The original
certificate uses exact SymPy arithmetic; the independent audit uses a separate
standard-library sparse rational-polynomial implementation.
