def chunk_text(text: str, max_words: int = 350):
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        if len(chunk) > 50:
            chunks.append(chunk)

    return chunks

