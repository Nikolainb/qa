from playwright.sync_api import sync_playwright


def test_example_domain():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless=True = без окна
        page = browser.new_page()
        page.goto("https://example.com")
        assert "Example Domain" in page.title()
        browser.close()
    print("Playwright OK")
