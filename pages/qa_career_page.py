from playwright.sync_api import Page, expect
import allure

class QACareerPage:
    def __init__(self, page: Page):
        self.page = page


    @allure.step('Verify QA career page is loaded')
    def verify_qa_career_page_is_loaded(self):
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_title('Insider quality assurance job opportunities')

    @allure.step('Navigate to the QA career page')
    def navigate(self):
        self.page.goto('/careers/quality-assurance/')
    
