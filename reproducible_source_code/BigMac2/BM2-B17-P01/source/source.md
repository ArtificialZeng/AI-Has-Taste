# bigMac-00017-p01 source statement

For integers `n>=2` and `1<=a<n/2`, define

```
D(n)   = binom(2n-2,n-1)/n,
G(n,a) = (n-2a+1) binom(n,a) binom(n-2,a-1)/(n-a),
R_n(a) = G(n,a)/D(n),
rho(n) = max_{1<=a<n/2} R_n(a).
```

Prove or disprove that `rho(n)<1` for every integer `n>=496`.

This is the exact one-variable equivalent of Conjecture 7.4 in Juan Gil,
Zhenni Liang, Ayodeji Odetola and Michael Weiner, *Points of maximal traffic
on a grid with obstruction*, arXiv:2609.01562v1, Proposition 7.2, Lemma 7.3
and Conjecture 7.4. The source verifies the claim exactly for `496<=n<=2000`
and gives the adjacent-ratio identity, but does not prove the universal range.

Primary PDF: `batches/literature/bigMac-17/2609.01562v1.pdf`.
Source status: open-supported. Preserve all quantifiers and strict inequality.
Finite exact checking, floating-point logs, or asymptotics without explicit
uniform remainder do not resolve the statement.
