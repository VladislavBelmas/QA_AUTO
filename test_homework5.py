import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    yield driver
    driver.quit()


def test_iframes(driver):
    iframe_element = driver.find_elements(By.TAG_NAME, 'iframe')
    found = False
    for index in range(len(iframe_element)):
        try:
            driver.switch_to.frame(index)
            result = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[contains(., "semper posuere integer")]'))
            )

            assert result.is_displayed()
            found = True
            break
        except (NoSuchElementException, TimeoutException):
            driver.switch_to.default_content()

    assert found