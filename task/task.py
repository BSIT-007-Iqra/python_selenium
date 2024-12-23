import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# Fixture for setup and teardown
@pytest.fixture(scope="function")
def setup_and_teardown():
    # Initialize the driver for each test case
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://missrosepk.com/account/login")
    #driver.maximize_window()
    yield driver  # Provide the driver instance to the test
    driver.quit()  # Cleanup after the test

# Test data
def function_check():
    return [
        ('yousafge00@gmail.com', 'iqra@12.'),
        ('zainab841@gmail.com', 'zaini123.!'),
        ('fizaakram56@gmail.com', 'fiza!_130')
    ]

@pytest.mark.parametrize("username,password", function_check())
def test_login(username, password, setup_and_teardown):  # Accept the fixture here
    driver = setup_and_teardown
    try:
        # Enter username and password
        driver.find_element(By.ID, "CustomerEmail").send_keys(username)
        driver.find_element(By.ID, "CustomerPassword").send_keys(password)
        # Assuming there's a login button to click
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        allure.attach(driver.get_screenshot_as_png(),name="login_sc",attachment_type=AttachmentType.PNG)

        # Assertion (modify as per your app's success indicator)
        assert "account" in driver.current_url, f"Login failed for {username}!"
        print(f"Login successful for {username}!")
    except NoSuchElementException as e:
        pytest.fail(f"Test failed due to missing element: {str(e)}")

