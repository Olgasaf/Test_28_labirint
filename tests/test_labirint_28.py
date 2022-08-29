# python -m pytest -v --driver chrome --driver-path chromedriver.exe tests/test_labirint_28.py
import pytest
from config import TestData
from pages.locators import MainPage
import time
@pytest.mark.xfail
def test_loud_page(web_browser):
    page = MainPage(web_browser)
    page.wait_page_loaded()
    assert page.check_js_errors()

def test_main_page(web_browser):
    """ Проверка перехода на главную страницу """

    page = MainPage(web_browser)
    page.Locator_logo_img.click()
    assert page.get_current_url() == TestData.base_url

def test_go_menu_books(web_browser):
    """ Проверка перехода на страницу КНИГИ  """

    page = MainPage(web_browser)
    page.Locator_menu_bookc.click()
    assert page.get_current_url() == TestData.base_url_books

def test_go_menu_best(web_browser):
    """ Проверка перехода на страницу Главное """

    page = MainPage(web_browser)
    page.Locator_menu_best.click()
    assert page.get_current_url() == TestData.base_url_best

def test_go_menu_school(web_browser):
    """ Проверка перехода на страницу ШКОЛА """

    page = MainPage(web_browser)
    page.Locator_menu_school.click()
    assert page.get_current_url() == TestData.base_url_school

def test_go_menu_games(web_browser):
    """ Проверка перехода на страницу ШКОЛА """

    page = MainPage(web_browser)
    page.Locator_menu_games.click()
    assert page.get_current_url() == TestData.base_url_games

def test_go_menu_office(web_browser):
    """ Проверка перехода на страницу КАНЦТОВАРЫ """

    page = MainPage(web_browser)
    page.Locator_menu_office.click()
    assert page.get_current_url() == TestData.base_url_office

def test_go_menu_multimedia(web_browser):
    """ Проверка перехода на страницу CD """

    page = MainPage(web_browser)
    page.Locator_menu_multimedia.click()
    assert page.get_current_url() == TestData.base_url_multimedia

def test_go_menu_contact(web_browser):
    """ Проверка перехода на страницу КОНТАКТЫ """

    page = MainPage(web_browser)
    page.Locator_menu_contact.click()
    assert page.get_current_url() == TestData.base_url_contact



def test_check_main_search(web_browser):
    """ Убедитесь, что основной поиск работает нормально. """

    page = MainPage(web_browser)

    page.Locator_search = 'Азбука загадок'
    page.Locator_search_btn.click()

    # Убедитесь, что пользователь может видеть список продуктов:
    assert page.products_titles.count() == 159

    # Убедитесь, что пользователь нашел соответствующие продукты
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'Азбука загадок' in title.lower(), msg

def test_check_wrong_input_in_search(web_browser):
        """ Убедитесь, что ввод с неправильной раскладкой клавиатуры работает нормально. """
        page = MainPage(web_browser)

        page.Locator_search = 'fp,erf pfufljr'
        page.search_run_button.click()

        # Verify that user can see the list of products:
        assert page.products_titles.count() == 159

        # Make sure user found the relevant products
        for title in page.products_titles.get_text():
            msg = 'Wrong product in search "{}"'.format(title)
            assert 'Азбука загадок' in title.lower(), msg

@pytest.mark.xfail(reason="Filter by price doesn't work")
def test_check_sort_by_price(web_browser):
    """ Убедитесь что сортировка по цене работает нормально"""

    page = MainPage(web_browser)

    page.Locator_search = 'Дарья Донцова'
    page.Locator_search_btn.click()

    # Прокрутить элемент
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Получить цену на товар в результатах поиска
    all_prices = page.products_prices.get_text()

    #Преобразовать все цены из строк в цифры
    all_prices = [float(p.replace(' ', '')) for p in all_prices]

    print(all_prices)
    print(sorted(all_prices))

    # Убедитесь, что товары правильно отсортированы по цене:
    assert all_prices == sorted(all_prices), "Сортировка по цене работает"

def test_scroll_page(web_browser):
    """ Проверка прокрутки страницы """
    page = MainPage(web_browser)
    page.Locator_search.send_keys(TestData.title_search_books)
    page.Locator_search_btn.click()
    page.Locator_book_Donzova.scroll_to_element()
    assert page.Locator_book_Donzova.is_clickable()
    page.Locator_book_Donzova.highlight_and_make_screenshot('scrolling.png')

def test_visible(web_browser):
    """ Ссылка на доставку и оплату видна на экране """
    page = MainPage(web_browser)
    assert page.Locator_icon.is_visible()

def test_sale_visible(web_browser):
    """ Ссылка на скидки видна на экране """
    page = MainPage(web_browser)
    assert page.Locator_sale.is_visible()


def test_and_basket(web_browser):
    """ Проверка добавления книги в корзину """
    page = MainPage(web_browser)
    page.Locator_search.send_keys(TestData.title_search_books_Acunin)
    page.Locator_search_btn.click()
    page.Locator_books_Acunin.click()
    page.Locator_add_basket.click()
    page.Locator_basket.click()

    # проверим что локатор книги виден в корзине
    assert page.Locator_books_Acunin.is_visible()
    # проверим счетчик корзины
    assert page.Locator_count_basket.get_text() == '1 товар'

def test_clear_basket(web_browser):
    """ Проверка удаления товара из корзины """
    page = MainPage(web_browser)
    page.Locator_search.send_keys(TestData.title_search_books_Acunin)
    page.Locator_search_btn.click()
    page.Locator_books_Acunin.click()
    page.Locator_add_basket.click()
    page.Locator_basket.click()
    page.Locator_clear_basket.click()

    assert page.Locator_basket_0.get_text() == 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?'

def test_recover_basket(web_browser):
    """ Проверка восстановления удаленного товара """
    page = MainPage(web_browser)
    page.Locator_search.send_keys(TestData.title_search_books_Acunin)
    page.Locator_search_btn.click()
    page.Locator_books_Acunin.click()
    page.Locator_add_basket.click()
    page.Locator_basket.click()
    page.Locator_clear_basket.click()
    page.Locator_recover.click()

    assert page.Locator_count_basket.get_text() == '1 товар'

