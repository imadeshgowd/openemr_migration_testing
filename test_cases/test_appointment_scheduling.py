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

def test_appointment_scheduling(setup):
    driver = setup
    driver.find_element_by_xpath('//div[text()="Calendar"]').click()
    driver.switch_to.frame(driver.find_element_by_name('cal'))
    driver.find_element_by_xpath('//button[text()="Add"]').click()
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="/openemr/interface/main/calendar/add_edit_event.php"]'))
    driver.find_element_by_id('form_date').send_keys("2024-05-20")
    driver.find_element_by_id('form_time').send_keys("10:00")
    driver.find_element_by_id('form_save').click()
    success_message = driver.find_element_by_xpath("//div[contains(text(), '10:00')]").text
    assert "10:00" in success_message