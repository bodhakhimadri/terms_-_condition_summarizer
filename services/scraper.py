import requests
from bs4 import BeautifulSoup

def scrape_from_url(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator=" ")
        return " ".join(text.split())

    except:
        raise ValueError("Failed to scrape content from URL")


def scrape_from_text(text: str) -> str:
    return text.strip()
