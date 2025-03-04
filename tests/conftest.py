from fixture.api_fixture import api_request_context
from fixture.ui_fixture import setup, career_page, home_page, qa_career_page
import playwright
import allure

# Hook to capture screenshots on failure and attach them to Allure
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure and attach it to Allure report."""
    if call.excinfo is not None: 
        page = item.funcargs.get("home_page") or item.funcargs.get("career_page") or item.funcargs.get("qa_career_page")
        
        if page and hasattr(page, 'page') and isinstance(page.page, playwright.sync_api.Page):
            screenshot = page.page.screenshot()
            allure.attach(screenshot, name=f"Failed Test Screenshot for {item.nodeid}", attachment_type=allure.attachment_type.PNG)