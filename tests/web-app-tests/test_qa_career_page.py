"""

"""
import allure
import pytest

@allure.title("Check all teams section in career page is visible")
@pytest.mark.parametrize('location, department', [
    ('Istanbul, Turkiye', 'Sales'),
    ('Paris, France', 'Customer Success'),
])
def test_department_location_selection(qa_career_page, location, department):
    qa_career_page.click_on_see_all_qa_jobs_button()
    qa_career_page.select_location(location)
    qa_career_page.select_department(department)
    qa_career_page.verify_all_jobs_has_department_and_location(department, location)

@allure.title('Check all listed jobs has QA department')
def test_all_jobs_has_qa_department(qa_career_page):
    qa_career_page.click_on_see_all_qa_jobs_button()
    qa_career_page.verify_all_jobs_has_department("Quality Assurance")

@allure.title("Check redirection to Lever application form")
def test_redirection_to_application_form(qa_career_page):
    qa_career_page.click_on_see_all_qa_jobs_button()
    qa_career_page.select_location("Istanbul, Turkiye")
    qa_career_page.verify_redirection_to_application_form()