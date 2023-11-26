import allure
import time

import pytest_check as check

import pytest

from data.credentials import valid_usernames, invalid_usernames, password
from pages.login_page import LoginPage


@pytest.mark.parametrize('username', valid_usernames)
def test_login(browser, username):
    """ Testing login to saucedemo.com with valid users """
    page = LoginPage(browser, browser.current_url)

    start = time.time()
    page.do_login(username, password)
    page.should_be_logout_button()
    end = time.time()
    info = page.check_login_duration(start, end, username)
    # ==========Soft assert==========
    check.is_true(info[0], f"Login operation too long for user {info[2]} and takes {info[1]}")

    flag = page.check_pictures(username)
    assert flag == True, f"One or more pictures are incorrect. Username is {username} "


@pytest.mark.parametrize('locked_username', invalid_usernames)
def test_locked_user_login(browser, locked_username):
    """ Testing login to saucedemo.com with invalid users """
    page = LoginPage(browser, browser.current_url)

    page.do_login(locked_username, password)
    error = page.get_error_text()
    assert error == "Epic sadface: Sorry, this user has been locked out.", \
                    f"Unexpected error text. Current error message: {error}"
