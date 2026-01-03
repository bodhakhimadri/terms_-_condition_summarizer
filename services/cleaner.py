import re

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def remove_prompt_leakage(text: str) -> str:
    patterns = [
        r"Summarize the following.*?points\.",
        r"Summarize the following.*?\."
    ]
    for p in patterns:
        text = re.sub(p, "", text, flags=re.IGNORECASE)
    return text.strip()


