# 第二十一批 B21 最终审计

审计日期：2026-09-02（Asia/Shanghai）

## 运行与队列

- 源文档中的 15 个课题均建立了独立项目和命名 tmux/Codex 窗口。
- 15/15 个任务提示词的第一行逐字符等于用户指定的 `prove-or-disprove-math` skill 调用文本。
- 15/15 个 `codex --yolo --search exec` 进程退出码为 0；15/15 个项目存在可解析的 `results/final_status.json`。
- 最大并发数为 4，实测峰值为 4；队列终态为 `launched=15, active=0, final_status=15, complete=true`。
- 终态统计：`disproved` 3 项，`certified finite result` 6 项，`open after search` 6 项。

## 投稿闸门

仅有下列两项同时通过数学正确性、现有文献边界、引用键、可复算证书、干净 LaTeX 构建、PDF 视觉检查和源码 ZIP 隔离重建，因此生成投稿 PDF：

1. B21-07，*A Counterexample to the Proposed Last Occurrence in the Largest-Odd-Divisor Recurrence*。
   - 精确见证为 `n=78,493,252`、`p_n=1,579,691,809`、`a_{n-1}=567,791,839`，两者之和为 `2,147,483,648=2^31`，故 `a_n=1`。
   - 独立 SymPy 复算从最终源码 ZIP 在空临时目录运行并通过；该复算耗时约 68.4 秒。
   - 论文不声称这是 33,900 之后的首次命中，也不声称不存在更晚命中。
2. B21-13，*A Counterexample to an Exponential Divisibility Recurrence*。
   - 首个失败位置为 `n=7`，且精确证明与两套独立验证器均得到 `(2^{a_6}+1) mod 171 = 9`。
   - Python 与 Ruby 验证器均从最终源码 ZIP 在空临时目录运行并通过。

B21-06 也得到严格反例 `k=27`，因为
`b^27-27=(b^9-3)(b^18+3b^9+9)`；但该反例已有公开记录，未通过新颖性闸门，因此没有生成投稿稿件。其余 12 项只有有限范围证书、结构性引理或未闭合搜索，不强行生成 PDF。

## 引用、构建与版面

- 两份论文各引用 2 个条目；最终审计均为 `cited_keys=2, bib_keys=2, missing=0, unused=0`。
- 最终 LaTeX 日志中没有未定义引用、未定义文献、LaTeX error、emergency stop 或 fatal error。
- 两份最终 PDF 均为 2 页，标题和唯一署名均正确：Xiaojian Zeng；PBC School of Finance, Tsinghua University, 100190；xiaojianzeng@foxmail.com。
- 四个 PDF 页面均经 144 dpi 渲染并逐页检查，无裁切、重叠、缺字、黑块或断裂引用。
- 最终 PDF 文本中未发现 `SHA-256`、长十六进制摘要、Codex 或 OpenAI 字样。
- 两份最终源码 ZIP 均在全新临时目录中完成 LaTeX 重建和证书复算；项目 release manifest 随最终文件重新生成并验证通过（B21-07：69 个文件；B21-13：57 个文件）。
- 两项结果均未使用证明助理；论文中的相关披露按实际工作流书写。

## 最终文件

- 完整四列进度表：`progress.md`
- 全部 15 项的投稿/不投稿终态：`publication_artifacts.md`
- B21-07：`07_oddpart_recurrence/paper/main.pdf` 与 `07_oddpart_recurrence/results/Zeng_oddpart_counterexample_source.zip`
- B21-13：`13_exponential_divisibility/paper/main.pdf` 与 `13_exponential_divisibility/results/A078590_counterexample_source.zip`
