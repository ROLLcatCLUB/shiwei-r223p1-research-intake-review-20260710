# R223P-1 两份研究来源对比

stage_id: 1013R_R223P_1_ART_CLASSROOM_PRACTICE_RESEARCH_INTAKE_AND_GAP_ANALYSIS

## 对比表

| 维度 | 报告 1：研究定位与证据基础 | 报告 2：深度研究摘要与设计原则 | R223P-1 处理 |
| --- | --- | --- | --- |
| 主要价值 | 证据基础、模式映射、实践支架类型 | 系统字段、schema 建议、模式链和模板 | 合并为候选模式/字段/规则 |
| 核心观点 | 美术课堂支架密度频繁切换 | 课堂事件应成为带支架属性的实践节点 | 进入 v0.2 delta 候选 |
| 模式分类 | 观察发现、对比判断、作品赏析、教师示范、前置小练习等 | 观察发现、对比判断、教师示范、微型练习、作品赏析等 | 去重合并为 10 类 practice patterns |
| 示范类型 | 完整、局部、起稿、构图、工具材料、技法、错误修补等 | 完整、局部、起稿、技法、突破、错误修补、慢动作、半成品等 | 合并为 demonstration_type 候选库 |
| 小练习类型 | 试画一笔、试印一次、调色、剪纹样、构图、小样等 | 试画、试调色、试印、纹样、构图、材料小样、组合方案等 | 合并为 micro_practice_type 候选库 |
| 赏析支架 | 大师、同龄、教师范作、生活、民间、步骤图、展馆资源 | 大师、同龄、教师范作、生活、民间、学生半成品、正误对照 | 合并为 appreciation_scaffold 候选库 |
| 证据输出 | 观察记录、理由、作品说明、过程照片、评价语 | 草图、色卡、小样、判断理由、修改痕迹、作品说明 | 进入 evidence / student_practice_output 候选 |
| 系统接口 | 大屏、组件、学习单、评价证据映射 | 实践模式到大屏/组件/学习单/评价的字段化 | 进入 pattern_to_screen_component_evidence_mapping |
| schema 建议 | 目标—支架—行为—证据—分支 | event 对象字段与 v0.2 修订建议 | 形成 recommended_schema_delta_for_v0_2 |
| 风险 | 可能把研究内容直接塞入 schema | 字段可能过多、默认稿变重 | P1 只候选化，不发布 v0.2 |

## 去重原则

1. 同义模式合并为一个 `practice_pattern_type`，保留中文别名。
2. 支架类型先进入候选 registry，不直接改 `R223M_P5_classroom_event_schema_lock.json`。
3. 如果字段能由现有 R89 / R221B / R223M-P5 字段表达，则记录为 enhancement，不作为强制新增。
4. 如果字段表达的是美术学科实践特性，则归入 `art_subject_adapter`，不进入 `general_pedagogy_core`。
5. 如果字段控制大单元课时强度，则归入 `unit_lesson_practice_intensity_router`。

## 需要后续回归验证的内容

```text
practice_pattern_type
demonstration_type
micro_practice_type
appreciation_scaffold_type
student_practice_output
time_control_point
transition_to_formal_creation
unit_phase_role
practice_intensity
```

这些字段可能提升课堂展开质量，也可能造成 review ledger 变重，必须在 R223P-4 三样本回归中验证。
