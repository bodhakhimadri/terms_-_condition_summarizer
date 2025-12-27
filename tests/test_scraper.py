from services.scraper import scrape_from_text

def test_scrape_from_text():
    sample_text = "These are sample terms and conditions."
    result = scrape_from_text(sample_text)

    assert isinstance(result, str)
    assert len(result) > 0
