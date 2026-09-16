# Research proof audit: nonexistence of `SDS(9,8,1,C_3^2)`

Date: 2026-09-10 (Asia/Shanghai)  
Job: `win-00086-p05-research-236d0a28a39b`  
Frozen statement: `source.md`, SHA-256
`d75270377823488dfaa65912e4a0a2bd57b396960d1b0ebb4865216db77bfb7f`

## Exact theorem

There is no coefficient function

\[
 a:\mathbb F_3^2\longrightarrow\{0,1,-1\}
\]

having exactly eight nonzero values and satisfying

\[
 DD^{(-1)}=7[0]+\sum_{x\in\mathbb F_3^2}[x],
 \qquad D=\sum_x a_x[x].
\]

Thus `SDS(9,8,1,C_3^2)` does not exist.

## Complete argument

Assume that such a `D` exists. Applying the principal character to the
displayed identity gives

\[
 \left(\sum_x a_x\right)^2=7+9=16.
\]

If `p` and `n` are the numbers of positive and negative coefficients, then
`p+n=8` and `p-n=\pm4`. Multiplying all coefficients by `-1` if necessary
therefore gives `p=6` and `n=2`. This global sign change leaves
`DD^{(-1)}` unchanged.

There is a unique zero position `z`. Translating by `-z` replaces the
coefficient at `x` by `a_{x+z}` and leaves every autocorrelation coefficient
unchanged. Hence the zero can be put at `0`. If the two negative positions
are distinct nonzero vectors `a,b`, the normalized group-ring element is

\[
 D=\sum_{x\ne0}[x]-2([a]+[b]). \tag{1}
\]

Let `\omega` be a primitive cube root of unity, and for nonzero
`u\in\mathbb F_3^2` define the nonprincipal character

\[
 \chi_u(x)=\omega^{u\mathbin\cdot x}.
\]

Applying `\chi_u` to the assumed group-ring identity gives the necessary
condition

\[
 |\chi_u(D)|^2=7, \tag{2}
\]

because `\sum_x\chi_u(x)=0`. The same equality also shows that
`\sum_{x\ne0}\chi_u(x)=-1`; hence (1) yields

\[
 \chi_u(D)=-1-2\bigl(\chi_u(a)+\chi_u(b)\bigr). \tag{3}
\]

The pair `{a,b}` has exactly one of the following two types. If it is
linearly dependent, then, since its members are distinct and nonzero over
`\mathbb F_3`, necessarily `b=-a`. Choose a nonzero `u` in the kernel of the
nonzero functional `u\mapsto u\cdot a`. Then `u\cdot a=u\cdot b=0`, and (3)
gives

\[
 \chi_u(D)=-5,\qquad |\chi_u(D)|^2=25\ne7,
\]

contradicting (2).

Otherwise `a,b` are a basis. The linear map

\[
 u\longmapsto(u\cdot a,u\cdot b)
\]

is then invertible, so there is a unique `u` with
`u\cdot a=u\cdot b=1`; this `u` is nonzero. Equation (3) gives

\[
 \chi_u(D)=-1-4\omega.
\]

Using `\omega+\omega^2=-1`, its exact Eisenstein norm is

\[
 (-1-4\omega)(-1-4\omega^2)
 =1+4(\omega+\omega^2)+16=13\ne7,
\]

again contradicting (2). The two cases exhaust every possible pair, so the
assumed `D` cannot exist.

## Symmetry and coverage audit

The proof does not discard any pair merely by naming a representative. For
comparison with the frozen statement's requested symmetry check, the four
opposite unordered pairs are precisely the four one-dimensional subspaces of
`\mathbb F_3^2`; the remaining `\binom82-4=24` pairs are bases. `GL(2,3)` is
transitive on each class, so these are exactly its two orbits, of sizes 4 and
24. Translation and global sign were justified directly above, and an
automorphism only permutes group elements and characters.

`evidence/research_independent_audit.py` is an independently written exact
replay (SHA-256
`ee66fdeb572b2073eda05fe26cc4b4bd90bf2851ceef6d8e3f20f0436f6ec8a5`).
It imports neither earlier checker. It verifies:

- all 2,304 raw placements/sign assignments;
- all 504 assignments allowed by the principal-character equation;
- normalization onto all 28 pairs, each with exactly 18 raw preimages;
- all 48 matrices in `GL(2,3)` and orbit sizes 4 and 24;
- four selected characters of norm 25 and 24 selected characters of norm 13;
- zero raw solutions by exact integer autocorrelation.

Its output ends with

```text
character_certificates=opposite:4:norm25,independent:24:norm13
raw_solutions=0
RESULT=PASS: normalization, orbit exhaustion, and all exact character obstructions verified
```

The finite computation corroborates the proof but is not needed for its
logical completeness. Known proof gaps: none identified in this research
pass. The candidate still requires a fresh referee audit.
