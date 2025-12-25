from services.scraper import scrape_from_url, scrape_from_text
from services.cleaner import clean_text
from services.chunker import chunk_text
from services.summarizer import summarize_chunks
from core.constants import SUMMARY_PROMPTS, DEFAULT_SUMMARY_TYPE


def run_pipeline(text: str = None, url: str = None, summary_type: str = DEFAULT_SUMMARY_TYPE):
    """
    Complete Workflow:
    url/text → scrape → clean → chunk → summarize → response format
    """

    # 1️⃣ Input Validation
    if not text and not url:
        raise ValueError("Either text or URL must be provided")

    # 2️⃣ Scrape Text
    if url:
        raw_text = scrape_from_url(url)
    else:
        raw_text = scrape_from_text(text)

    # 3️⃣ Clean Text
    cleaned = clean_text(raw_text)

    # 4️⃣ Chunk for LLM
    chunks = chunk_text(cleaned)

    # 5️⃣ Summarization
    prompt = SUMMARY_PROMPTS.get(summary_type, SUMMARY_PROMPTS["simple"])
    final_summary, key_points, risk_notes = summarize_chunks(chunks, prompt, summary_type)

    # 6️⃣ Final API Response
    return {
        "summary": final_summary,
        "key_points": key_points,
        "risk_notes": risk_notes
    }
