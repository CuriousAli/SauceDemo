from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators


class BasePage:
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException,):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=15):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def check_footer_social_links(self):
        """ Checks links presence. Returns boolean True for success or False for failure """
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        twitter = self.is_element_present(*BasePageLocators.TWITTER_LINK)
        fb = self.is_element_present(*BasePageLocators.FACEBOOK_LINK)
        linkedin = self.is_element_present(*BasePageLocators.LINKEDIN_LINK)
        flag = True if twitter and fb and linkedin else False
        return flag

    def do_login(self, username, password):
        """ Authenticates user and asserts login process """
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(username)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

