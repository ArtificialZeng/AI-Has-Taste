# Final status: CERTIFIED_FINITE_RESULT

## 结论

对每个 9 个顶点的 simple graph \(G\)，若
\(e(\overline G)\le6\)，则
\[
q(G)=2.
\]
这是一个由完整规范枚举和精确代数证书支持的有限阶定理。它同时从序列化输入独立
重建已知的 \(n=7,8\) 基线，但不声称证明 \(n\ge10\) 或全阶猜想。

## 完整性与证书

- 补图同构类总数：\(n=7,8,9\) 分别为 19、44、108；component-multiset
  枚举与独立 Burnside edge-stratum 计数逐项一致。
- \(n=9\) 的不交路由为 72 个 bipartite、24 个 balanced connected join、
  12 个 exact frame。
- 14 个 frame（含 \(n=7,8\) 各一个）以 rational directions 和 positive
  rational weights 精确满足 support 与 Parseval 恒等式，从而给出
  \(Q=I-2VV^{\mathsf T}\in S(G)\) 且 \(Q^2=I\)。
- 主证书：`certificates/n9_exact_frames.json`，SHA-256
  `d78b49e23eaebba29d0ab70661df9688a09baabce7e0333040b43186a808fd5d`。
- 独立验证器：`verification/verify_n9_certificate.py`，SHA-256
  `5b298d8cac3eb4a890308475aa0f93f2dd0565e76d6150902b7737e3f2b49613`。

## 对抗审计

验证器不 import 或读取 discovery 结论，所有决定性检查使用 exact
`Fraction`、图分解和 Burnside 计数。合法证书通过；18 个维护的损坏输入全部拒绝。
独立裁判另用 fresh nauty、bit-graph 分类、canonical labeling 和第二套 SymPy
`Rational` 运算重建结论。裁判发现的两批 parser major 问题均已修复；最终报告没有
未解决的 fatal/major issue，见 `audit/agent_referee_report.md`。

## 新颖性、引用与发布审计

截至 2026-08-29 的 Gate 1 和论文冻结后的 Gate 6 检索均未找到公开的完整
\(n=9\) 解答或同端点 exact certificate。该否定结论严格限于记录的数据库、查询和
日期；Fei--Luo arXiv:2608.27227v1 处理的是不同的 path-complement
multiplicity endpoint。

五条论文引用全部绑定到 primary source 和具体 theorem/location；LaTeX 审计为
`cited=5 bib=5 missing=0 unused=0`。洁净构建无最终 warning，五页 PDF 已逐页检查，
作者、单位和两个邮箱均与授权信息一致。详细记录见 `audit/`，最终目录由
`release/MANIFEST.json` 绑定。

## 复现

```bash
python verification/verify_n9_certificate.py certificates/n9_exact_frames.json
python verification/test_fail_closed.py
python /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py \
  release release/MANIFEST.json
```

预期输出分别包含 `"status": "VERIFIED"`、
`PASS: valid certificate accepted; 18 damaged certificates rejected` 和
manifest 的 `verified ... files`。

## 证明助手

未使用 Lean、Coq、Isabelle 或其他证明助手；没有声称任何未实际绑定的 formal
theorem endpoint。
