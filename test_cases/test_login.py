import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.config import BASE_URL, USERNAME, PASSWORD, DRIVER_PATH

@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_service = Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(BASE_URL + '/interface/login/login.php?site=default')
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup
    driver.find_element_by_id('authUser').send_keys(USERNAME)
    driver.find_element_by_id('clearPass').send_keys(PASSWORD)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    assert "Flow Board" in driver.title