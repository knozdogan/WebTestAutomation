# E2E Test Automation

## Project Overview
This project provides end-to-end (E2E) test automation for web applications and APIs. It includes UI testing, API testing, and performance testing using modern tools like **Playwright** and **Locust**. The project follows the **Page Object Model (POM)** design pattern for UI tests and integrates with **Allure** for reporting and **GitHub Actions** for continuous integration (CI).

---
## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Tools and Frameworks](#tools-and-frameworks)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Running Tests](#running-tests)
   - [UI Tests](#ui-tests)
   - [API Tests](#api-tests)
   - [Performance Tests](#performance-tests)
6. [Directory Structure](#directory-structure)
7. [Continuous Integration (CI)](#continuous-integration-ci)
---

## **Project Overview**
This project is designed to automate end-to-end testing for web applications and APIs. It includes:
- **UI Testing**: Automated tests for the Insider web application, including the home page, career page, and QA career page.
- **API Testing**: Automated tests for the PetStore API, covering CRUD operations and schema validation.
- **Performance Testing**: Load testing for the search module of `https://www.n11.com/` using Locust.

---
## **Tools and Frameworks**
- **Playwright**: For UI and API testing.
- **Locust**: For performance testing.
- **Pydantic**: For schema validation in API tests.
- **Allure**: For test reporting.
- **GitHub Actions**: For continuous integration (CI).

---

## **Prerequisites**
- **Python 3.7 or higher**
- **pip**: Python package installer.
- **Git**: For version control and CI integration.
- **Allure Commandline**: For generating Allure reports locally (optional).

---

## Installation
To install the necessary dependencies, run the following command:
```bash
pip install -r requirements.txt
```
To install Playwright browsers, run the following command:
```bash
python -m playwright install --with-deps
```
---
## Running Tests
### UI Tests
To run the UI tests, use the following command:
```bash
pytest tests/web-app-tests/ -v
```

#### Browser selection
You can run tests in different browsers by setting the BROWSER environment variable:
```bash
export BROWSER=firefox  # or chromium, webkit
pytest tests/web-app-tests/ -v
```

#### Allure report
To generate Allure reports for UI tests:
```bash
pytest tests/web-app-tests/ --alluredir=allure-results
allure serve allure-results
```
---
### API Tests
To run the API tests, use the following command:
```bash
pytest tests/api-tests/ -v
```
---
### Performance Tests
To run the performance tests using Locust:
```bash
locust -f tests/performance-tests/locustfile.py --headless --users 1 -t 10s -H https://www.n11.com --html test-results/report.html
```
---
## Directory Structure
```
/WebTestAutomation
├── .github/
│   └── workflows/
│       ├── ci.yml               # GitHub Actions workflow for Playwright tests
│       └── performance-tests.yml # GitHub Actions workflow for Locust tests
├── api/
│   ├── petstore_api.py          # PetStore API client
│   └── schema.py                # Pydantic schemas for API validation
├── fixtures/
│   ├── api_fixture.py           # Fixtures for API tests
│   └── ui_fixture.py            # Fixtures for UI tests
├── pages/
│   ├── career_page.py           # Career page interactions
│   ├── home_page.py             # Home page interactions
│   └── qa_career_page.py        # QA career page interactions
├── tests/
│   ├── api-tests/               # API tests
│   ├── web-app-tests/           # UI tests
│   ├── performance-tests/       # Performance tests
│   └── conftest.py              # Shared fixtures and hooks
├── utils/
│   └── request_helper.py        # Utility for sending API requests
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Continuous Integration (CI)
This project uses GitHub Actions for CI. The following workflows are defined:
- **Playwright Tests:** Runs UI and API tests on push or pull request to the main branch. [Latest Allure Report](https://knozdogan.github.io/WebTestAutomation/)
- **Performance Tests:** Runs Locust performance tests on push or pull request to the main branch.
These workflows are triggered on push and pull request events to ensure that all tests are run automatically.