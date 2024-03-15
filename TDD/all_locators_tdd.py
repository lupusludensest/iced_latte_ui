from selenium.webdriver.common.by import By

# Locators
USER_AUTH_ICON = (By.XPATH, "//img[@alt='auth icon']")
REGISTER_BTN = (By.XPATH, "//button[@type='button']")
FRST_NM_FLD = (By.XPATH, "//input[@id='firstName']")
LST_NM_FLD = (By.XPATH, "//input[@id='lastName']")
EML_FLD = (By.XPATH, "//input[@id='email']")
PSWRD_FLD = (By.XPATH, "//input[@id='password']")
REGISTER_USER_BTN = (By.XPATH, "//button[@type='submit']")