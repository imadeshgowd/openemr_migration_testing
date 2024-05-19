# OpenEMR Migration Testing

This repository contains automated test scripts for the migration of the OpenEMR system from a legacy system to a new platform. The tests are written in Python using Selenium for browser automation.

## Project Structure

- `test_cases/`: Contains all test scripts.
- `utils/`: Utility functions and configuration.
- `reports/`: Directory for test reports.
- `run_tests.py`: Script to execute all tests.
- `requirements.txt`: Python dependencies.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/openemr_migration_testing.git
    cd openemr_migration_testing
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download ChromeDriver**:
   Download the ChromeDriver from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   Ensure the version matches your installed Google Chrome version. Extract it and note the path to `chromedriver`.

4. **Update `config.py`**:
   Edit `utils/config.py` and set the `DRIVER_PATH` to the location of your `chromedriver`.

    ```python
    # Configuration for the test environment

    BASE_URL = 'https://demo.openemr.io/openemr'
    USERNAME = 'admin'
    PASSWORD = 'pass'
    DRIVER_PATH = '/path/to/your/chromedriver'  # Update this path to the correct location
    ```

5. **Ensure Executable Permissions**:
    Make sure that the ChromeDriver executable has the necessary permissions to run:
    ```bash
    chmod +x /path/to/your/chromedriver
    ```

## Running Tests

To run all tests and generate a report:
```bash
python run_tests.py
```

## Test Cases

- `test_login.py`: Tests user login functionality.
- `test_patient_registration.py`: Tests patient registration functionality.
- `test_appointment_scheduling.py`: Tests appointment scheduling functionality.
- `test_billing.py`: Tests billing functionality.
- `test_data_migration.py`: Validates data migration.

## Reports

Test reports are generated in the `reports/` directory.