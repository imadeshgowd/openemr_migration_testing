import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.config import BASE_URL, DRIVER_PATH

@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_service = Service(DRIVER_PATH)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(BASE_URL + '/interface/login/login.php?site=default')
    driver.find_element_by_id('authUser').send_keys('admin')
    driver.find_element_by_id('clearPass').send_keys('pass')
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    yield driver
    driver.quit()

def test_billing(setup):
    driver = setup
    driver.find_element_by_xpath('//div[text()="Fees"]').click()
    driver.find_element_by_xpath('//div[text()="Billing"]').click()
    driver.switch_to.frame(driver.find_element_by_name('fin'))
    driver.find_element_by_id('searchString').send_keys("Doe")
    driver.find_element_by_id('bn_search').click()
    success_message = driver.find_element_by_xpath("//span[contains(text(), 'Doe')]").text
    assert "Doe" in success_message