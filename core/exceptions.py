class ScraperError(Exception):
    """Raised when scraping fails"""
    pass

class CleaningError(Exception):
    """Raised when cleaning fails"""
    pass

class ChunkingError(Exception):
    """Raised when chunking fails"""
    pass

class SummarizationError(Exception):
    """Raised when LLM summarization fails"""
    pass
