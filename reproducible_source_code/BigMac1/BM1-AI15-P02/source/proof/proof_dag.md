# Proof dependency graph

## Endpoint

**T0.** Under the fixed Klein-four rectangle action (also at `n=2`), the
A321614 generating function is Barker's displayed reduced rational function;
therefore its minimal scalar recurrence has order ten and holds for every
`n >= 10`.

## Dependencies

```text
L1 maximum = 2n and equality structure
  └─ L2 bijection with paths in the exact 12-state graph
       ├─ L3 identity fixed count
       └─ L4 exact action of h, v, hv on state words
            ├─ L5 horizontal fixed count H_n=n+1
            ├─ L6 vertical parity/middle-edge formula
            └─ L7 half-turn parity/middle-state formula

C1 integer resolvent identity Z(y)(I-yT)=D0(y)1^T
  ├─ C2 identity branch rational function (uses L3)
  ├─ C3 vertical branch rational function (uses L6)
  └─ C4 half-turn branch rational function (uses L7)

L5 + C2 + C3 + C4
  └─ L8 Burnside average
       └─ C5 exact rational addition gives Barker numerator/denominator
            ├─ C6 coefficient comparison gives recurrence for all n>=10
            └─ C7 gcd/Bezout certificate gives minimal order exactly ten

D1 direct board enumeration at n=2
  └─ D2 Klein four gives 23, full square D4 gives 14
       └─ repaired formal group convention required by T0
```

## Exact evidence map

| Node | Human proof | Machine evidence | Independent cross-check |
|---|---|---|---|
| L1–L4 | `proof/main_proof.md`, Sections 1–2 | `agents/builder/certificate.json` | `agents/breaker/exact_audit.py` uses column masks rather than the root 12-state representation |
| C1–C5 | `proof/main_proof.md`, Sections 3–4 | `agents/builder/verify_certificate.py` reconstructs and checks the polynomial matrix identity | `code/verify_certificate.py` reconstructs a separate 68-dimensional global representation |
| C6 | `proof/main_proof.md`, Section 4 | 68 exact observable zeros plus Cayley–Hamilton in `certificate/a321614_certificate.json` | builder's direct resolvent certificate |
| C7 | factor remainders in `proof/main_proof.md`, Section 5 | serialized rational Bezout identity in the root certificate | independent Euclidean algorithm in builder verifier |
| D1–D2 | `proof/main_proof.md`, Section 6 | builder's raw `4 x 4` enumeration | breaker scans all `C(16,4)=1820` subsets independently |

No proof assistant is used. The only non-computational dependencies are
Burnside's lemma, Cayley–Hamilton, and the elementary fact that a reduced
rational ordinary generating function has recurrence order equal to the
degree of its denominator.
