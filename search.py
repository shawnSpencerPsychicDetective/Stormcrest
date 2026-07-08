from ddgs import DDGS


def search(query):
    """
    Returns the top 5 URLs for a search query using DuckDuckGo Search.

    Args:
        query (str): Search query.

    Returns:
        list[str]: List of up to 5 URLs.
    """
    urls = []

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)

        for result in results:
            url = result.get("href") or result.get("url")
            if url:
                urls.append(url)

    return urls
