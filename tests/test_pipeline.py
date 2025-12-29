from core.pipeline import run_pipeline

def test_pipeline_with_text():
    sample_text = "These terms apply to all users."

    result = run_pipeline(text=sample_text)

    assert isinstance(result, dict)
    assert "summary" in result
    assert "key_points" in result
    assert "risk_notes" in result

    assert isinstance(result["summary"], str)
    assert isinstance(result["key_points"], list)
    assert isinstance(result["risk_notes"], list)

