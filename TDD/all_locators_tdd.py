from selenium.webdriver.common.by import By

# Locators
USER_AUTH_ICON = (By.XPATH, "//img[@alt='auth icon']")
REGISTER_BTN = (By.XPATH, "//button[@type='button']")
FRST_NM_FLD = (By.XPATH, "//input[@id='firstName']")
LST_NM_FLD = (By.XPATH, "//input[@id='lastName']")
EML_FLD = (By.XPATH, "//input[@id='email']")
PSWRD_FLD = (By.XPATH, "//input[@id='password']")
REGISTER_USER_BTN = (By.XPATH, "//button[@type='submit']")
LGN_BTN = (By.XPATH, "//button[@type='submit']")
# REGISTERED_USR_LOGGED_LOGO = (By.XPATH, "//div[@class='text-primary font-medium text-[12px] md:text-[16px] overflow-hidden whitespace-nowrap sm:block hidden']")
REGISTERED_USR_LOGGED_LOGO = (By.XPATH, "//div[text() = 'Viachesla...']")


