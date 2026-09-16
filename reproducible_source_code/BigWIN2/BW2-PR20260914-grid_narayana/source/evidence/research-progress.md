# Research progress: rank-one commutator route

Job: primary-20260914-grid-narayana-research-12ef05d8a66f.
Original source unchanged. This interim record is superseded by the
completed `research-proof.md` and `research-verifier.json`. The trace and
coefficient steps below were resolved in that proof; `claim.json` now
requests fresh review. The runner owns freezing.

After shifting the catalytic variables x=1+u, y=1+v, the exact
column transfer is T=BA, where U_i is multiplication by its variable,
D_i deletes one power (and kills constants), E_i is constant projection,
c=1+t, A=U_1+c+tD_1, and B=U_2+c+tD_2+tD_1 E_2.
Thus [B,A]=t E_1 E_2, a rank-one operator.
The target is H_n=<0|A(BA)^(n-1)|0>.

A prospective trace calculation gives, writing S(u)=u+c+t/u,
C_(m,k)=[u^k]S(u)^m,

  H_n = 1/(n(n+1)t) sum_(k=1)^n k t^k C_(n+1,k) C_(n,k).

If the trace calculation is fully justified, this evaluates immediately:
k C_(n+1,k)=(n+1)(C_(n,k-1)-t C_(n,k+1)), so the sum telescopes
to (n+1)t C_(n,0) C_(n,1). The resulting answer is
C_(n,0) C_(n,1)/n = B_n(t) A_(n-1)(t).

Remaining work in this pass: justify the finite-rank trace/boundary
calculation and the rank-one perturbation coefficient formula; implement
exact independent matrix/transfer comparisons and adversarial checks.
This is a proof route under verification, not a claimed resolution.
