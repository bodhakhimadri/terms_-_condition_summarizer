def summarize_chunks(chunks, prompt, summary_type):
    summaries = []

    for part in chunks:
        summary = f"{prompt}\n\n🔹 {part[:200]}..."  # mock summary
        summaries.append(summary)

    final = "\n".join(summaries)

    key_points = [f"Point {i+1}: extracted summary" for i in range(3)] if summary_type!="risk" else []
    risk = ["⚠ Note: Risk-related section here"] if summary_type=="risk" else []

    return final, key_points, risk
