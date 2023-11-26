import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

from data.data import BASE_URL


@pytest.fixture(scope="function")
def browser():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1920, 1080)
    browser.get(BASE_URL)
    yield browser
    browser.quit()
