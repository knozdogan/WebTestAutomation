"""
This module contains tests for the home page of the web application.
"""

def test_home_page(home_page):
    home_page.companyNavbar.click()
    assert home_page.companyNavbar.is_visible()

def test_careers_navbar(career_page):
    career_page.find_your_role_button.click()