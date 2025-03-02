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
locust
```

To run the API and UI tests using Python Playwright, use the following command:
```bash
pytest
```

## Directory Structure
```
/WebTestAutomation
├── .github
│   ├── workflows
│       ├── api-tests.yml
│       ├── ui-tests.yml
│       ├── performance-tests.yml
├── fixtures
├── tests
│   ├── api-tests
│   ├── ui-tests
│   └── performance-tests
└── requirements.txt
```

## Continuous Integration
This project uses GitHub Actions for continuous integration. The following workflows are defined:
- **API Tests**: `.github/workflows/api-tests.yml`
- **UI Tests**: `.github/workflows/ui-tests.yml`
- **Performance Tests**: `.github/workflows/performance-tests.yml`

These workflows are triggered on push and pull request events to ensure that all tests are run automatically.
