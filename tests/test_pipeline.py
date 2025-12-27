from core.pipeline import run_pipeline

def test_pipeline_with_text():
    sample_text = "These terms apply to all users."

    result = run_pipeline(text=sample_text)

    assert "summary" in result
    assert isinstance(result["summary"], str)
