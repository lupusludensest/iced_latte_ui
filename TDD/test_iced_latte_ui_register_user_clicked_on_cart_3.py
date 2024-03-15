from all_locators_tdd import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_iced_latte_ui_3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://iced-latte.uk/")
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    # Registered user is loggin with valid credentials
    email_valid = 'gurovvic@gmail.com'
    password_valid = 'qwertyuiop12!@'

    # Click user authorization icon
    driver.find_element(*USER_AUTH_ICON).click()
    sleep(4)

    # Send registered email to email field
    first_name_field = driver.find_element(*EML_FLD)
    first_name_field.clear()
    first_name_field.send_keys(email_valid)
    # sleep(2)

    # Send valid password to password field
    first_name_field = driver.find_element(*PSWRD_FLD)
    first_name_field.clear()
    first_name_field.send_keys(password_valid)
    # sleep(2)

    # Click login button
    driver.find_element(*LGN_BTN).click()
    # sleep(2)

    # Click on cart icon
    driver.find_element(*CLCK_ON_CART_ICN).click()
    # sleep(2)

    # Assert shopping cart page is open
    # Text 'Shopping cart' is here
    shopping_cart_txt = driver.find_element(*SHPNG_CRT_TXT)
    expected_text = 'Shopping cart'
    actual_text = shopping_cart_txt.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # URL "https://iced-latte.uk/cart" is active
    driver.get("https://iced-latte.uk/cart")
    if driver.current_url == "https://iced-latte.uk/cart":
        print("The expected URL 'https://iced-latte.uk/cart' is open.")
    else:
        print(f"Unexpected URL opened: {driver.current_url}")

    # Text 'Your cart is empty' is here
    your_cart_is_empty = driver.find_element(*YR_CRT_IS_EMPTY)
    expected_text = 'Your cart is empty'
    actual_text = your_cart_is_empty.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # Continue Shopping button is here
    cntnue_shpng_btn = driver.find_element(*CNTNUE_SHPNG_BTN)
    expected_text = 'Continue Shopping'
    actual_text = cntnue_shpng_btn.text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


    sleep(4)
    driver.delete_all_cookies()
    # driver.quit()