# banking-test-automation

# ParaBank Banking Automation Framework 🏦

A comprehensive test automation framework for ParaBank banking application, demonstrating UI, API, and cloud testing capabilities.

## 🎯 Project Overview

This framework tests critical banking functionalities including:
- User authentication and registration
- Account management
- Fund transfers
- Transaction history
- Bill payments

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **UI Automation:** Selenium WebDriver
- **API Testing:** Requests, JSON Schema validation
- **Test Framework:** Pytest
- **Reporting:** Allure Reports, Pytest-HTML
- **Cloud Testing:** BrowserStack
- **CI/CD:** GitHub Actions
- **Performance:** Locust

## 📁 Project Structure

parabank-automation-framework/
├── tests/              # Test suites (UI, API, Integration)
├── pages/              # Page Object Model
├── api/                # API client modules
├── config/             # Configuration management
├── utils/              # Reusable utilities
├── docs/               # Test plans and documentation
└── reports/            # Test execution reports


## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Chrome/Firefox browser
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/parabank-automation-framework.git
cd parabank-automation-framework
```

2. Create virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Setup environment variables:

cp .env.example .env
# Edit .env with your configuration

▶️ Running Tests

Run all tests:
```commandline
pytest

```

Run specific test suites:

pytest tests/ui_tests/          # UI tests only
pytest tests/api_tests/         # API tests only
pytest -m smoke                 # Smoke tests only

Generate Allure Report:

pytest --alluredir=reports/allure-results
allure serve reports/allure-results

📊 Test Coverage

✅ UI Automation (Login, Transfer, Account Management)
✅ API Testing (REST API validation)
✅ Integration Testing (End-to-end workflows)
✅ Cross-browser Testing (Chrome, Firefox, Edge)
✅ Cloud Testing (BrowserStack integration)
✅ CI/CD Pipeline (GitHub Actions)

5. ✅ Commit and push:

git add .
git commit -m "Initial project setup"
git push origin main



