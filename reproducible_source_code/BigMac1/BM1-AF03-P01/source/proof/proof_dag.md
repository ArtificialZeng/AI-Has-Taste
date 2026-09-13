# Proof dependency graph

## Main theorem

`T0`: for every \(n\ge9\) and intersecting
\(\mathcal F\subseteq\binom{[n]}4\), \(\delta_3(\mathcal F)\le1\).

```text
negation δ3≥2 + fixed E∈F
        |
        v
L1: exterior triple identity d_F(T)=|C(T)|≥2
        |
        +----------------------------+
        |                            |
        v                            v
L2: |X|≥6, two disjoint triples      L3: n=9 forcing choices x_e
        |                            |
        v                            v
distinct labels give disjoint edges  L4: e↦x_e injective; unused x0
                                     |
                                     v
                              L5: mixed triples force type-(2,2) edges
                                     |
                                     v
                              L6: fixed S has |C(S)|=2 and ≥3
        |                            |
        +--------------+-------------+
                       v
                 contradiction → T0
```

Dependencies use only definitions, finite set complementation, and integer
counting.  No cited theorem, solver output, or proof assistant is in the main
proof chain.  The independently checked LRAT certificates bind the two
original finite endpoints but are a separate verification chain.
