# Explicit proof capsule

For `k>=2`, let `t_k=(1 2)`, `c_k=(1 2 ... k)`, and let
`e_k=c_k` for odd `k`, while `e_k=t_k c_k` for even `k`.  Then `e_k` is even
and `<t_k,e_k>=S_k`.

For unequal `m>n`, except `(4,3)`, the two elements
`(t_m,t_n)` and `(e_m,e_n)` generate `Gamma`: their projections are onto,
and Goursat plus the normal-subgroup lists of symmetric groups says the only
unequal-degree extra common quotient is `S_4/V_4 ~= S_3` at `(4,3)`.

For `m=n=k>=5`, use `(t_k,t_ke_k)` and `(e_k,e_k)`.  A proper subdirect
subgroup inside `Gamma` would be an automorphism graph.  This is impossible
because `ord(t_k)=2`, whereas `ord(t_ke_k)=k-1` for odd `k` and `k` for even
`k`.

See `audit/builder.md` for all boundary cases and exception proofs.
