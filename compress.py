from .generate import generate

SYSTEM_PROMPT = "You are a compressor, your sole aim is to compress a chunk of text under 10,000 tokens while keeping as much of the"
SYSTEM_PROMPT += " information as you can (preferably all the information)"


def chunk_text_by_words(text, chunk_size=100_000):
    words = text.split()

    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i : i + chunk_size])
        chunks.append(chunk)

    return chunks


def compress(text):
    while len(text.split()) > 10000:
        compressed = ""
        count = 0
        chunks = chunk_text_by_words(text)
        for chunk in chunks:
            USER_PROMPT = f"Compress the following text in under 10,000 tokens: {chunk}"
            compressed += generate(
                user_prompt=USER_PROMPT, system_prompt=SYSTEM_PROMPT, temperature=0
            )
            compressed += "\n"
        text = compressed
    return text
