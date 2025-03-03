from playwright.sync_api import Page, expect
import allure
import re

TIMEOUT = 10000

class QACareerPage:
    def __init__(self, page: Page):
        self.page = page
        self.see_all_qa_jobs_button = page.get_by_role("link", name="See all QA jobs")
        self.location_container = page.get_by_test_id('filter-by-location') #page.locator("#select2-filter-by-location-container")
        self.department_container = page.get_by_test_id('filter-by-department')
        self.view_role_button = page.get_by_role("link", name="View Role")
        self.job_list = page.locator(".position-list-item-wrapper")



    @allure.step('Verify QA career page is loaded')
    def verify_qa_career_page_is_loaded(self):
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_title('Insider quality assurance job opportunities')

    @allure.step('Navigate to the QA career page')
    def navigate(self):
        self.page.goto('/careers/quality-assurance/')

    @allure.step('Click on see all QA jobs button')
    def click_on_see_all_qa_jobs_button(self):
        with self.page.expect_response(lambda response: 'postings/useinsider' in response.url and response.status == 200, timeout=TIMEOUT):
            self.see_all_qa_jobs_button.click()
            expect(self.department_container).to_have_value('Quality Assurance', timeout=TIMEOUT)

    @allure.step('Select location')
    def select_location(self, location: str):
        with self.page.expect_response(lambda response: 'postings/useinsider' in response.url and response.status == 200):
            self.location_container.select_option(value=location)
            expect(self.location_container).to_have_value(location, timeout=TIMEOUT)

    @allure.step('Select department')
    def select_department(self, department: str):
        with self.page.expect_response(lambda response: 'postings/useinsider' in response.url and response.status == 200):
            self.department_container.select_option(value=department)
            expect(self.department_container).to_have_value(department, timeout=TIMEOUT)

    @allure.step('Verify all listed jobs has department')
    def verify_all_jobs_has_department(self, department: str,):
        count = self.job_list.count()
        assert count > 0, "There is no open positions"

        for i in range(count):
            expect(
                self.job_list.nth(i),
                f"Job at index {i} is missing expected department.").to_contain_text(department)

    @allure.step('Verify all listed jobs has department and location')
    def verify_all_jobs_has_department_and_location(self, department: str, location: str):
        count = self.job_list.count()
        assert count > 0, "There is no open positions"

        for i in range(count):
            expect(
                self.job_list.nth(i),
                f"Job at index {i} is missing expected department.").to_contain_text(department)
            expect(
                self.job_list.nth(i),
                f"Job at index {i} is missing expected location.").to_contain_text(location)

    @allure.step('Verify redirection to Lever application form')
    def verify_redirection_to_application_form(self):
        with self.page.expect_popup() as new_tab:
            self.job_list.first.click()
            self.view_role_button.first.click()
            expect(new_tab.value).to_have_url(re.compile(r"^https://jobs.lever.co/useinsider/"))

    
