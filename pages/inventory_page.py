from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from locators.inventory_page_locators import InventoryPageLocators
from data.data import ITEMS_TITLES



class InventoryPage(BasePage):
    def add_item_to_the_cart(self, items_titles: list):
        """ Adds one item to the cart"""
        for elem in items_titles:
            item = ITEMS_TITLES[elem]
            InventoryPageLocators.ITEM_BUTTON_UNIVERSAL[1] = f"{item[0]}"
            self.browser.find_element(*InventoryPageLocators.ITEM_BUTTON_UNIVERSAL).click()

    def go_to_the_cart(self):
        """ Open cart page """
        self.browser.find_element(*InventoryPageLocators.CART_ICON).click()

    def add_all_items_to_the_cart(self, ITEMS: dict):
        """ Adds all item from pre-setuped dict to the cart """
        keys_list = list(ITEMS.keys())
        for elem in keys_list:
            # fill flexible selector by the value
            value = ITEMS[elem]
            InventoryPageLocators.ITEM_BUTTON_UNIVERSAL[1] = f"{value[0]}"
            self.browser.find_element(*InventoryPageLocators.ITEM_BUTTON_UNIVERSAL).click()

    def get_cart_item_quantity(self):
        """ Returns zero or exact quantity of items"""
        if self.is_element_present(*InventoryPageLocators.CART_ITEM_QUANTITY):
            amount = self.browser.find_element(*InventoryPageLocators.CART_ITEM_QUANTITY).text
        else:
            amount = "Cart is empty"
        return amount

    def check_state_of_items_button(self, button_type: list):
        """ Return True if element present on page """
        InventoryPageLocators.ITEM_BUTTON_UNIVERSAL[1] = f"{button_type}"
        state = self.is_element_present(*InventoryPageLocators.ITEM_BUTTON_UNIVERSAL)
        return state

    def sort_inventory_page(self, sorting: str):
        """ Sorts items by given value. Acceptable values: 'A-Z'; 'Z-A'; 'L-H'; 'H-L' """
        if sorting == 'A-Z':
            self.browser.find_element(*InventoryPageLocators.A_Z_SORTING).click()
        elif sorting == 'Z-A':
            self.browser.find_element(*InventoryPageLocators.Z_A_SORTING).click()
        elif sorting == 'L-H':
            self.browser.find_element(*InventoryPageLocators.ASC_PRICE_SORTING).click()
        elif sorting == 'H-L':
            self.browser.find_element(*InventoryPageLocators.DESC_PRICE_SORTING).click()
        else:
            raise AttributeError

    def get_titles(self):
        """ Returns list filled titles of items """
        titles_raw = self.browser.find_elements(*InventoryPageLocators.TITLE_OF_ANY_ITEM)
        titles = []
        for elem in titles_raw:
            elem = elem.text
            titles.append(elem)
        return titles

    def get_prices(self):
        """ Returns list filled prices of items """
        prices_raw = self.browser.find_elements(*InventoryPageLocators.PRICE_OF_ANY_ITEM)
        prices = []
        for elem in prices_raw:
            elem = elem.text
            prices.append(float(elem.replace('$', '')))
        return prices
