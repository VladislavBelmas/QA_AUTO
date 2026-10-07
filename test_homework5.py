from dataclasses import asdict
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def driver():
    options = Options()
    options.set_preference("privacy.trackingprotection.enabled", True)
    options.set_preference("dom.webnotifications.enabled", False)
    options.set_preference("dom.push.enabled", False)
    options.set_preference("network.cookie.cookieBehavior", 1)
    driver = webdriver.Firefox(options=options)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    yield driver
    driver.quit()


def test_iframes(driver):
    wait = WebDriverWait(driver, 10)
    iframes = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "iframe")))

    found = False
    for i in iframes:
        driver.switch_to.default_content()
        wait.until(EC.frame_to_be_available_and_switch_to_it(i))

        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(., 'semper posuere')]"))
            )
            found = True
            break
        except TimeoutException:
            continue

    assert found


def test_drag_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    gallery = wait.until(EC.visibility_of_element_located((By.ID, 'gallery')))
    pics_in_gallery_old = gallery.find_elements(By.TAG_NAME, 'img')
    bucket = driver.find_element(By.ID, 'trash')
    action = ActionChains(driver)
    pic_1 = gallery.find_element(By.TAG_NAME, 'img')
    action.drag_and_drop(pic_1, bucket).perform()
    wait.until(lambda d: len(bucket.find_elements(By.TAG_NAME, 'img')) > 0)
    pics_in_gallery_new = gallery.find_elements(By.TAG_NAME, 'img')

    assert len(pics_in_gallery_new) + 1 == len(pics_in_gallery_old)
