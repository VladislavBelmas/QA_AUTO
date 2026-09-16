from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:

    driver.get('https://itcareerhub.de/ru')

    sleep(5)

    driver.find_element(By.LINK_TEXT, 'Способы оплаты').click()

    driver.maximize_window()

    sleep(3)

    driver.save_screenshot('C:\\Users\\vladb\\Documents\\ICH\\ich_screen.png',)

    sleep(10)

finally:
    driver.quit()

