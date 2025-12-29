from services.scraper import scrape_from_url, scrape_from_text
from services.cleaner import clean_text
from services.chunker import chunk_text
from services.summarizer import summarize_chunks
from core.constants import SUMMARY_PROMPTS, DEFAULT_SUMMARY_TYPE


def run_pipeline(
    text: str = None,
    url: str = None,
    summary_type: str = DEFAULT_SUMMARY_TYPE
):
    """
    Complete Workflow:
    text / url → scrape → clean → chunk → summarize → response
    """

    # 1️⃣ Input Validation
    if not text and not url:
        raise ValueError("Either text or URL must be provided")

    # 2️⃣ Get Raw Text
    if url:
        raw_text = scrape_from_url(url)
    else:
        raw_text = scrape_from_text(text)

    if not raw_text or not raw_text.strip():
        raise ValueError("No valid text extracted from input")

    # 3️⃣ Clean Text
    cleaned_text = clean_text(raw_text)

    # 4️⃣ Chunk Text
    chunks = chunk_text(cleaned_text)

    if not chunks:
        raise ValueError("Chunking failed: no chunks created")

    # 5️⃣ Select Prompt
    prompt = SUMMARY_PROMPTS.get(
        summary_type,
        SUMMARY_PROMPTS[DEFAULT_SUMMARY_TYPE]
    )

    # 6️⃣ Summarization
    final_summary, key_points, risk_notes = summarize_chunks(
        chunks=chunks,
        prompt=prompt,
        summary_type=summary_type
    )

    # 7️⃣ Final Response
    return {
        "summary": final_summary,
        "key_points": key_points,
        "risk_notes": risk_notes
    }

