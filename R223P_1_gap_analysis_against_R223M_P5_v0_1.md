# R223P-1 对 R223M-P5 v0.1 的缺口分析

stage_id: 1013R_R223P_1_ART_CLASSROOM_PRACTICE_RESEARCH_INTAKE_AND_GAP_ANALYSIS
base_standard: GOLDEN_CLASSROOM_EVENT_EXPANSION_STANDARD_V0.1_LOCK_CANDIDATE

## v0.1 已经具备的能力

R223M-P5 v0.1 已经覆盖：

```text
event_id
event_name
section
source_anchor
teaching_responsibility
student_problem
task_release
expected_student_responses
likely_misconceptions_or_failures
teacher_follow_up_questions
teacher_scaffolding_moves
teacher_rescue_strategy
screen_trigger
component_trigger
learning_sheet_trigger
evidence_trigger
assessment_alignment
transition_chain
teacher_visible_note
control_points
```

这些字段能支撑：

```text
课堂事件展开
学生反应预判
教师追问与补救
大屏 / 组件 / 学习单 / 证据触发
教师默认稿与 review ledger 分层
```

## 主要缺口

### 1. 缺少实践模式主键

v0.1 有课堂事件，但没有明确回答：

```text
这个事件属于观察、比较、赏析、示范、小练、材料实验、创作推进，还是展示评价？
```

建议候选字段：

```text
practice_pattern_type
```

### 2. 缺少示范 / 小练 / 赏析的类型化治理

v0.1 有 `teacher_scaffolding_moves` 和 `component_trigger`，但不区分：

```text
完整示范 / 局部示范 / 起稿示范 / 技法示范 / 错误修补示范
试画 / 试印 / 调色 / 材料小样 / 构图草模
大师作品 / 同龄作品 / 教师范作 / 正误对照 / 学生半成品
```

建议候选字段：

```text
demonstration_type
micro_practice_type
appreciation_scaffold_type
artwork_reference_type
teacher_demo_purpose
```

### 3. 缺少学生输出对象的强约束

v0.1 有 `evidence_trigger`，但没有强制声明学生实际产出是什么。

建议候选字段：

```text
student_practice_output
process_evidence
revision_trace
```

### 4. 缺少练习到正式创作的迁移关系

研究报告强调小练习必须服务正式创作，不能成为热身或消耗。

建议候选字段：

```text
transition_to_formal_creation
checkpoint
exit_condition
```

### 5. 缺少美术语言焦点的枚举化

v0.1 可写美术语言，但没有候选枚举约束。

建议候选字段：

```text
aesthetic_language_focus
```

候选值：

```text
主次
疏密
节奏
冷暖
明暗
层次
肌理
边缘
稳定
留白
对称
色相
```

### 6. 缺少时间与材料管理字段

美术课的示范、小练、材料实验极易拖时或失控。

建议候选字段：

```text
time_control_point
estimated_minutes
material_safety_or_management
```

### 7. 缺少大单元课时实践强度路由

v0.1 已能展开单课事件，但没有明确判断这节课在大单元中是理解导入、技法准备、实践创作还是展示评价。

建议候选字段：

```text
unit_phase_role
lesson_position_in_unit
practice_intensity
student_work_time_ratio
teacher_support_density
performance_task_link
stage_evidence_link
```

## 不建议进入 v0.2 的内容

| 内容 | 原因 |
| --- | --- |
| 研究报告中的全部案例描述 | 太重，适合知识库，不适合 schema |
| 所有参考来源字段 | 可放 source ledger，不放事件对象主体 |
| 过细的组件参数 | 应留给 R222D / R223A 后续组件合同 |
| 每个模式固定流程顺序 | 会导致美术课模板化 |

## 缺口判断

```text
v0_1_core_valid=true
v0_1_needs_practice_pattern_layer=true
v0_1_needs_support_type_layer=true
v0_1_needs_student_output_layer=true
v0_1_needs_unit_intensity_router=true
direct_upgrade_to_v0_2=false
```
