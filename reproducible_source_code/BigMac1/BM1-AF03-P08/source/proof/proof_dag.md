# Proof dependency graph

```text
F1  rank-matrix Bruhat criterion
F2  subword property for the reduced word Omega_n
F3  Dyer recurrence for tilde R
F4  ordinary R recurrence and exact change of variables
F5  deg(F_h)=floor(h/2)

E1  full S_n filter below v_n                         [F1]
E2  2^(2n-4) subword set equals E1                   [F2, exact set check]
E3  all comparable pairs regenerated                 [E1, F1]
E4  exact normalized B_uv reconstructed              [E3, F3, rank induction]
E5  complete degree<=8 Fibonacci monoid catalog      [F5, exact enumeration]
E6  every E4 value belongs to E5                     [6,229,297 exact checks]
E7  ordinary R evaluator gives the same class        [E3, F4, exact checks]
E8  n=2,...,9 baseline passes                        [E1--E7]
E9  malformed/tampered inputs fail closed            [parser/rejection suite]
E10 index-sum pattern classes equal observed classes [exact set equality]

T10 n=10 finite product theorem                      [E1--E10]
```

`T10` has no dependency on the discovery output under `experiments/breaker/`.
The all-$n$ conjecture would additionally require a structural induction or block
decomposition not supplied by this DAG.
