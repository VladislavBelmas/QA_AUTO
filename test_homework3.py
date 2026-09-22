import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options)
    browser.get('https://itcareerhub.de/ru')
    yield browser
    browser.quit()


buttons = ['/html/body/div[1]/div[7]/div/div/div[4]/a/img' ,
           '/html/body/div[1]/div[7]/div/div/div[3]/div/div[1]',
           '/html/body/div[1]/div[7]/div/div/div[3]/div/div[2]',
           '/html/body/div[1]/div[7]/div/div/div[3]/div/div[3]',
           '/html/body/div[1]/div[6]/div/div/div[2]/ul/li[2]/a',
           '/html/body/div[1]/div[7]/div/div/div[3]/div/div[5]',
           '/html/body/div[1]/div[7]/div/div/div[3]/div/div[6]',
           '/html/body/div[1]/div[7]/div/div/div[5]',
           '/html/body/div[1]/div[7]/div/div/div[6]'
           ]


buttons_to_click = ['/html/body/div[1]/div[6]/div/div/div[2]/ul/li[2]/a']


@pytest.mark.parametrize('xpath_locator', buttons, ids=['logo', 'programs', 'payments', 'about', 'contacts', 'reviews',
                                                        'blog', 'de button', 'ru button'])
def test_visibility_of_all_buttons(driver, xpath_locator):
    button = driver.find_element(By.XPATH, xpath_locator)
    assert button.is_displayed()


# без наводки очевидно тест на видимость контактов падает, а вилку в первом тесте будто колхоз делать,
# по крайней мере для одного теста
def test_find_contacts_with_action(driver):
    parent = driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div/div/div[3]/div/div[3]')
    action = ActionChains(driver)
    action.move_to_element(parent).perform()

    sleep(2)

    button = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div[2]/ul/li[2]/a')
    assert button.is_displayed()



def test_clicks(driver):
    about_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div/div/div[3]/div/div[3]')
    action = ActionChains(driver)
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div[2]/ul/li[2]/a')
    action.move_to_element(about_button).click(button).perform()

    sleep(2)

    call_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[10]/div/div/div[4]')
    action.click(call_button).perform()

    sleep(2)

    message = driver.find_element(By.XPATH, "//*[contains(text(), 'Запишитесь на ')]")
    assert message

