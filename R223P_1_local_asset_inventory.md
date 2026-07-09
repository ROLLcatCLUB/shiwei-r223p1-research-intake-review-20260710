# R223P-1 窄范围本地资产盘点

stage_id: 1013R_R223P_1_ART_CLASSROOM_PRACTICE_RESEARCH_INTAKE_AND_GAP_ANALYSIS
scope: narrow_asset_inventory_only
created_at: 2026-07-10
formal_ui: false
r97b_modified: false
runtime_connected: false
provider_model_connected: false
database_written: false
formal_apply: false

## 盘点边界

本盘点只覆盖 R223P-1 指定的五类资产，不做全库扫描，不改历史文件，不生成新教案，不升级 v0.2。

## A. 字段基础

| 资产 | 路径 | 用途 | R223P-1 输入状态 | 备注 |
| --- | --- | --- | --- | --- |
| 073B0 foundation field registry report | `docs/audit/foundation_field_registry_073B0_report.md` | 证明早期已有正式字段注册基础 | 可作为字段基础证据 | 报告显示正式纳入字段 60 个 |
| 073B0 foundation field registry | `docs/foundation/field_registry_073B0.md` | 早期 foundation 字段总表 | 可作为历史参考 | 不直接覆盖 R223 schema |
| 073B1 field definition review | `docs/audit/field_definition_review_073B1_report.md` | 课堂步骤字段审核 | 可作为字段缺口证据 | 已指出 `process_steps` 缺少显式 `step_purpose` |
| R88 field generation static lab | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R88_FIELD_GENERATION_QUALITY_STATIC_LAB/` | 字段生成质量实验 | 历史参考 | 不作为 R223P 直接 schema |
| R89 field contract convergence | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R89_FIELD_CONTRACT_CONVERGENCE_AND_CAUSAL_CHAIN_GATE/` | 生成阶段与字段簇注册 | 可作为字段簇基础输入 | 已有 `classroom_flow_line_contract` |
| R221B field semantic contract | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R221B_FIELD_SEMANTIC_CONTRACT_AND_UNIT_REASONING_CHAIN/` | 大单元字段语义合同 | 关键输入 | 定义 16 个 priority fields 与污染控制 |
| R223M-P5 classroom_event schema v0.1 | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R223M_P5_GOLDEN_STANDARD_LOCK_PACKAGE/R223M_P5_classroom_event_schema_lock.json` | 当前课堂事件标准 v0.1 | 核心对照输入 | v0.2 delta 只能在此基础上提出 |

## B. 当前课堂事件标准

| 资产 | 路径 | 用途 | R223P-1 输入状态 |
| --- | --- | --- | --- |
| Golden standard lock package | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R223M_P5_GOLDEN_STANDARD_LOCK_PACKAGE/` | v0.1 候选标准锁定包 | 核心输入 |
| Teacher default view standard | `R223M_P5_teacher_default_view_standard.md` | 默认教师阅读层规则 | 输入 |
| Review ledger view standard | `R223M_P5_review_ledger_view_standard.md` | 审核 ledger 层规则 | 输入 |
| classroom_event_schema v0.1 | `R223M_P5_classroom_event_schema_lock.json` | 当前 schema | 核心对照 |
| 25 分 control point rubric | `R223M_P5_control_point_rubric_lock.md` | 人工审核规准 | 输入 |

## C. 跨样本验证资产

| 资产 | 路径 | 用途 | R223P-1 输入状态 |
| --- | --- | --- | --- |
| R223N cross-sample validation | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R223N_CROSS_SAMPLE_CLASSROOM_EVENT_EXPANSION_VALIDATION/` | 《有趣的纸印》材料技法/印痕探究验证 | 输入 |
| R223N-P3 teacher manuscript grammar | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R223N_P3_TEACHER_MANUSCRIPT_GRAMMAR_ALIGNMENT/` | 教师文稿文法对齐 | 输入 |
| R223N-P3-P1 light polish | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R223N_P3_P1_LIGHT_SAMPLE_FLAVOR_AND_LAYOUT_POLISH/` | 《有趣的纸印》最终轻润色通过稿 | 核心输入 |
| R223O second cross-sample validation | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R223O_SECOND_CROSS_SAMPLE_VALIDATION/` | 《色彩的碰撞》色彩感知验证 | 输入 |
| R223O-P1 structure recovery | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R223O_P1_COLOR_MANUSCRIPT_STRUCTURE_RECOVERY/` | 色彩课文稿结构恢复 | 核心输入 |

## D. 深度研究资产

| 资产 | 路径 | 用途 | R223P-1 输入状态 |
| --- | --- | --- | --- |
| 研究资料目录 | `docs/foundation/research/1013R_R223_ART_CLASSROOM_PRACTICE_MODES_RESEARCH/` | 两份研究归档与状态锁 | 核心输入 |
| 研究报告 1 | `01_art_classroom_expansion_modes_evidence_basis.md` | 证据基础、模式映射、支架类型 | 核心输入 |
| 研究报告 2 | `02_art_classroom_practice_scaffolds_deep_research.md` | 设计原则、schema 建议、模板库 | 核心输入 |
| R223P foundation note | `03_R223P_1_research_intake_cross_subject_core_and_field_library_note.md` | 跨学科底座、字段库边界 | 输入 |
| Foundation record status lock | `04_R223P_1_foundation_record_status_lock.md` | 确认 record 不是 full intake | 输入 |

## E. 组件库资产

| 资产 | 路径 | 用途 | R223P-1 输入状态 |
| --- | --- | --- | --- |
| R222D classroom component registry | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R222D_CLASSROOM_COMPONENT_REGISTRY_AND_PREP_BINDING_CONTRACT/` | 课堂组件候选池与备课绑定 | 输入 |
| R222D-P1 component hardening | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R222D_P1_COMPONENT_PEDAGOGICAL_HARDENING/` | 组件教学责任、媒体需求、证据输出 | 核心输入 |
| R223A-P1 component-aware planning gate | `outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R223A_P1_COMPONENT_AWARE_MINIMAL_WORKBENCH_PLANNING_GATE/` | 组件如何嵌入备课工作台规划 | 输入 |

## 初步判断

```text
field_base_exists=true
field_library_for_R223P=not_yet_unified
research_assets_ready=true
component_assets_ready=true
R223M_P5_v0_1_ready_for_gap_analysis=true
R223N_R223O_ready_for_regression_reference=true
```

本地资产足以启动正式 R223P-1 研究接收包，但不足以直接发布 classroom_event_schema v0.2。
