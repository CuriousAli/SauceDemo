from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGOUT_MENU_BUTTON = (By.ID, "logout_sidebar_link")
    TWITTER_LINK = (By.XPATH, "//a[@href='https://twitter.com/saucelabs']")
    FACEBOOK_LINK = (By.XPATH, "//a[@href='https://www.facebook.com/saucelabs']")
    LINKEDIN_LINK = (By.XPATH, "//a[@href='https://www.linkedin.com/company/sauce-labs/']")
