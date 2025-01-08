# Automation Project: API, Frontend, and GitHub Actions Validation

This project is designed to validate APIs, frontend (FE) functionality, and CI/CD pipelines using GitHub Actions. It integrates Selenium for UI testing, Allure for detailed reporting, and a cron job for scheduled testing.

---

## Features

- **API Testing**: Validate API endpoints using pytest and custom utilities.
- **Frontend Testing**: Automate UI tests using Selenium.
- **GitHub Actions**: Automated workflows for continuous integration.
- **Selenium Hub**: Centralized test execution for cross-browser testing.
- **Allure Reporting**: Comprehensive test results with history tracking.
- **Scheduled Testing**: Execute tests at regular intervals using cron jobs.

---

## Setup and Installation

### Prerequisites

- **Python**: Version 3.13 or higher
- **Poetry**: For dependency management
- **Docker & Docker Compose**: To run Selenium Hub

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Yaronmd/Automation.git
   cd Automation
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Set up Selenium Hub using Docker Compose:
   ```bash
   docker-compose up -d
   ```

4. Install Allure CLI:
   ```bash
   mkdir -p allure
   curl -o allure.zip -L https://github.com/allure-framework/allure2/releases/download/2.32.0/allure-2.32.0.zip
   unzip allure.zip -d allure
   sudo ln -s $PWD/allure/allure-2.32.0/bin/allure /usr/local/bin/allure
   allure --version
   ```

---

## Running Tests

### Locally

1. Start Selenium Hub:
   ```bash
   docker-compose up -d
   ```

2. Run tests with pytest:
   ```bash
   poetry run pytest -s tests/ --alluredir=allure-results
   ```

3. Generate Allure Report:
   ```bash
   allure generate --clean allure-results -o allure-report
   allure open allure-report
   ```

### CI/CD with GitHub Actions

GitHub Actions is configured to:
- Run tests on every push and pull request to the `main` branch.
- Execute scheduled tests using cron jobs.

### Workflow Steps

1. **Checkout Code**: Pull the latest code from the repository.
2. **Set Up Docker**: Install Docker Compose for Selenium Hub.
3. **Run Tests**: Execute API and frontend tests using pytest.
4. **Generate Allure Reports**: Create test reports with history.
5. **Deploy Allure Reports**: Publish the reports to GitHub Pages.

---

## Scheduled Testing with Cron Job

The workflow includes a cron job that triggers tests at regular intervals (e.g., daily or weekly). This ensures continuous validation of API and frontend functionalities.


## Reporting with Allure

Allure provides:
- Test execution history.
- Detailed logs and screenshots for failed tests.
- Integration with GitHub Pages for hosted reports.

### History Management
To maintain test history across runs:
- Copy the `history` folder from the previous report.
- Merge it with the current test results before generating the new report.

---

## Contributing

Contributions are welcome! Please follow the standard fork-and-pull model:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your branch.
4. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
