from playwright.sync_api import Page, expect
from utils.step_decorator import step

class CareerPage:
    def __init__(self, page: Page):
        self.page = page
        self.find_your_role_button = page.locator("#page-head").get_by_role("link", name="Find your dream job")
    
    @step('Verify career page is loaded')
    def verify_career_page_is_loaded(self):
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_title('Ready to disrupt? | Insider Careers')
        