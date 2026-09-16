# Frozen source — win-00045-p02

Fix a real parameter `a>0`.  For `k>=0`, write

> `e_k(x)=x(x-1)...(x-k+1)/(a)_k`

with `e_0=1`, and let `L_a` be the linear map sending the normalized falling-factorial basis element `e_k` to `x^k`.

Decide the following first nontrivial low-degree case of the multiplication-closure problem:

> For every `a>0` and all polynomials `P_1,P_2` with `deg(P_1)=1` and `deg(P_2)=2`, if every zero of `L_a(P_1)` and `L_a(P_2)` lies in `[-1,0]`, must every zero of `L_a(P_1 P_2)` also lie in `[-1,0]`?

Equivalently, put

> `L_a(P_1)=x+r`,  `L_a(P_2)=(x+s)(x+t)`

for `r,s,t in [0,1]`.  Using

> `e_m e_n = sum_{j=0}^{min(m,n)} binom(m,j) binom(n,j) j! (a)_{m+n-j}/((a)_m(a)_n) e_{m+n-j}`,

the polynomial `R=L_a(P_1P_2)=c_0+c_1 x+c_2 x^2+c_3 x^3` has

> `c_0=rst`,
>
> `c_1=r(s+t)+st+(s+t)/a`,
>
> `c_2=r+((a+1)(s+t)+2)/a`,
>
> `c_3=(a+2)/a`.

A disproof must give exact admissible parameters (preferably rational) and a rigorous root-isolation certificate showing a zero outside `[-1,0]` or a nonreal zero.  A proof must cover the full semialgebraic parameter domain `a>0`, `0<=r,s,t<=1`; finite sampling or floating-point root finding is not a proof.  Exact Sturm sequences, discriminant/subresultant analysis, or a reproducible CAD certificate are suitable routes.

This is a deliberately narrower target than Open Problem 1.9 of Anna Vishnyakova, *Polynomially Deformed Normalized Pochhammer Sequences Having Generating Functions With Only Real Non-positive Zeros*, arXiv:2608.03723v1.  Theorem D proves multiplication closure only for `a=1`; Theorem 1.7 is a sufficient condition and does not settle the stated all-`a` low-degree case.

Primary PDF: `bigWin-45-materials/2608.03723.pdf`, SHA-256 `39aea7f8121ec98de64b9307066dcb6a9bf5daf67840584c9d27d52c8ab1d291`.

