# bigMac-00019-p03 — 812 顶点 Cayley base 的 H15 orientation CSP

令 `B` 为来源正式归档 `supplement.zip` 中唯一一行 graph6 文件
`agl_29_g14.g6` 所定义的 812 顶点、girth 14、三正则 `AGL(1,29)` Cayley 图。
判定是否存在函数 `u:V(B)->E(B)`，使每个 `v` 都与 `u(v)` 关联，并且对每个长度
`ell in {14,15,16}` 的简单圈 `C`，均有

```
#{v in V(C) : u(v) is an edge of C} <= 3*ell-33.
```

正例须给 812 个选择并穷尽复核这些圈；反例须给该固定 CSP 的可独立检查 UNSAT
证书。UNSAT 只关闭此 base，不关闭其他 base 或完整 `H15` 路线。

一手来源：Daniel Garcia, arXiv:2609.04686v1，Definition 3.1、Lemma 3.2、
Lemma 5.2 后的 AGL 搜索，pp.3--4,6--7；正式数据归档
`https://doi.org/10.5281/zenodo.22180583`。本地归档：
`batches/literature/bigMac-19/supplement.zip`；Zenodo MD5
`2a3ac93eaa5c9e6dc72d4bc3d42bdcb6`，SHA-256
`5dd250b705e4ed8e9fe6be625285adffea0d98d9f18b3640071ed4a6e4290fe4`。
