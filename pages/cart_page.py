from data.data import ITEMS_TITLES
from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    def open_checkout_form(self):
        """ Opens checkout form """
        self.browser.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()

    def fill_checkout_form(self, f_name, l_name, postal_code):
        """ Fill checkout form """
        self.browser.find_element(*CartPageLocators.CHECKOUT_FIRSTNAME).send_keys(f_name)
        self.browser.find_element(*CartPageLocators.CHECKOUT_LASTNAME).send_keys(l_name)
        self.browser.find_element(*CartPageLocators.CHECKOUT_POSTAL_CODE).send_keys(postal_code)

    def submit_checkout_form(self):
        """ Submits checkout form """
        self.browser.find_element(*CartPageLocators.CHECKOUT_CONTINUE_BUTTON).click()

    def get_payment_info(self):
        """ Returns payment information """
        payment_text = self.browser.find_element(*CartPageLocators.PAYMENT_INFO_TEXT).text
        return payment_text

    def get_shipping_info(self):
        """ Returns shipping information """
        shipping_text = self.browser.find_element(*CartPageLocators.SHIPPING_INFO_TEXT).text
        return shipping_text

    def __count_amount_of_cart(self):
        """ Count cart price by addition each item's price it the cart"""
        prices = self.browser.find_elements(*CartPageLocators.PRICES_FROM_CART_CUSTOM)
        total_price = 0
        for i in prices:
            i = i.text
            total_price += float(i.replace('$', ''))
        return total_price

    def __count_tax_amount(self, func):
        """ Calculate tax amount """
        price = func
        tax_raw = price*0.08
        tax = format(tax_raw, '.2f')
        return tax

    def check_item_total_price(self):
        """ Count manualy item's total price and compare with value of 'Item total' field """
        total_price = self.__count_amount_of_cart()
        value = self.browser.find_element(*CartPageLocators.ITEM_TOTAL).text
        value = float(value[value.find("$")+1:])
        flag = total_price == value
        return flag, value


    def check_tax_amount(self):
        """ Count manualy tax amount and compare with value of 'tax' field """
        tax = self.__count_tax_amount(self.__count_amount_of_cart())
        value = self.browser.find_element(*CartPageLocators.TAX).text
        value = value[value.find("$")+1:]
        flag = float(tax) == float(value)
        return flag, value

    def finish_checkout(self):
        """ Finish checkout """
        self.browser.find_element(*CartPageLocators.FINISH_BUTTON).click()

    def return_success_message(self):
        """ Returns success message """
        success_text = self.browser.find_element(*CartPageLocators.COMPLETED_MESSAGE).text
        return success_text

    def get_list_of_highlighted_field(self):
        """ Returns validation error list of elements """
        error_fields = self.browser.find_elements(*CartPageLocators.ERROR_RED_FIELDS)
        return error_fields

    def get_error_text_from_button(self):
        """ Returns text from error button of checkout form page """
        error_text = self.browser.find_element(*CartPageLocators.ERROR_BUTTON_TEXT).text
        return error_text

    def count_items_in_the_cart(self):
        """ Returns number of items in the cart """
        amount = len(self.browser.find_elements(*CartPageLocators.CART_ITEM))
        return amount

    def remove_item_from_the_cart(self, items_titles: list):
        """ Removes one item out of the cart"""
        for elem in items_titles:
            item = ITEMS_TITLES[elem]
            CartPageLocators.REMOVE_BUTTON_UNIVERSAL[1] = f"{item[1]}"
            self.browser.find_element(*CartPageLocators.REMOVE_BUTTON_UNIVERSAL).click()

    def remove_all_items_from_the_cart(self, ITEMS: dict):
        """ Removes all item from pre-setuped dict out of the cart """
        keys_list = list(ITEMS.keys())
        for elem in keys_list:
            # fill flexible selector by the value
            value = ITEMS[elem]
            CartPageLocators.REMOVE_BUTTON_UNIVERSAL[1] = f"{value[1]}"
            self.browser.find_element(*CartPageLocators.REMOVE_BUTTON_UNIVERSAL).click()

    def check_cart_is_empty(self):
        """ Returns True if cart is empty """
        flag = self.is_not_element_present(*CartPageLocators.CART_ITEM, timeout=5)
        return flag

    def go_to_continue_shopping(self):
        """ Move back to inventory page """
        self.browser.find_element(*CartPageLocators.CONTINUE_SHOPPING_BUTTON).click()

