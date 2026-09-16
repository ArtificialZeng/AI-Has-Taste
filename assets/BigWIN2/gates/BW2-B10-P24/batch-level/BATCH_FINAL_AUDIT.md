# 第十批 B10 最终批次审计

审计时间：2026-08-31 16:37（Asia/Shanghai）

## 范围与去重

- 从用户给定文档抽取 A186--A210，共 25 个课题。
- 与此前实际研究的 60 个课题（第一组、第六批、第七批、第八批）及 B10 内部互相比较。
- 结论：25 个课题均不重复；逐题判定见 `dedup_audit.md`。

## CLI、技能与并发

- 25 个 prompt 的第一行逐一复核，均精确为用户指定的
  `[$prove-or-disprove-math](C:\Users\87510\\.codex\skills\prove-or-disprove-math\SKILL.md)`。
- 25 个项目均有 `results/launch_meta.json`，并经 `run_task.sh` 使用
  `codex --yolo --search exec` 启动。
- `launch_task.ps1` 在启动前统计 Codex CLI；活动进程达到 4 时拒绝继续启动。
  所有任务均由该入口顺序调度，因此并发上限为 4。
- 25 个 B10 tmux 会话均保留并使用可识别课题名；最终活动 Codex CLI 为 0，
  第 15 题 SAT/DRAT 求解器残留为 0。

## 终态与进度

- `task_manifest.json`：25 个任务。
- `results/final_status.json`：25 份，全部存在且可解析。
- 科学终态：22 项 `open after search`，3 项 `certified finite result`。
- 进度表：`progress.md`，25 行；投稿成果表：`publication_artifacts.md`，25 行。
- 所有项目的冻结 manifest 均由技能自带 `verify_manifest.py` 验证通过：
  22 份标准 release/final manifest，加第 15、17、18 题的非标准命名 manifest，
  合计 25/25。第 15 题 manifest 覆盖 17,334 个文件。

## 成稿门槛与投稿成果

- 仅第 24 题达到成稿门槛：严格有限结论 `F(62)=31`。
- 最终 PDF：`24_erdos425_f62/paper/main.pdf`；LaTeX ZIP：
  `24_erdos425_f62/results/F62_latex.zip`。两者均存在，并与第 24 题
  `final_status.json` 对应。
- PDF 元数据：标题 *The Strict-Pair Product Extremal Value at 62 Is 31*，
  作者 Zijian Zeng，共 3 页，letter 纸张。
- PDF 全页视觉检查、干净 ZIP 重建、数学证书重放、三条引用逐条核验均通过；
  详见 `24_erdos425_f62/audit/ROOT_DELIVERY_AUDIT.md`。
- 最终 PDF 文本再次扫描，未发现 SHA-256 样式工作流标记、模型/厂商名、
  prompt/agent/workflow 或生成痕迹。
- 第 5、7 题虽有严格有限结果，但新颖性/实质性不足，未生成 PDF。

## 第 15 题特殊终态

- 严格得到 41 边 `Q_3`-free 构造，并以两个独立验证器复核。
- 42 边上界的最大度 `d=7` 分支有两份独立检查通过的 DRAT 证书；
  `d=8,9,10,11` 未获得完整证书。
- 继续完成全部分支的信心降至 45%，低于用户规定的 60% 停止门槛，故终态为
  `open after search`，没有 PDF/ZIP，也不声称 `ex(12,Q_3)=41`。
- 无法检查的截断 DRAT 在删除前已把文件名与字节数写入
  `15_ex12_q3/audit/incomplete_trace_inventory.txt`；这些中间轨迹不可恢复，
  只能重新计算。源码、CNF、完成证书、日志和 referee 报告均保留。

## 最终判定

PASS：去重、25 个首行技能 prompt、WSL/tmux/Codex 调度、25 个终态、进度表、
信心阈值、成稿门槛、唯一 PDF/ZIP 对应关系、PDF 视觉/文本/构建审计、冻结
manifest 验证及无活动求解进程均已闭环。没有把未解决课题包装为投稿稿件。
