import os  # For accessing environment variables
from .env import load_dotenv  # For reading .env file

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    This class reads settings from .env file and makes them available
    to all our test files in one place

    Think of it as a "Settings Remote Control" for your entire project
    """

    # URLs - Where to test
    # os.getenv('BASE_URL') reads BASE_URL from .env file
    # If not found, uses the default value after the comma
    BASE_URL = os.getenv('BASE_URL', 'https://parabank.parasoft.com/parabank')
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://parabank.parasoft.com/parabank/services/bank')

    # Browser Settings
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'  # Convert string to boolean

    # Timeouts - How long to wait
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', 10))  # Convert string to number
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', 20))

    # Test Credentials - Login info
    TEST_USERNAME = os.getenv('TEST_USERNAME', 'john')
    TEST_PASSWORD = os.getenv('TEST_PASSWORD', 'demo')

    # Paths - Where to save stuff
    SCREENSHOTS_DIR = 'reports/screenshots'  # Save failed test screenshots here
    REPORTS_DIR = 'reports'  # Save test reports here