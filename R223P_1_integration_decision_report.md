# R223P-1 研究接收与缺口分析决策报告

stage_id: 1013R_R223P_1_ART_CLASSROOM_PRACTICE_RESEARCH_INTAKE_AND_GAP_ANALYSIS
decision: PASS_CONTINUE_TO_R223P_2_PATTERN_REGISTRY
formal_ui: false
r97b_modified: false
frontend_backend_modified: false
runtime_connected: false
provider_model_connected: false
prompt_modified: false
database_written: false
formal_apply: false

## 决策

```text
R223P-1 = PASS_RESEARCH_INTAKE_AND_GAP_ANALYSIS
NEXT_ALLOWED = R223P-2_ART_CLASSROOM_PRACTICE_PATTERN_REGISTRY
R223P-3/4/5 = BLOCKED_UNTIL_P2_PASS
R223M_STANDARD_V0_2 = NOT_PUBLISHED
R223M-P5_v0_1 = PRESERVED
```

## 通过理由

1. 已完成窄范围本地资产盘点，确认字段基础、R223M-P5 标准、跨样本验证、深度研究和组件库资产均存在。
2. 已将两份深度研究去重归并为候选模式、示范类型、小练习类型、赏析支架类型和 schema delta。
3. 已保留三层架构判断：

   ```text
   general_pedagogy_core
   art_subject_adapter
   unit_lesson_practice_intensity_router
   ```

4. 已明确字段不是野生字段，但 R223P 所需的统一候选字段库尚未形成。
5. 已明确 v0.2 不能直接发布，必须经过 R223P-2 / P3 / P4。

## 哪些内容可进入 v0.2 schema 候选

```text
practice_pattern_type
creation_phase
student_practice_output
unit_phase_role
practice_intensity
time_control_point
transition_to_formal_creation
```

## 哪些内容只进入候选库

```text
demonstration_type
micro_practice_type
appreciation_scaffold_type
artwork_reference_type
aesthetic_language_focus
material_safety_or_management
teacher_demo_purpose
technique_breakthrough_point
```

## 哪些只是研究参考

```text
完整参考资料清单
具体公开课例细节
全部案例叙述
未验证的跨学科模式猜想
```

## 哪些字段可能导致过度复杂

```text
branch_to
revision_trace
material_safety_or_management
artwork_reference_type
teacher_demo_purpose
```

这些字段建议先进入 review ledger 或候选库，不进入教师默认稿。

## 必须经过三样本回归的字段

```text
practice_pattern_type
demonstration_type
micro_practice_type
appreciation_scaffold_type
student_practice_output
unit_phase_role
practice_intensity
transition_to_formal_creation
```

## 后续门控

R223P-2 只能做美术课堂实践模式注册表，不改生成链。

R223P-3 只能做 schema v0.2 delta，不发布 v0.2。

R223P-4 才允许对三样本做回归验证。

R223P-5 才判断是否进入：

```text
R223M_STANDARD_V0_2_CANDIDATE
```

## 边界

本包未改 R97B，未新增正式 route，未改 frontend/backend，未接 runtime、provider/model、prompt、db，未改 R223M/N/O 已有教师稿，未发布 v0.2，未 formal apply。
