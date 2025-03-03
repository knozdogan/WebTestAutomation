from playwright.sync_api import Page, expect
import allure

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.companyNavbar = page.get_by_role("link", name="Company")
        self.careersNavbar = page.get_by_role("link", name="Careers")
        self.accept_cookies_dialog = page.get_by_role("dialog", name="cookieconsent")
        self.accept_all_button = page.get_by_role("button", name="Accept All")

    @allure.step('Navigate to the home page')
    def navigate(self):
        self.page.goto('/')

    @allure.step('Validate the home page is loaded')
    def verify_home_page_is_loaded(self):
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_title('#1 Leader in Individualized, Cross-Channel CX — Insider')

    @allure.step('Accept all cookies if cookie dialog is displayed')
    def accept_all_cookies(self):
        if self.accept_cookies_dialog.is_visible(timeout=5000):
            self.accept_all_button.click()
    
    @allure.step('Verify the home page is displayed')
    def verify_home_page(self):
        expect(self.companyNavbar).to_be_visible()

    @allure.step('Click on the Company navbar')
    def click_company_navbar(self):
        self.companyNavbar.click()

    @allure.step('Verify the Company navbar is displayed')
    def verify_company_navbar(self):
        expect(self.companyNavbar).to_be_visible()
    
    @allure.step('Click on the Careers navbar')
    def click_careers_navbar(self):
        self.careersNavbar.click()

    @allure.step('Verify the Careers navbar is displayed')
    def verify_careers_navbar(self):
        expect(self.careersNavbar).to_be_visible()
    
    