# Independent length-9 baseline audit

## Result

The reported conflict is real: under the corrected disk stated in the user
task, the length-9 regular word

\[
w=\varepsilon LRLRLRLRL
\]

is already an exact counterexample.  Thus the paper's claim that the conjecture
was verified for all words through length 9 is incompatible with the natural
parameter repair used in this project.

This audit did not read or import any main-thread discovery code or JSON.  It
started from the original paper's recursive cover relations and directly
enumerated linear extensions.

## Independent exact reconstruction

The 22-element source poset has 5,741 linear extensions.  Their exact descent
enumerator is

\[
h^*(w;z)=1+19z+145z^2+575z^3+1289z^4+1683z^5
+1289z^6+575z^7+145z^8+19z^9+z^{10}.
\]

Let

\[
u=2t+13,\qquad s=u^2.
\]

The corrected disk \(|t+13/2|\le11/2\) is equivalent to \(|u|\le11\), hence
to \(|s|\le121\) for a root with \(s=u^2\).  Reconstructing \(22!L(t)\) in
the binomial basis gives the integer identity

\[
2^{22}22!L\!\left(\frac{u-13}{2}\right)
=\prod_{k\in\{1,3,5,7,9,11\}}(u^2-k^2)(u^2-1)R(u^2),
\]

where

\[
R(s)=5741s^4+1132460s^3+121839662s^2
+3606687468s+64103928525.
\]

## Exact isolating disk

Set \(c=-82+91i\) and \(r=1/2\).  For
\(R(c+v)=\sum_{j=0}^4a_jv^j\), direct Gaussian-integer evaluation gives

\[
\begin{aligned}
a_0&=-3538359412+2090315136i,\\
a_1&=12454208952-3678772552i,\\
a_2&=-210377920-204910524i,\\
a_3&=-750588+2089724i,\\
a_4&=5741.
\end{aligned}
\]

Their recomputed exact norm bounds are

\[
\begin{aligned}
|a_0|&<4110000000,& |a_1|&>12980000000,\\
|a_2|&<294000000,& |a_3|&<2221000,& |a_4|&\le5741.
\end{aligned}
\]

On \(|v|=1/2\), the lower bound for \(|a_1v|\) exceeds the upper bound for
the other terms by

\[
\frac{36899552259}{16}>0.
\]

Rouché's theorem therefore isolates exactly one algebraic root \(s_0\) of
\(R\) in \(|s_0-c|<1/2\).  The entire disk lies outside \(|s|=121\), because

\[
|c|^2-\left(121+\frac12\right)^2
=15005-\frac{59049}{4}=\frac{971}{4}>0.
\]

Thus \(|s_0|>121\).  For either \(u_0^2=s_0\) and
\(t_0=(u_0-13)/2\), the exact factorization gives \(L(w;t_0)=0\), while

\[
|t_0+13/2|=|u_0|/2=\sqrt{|s_0|}/2>11/2.
\]

This strictly disproves the corrected disk conjecture already at length 9.

For localization only,

\[
s_0\approx-81.6911753099+90.9240584149i,
\]

and one corresponding Ehrhart root is

\[
t_0\approx-4.2488695943+5.0488000486i,
\qquad |t_0+13/2|\approx5.5279263775>5.5.
\]

No decimal is used by the certificate.

## Verification

From the project root:

```bash
python -I discovery/breaker_length9_verify_counterexample.py \
  experiments/breaker_length9_counterexample_certificate.json
PYTHONDONTWRITEBYTECODE=1 python discovery/breaker_length9_test_rejections.py
```

The verifier reconstructs the poset, all 5,741 linear extensions, \(h^*\),
the Ehrhart numerator, the factorization, all Taylor coefficients, all norm
bounds, the strict Rouché inequality, and the outside-disk separator.  It does
not import a discovery program.  Eight corrupted certificates are required to
fail closed.

No proof assistant (Lean, Coq, Isabelle, or other) was used.

Recorded execution environment: Python 3.13.5 (Anaconda build, Clang 14.0.6)
on macOS 26.5 arm64.  The verifier itself uses only the Python standard
library.
