# Final status: PROVED

## 结论

对所有 \(n\ge0\)，将 \(4\times2n\) 棋盘按固定的四元矩形群
\(G=\{1,h,v,hv\}\) 取轨道（包括 \(n=2\) 的正方形特例），A321614 的
生成函数为

\[
A(x)=\frac{1-8x+29x^2-52x^3+34x^4+11x^5-8x^6-15x^7+6x^8}
{1-12x+54x^2-98x^3-17x^4+346x^5-505x^6+210x^7+120x^8-126x^9+27x^{10}}.
\]

该分式已约分，因此分母次数恰为 10。于是题给 Barker 递推对每个
\(n\ge10\) 成立，并且不存在更低阶的常系数齐次标量递推。

## 决定性证据

- 从 king 攻击定义独立重建出的 12 状态自动机；
- 四个 Burnside 分支的精确整数多项式 resolvent 等式；
- 68 维整数线性表示上的 68 个连续零矩，结合 Cayley--Hamilton 得到
  全 \(n\) 结论；
- 分子分母的精确有理 Bezout 恒等式，证明 gcd 为 1；
- 第二套结构不同的证书与 verifier，以及独立枚举/对抗审计；
- 第二轮 referee、二次 novelty 检索、20/20 引用审计、LaTeX 审计、
  洁净构建和 5 页逐页 PDF 检查均通过。

## 必要限制

OEIS 的数值 \(a(2)=23\) 对应固定四元群，而不是正方形的完整八元
\(D_4\)。若在 \(n=2\) 改用完整 \(D_4\)，精确轨道数为 14，原递推在
\(n=10,11,12\) 分别出现非零残差；因此该字面版本并非本定理。

## 复现命令

```sh
make verify
python3 code/verify_certificate.py certificate/a321614_certificate.json
python3 agents/builder/verify_certificate.py
python3 agents/referee/verify_no_import.py certificate/a321614_certificate.json
python3 code/test_fail_closed.py --python /usr/bin/python3 --python /opt/homebrew/bin/python3
python3 agents/breaker/verify_audit.py agents/breaker/audit_output.json
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py release/frozen release/manifest.json
```

没有使用 Lean、Coq、Isabelle 或其他证明助手。决定性步骤均由所附
Python verifier 以精确整数/有理数运算复核。
