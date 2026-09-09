# 首轮验收矩阵

| 项目 | 可观察通过条件 | 证据 |
|---|---|---|
| 营销过滤 | `REJECTED_FOR_CORE` | `benchmark_report.json` Case 1 |
| 重复去重 | `MAP_TO_EXISTING` | Case 2 |
| 未知能力 | `UNKNOWN_NEEDS_REALITY_PROBE` | Case 3与`capability_probes/` |
| 复杂度控制 | 简单邮件为`DIRECT_REQUEST` | Case 4 |
| 权限控制 | 群发并付款要求人工批准 | Case 5 |
| 失败学习 | 根因、约束、回归测试齐全 | Case 6与Failure Library |
| 最终制品 | 最终制品错则整体FAIL | Case 7 |
| 方法竞争 | 无指标时要求Benchmark | Case 8 |
| PROVEN门 | 无证据能力被拒绝 | invariants |
