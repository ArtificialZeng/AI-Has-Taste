# Chan--Oh Theorem 4.9(1): primary-source provenance and hypothesis map

- Primary source: Wai Kiu Chan and Byeong-Kweon Oh, *Representations of
  integral quadratic polynomials*, arXiv:1208.6060.
- Official source URL: `https://arxiv.org/pdf/1208.6060`.
- Retrieved: 2026-09-06 (Asia/Shanghai).
- Local file: `bigWin-43-materials/1208.6060.pdf`.
- PDF SHA-256:
  `017aef94f27c9fce017f5cf1afe27da4a5559ea316cc80137ceae06237b08c74`.
- Exact locator: PDF page 15, definition immediately above Corollary 4.8 and
  Theorem 4.9(1), including its proof on the same page.

On PDF page 12, the source defines an `o`-coset as `M+v`, where `M` is an
`o`-lattice in a nondegenerate quadratic space, and calls it integral when
`Q(M+v)` is contained in `o`.  Definition 4.1 defines its genus by local
isometry at every place in the Dedekind set.  On PDF page 15, the source says
that `gen(M+v)` represents a nonzero target when the ambient quadratic space
represents it at every place outside the integral finite places and the local
coset represents it at every integral finite place.  Theorem 4.9(1) states
that for an `o`-coset on a positive-definite quadratic space over a totally
real number field, if the genus represents the target and `dim(M)>=5`, the
fixed coset represents the target once its field norm exceeds a
coset-dependent constant.  Unlike part (2), part (1) has no primitive-
representation hypothesis.

Required mapping for the next research pass and fresh referee:

1. Take the totally real field to be `F=Q` and its integers to be `Z`.
2. Put `V={y in Q^6: sum y_r=0}`, `Q(y)=sum y_r^2`, and
   `M=6A_5={6u: u in Z^6, sum u_r=0}`.  This is a free rank-five `Z`-lattice
   on a positive-definite quadratic space.  If
   `d=(-2,-1,0,1,2,3)` and
   `v_eps=3eps+d-(a+1)/2*(1,1,1,1,1,1)`, the four selected cosets have
   respectively

   ```
   a=1, eps={1}:       v=( 0,-2,-1, 0,1,2)
   a=1, eps={2}:       v=(-3, 1,-1, 0,1,2)
   a=3, eps={1,2,3}:   v=(-1, 0, 1,-1,0,1)
   a=3, eps={1,2,4}:   v=(-1, 0,-2, 2,0,1).
   ```

   Each vector is integral and has coordinate sum zero, so every `M+v_eps`
   is a fixed integral `Z`-coset of rank five.
3. The identity `Q(6u+v_eps)=6Q_eps(u)+D_a` has `D_1=10` and `D_3=4`.
   Thus the relevant norm target is `6n+10` for charge 1 and `6n+4` for
   charge 3.  It is a positive nonzero rational integer, and its `Q/Q` norm
   tends to infinity with `n`.
4. For every odd prime, the proof in `evidence/parity-coset-local.md` makes
   `Q_eps(u)=n` soluble over `Z_p` for each of these fixed cosets.  At `p=2`,
   the `{1}` and `{1,2,3}` cosets cover even `n`, while the `{2}` and
   `{1,2,4}` cosets cover odd `n`.  The displayed identity gives local
   representation of `6n+D_a` by the same centered coset.  At the real place,
   `6n+D_a>0` is represented by the ambient positive-definite space `V`.
   This is precisely genus representation under the definition on PDF page
   15.
5. Apply Theorem 4.9(1) separately to the even- and odd-`n` cosets for each
   charge.  Taking the maximum of their four constants gives one ineffective
   finite-exception cutoff.  This does not prove positivity below the cutoff.

The candidate makes no priority assertion.  Its contribution comparison is
only to the frozen Gerber--Norton source, which gives finite computational
support but no all-orders argument.
