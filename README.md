# E2E Test Automation

## Project Overview
This project is designed to provide end-to-end (E2E) test automation for web applications. It uses modern testing frameworks and tools to ensure the reliability and performance of web applications.

## Tools Used
- **Locust**: For performance testing.
- **Python Playwright**: For API and UI testing.

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

## Installation
To install the necessary dependencies, run the following command:
```bash
pip install -r requirements.txt
```

## Usage
To run the performance tests using Locust, use the following command:
```bash
locust -f tests/performance-tests/locustfile.py --headless --users 1 -t 10s -H https://www.example.com --html test-results/report.html
```

To run the API and UI tests using Python Playwright, use the following command:
```bash
pytest -v
```

## Directory Structure
```
/WebTestAutomation
├── .github/
│   └── workflows/
│       ├── ci-tests.yml
│       └── performance-tests.yml
├── fixtures/
│   ├── api_fixture.py
│   └── ui_fixture.py
├── api/
│   ├── petstore_api.py
│   └── schema.py
├── pages/
│   ├── career_page.py
│   ├── home_page.py
│   └── qa_career_page.py
├── tests/
│   ├── api-tests/
│       └── test_petstore_api.py
│   ├── web-app-tests/
│       ├── test_career_page.py
│       └── test_qa_career_page.py
│   ├── performance-tests/
│       └── locustfile.py
│   ├── __init__.py
│   └── conftest.py
├── utils/
│   └── request_helper.py
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Continuous Integration
This project uses GitHub Actions for continuous integration. The following workflows are defined:
- **Playwright Tests**: `.github/workflows/ci-tests.yml`
- **Performance Tests**: `.github/workflows/performance-tests.yml`

These workflows are triggered on push and pull request events to ensure that all tests are run automatically.
