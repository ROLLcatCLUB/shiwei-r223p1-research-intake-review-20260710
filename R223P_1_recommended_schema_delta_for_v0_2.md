# R223P-1 推荐 schema v0.2 delta

stage_id: 1013R_R223P_1_ART_CLASSROOM_PRACTICE_RESEARCH_INTAKE_AND_GAP_ANALYSIS
status: schema_delta_candidate_only

## 原则

本文件只提出 classroom_event_schema v0.2 候选增量，不发布 v0.2，不覆盖 R223M-P5 v0.1。

每个候选字段必须经过 R223P-4 三样本回归后，才可能进入 v0.2。

## 候选字段分层

### A. general_pedagogy_core

通用教学推理底座字段，不限于美术：

| 字段 | 用途 | 风险 |
| --- | --- | --- |
| `source_evidence_weighting` | 区分来源证据、系统推理、教师确认 | 需要 source ledger 配合 |
| `learner_problem_prediction` | 学生问题预测 | 不能泛化成空话 |
| `teacher_response_strategy` | 教师追问、补救、转向 | 不能替代教师专业判断 |
| `evidence_chain` | 连接任务、活动、学生输出和评价 | 已有旧字段，需要对齐 |
| `teacher_readable_manuscript_rendering` | 控制默认稿人话化 | 不进入课堂事件主体 |

### B. art_subject_adapter

美术学科实践模式适配字段：

| 字段 | 用途 | 候选状态 |
| --- | --- | --- |
| `practice_pattern_type` | 标明课堂事件实践模式 | required_candidate |
| `demonstration_type` | 标明示范类型 | conditional_candidate |
| `teacher_demo_purpose` | 说明示范解决什么问题 | optional_candidate |
| `micro_practice_type` | 标明小练习类型 | conditional_candidate |
| `appreciation_scaffold_type` | 标明赏析支架类型 | conditional_candidate |
| `artwork_reference_type` | 区分大师、同龄、教师范作等 | optional_candidate |
| `technique_breakthrough_point` | 标明局部技法卡点 | optional_candidate |
| `aesthetic_language_focus` | 美术语言焦点 | recommended_candidate |
| `material_safety_or_management` | 材料安全、清洁、管理 | recommended_candidate |

### C. unit_lesson_practice_intensity_router

大单元—课时实践强度路由字段：

| 字段 | 用途 | 候选状态 |
| --- | --- | --- |
| `unit_phase_role` | 课时在大单元中的阶段责任 | required_candidate |
| `lesson_position_in_unit` | early / middle / late / final | recommended_candidate |
| `practice_intensity` | low / medium / high | required_candidate |
| `student_work_time_ratio` | 学生动手时间比例 | recommended_candidate |
| `teacher_support_density` | 教师支架密度 | recommended_candidate |
| `performance_task_link` | 连接单元表现性任务 | required_if_unit_task_exists |
| `stage_evidence_link` | 连接阶段证据 | required_if_stage_exists |

### D. evidence_and_flow_control

证据、节奏和分支字段：

| 字段 | 用途 | 候选状态 |
| --- | --- | --- |
| `student_practice_output` | 学生输出对象 | required_candidate |
| `creation_phase` | before / during / after creation | recommended_candidate |
| `time_control_point` | 时间控制点 | recommended_candidate |
| `estimated_minutes` | 建议分钟数 | optional_candidate |
| `transition_to_formal_creation` | 小练到正式创作的迁移 | conditional_candidate |
| `branch_to` | 补救或转向分支 | optional_candidate |
| `process_evidence` | 过程证据 | recommended_candidate |
| `checkpoint` | 进入下一事件的检查点 | recommended_candidate |
| `revision_trace` | 修改痕迹 | optional_candidate |

## 候选规则

```text
规则 1：
包含 demonstration_type 的事件，必须关联 micro_practice_type 或 transition_to_formal_creation。

规则 2：
包含 appreciation_scaffold_type 的事件，必须关联 observation_prompt 和 expected_student_responses。

规则 3：
大屏 / 组件 / 学习单 / 评价证据必须服务明确支架目标。

规则 4：
小练习必须说明如何迁移到正式创作。

规则 5：
学生输出对象 student_practice_output 必须明确，否则课堂事件不得通过。

规则 6：
每个 lesson event 必须声明 unit_phase_role 和 practice_intensity。
```

P1 阶段这些规则只作为候选规则，不进入正式 validator。

## 复杂度风险

| 风险 | 处理 |
| --- | --- |
| 字段过多导致默认教师稿变重 | 新字段默认进入 review ledger，不直接进入 teacher default view |
| 美术字段误当通用字段 | 所有美术字段标注 `art_subject_adapter` |
| 小练习字段造成所有课都强行练习 | 受 `unit_phase_role` 和 `practice_intensity` 控制 |
| 组件绑定过早实现 | 仅做候选映射，不改 R222D / R223A |
| v0.2 破坏 v0.1 稳定性 | 只做 delta，需三样本回归 |

## 当前结论

```text
schema_delta_ready_for_P2_discussion=true
schema_v0_2_publish_allowed=false
regression_required=true
```
