def chunk_text(text: str, max_length: int = 1200):
    words = text.split()
    chunks = []
    current = []

    for word in words:
        if sum(len(w) for w in current) + len(word) > max_length:
            chunks.append(" ".join(current))
            current = []
        current.append(word)

    if current:
        chunks.append(" ".join(current))

    return chunks
