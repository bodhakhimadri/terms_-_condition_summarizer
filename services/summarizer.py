def summarize_chunks(chunks, llm_call, prompt):
    """
    Always returns a DICT that matches FastAPI response schema
    """

    # Call LLM once (mocked for now)
    llm_output = llm_call(" ".join(chunks), prompt)

    bullets = [
        line.strip("-• ").strip()
        for line in llm_output.split("\n")
        if len(line.strip()) > 10
    ][:7]

    risk_notes = [
        b for b in bullets
        if any(k in b.lower() for k in ["suspend", "terminate", "risk", "liable"])
    ]

    return {
        "summary": " ".join(bullets),
        "key_points": bullets,          # ✅ LIST
        "risk_notes": risk_notes        # ✅ LIST
    }

