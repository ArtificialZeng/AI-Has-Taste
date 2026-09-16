# 第二十三批 B23 最终审计

审计日期：2026-09-02（Asia/Shanghai）

## 队列与提示词

- 从 `23batchmath.md` 抽取 15 个题目行；附件中的建议路线、难度、证书描述和开放状态均仅作为待核验题源内容。
- 15/15 个任务提示词首行逐字符等于用户指定的 `prove-or-disprove-math` skill 调用文本。
- 15/15 个 `codex --yolo --search exec` 进程退出码为 0；15/15 个 `results/final_status.json` 可解析且通过字段、百分比和路径检查。
- 队列终态：`launched=15, active=0, final_status=15, complete=true`；最大允许并发为 4，实测峰值为 4。
- 科学终态统计：`proved` 5 项，`disproved` 2 项，`certified finite result` 5 项，`open after search` 3 项。

## 唯一通过投稿闸门的结果

**B23-01：The Alternating Extremal-Ratio Sequence A022030 Satisfies Its Conjectured Linear Recurrence**

对当前奇偶交替的严格取整递推，论文证明

\[
a_n=4a_{n-1}-a_{n-3}+a_{n-4}\qquad(n\ge4).
\]

证明定义候选线性递推 `L` 及带符号缺陷
`e_n=(-1)^n(L_{n+1}^2-L_nL_{n+2})`，先得到正系数递推

\[
231e_n=460e_{n-2}+3435e_{n-3}+3585e_{n-5}
+215e_{n-8}+30e_{n-9}+6e_{n-10},
\]

再用 `L_n>3L_{n-1}` 和精确系数和
`3801197/19683<231` 归纳证明 `1<=e_n<=L_n`。这一范围恰好处理严格 ceiling/floor 的整除端点。

根审计使用与原证书不同的 SymPy 程序，从四个符号初值独立推出缺陷递推，验证两项多项式恒等式，精确比较 5000 项线性/非线性递推，并重算系数界；全部通过。论文的无限结论来自归纳证明，不依赖有限采样。未使用 Lean 或其他证明助理。

## 文献与新颖性边界

- 当前 OEIS A022030 页面记录的是奇偶交替规则及四阶递推猜想。
- 固定 Formal Conjectures 源同样陈述奇偶交替规则，并在指定提交中保留 `sorry`。
- arXiv:2608.11941v2 的 A022030 表格行实际陈述并证明的是始终选择最大整数的旧非交替序列及其三阶递推，不是本稿的交替四阶端点。
- 最终稿有 3 个引用键和 3 个 BibTeX 条目：零缺失、零未使用、最终 AUX 完全一致。新颖性表述仅限记录的来源与 2026-09-02 检索截止日，不声称穷尽全球优先权，也不暗示同行评审或期刊接收。

## 构建、PDF 与源码 ZIP

- 最终 LaTeX 从清理后的状态收敛构建；日志无未定义引用、未定义文献、LaTeX error、emergency stop 或 fatal error。
- PDF 共 3 页，大小 291,038 字节，SHA-256 为 `84e7c8fccb0b960f32436a0c70cc3bcf91c008b63e6c304e9bf2ca8b6c60bda6`。
- PDF 标题和唯一作者元数据正确；正文署名为 Xiaojian Zeng，单位为 PBC School of Finance, Tsinghua University, 100190，邮箱为 xiaojianzeng@foxmail.com。
- 全部 3 页以 150 dpi 重新渲染并按原分辨率逐页检查；无裁切、重叠、缺字、黑块、断裂引用或异常留白。
- PDF 文本未出现 SHA-256、长十六进制摘要、Codex 或 OpenAI 字样；自动化协助披露准确且不包含厂商宣传或内部提示词。
- 最终源码 ZIP 含 22 个明确文件，大小 17,511 字节，SHA-256 为 `196f72e5317cc13f3b0e8493efd968f55cded9a47cdbfd51027a5fbe6919d1f1`。
- ZIP 在全新临时目录中通过内部 SHA 清单、两套精确验证、引用键审计和完整 LaTeX 重建；最终项目 release manifest 重新生成并验证 51 个文件。

## 其余 14 项

- B23-02、04、09、11 的原命题已由截止日前的既有工作证明；只保留审计记录，不以 Xiaojian Zeng 名义生成重复论文。
- B23-06、08 得到精确反例，但相同反例已在截止日前公开，未通过新颖性门槛。
- B23-03、07、10、12、13 仅达到认证有限范围；B23-05、14、15 仍为开放搜索终态。它们都保留范围、证书、致命缺口和停止理由，不创建占位 PDF。

## 交付索引

- 完整四列进度表：`progress.md`
- 全部 15 项投稿／不投稿说明：`publication_artifacts.md`
- 投稿 PDF：`01_floor_linear_recurrence/results/A022030_linear_recurrence_proof.pdf`
- 对应源码 ZIP：`01_floor_linear_recurrence/results/A022030_linear_recurrence_source.zip`
