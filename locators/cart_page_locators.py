from selenium.webdriver.common.by import By


class CartPageLocators:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CHECKOUT_FIRSTNAME = (By.ID, "first-name")
    CHECKOUT_LASTNAME = (By.ID, "last-name")
    CHECKOUT_POSTAL_CODE = (By.ID, "postal-code")
    CHECKOUT_CONTINUE_BUTTON = (By.ID, "continue")
    PAYMENT_INFO_TEXT = (By.XPATH, "//*[@class='summary_value_label'][1]")
    SHIPPING_INFO_TEXT = (By.XPATH, "//*[@class='summary_value_label'][2]")
    PRICES_FROM_CART_CUSTOM = (By.CLASS_NAME, "inventory_item_price")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETED_MESSAGE = (By.CLASS_NAME, "complete-header")
    ERROR_RED_FIELDS = (By.CLASS_NAME, "input_error.form_input.error")
    ERROR_BUTTON_TEXT = (By.XPATH, "//h3[contains(@data-test,'error')]")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")
    REMOVE_BUTTON_UNIVERSAL = [By.ID, ""]
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
