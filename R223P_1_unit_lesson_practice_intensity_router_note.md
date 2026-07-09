# R223P-1 大单元—课时实践强度路由说明

stage_id: 1013R_R223P_1_ART_CLASSROOM_PRACTICE_RESEARCH_INTAKE_AND_GAP_ANALYSIS
status: candidate_router_note_only

## 为什么需要该路由

R223M/N/O 已经证明课堂事件可以在单课层面展开，但美术大单元中的课时并不具有同样的实践密度。

同一单元中可能有：

```text
理解导入课
欣赏评述课
技法准备课
实践创作课
展示评价课
综合项目课
```

如果没有实践强度路由，系统会把所有课都写成同一种：

```text
观察 → 示范 → 小练 → 创作 → 评价
```

这会导致简单理解课被写重，实践创作课又缺少足够的巡视、支架、证据和评价依据。

## 候选字段

```json
{
  "unit_phase_role": "intro_understanding | appreciation_discussion | technique_preparation | practice_creation | showcase_evaluation | project_synthesis | transfer_closure",
  "lesson_position_in_unit": "early | middle | late | final",
  "practice_intensity": "low | medium | high",
  "student_work_time_ratio": "low | medium | high",
  "teacher_support_density": "light | normal | heavy",
  "performance_task_link": "string",
  "stage_evidence_link": "string"
}
```

## 路由建议

| unit_phase_role | practice_intensity | 学生动手 | 教师支架 | 系统应加强 |
| --- | --- | --- | --- | --- |
| intro_understanding | low | 少 | light | 观察问题、赏析支架、表达句式 |
| appreciation_discussion | low/medium | 少到中 | normal | 作品阅读路径、评价语言、观点证据 |
| technique_preparation | medium | 中 | normal/heavy | 示范、小练、步骤图、错误修补 |
| practice_creation | high | 多 | heavy | 巡视观察点、分层支架、过程证据、时间控制 |
| showcase_evaluation | medium | 中 | normal | 评价句式、作品说明、互评、迁移 |
| project_synthesis | high | 多 | heavy | 分工、任务单、进度节点、阶段成果 |
| transfer_closure | low | 少 | light | 方法总结、生活迁移、后续任务 |

## 与 v0.2 的关系

该路由不直接发布为 v0.2，但建议作为 R223P-3 的候选 schema delta，并在 R223P-4 三样本回归中验证。

回归要看：

```text
我为文具代言：设计应用 / 中后段实践创作是否需要 high 支架密度；
有趣的纸印：材料技法 / 印痕试验是否需要 medium-high 小练和实验支架；
色彩的碰撞：色彩感知 / 调色微练是否需要 medium 练习密度。
```

## 当前边界

本文件不改 R223M/N/O 已有稿，不生成新教案，不改 schema，只记录候选路由。
