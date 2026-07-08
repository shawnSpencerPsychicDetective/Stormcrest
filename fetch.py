from playwright.sync_api import sync_playwright

from .compress import compress


def scrape_url(url, timeout=30000):
    """
    Scrape all visible text from a webpage using a headless browser.

    Args:
        url (str): URL to scrape.
        timeout (int): Timeout in milliseconds.

    Returns:
        str: Extracted page text.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
            ],
        )

        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            )
        )

        try:
            page.goto(url, wait_until="networkidle", timeout=timeout)

            # Remove non-content elements
            page.evaluate("""
                () => {
                    document.querySelectorAll(
                        'script, style, noscript, svg, canvas'
                    ).forEach(el => el.remove());
                }
            """)

            text = page.locator("body").inner_text()

            # Normalize whitespace
            text = "\n".join(line.strip() for line in text.splitlines() if line.strip())

            return text

        finally:
            browser.close()


def fetch(url):
    return compress(scrape_url(url))
