import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    options = Options()
    driver = webdriver.Firefox(options)
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.close()


def test_button(driver):
    driver.get("http://uitestingplayground.com/textinput")
    input_field = driver.find_element(By.CLASS_NAME, 'form-control')
    input_field.send_keys('itch')
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()

    result = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'btn-primary'), 'itch'))

    assert result, 'not itch'


def test_img(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, '#landscape')))

    alt = driver.find_element(By.CSS_SELECTOR, '#award')

    assert alt.get_attribute('alt') == 'award'