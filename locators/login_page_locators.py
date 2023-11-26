from selenium.webdriver.common.by import By


class LoginPageLocators:
   LOGIN_BUTTON = (By.ID, "login-button")
   USERNAME_FIELD = (By.ID, "user-name")
   PASSWORD_FIELD = (By.ID, "password")
   LOGIN_ERROR = (By.CSS_SELECTOR, "h3[data-test='error'")
   ITEM_PICTURE = (By.CSS_SELECTOR, "img.inventory_item_img")