from playwright.sync_api import Page, expect
from utils.step_decorator import step

class CareerPage:
    def __init__(self, page: Page):
        self.page = page
        self.find_your_role_button_1st = page.locator("#page-head").get_by_role("link", name="Find your dream job")
        
        # all teams
        self.all_teams_button = page.get_by_role("link", name="See all teams")
        self.team_customer_success_lin = page.get_by_role("link", name="Customer Success")
        self.team_sales = page.get_by_role("link", name="Sales")
        self.team_engineering = page.get_by_role("link", name="Product & Engineering")
        self.team_business_support = page.get_by_role("link", name="Finance & Business Support")
        self.team_marketing = page.get_by_role("link", name="Marketing")
        self.team_ceo_executive_office = page.get_by_role("link", name="CEO's Executive Office")
        self.team_operations = page.get_by_role("link", name="Purchasing & Operations")
        self.team_culture = page.get_by_role("link", name="People & Culture")
        self.team_bussines_intelligence = page.get_by_role("link", name="Business Intelligence")
        self.team_secuirty_engineering = page.get_by_role("link", name="Security Engineering")
        self.team_partnership = page.get_by_role("link", name="Partnerships")
        self.team_qa = page.get_by_role("link", name="Quality Assurance")
        self.team_mobile_business = page.get_by_role("link", name="Mobile Business Unit")
        self.team_partner_support = page.get_by_role("link", name="Partner Support Development")
        self.team_product_design = page.get_by_role("link", name="Product Design")

        # locations
        self.location_heading = page.get_by_role("heading", name="Our Locations")
        self.location_brazil = page.get_by_role("listitem").filter(has_text="Brazil")
        self.location_amsterdam = page.get_by_role("listitem").filter(has_text="Amsterdam")
        self.location_new_york = page.get_by_role("listitem").filter(has_text="New York")

        # life at insider
        self.life_at_insider_heading = page.get_by_role("heading", name="Life at Insider")
        self.slider = page.locator('.elementor-widget-container')



    @step('Verify career page is loaded')
    def verify_career_page_is_loaded(self):
        self.page.wait_for_load_state("load")
        expect(self.page).to_have_title('Ready to disrupt? | Insider Careers')
    
    @step('Click on Find your role button')
    def click_on_find_your_role_button(self):
        self.find_your_role_button_1st.click()

    @step('Click on See all teams button')
    def click_on_see_all_teams_button(self):
        self.all_teams_button.click()

    @step('Verify all teams are displayed')
    def verify_all_teams_are_displayed(self):
        expect(self.team_customer_success_lin).to_be_visible()
        expect(self.team_sales).to_be_visible()
        expect(self.team_engineering).to_be_visible()
        expect(self.team_business_support).to_be_visible()
        expect(self.team_marketing).to_be_visible()
        expect(self.team_ceo_executive_office).to_be_visible()
        expect(self.team_operations).to_be_visible()
        expect(self.team_culture).to_be_visible()
        expect(self.team_bussines_intelligence).to_be_visible()
        expect(self.team_secuirty_engineering).to_be_visible()
        expect(self.team_partnership).to_be_visible()
        expect(self.team_qa).to_be_visible()
        expect(self.team_mobile_business).to_be_visible()
        expect(self.team_partner_support).to_be_visible()
        expect(self.team_product_design).to_be_visible()

    @step('Press right arrow key')
    def press_right_arrow_key(self):
        self.page.locator("body").press("ArrowRight")

    @step('Press left arrow key')
    def press_left_arrow_key(self):
        self.page.locator("body").press("ArrowLeft")


    @step('Verify all locations are displayed')
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

    @step('Verify life at insider section is displayed')
    def verify_life_at_insider_section_is_displayed(self):
        self.life_at_insider_heading.scroll_into_view_if_needed()
        expect(self.life_at_insider_heading).to_be_visible()
        expect(self.slider).to_be_visible()
