from scripts.workbuddy import w0_audit


def test_v0321_export_pipeline_contract_inventory_is_complete():
    result = w0_audit.audit_pipelines()

    assert result["pipeline_count"] == 4
    assert result["pipeline_skill_count"] == 44
    assert result["comparison_base_commit"] == "4eab34c5cfcccaa4f1970554928feccce73ee930"
    assert result["changed_contract_test_count"] == 10
    assert result["added_contract_test_count"] == 8
    assert result["reviewer_skill_present"] is True
    assert result["checkpoint_skill_present"] is True

    for pipeline in result["pipelines"].values():
        assert pipeline["manifest_absent_from_locked_upstream"] is True
        assert pipeline["schema_valid"] is True
        assert pipeline["pipeline_skill_count"] == 11
        assert pipeline["reviewer_skill_declared"] is True
        assert pipeline["checkpoint_skill_declared"] is True
        assert pipeline["missing_tool_registry_refs"] == []
        assert all(pipeline["artifact_schema_checks"].values())
        assert all(stage["skill_exists"] for stage in pipeline["stage_checks"])
        assert all(stage["checkpoint_required"] for stage in pipeline["stage_checks"])
        assert all(stage["review_focus_present"] for stage in pipeline["stage_checks"])
        assert all(stage["success_criteria_present"] for stage in pipeline["stage_checks"])


def test_direct_agent_runtime_boundary_excludes_nested_agent_host():
    result = w0_audit.runtime_isolation_scan()

    assert result["authority"] == {
        "invocation_model": "direct_agent",
        "nested_agent_host_allowed": False,
    }
    assert result["forbidden_reference_hits"] == []
    assert all(result["forbidden_core_paths_absent"].values())
    assert result["static_result"] in {"pass", "not_yet_applicable"}


def test_public_candidate_lineage_excludes_private_core_ancestry():
    result = w0_audit.audit_lineage()

    assert result["public_base"] == "origin/main"
    assert result["public_base_is_head_ancestor"] is True
    assert result["private_core_source_is_head_ancestor"] is False
    assert result["official_direct_sync_allowed"] is False
    assert result["private_git_ancestry_merge_allowed"] is False
