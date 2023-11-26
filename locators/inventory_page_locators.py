from selenium.webdriver.common.by import By


class InventoryPageLocators:
    ITEM_BUTTON_UNIVERSAL = [By.ID, '']
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM_QUANTITY = (By.CLASS_NAME, "shopping_cart_badge")
    TITLE_OF_ANY_ITEM = (By.CLASS_NAME, "inventory_item_name")
    PRICE_OF_ANY_ITEM = (By.CLASS_NAME, "inventory_item_price")
    A_Z_SORTING = (By.XPATH, "//option[@value='az']")
    Z_A_SORTING = (By.XPATH, "//option[@value='za']")
    ASC_PRICE_SORTING = (By.XPATH, "//option[@value='lohi']")
    DESC_PRICE_SORTING = (By.XPATH, "//option[@value='hilo']")

