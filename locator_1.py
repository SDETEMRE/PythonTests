from playwright.sync_api import sync_playwright

with sync_playwright() as page:
    browser = page.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Index.html')

    emailtxtbox = page.wait_for_selector('#email')
    emailtxtbox.type('test@gmail.com')
    page.wait_for_timeout(3000)