# R223P-1 跨学科通用底座与美术适配层说明

stage_id: 1013R_R223P_1_ART_CLASSROOM_PRACTICE_RESEARCH_INTAKE_AND_GAP_ANALYSIS

## 结论

当前 R223P 处理的是小学美术课堂展开模式，但系统设计不能被锁死为美术孤岛。正确架构是：

```text
general_pedagogy_core
→ subject_standard_layer
→ subject_practice_adapter
→ subject_resource_component_evidence_mapping
→ teacher_readable_manuscript
```

## general_pedagogy_core

通用教学推理底座应保留：

```text
standard_alignment
unit_to_lesson_reasoning
source_evidence_weighting
learner_problem_prediction
classroom_event_expansion
teacher_response_strategy
evidence_chain
teacher_readable_manuscript_rendering
preview_confirmation_gate
```

这些能力未来科学、语文、数学也需要。

## art_subject_adapter

当前两份研究报告提供的是美术学科适配层：

```text
observation_discovery
comparison_judgment
artwork_appreciation
teacher_demonstration
micro_practice
material_experiment
idea_generation
creation_progression
showcase_evaluation
closure_transfer
```

这些模式体现美术课堂的实践特征，不应直接升级为所有学科通用模式。

## 未来学科迁移示意

| 学科 | 复用 general_pedagogy_core | 替换 subject_practice_adapter |
| --- | --- | --- |
| 美术 | 是 | 观察、赏析、示范、小练、材料实验、创作、展示评价 |
| 科学 | 是 | 观察现象、提出假设、实验设计、变量控制、数据记录、解释证据 |
| 数学 | 是 | 情境建模、问题分解、操作探究、算理表达、变式练习、错例辨析 |
| 语文 | 是 | 文本初读、精读品析、朗读支架、表达训练、写作构思、迁移运用 |

## 对 R223P 的要求

R223P-1 之后的所有 registry 必须标明字段归属：

```text
general_pedagogy_core
art_subject_adapter
unit_lesson_practice_intensity_router
evidence_and_flow_control
```

凡是属于 `art_subject_adapter` 的字段，不得自动视为跨学科通用字段。

## 当前边界

本文件只做系统设计分层说明，不启动科学、语文、数学研究，不创建其他学科 registry。
