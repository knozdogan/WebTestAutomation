import pytest
from playwright.sync_api import APIRequestContext, Playwright
import os
from dotenv import load_dotenv
from typing import Generator

if not os.getenv('API_BASE_URL'):
    load_dotenv()

BASE_URL = os.getenv('API_BASE_URL')
assert BASE_URL, "API_BASE_URL is not defined"

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    """
    Provides a Playwright APIRequestContext for making API calls.
    """
    request_context = playwright.request.new_context(
        base_url=BASE_URL,
        extra_http_headers={'accept': 'application/json'}
    )
    yield request_context
    request_context.dispose()