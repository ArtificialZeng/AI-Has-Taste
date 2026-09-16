# Exact cheapest test: degree one

This calculation uses equation (60) with \(p=1\) and arbitrary
\(D:=\gamma_D>1\).  Write \(u'(x)=c\), \(q'(x)=b\), and use
\(y:=q(\kappa)\) in place of the free constant coefficient of \(q\).  Then
\[
a^{(2)}_{\kappa,\gamma}
=c^2+\kappa b^2-2by+Dy^2+\gamma(b-c)^2.
\]
Completing the two independent squares gives
\[
Dy^2-2by=D(y-b/D)^2-b^2/D,
\]
and
\[
c^2+\gamma(b-c)^2
=(1+\gamma)\left(c-\frac{\gamma b}{1+\gamma}\right)^2
+\frac{\gamma}{1+\gamma}b^2.
\]
Consequently the form is positive semidefinite exactly when
\[
\kappa-\frac1D+\frac{\gamma}{1+\gamma}\geq0.
\]
Thus
\[
\tau_1(\kappa)=
\begin{cases}
\dfrac{1-D\kappa}{D-1+D\kappa},&0<\kappa<1/D,\\[4pt]
0,&1/D\leq\kappa<1.
\end{cases}
\]
For the required \(D=10\), this is strictly decreasing on
\((0,1/10)\), so
\[
\Gamma_1=\frac19,
\]
with no interior maximizer; it is realized only by the limiting cut
\(\kappa\to0^+\).  The displayed completion of squares is an exact PSD and
necessity certificate.  This settles only the \(p=1\) member, not the frozen
five-degree problem.
