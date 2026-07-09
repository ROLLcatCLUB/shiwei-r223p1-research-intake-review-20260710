# R223P-1 实践模式到大屏、组件、学习单、评价证据映射

stage_id: 1013R_R223P_1_ART_CLASSROOM_PRACTICE_RESEARCH_INTAKE_AND_GAP_ANALYSIS
status: candidate_mapping_only

## 映射原则

大屏、组件、学习单和评价证据不能从环节标题直接生成，应从 `practice_pattern_type` 和支架目标生成。

```text
课堂事件
→ practice_pattern_type
→ 支架目标
→ 大屏输入
→ 组件辅助
→ 学习单记录
→ 评价证据
```

## 候选映射表

| practice_pattern_type | 大屏建议 | 组件建议 | 学习单字段 | 评价证据 | 误用风险 |
| --- | --- | --- | --- | --- | --- |
| observation_discovery | 观察图、局部放大、生活场景 | observe_and_mark / circle_and_annotate | observation_features[] | 学生能指出关键特征 | 只看热闹，不留下观察依据 |
| comparison_judgment | 双图/三图对比、正误样例 | compare_two_images / right_wrong_compare | difference_and_reason | 学生能给出判断理由 | 变成投票谁更好看 |
| artwork_appreciation | 大师/同龄/范作/民间作品组 | artwork_annotation / gallery_walk | appreciation_notes | 学生能说出方法或视觉依据 | 赏析空谈，教师独讲 |
| teacher_demonstration | 步骤图、局部放大、短视频、俯拍 | technique_step_demo / demo_pause_card | step_keypoints | 学生能复述或完成关键动作 | 示范悬空，学生只看不练 |
| micro_practice | 任务语、计时器、成功标准 | micro_practice_submit / timer | practice_result / self_check | 小样、色卡、草图、试印记录 | 练习与正式作品脱节 |
| material_experiment | 材料对比表、实验目标、安全提示 | material_test_record | material_option / test_conclusion | 材料选择理由、实验小样 | 只玩材料，不回到任务 |
| idea_generation | 关键词、主题词云、版式骨架 | idea_cards / layout_dragger | idea_sketches[] / selection_reason | 至少外显一个方案 | 想法发散但无执行方案 |
| creation_progression | 阶段进度条、中途样例、常见问题墙 | midway_projection_review | midway_revision_note | 修改痕迹、半成品照片 | 教师包办代改或放任失控 |
| showcase_evaluation | 作品墙、评价句式、关键词 | peer_review_board | peer_feedback[] / artist_statement | 作品说明、互评记录 | 只说好看，不说证据 |
| closure_transfer | 方法总结板、生活应用图 | transfer_task_prompt | next_use_scenario | 迁移说明、课后延展 | 收束口号化 |

## 对 R222D / R222D-P1 的影响

R222D-P1 已经把组件从活动名加厚为课堂教学动作单元。R223P-1 建议后续为组件增加候选字段：

```text
practice_pattern_binding
support_goal
student_problem_binding
evidence_output_binding
misuse_risk
```

示例：

```text
compare_two_images
→ comparison_judgment
→ 解决判断维度不清
→ 输出 difference_and_reason
```

```text
technique_step_demo
→ teacher_demonstration
→ 解决关键动作看不清
→ 输出 step_keypoints / micro_practice_result
```

```text
learning_sheet_record
→ micro_practice / material_experiment / evidence_capture
→ 输出 practice_result / material_test_conclusion
```

## 当前边界

本文件只是候选映射，不改 R222D 组件库，不改 R223A 工作台规划，不生成 UI，不接大屏和学习单 runtime。
