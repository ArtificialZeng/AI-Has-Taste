# Proof dependency graph

## Length-10 endpoint

```text
S0  source Definition 2.1/2.2 + Theorem 2.9
 ├─ S1  actual length 10 => d=24, center -7, radius 6
 └─ S2  source cover relation for w=epsilon LRLRLRLRLR
       ├─ E1  linear-extension enumeration => h* (primary verifier)
       │    └─ F1  exact binomial expansion and factorization (4)
       │         └─ R1  rational Rouché disk contains one Q-root
       │              └─ R2  disk lies strictly outside |y|=36
       │                   └─ C  choose x^2=y, rho=x-7 => |rho+7|>6
       └─ E2  order-ideal multichains => same h* (independent verifier)
            └─ F2  independent factor reconstruction
                 └─ H1  exact Cayley polynomial and nonsingular Routh table
                      └─ H2  two RHP roots; positivity excludes real ones
                           └─ C  Q has a conjugate pair with |y|>36
```

`E1/F1/R1/R2` and `E2/F2/H1/H2` share the source word and elementary
definition, but use different Ehrhart evaluators and different exact
root-location theorems.  The serialized input to the second route contains no
polynomial coefficients.

## Length-9 baseline audit

```text
S0 -> source covers for epsilon LRLRLRLRL
   -> enumerate 5,741 linear extensions and reconstruct h*
   -> exact factorization (6) in u=2t+13 and s=u^2
   -> rational Rouché disk |s-(-82+91i)|<1/2
   -> exact separator: the disk is outside |s|=121
   -> an Ehrhart root satisfies |t+13/2|>11/2
```

The length-9 route is not needed to disprove the requested length-10 universal
statement.  It independently audits and overturns the author-reported
baseline under the same corrected parameter convention.

## External-scope dependencies

- Literature metadata and the statement repair are audited in
  `audit/referee_novelty.md` and `audit/CITATION_AUDIT.md`.
- Absolute novelty, minimal failing length, and a general reversal symmetry
  are not theorem dependencies and are not claimed.
- No proof assistant is present; the exact endpoints are the theorems actually
  reconstructed by the three Python verifiers.

