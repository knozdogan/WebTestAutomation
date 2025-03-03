"""
This module contains all tests of career page for the web application.
"""
import allure

@allure.title("Check all teams section in career page is visible")
def test_teams_section(career_page):
    career_page.click_on_see_all_teams_button()
    career_page.verify_all_teams_are_displayed()

@allure.title("Check all locations section in career page is visible")
def test_locations_section(career_page):
    career_page.verify_locations_are_displayed()

@allure.title("Check life at insider section in career page is visible")
def test_life_at_insider_section(career_page):
    career_page.verify_life_at_insider_section_is_displayed()

