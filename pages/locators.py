import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    Locator_logo_img = WebElement(css_selector='span.b-header-b-logo-e-logo')

    #Локатор Вход и регистрация
    Locator_auth = WebElement(css_selector='a.top-link-main_cabinet')
    input_phone = WebElement(css_selector='input[placeholder="Введите свой код скидки, телефон или эл.почту"]')

    locator_enter_btn = WebElement(id='g-recap-0-btn')
    Locator_text =WebElement(id="_inputnamepin_95")
    Locator_negative = WebElement(xpath='//*@class="full-input__msg-small js-msg-small"]')

    # Локатор кнопки поиск
    Locator_search = WebElement(id='search-field')
    Locator_search_btn = WebElement(class_name='b-header-b-search-e-btn')

    Locator_book_Donzova = WebElement(
        xpath='//img[@src="https://img4.labirint.ru/rc/e468b504011fc8763e28b3b56862c1a5/363x561q80/books60/596096/cover.jpg?1564030775"]')
    Locator_icon = WebElement(css_selector='li[data-event-label]>a[href="/help/"]')

    Locator_menu_bookc = WebElement(css_selector='span>a[href="/books/"]')
    Locator_menu_best = WebElement(css_selector='span>a[href="/best/"]')
    Locator_menu_school = WebElement(css_selector='span>a[href="/school/"]')
    Locator_menu_games = WebElement(css_selector='span>a[href="/games/"]')
    Locator_menu_office = WebElement(css_selector='span>a[href="/office/"]')
    Locator_menu_text_multimedia = WebElement(css_selector='span>a[href="/office/"]')
    Locator_menu_multimedia = WebElement(xpath='//*[@href="multimedia"]')
    Locator_menu_contact = WebElement(css_selector='li[data-event-content="Контакты"]>a[href="/contact/"]')
    Locator_abc = WebElement(xpath='//*[@class="b-stab-e-slider-item-e-txt-m-small js-search-tab-count"]')
    # ссылка скидки
    Locator_sale = WebElement(xpath='//a[@href="/sale/"]')

    # локаторы для тестов корзины
    Locator_add_basket = WebElement(xpath='//a[@class="btn btn-small btn-primary btn-buy"]')
    Locator_basket = WebElement(css_selector='.b-header-b-personal-e-list-item.have-dropdown.last-child')
    Locator_decoration = WebElement(xpath='//a[@class="btn btn-small btn-more tobasket"]')  # оформить заказ
    Locator_count_basket = WebElement(xpath=('//*[@id="basket-default-prod-count2"]'))  # счетчик корзины
    Locator_clear_basket = WebElement(xpath='//a[@class="b-link-popup"]')

    # локатор пустой корзины
    Locator_basket_0 = WebElement(xpath='//span[@class="g-alttext-small g-alttext-grey g-alttext-head" and '
                                          'contains (text(), "Ваша корзина пуста. Почему?")]')
    # локатор ссылки востановления удаленного товара
    Locator_recover = WebElement(css_selector='.b-link-popup.g-alttext-deepblue')

    Locator_link_postponed = WebElement(class_name='fave')  # в отложеное
    Locator_menu_postponed = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-putorder.basket-in-dreambox-a')  # https://www.labirint.ru/cart/

    # локатор книги
    Locator_books_Acunin = WebElement(
        xpath='//img[@src="https://img3.labirint.ru/rc/bde7b73106e94b27ba9744a18c879942/363x561q80/books83/829889/cover.jpg?1635308706"]')

    locator_clear_basket = WebElement(xpath='//a[@class="b-link-popup"]')
    locator_recover = WebElement(css_selector='.b-link-popup.g-alttext-deepblue')

