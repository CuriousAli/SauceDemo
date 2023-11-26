import pytest_check as check

from data.credentials import valid_usernames, password
from pages.inventory_page import InventoryPage


def test_item_sorting(browser):
    page = InventoryPage(browser, browser.current_url)

    page.do_login(valid_usernames[0], password)
    titles = page.get_titles()
    prices = page.get_prices()
    titles = sorted(titles)
    prices = sorted(prices)
    page.sort_inventory_page("A-Z")
    sorted_titles = page.get_titles()
    # ==========Soft assert==========
    check.equal(sorted_titles, titles, f"A-Z sorting doesn't work. Current state {sorted_titles}")
    page.sort_inventory_page("Z-A")
    sorted_titles = page.get_titles()
    # ==========Soft assert==========
    check.equal(sorted_titles, titles[::-1], f"Z-A sorting doesn't work. "
                                             f"Current state {sorted_titles}")
    page.sort_inventory_page("L-H")
    sorted_prices = page.get_prices()
    # ==========Soft assert==========
    check.equal(sorted_prices, prices, f"Low-High sorting doesn't work. "
                                       f"Current state {sorted_prices}")
    page.sort_inventory_page("H-L")
    sorted_prices = page.get_prices()
    # ==========Soft assert==========
    check.equal(sorted_prices, prices[::-1], f"High-Low sorting doesn't work. "
                                             f"Current state {sorted_prices}")