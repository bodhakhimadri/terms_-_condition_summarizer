from services.scraper import scrape_from_url, scrape_from_text
from services.cleaner import clean_text, remove_prompt_leakage
from services.chunker import chunk_text
from services.summarizer import summarize_chunks
from core.constants import SUMMARY_PROMPTS, DEFAULT_SUMMARY_TYPE
from services.llm import llm_call


def run_pipeline(text: str = None, url: str = None, summary_type: str = DEFAULT_SUMMARY_TYPE):

    if not text and not url:
        raise ValueError("Either text or URL must be provided")

    raw_text = scrape_from_url(url) if url else scrape_from_text(text)
    if not raw_text or not raw_text.strip():
        raise ValueError("No valid text extracted")

    cleaned = clean_text(raw_text)
    cleaned = remove_prompt_leakage(cleaned)

    chunks = chunk_text(cleaned)
    if not chunks:
        raise ValueError("Chunking failed")

    prompt = SUMMARY_PROMPTS.get(summary_type, SUMMARY_PROMPTS[DEFAULT_SUMMARY_TYPE])

    # ✅ RETURN DICT (matches response schema)
    result = summarize_chunks(chunks, llm_call, prompt)
    return result
