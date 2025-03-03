import pytest
import os
from dotenv import load_dotenv
from pages.home_page import HomePage
from pages.career_page import CareerPage
from pages.qa_career_page import QACareerPage
from playwright.sync_api import Playwright

if not os.getenv('WEB_BASE_URL'):
    load_dotenv()

BASE_URL = os.getenv('WEB_BASE_URL')
assert BASE_URL, "WEB_BASE_URL is not defined"

BROWSER = os.getenv("BROWSER", "chromium")

@pytest.fixture(scope="session")
def setup(playwright: Playwright):
    """Provides a browser session for UI tests."""
    browser = getattr(playwright, BROWSER).launch(headless=False)
    context = browser.new_context(base_url=BASE_URL)
    page = context.new_page()
    yield page
    browser.close()

@pytest.fixture(scope="function")
def home_page(playwright: Playwright):
    """Provides a browser session for UI tests."""
    browser = getattr(playwright, BROWSER).launch(headless=False)
    context = browser.new_context(base_url=BASE_URL)
    new_page = context.new_page()
    page = HomePage(new_page)
    page.navigate()
    page.accept_all_cookies()
    page.verify_home_page_is_loaded()
    yield page
    browser.close()

@pytest.fixture(scope="function")
def career_page(playwright: Playwright):
    """Provides a browser session for UI tests."""
    browser = getattr(playwright, BROWSER).launch(headless=False)
    context = browser.new_context(base_url=BASE_URL)
    new_page = context.new_page()
    page = HomePage(new_page)
    page.navigate()
    page.accept_all_cookies()
    page.click_company_navbar()
    page.click_careers_navbar()
    page = CareerPage(new_page)
    page.verify_career_page_is_loaded()
    yield page
    browser.close()

@pytest.fixture(scope="function")
def qa_career_page(playwright: Playwright):
    """Provides a browser session for UI tests."""
    playwright.selectors.set_test_id_attribute('data-select2-id')
    browser = getattr(playwright, BROWSER).launch(headless=False)
    context = browser.new_context(base_url=BASE_URL)
    new_page = context.new_page()
    page = HomePage(new_page)
    page.navigate()
    page.accept_all_cookies()
    page = QACareerPage(new_page)
    page.navigate()
    page.verify_qa_career_page_is_loaded()
    yield page
    browser.close()