# python -m pytest -v --driver chrome --driver-path chromedriver.exe tests/test_1.py
import pytest

import config
from config import TestData
from pages.locators import MainPage
import time

def test_main_auth_page(web_browser):
    """ Проверка вход и регистрация по телефону"""

    page = MainPage(web_browser)
    page.Locator_auth.click()
    page.input_phone = config.TestData.phone_number
    page.locator_enter_btn.click()
    assert page.Locator_text.get_text() == 'Введите 4 цифры кода подтверждения'

def test_main_auth_page_e_mail(web_browser):
    """ Проверка вход и регистрация по электронной почте"""

    page = MainPage(web_browser)
    page.Locator_auth.click()
    page.input_phone = config.TestData.email
    page.locator_enter_btn.click()
    assert page.Locator_text.get_text() == 'Вы зарегистрированы'

def test_main_auth_negative(web_browser):
    """ Проверка вход и регистрация при вводе нправильных данных"""

    page = MainPage(web_browser)
    page.Locator_auth.click()
    page.input_phone = config.TestData.negative
    page.locator_enter_btn.click()
    assert page.Locator_negative.get_text() == 'Введенного кода не существует'





