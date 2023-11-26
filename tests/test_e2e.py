import pytest_check as check

from data.data import ITEMS_TITLES
from data.credentials import valid_usernames, password, cart_creds
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_case_five(browser):
    page = InventoryPage(browser, browser.current_url)

    page.do_login(valid_usernames[0], password)
    page.add_item_to_the_cart(["Backpack", "Fleese Jacket", "T-Shirt Red"])
    page.go_to_the_cart()
    page = CartPage(browser, browser.current_url)
    page.open_checkout_form()
    page.fill_checkout_form(*cart_creds)
    page.submit_checkout_form()
    payment_info = page.get_payment_info()
    # ==========Soft assert==========
    check.equal(payment_info, "SauceCard #31337", f"Payment info has unexpected value - "
                                                  f"{payment_info}")
    shipping_info = page.get_shipping_info()
    # ==========Soft assert==========
    check.equal(shipping_info, "Free Pony Express Delivery!",
                                f"Shipping info has unexpected value - {shipping_info}")
    flag, item_value = page.check_item_total_price()
    # ==========Soft assert==========
    check.is_true(flag, f" Item total price is incorrect: {item_value}")
    flag, tax_value = page.check_tax_amount()
    # ==========Soft assert==========
    check.is_true(flag, f" Item tax is incorrect: {tax_value} flag is {flag}")
    page.finish_checkout()
    success_text = page.return_success_message()
    assert success_text == "Thank you for your order!", \
                            f"Something went wrong or success message had been changed." \
                            f" Current text is: {success_text}"


def test_case_six(browser):
    page = InventoryPage(browser, browser.current_url)

    page.do_login(valid_usernames[0], password)
    page.add_item_to_the_cart(["Backpack", "Fleese Jacket", "T-Shirt Red"])
    page.go_to_the_cart()

    page = CartPage(browser, browser.current_url)

    page.open_checkout_form()
    page.submit_checkout_form()
    error_elems = page.get_list_of_highlighted_field()
    # ==========Soft assert==========
    check.equal(len(error_elems), 3, f"All 3 fields should be marked as error. "
                                     f"Current amount is {len(error_elems)}")
    button_text = page.get_error_text_from_button()
    assert button_text =="Error: First Name is required", \
                            f"No error text or error text had been changed." \
                            f"Current text value% {button_text}"


def test_case_seven(browser):
    page = InventoryPage(browser, browser.current_url)

    page.do_login(valid_usernames[0], password)
    page.add_all_items_to_the_cart(ITEMS_TITLES)
    page.go_to_the_cart()
    page = CartPage(browser, browser.current_url)
    items_amount = len(ITEMS_TITLES)
    items = page.count_items_in_the_cart()
    # ==========Soft assert==========
    check.equal(items, items_amount, f"Unexpected amount of items. Actual amount {items}")
    page.remove_all_items_from_the_cart(ITEMS_TITLES)
    flag = page.check_cart_is_empty()
    # ==========Soft assert==========
    check.is_true(flag, f"Cart is not empty. Flag value is {flag}")
    page.go_to_continue_shopping()
    page = InventoryPage(browser, browser.current_url)
    cart_items_value = page.get_cart_item_quantity()
    assert cart_items_value == "Cart is empty", f"Cart is not empty. " \
                                                f"Actual value is {cart_items_value}"


def test_case_eight(browser):
    page = InventoryPage(browser, browser.current_url)

    page.do_login(valid_usernames[0], password)
    page.add_all_items_to_the_cart(ITEMS_TITLES)
    page.go_to_the_cart()
    page = CartPage(browser, browser.current_url)
    page.remove_item_from_the_cart(["Backpack", "Fleese Jacket", "T-Shirt Red"])
    page.go_to_continue_shopping()
    page = InventoryPage(browser, browser.current_url)
    cart_items_value = page.get_cart_item_quantity()
    # ==========Soft assert==========
    check.equal(cart_items_value, "3", f"Unexpected amount of item in cart. "
                                       f"Current value is {cart_items_value}")

    # Checks that removed items from cart have 'Add to cart' button
    flag = page.check_state_of_items_button(ITEMS_TITLES["Backpack"][0])
    # ==========Soft assert==========
    check.is_true(flag, f"Expected 'Add to cart' button is present for Backpack")
    flag = page.check_state_of_items_button(ITEMS_TITLES["Fleese Jacket"][0])
    # ==========Soft assert==========
    check.is_true(flag, f"Expected 'Add to cart' button is present for Fleese Jacket")
    flag = page.check_state_of_items_button(ITEMS_TITLES["T-Shirt Red"][0])
    # ==========Soft assert==========
    check.is_true(flag, f"Expected 'Add to cart' button is present for T-Shirt Red")

    # Checks that added items to the cart have 'Remove' button
    flag = page.check_state_of_items_button(ITEMS_TITLES["Bike Light"][1])
    # ==========Soft assert==========
    check.is_true(flag, f"Expected 'Remove' button is present for Bike Light")
    flag = page.check_state_of_items_button(ITEMS_TITLES["Onesie"][1])
    # ==========Soft assert==========
    check.is_true(flag, f"Expected 'Remove' button is present for Onesie")
    flag = page.check_state_of_items_button(ITEMS_TITLES["Bolt T-Shirt"][1])
    # ==========Soft assert==========
    check.is_true(flag, f"Expected 'Remove' button is present for Bolt T-Shirt")


def test_links_at_footer(browser):
    page = InventoryPage(browser, browser.current_url)

    page.do_login(valid_usernames[0], password)
    flag = page.check_footer_social_links()
    assert flag == True, f"Links or HTML elements had been changed at inventory page"
    page.add_item_to_the_cart(["Onesie"])
    page.go_to_the_cart()

    page = CartPage(browser, browser.current_url)

    flag = page.check_footer_social_links()
    assert flag == True, f"Links or HTML elements had been changed at cart page"
    page.open_checkout_form()
    flag = page.check_footer_social_links()

    assert flag == True, f"Links or HTML elements had been changed at checkout form page"
    page.fill_checkout_form(*cart_creds)
    page.submit_checkout_form()
    flag = page.check_footer_social_links()

    assert flag == True, f"Links or HTML elements had been changed " \
                         f"at checkout form page after submition"
    page.finish_checkout()
    flag = page.check_footer_social_links()

    assert flag == True, f"Links or HTML elements had been changed " \
                         f"at checkout form page where success message"
