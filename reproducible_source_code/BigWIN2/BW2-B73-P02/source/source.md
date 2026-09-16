# win-00073-p02 — Sharp prime threshold for the arithmetic point-count formula

For every odd prime `p>3` and every `A,B in F_p`, compute `r` exactly by
equation (4) of arXiv:2609.05371v1 and compute `Nhat(A,B,p)` by its equation
(5).  Decide whether

`for all A,B in F_p, Nhat(A,B,p) = #{(x,y) in F_p^2 : y^2=x^3+Ax+B}`

holds if and only if `p>=17`.

Theorem 3 of the source proves the sufficient direction for every `p>=17`.
For necessity, independently verify or refute the following proposed exact
counterexamples `(p,A,B,N,r,Nhat)`:

- `(5,1,1,8,2,3)`;
- `(7,0,1,11,3,4)`;
- `(11,1,3,17,5,6)`;
- `(13,0,4,20,6,7)`.

The four discriminants `4A^3+27B^2 mod p` are respectively `1,6,5,3`, so the
proposed witnesses are nonsingular.  A valid result must show the integer
evaluation of equation (4), direct point enumeration, and an independent
replayable verifier; a mismatch in any row defeats the proposed certificate.

Primary source: Arno Fehm and Kurt Girstmair, *Short arithmetic terms express
the cardinality of elliptic curves in Weierstrass normal form over finite
fields*, arXiv:2609.05371v1, Lemmas 4--6 and Theorem 3, printed pp.7--8:
https://arxiv.org/abs/2609.05371v1 .  The sharp-threshold formulation and the
four small-prime witnesses are supervisor-generated, not source claims.
