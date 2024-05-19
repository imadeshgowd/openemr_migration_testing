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

def test_patient_registration(setup):
    driver = setup
    driver.find_element_by_xpath('//div[text()="Patient/Client"]').click()
    driver.find_element_by_xpath('//div[text()="New/Search"]').click()
    driver.switch_to.frame(driver.find_element_by_name('pat'))
    driver.find_element_by_id('form_fname').send_keys("John")
    driver.find_element_by_id('form_lname').send_keys("Doe")
    driver.find_element_by_id('form_DOB').send_keys("2023-05-20")
    driver.find_element_by_id('create').click()
    success_message = driver.find_element_by_xpath("//span[contains(text(), 'John Doe')]").text
    assert "John Doe" in success_message