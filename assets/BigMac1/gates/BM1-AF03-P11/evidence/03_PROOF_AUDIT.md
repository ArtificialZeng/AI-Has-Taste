# Proof audit

Audit date: 2026-08-29  
Endpoint: the finite relation at `n=7`, not Conjecture 4.4 for all `n`  
Status: **PASS**

## Audited dependency chain

1. The right-greedy legality criterion follows directly from the two
   forbidden patterns: a new top `x` creates `123` or `132` exactly when at
   least two old stack entries exceed `x`.
2. The large-label factorization was checked line by line. A large input
   cannot pop a small stack top; projected large-on-large pops may be delayed
   until the next small input or the final flush. The resulting symbolic map
   is therefore the projection of one literal stack-sort step. Iteration is
   by induction.
3. Berlow's periodicity criterion and Zhang's exact maximum transient reduce
   membership in `M_N` to a skeleton predicate with
   `m=floor((N-1)/2)`.
4. Each skeleton has exactly `(N-m)!` labelled lifts, so
   `|M_N|=|Q_N|(N-m)!`.
5. The independent verifier enumerates every skeleton at lengths 1--14. It
   obtains `|Q_13|=|Q_14|=9378` and checks the stronger set identity
   `Q_14={wL:w in Q_13}`.
6. Multiplication by `7!` and `8!` gives the two asserted integer counts.
   The set identity proves that delete-last-and-standardize has exactly the
   eight terminal-insertion inverses indexed by `j=7,...,14`.

## Independent and adversarial checks

- Enumerator A and Enumerator B agree for every length 1--14. Their
  skeleton generation, representative lifts, legality tests, and stopping
  logic differ.
- The no-import Python verifier reads only the serialized certificate and
  the bound source-statement hash. Its final SHA-256 is
  `c9d2df5bd7b28f17da0e28f09e277812a0f3a661c71af38174d5c44c2dfea46f`.
- Exhaustive literal-map/projection comparison passed 362,879 cases through
  length 8, over every relevant threshold.
- Six destructive certificate mutations were rejected: altered count,
  deleted record, duplicate record, unexpected field, Boolean substituted
  for an integer, and source-hash corruption.
- Printed Conjecture 4.3 and unrestricted deletion commutation were attacked
  and were not used: the former fails at the stated small endpoints and the
  latter is false outside the certified qualifying sets.

## Arithmetic and certificate binding

The certificate SHA-256 is
`1a3580a593bf6e5a640f0347f0c8ab385e7a5af559949b399925c2936891903e`.
The final full run returned

```text
PASS
|M_13| = 47,265,120
|M_14| = 378,120,960
378,120,960 = 8 * 47,265,120
Q_14 = {w followed by L : w in Q_13}
```

Only exact integers and complete finite enumeration are used. No random,
floating-point, modular-only, asymptotic, or heuristic step enters the
endpoint.

## Scope and formalization

The audit finds no open gap in the finite `n=7` theorem. The all-`n`
identity `Q_{2n}={wL:w in Q_{2n-1}}` remains open and is explicitly excluded
from the result. No Lean, Coq, Isabelle, or other proof assistant was used.
