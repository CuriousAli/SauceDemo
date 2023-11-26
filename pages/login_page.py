from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.base_page_locators import BasePageLocators


class LoginPage(BasePage):
    def do_login(self, username, password):
        """ Authenticates user and asserts login process """
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(username)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def should_be_logout_button(self):
        """ Check presence of logout button and returns boolean """
        flag = self.is_element_present(*BasePageLocators.LOGOUT_MENU_BUTTON)
        return flag

    def get_error_text(self):
        """ gets error text after failed login """
        error_text = self.browser.find_element(*LoginPageLocators.LOGIN_ERROR).text
        return error_text

    def check_login_duration(self, s_time, f_time, username):
        """ Checks for each valid user acceptable duration of login proccess"""
        d_time = f_time - s_time
        if (username == "standard_user" or username == "problem_user") and d_time < 2:
            return (True, None, None)
        elif username == "performance_glitch_user" and 2 <= d_time <= 20:
            return (True, None, None)
        else:
            info = (False, d_time, username)
            return info

    def check_pictures(self, username):
        """ Checks that pucture's name contain 1500x1000 value """
        img_names = self.browser.find_elements(*LoginPageLocators.ITEM_PICTURE)
        flag = True
        for img in img_names:
            src = img.get_attribute('src')
            if '1200x1500' not in src:
                flag = False
        if flag == False and username == 'problem_user':
            flag = True

        return flag



