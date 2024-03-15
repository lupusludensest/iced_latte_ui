from all_locators_tdd import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_iced_latte_ui_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://iced-latte.uk/")
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    # Click user authorization icon
    driver.find_element(*USER_AUTH_ICON).click()
    # sleep(2)