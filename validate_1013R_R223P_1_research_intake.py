import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223P_1_local_asset_inventory.md",
    "R223P_1_research_result_summary.md",
    "R223P_1_research_source_comparison.md",
    "R223P_1_practice_pattern_candidate_registry.json",
    "R223P_1_demonstration_type_candidate_registry.json",
    "R223P_1_micro_practice_type_candidate_registry.json",
    "R223P_1_appreciation_scaffold_candidate_registry.json",
    "R223P_1_pattern_to_screen_component_evidence_mapping.md",
    "R223P_1_gap_analysis_against_R223M_P5_v0_1.md",
    "R223P_1_recommended_schema_delta_for_v0_2.md",
    "R223P_1_cross_subject_core_and_art_adapter_note.md",
    "R223P_1_unit_lesson_practice_intensity_router_note.md",
    "R223P_1_integration_decision_report.md",
    "PACKAGE_MANIFEST.json",
    "README_FOR_GPT_REVIEW.md",
]

REQUIRED_PATTERNS = [
    "observation_discovery",
    "comparison_judgment",
    "artwork_appreciation",
    "teacher_demonstration",
    "micro_practice",
    "material_experiment",
    "idea_generation",
    "creation_progression",
    "showcase_evaluation",
    "closure_transfer",
]

REQUIRED_SCHEMA_DELTA_TERMS = [
    "practice_pattern_type",
    "demonstration_type",
    "micro_practice_type",
    "appreciation_scaffold_type",
    "creation_phase",
    "student_practice_output",
    "aesthetic_language_focus",
    "material_safety_or_management",
    "time_control_point",
    "transition_to_formal_creation",
    "unit_phase_role",
    "practice_intensity",
]

FORBIDDEN_BOUNDARY_FLAGS = [
    "r97b_modified\": true",
    "formal_ui\": true",
    "runtime_connected\": true",
    "provider_model_connected\": true",
    "database_written\": true",
    "schema_v0_2_published\": true",
    "formal_apply\": true",
]


def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")


def load_json(name):
    return json.loads(read_text(name))


def main():
    checks = []
    failures = []

    for filename in REQUIRED_FILES:
        ok = (ROOT / filename).exists()
        checks.append({"check": f"required_file:{filename}", "passed": ok})
        if not ok:
            failures.append(f"missing {filename}")

    manifest = load_json("PACKAGE_MANIFEST.json")
    checks.append({"check": "manifest_stage_id", "passed": manifest.get("stage_id") == "1013R_R223P_1_ART_CLASSROOM_PRACTICE_RESEARCH_INTAKE_AND_GAP_ANALYSIS"})
    checks.append({"check": "manifest_decision", "passed": manifest.get("decision") == "PASS_CONTINUE_TO_R223P_2_PATTERN_REGISTRY"})
    for key, expected in {
        "formal_ui": False,
        "r97b_modified": False,
        "frontend_backend_modified": False,
        "runtime_connected": False,
        "provider_model_connected": False,
        "prompt_modified": False,
        "database_written": False,
        "existing_teacher_drafts_modified": False,
        "schema_v0_2_published": False,
        "formal_apply": False,
    }.items():
        ok = manifest["boundary"].get(key) is expected
        checks.append({"check": f"boundary:{key}", "passed": ok})
        if not ok:
            failures.append(f"boundary {key} is not {expected}")

    pattern_registry = load_json("R223P_1_practice_pattern_candidate_registry.json")
    pattern_ids = {item.get("pattern_id") for item in pattern_registry.get("patterns", [])}
    for pattern in REQUIRED_PATTERNS:
        ok = pattern in pattern_ids
        checks.append({"check": f"pattern:{pattern}", "passed": ok})
        if not ok:
            failures.append(f"missing pattern {pattern}")
    checks.append({"check": "pattern_count_at_least_10", "passed": len(pattern_ids) >= 10})

    for registry_name, key in [
        ("R223P_1_demonstration_type_candidate_registry.json", "types"),
        ("R223P_1_micro_practice_type_candidate_registry.json", "types"),
        ("R223P_1_appreciation_scaffold_candidate_registry.json", "types"),
    ]:
        data = load_json(registry_name)
        ok = data.get("status") == "candidate_registry_only" and len(data.get(key, [])) >= 8
        checks.append({"check": f"candidate_registry:{registry_name}", "passed": ok})
        if not ok:
            failures.append(f"candidate registry invalid: {registry_name}")

    schema_delta = read_text("R223P_1_recommended_schema_delta_for_v0_2.md")
    for term in REQUIRED_SCHEMA_DELTA_TERMS:
        ok = term in schema_delta
        checks.append({"check": f"schema_delta_term:{term}", "passed": ok})
        if not ok:
            failures.append(f"missing schema delta term {term}")

    cross_subject = read_text("R223P_1_cross_subject_core_and_art_adapter_note.md")
    for term in ["general_pedagogy_core", "art_subject_adapter", "科学", "数学", "语文"]:
        ok = term in cross_subject
        checks.append({"check": f"cross_subject_term:{term}", "passed": ok})
        if not ok:
            failures.append(f"missing cross subject term {term}")

    router = read_text("R223P_1_unit_lesson_practice_intensity_router_note.md")
    for term in ["unit_phase_role", "practice_intensity", "student_work_time_ratio", "teacher_support_density"]:
        ok = term in router
        checks.append({"check": f"router_term:{term}", "passed": ok})
        if not ok:
            failures.append(f"missing router term {term}")

    decision = read_text("R223P_1_integration_decision_report.md")
    checks.append({"check": "decision_pass_continue", "passed": "PASS_CONTINUE_TO_R223P_2_PATTERN_REGISTRY" in decision})
    checks.append({"check": "v02_not_published", "passed": "NOT_PUBLISHED" in decision or "不发布" in decision})

    all_text = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in ROOT.iterdir() if p.suffix in {".md", ".json"})
    for forbidden in FORBIDDEN_BOUNDARY_FLAGS:
        ok = forbidden not in all_text
        checks.append({"check": f"forbidden_boundary:{forbidden}", "passed": ok})
        if not ok:
            failures.append(f"forbidden boundary found: {forbidden}")

    passed = all(item["passed"] for item in checks)
    result = {
        "passed": passed,
        "check_count": len(checks),
        "failed": len([item for item in checks if not item["passed"]]),
        "failures": failures,
        "decision": "PASS_CONTINUE_TO_R223P_2_PATTERN_REGISTRY" if passed else "HOLD_FOR_RESEARCH_SOURCE_RECHECK",
        "checks": checks,
    }
    (ROOT / "validate_1013R_R223P_1_research_intake_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({k: result[k] for k in ["passed", "check_count", "failed", "decision"]}, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
