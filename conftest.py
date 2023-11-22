from collections import Generator
import pytest
from playwright.sync_api import APIRequestContext, Playwright, sync_playwright
import libraries.test_data as data
import libraries.locators as locators
import logging
logging.basicConfig(filename="log.txt",level=logging.NOTSET)
@pytest.fixture(scope="session")
def page(playwright):
    # Basic logging setup
    
    logging.info("Initiating Chrome browser")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(data.env_url)
    page.wait_for_selector(locators.login_page["username_textbox"])
    page.fill(locators.login_page["username_textbox"], data.env_userid)
    page.fill(locators.login_page["password_textbox"], data.env_password)
    with page.expect_navigation():
        page.click(locators.login_page["login_button"])
    
    if page.locator(locators.inventory_page["products_header"]).text_content() != "Products":
        logging.error("Failed to load Inventory page")
        assert False
    yield page
    context.close()
    browser.close()


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept": "application/json",
        "Authorization": "token 8eCZ9HjMGTD0JMYuW8ZcEEds3qGYYE7XnVNpGyrB",
    }
    request_context = playwright.request.new_context(
        base_url=data.api_base_url, extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()

    