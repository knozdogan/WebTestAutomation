from playwright.sync_api import Page, expect
import allure

class CareerPage:
    def __init__(self, page: Page):
        self.page = page
        self.find_your_role_button_1st = page.locator("#page-head").get_by_role("link", name="Find your dream job")
        
        # all teams
        self.all_teams_button = page.get_by_role("link", name="See all teams")
        self.teams = [
            'customer-success', 
            'product-and-engineering', 
            'finance-and-accounting', 
            'marketing', 
            'ceos-executive-office', 
            'people-and-culture', 
            'business-intelligence', 
            'sales', 
            'security-engineering', 
            'partnership',
            'quality-assurance',
            'mobile-business-unit', 
            'partner-support-development', 
            'product-design',
        ]

        # locations
        self.location_heading = page.get_by_role("heading", name="Our Locations")
        self.location_brazil = page.get_by_role("listitem").filter(has_text="Brazil")
        self.location_amsterdam = page.get_by_role("listitem").filter(has_text="Amsterdam")
        self.location_new_york = page.get_by_role("listitem").filter(has_text="New York")

        # life at insider
        self.life_at_insider_heading = page.get_by_role("heading", name="Life at Insider")
        self.slider = page.locator('.elementor-swiper')


    @allure.step('Verify career page is loaded')
    def verify_career_page_is_loaded(self):
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_title('Ready to disrupt? | Insider Careers')
    
    @allure.step('Click on Find your role button')
    def click_on_find_your_role_button(self):
        self.find_your_role_button_1st.click()

    @allure.step('Click on See all teams button')
    def click_on_see_all_teams_button(self):
        self.all_teams_button.scroll_into_view_if_needed()
        self.all_teams_button.click()

    @allure.step('Verify all teams are displayed')
    def verify_all_teams_are_displayed(self):
        for team in self.teams:
            _ = [
                a.get_attribute("href") 
                for a in self.page.locator("a").all() 
                if team in (a.get_attribute("href") or "") and a.is_visible(timeout=1000)
            ]
            

    @allure.step('Press right arrow key')
    def press_right_arrow_key(self):
        self.page.locator("body").press("ArrowRight")

    @allure.step('Press left arrow key')
    def press_left_arrow_key(self):
        self.page.locator("body").press("ArrowLeft")


    @allure.step('Verify all locations are displayed')
    def verify_locations_are_displayed(self):
        self.location_heading.scroll_into_view_if_needed()
        expect(self.location_heading).to_be_visible()
        expect(self.location_brazil).to_be_visible()

        self.press_right_arrow_key()
        self.press_right_arrow_key()
        self.press_right_arrow_key()
        expect(self.location_amsterdam).to_be_visible()

        self.press_left_arrow_key()
        self.press_left_arrow_key()
        self.press_left_arrow_key()
        expect(self.location_new_york).to_be_visible()

    @allure.step('Verify life at insider section is displayed')
    def verify_life_at_insider_section_is_displayed(self):
        self.life_at_insider_heading.scroll_into_view_if_needed()
        expect(self.life_at_insider_heading).to_be_visible()
        expect(self.slider).to_be_visible()
