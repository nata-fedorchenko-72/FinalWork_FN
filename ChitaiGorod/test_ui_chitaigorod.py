import allure
import pytest
from ChitaiGorod.ui_chitaigorod import ChitaiGorodUI


@allure.title("Веб-сайт 'Читай город'")
@allure.description("UI проверки веб-сайта")
@allure.feature("")
@allure.severity("critical")

def test_chitai_gorod_title_size():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step(
        "Свернуть окно согласно заданным размерам"):
        main_page.resize_browser(100, 700)
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step("Проверить текст страницы"):
        assert main_page.get_page_text() == '«Читай-город» – интернет-магазин книг'
    with allure.step("Закрыть браузер"):
        main_page.close_browser()

def test_chitai_gorod_title_max():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step("Развернуть окно"):
        main_page.maximize_browser()
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step("Проверить текст страницы"):
        assert main_page.get_page_text() == '«Читай-город» – интернет-магазин книг'
    with allure.step("Закрыть браузер"):
        main_page.close_browser()

def test_shopping_items():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step("Развернуть окно"):
        main_page.maximize_browser()
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step(
        "Ввести текст в поле поиска, кликнуть кнопку Найти"):
        main_page.search_product("Педагогическая поэма")
    with allure.step("Кликнуть на кнопку Купить"):
        was = main_page.add_product()
    with allure.step("Кликнуть на кнопку Корзина"):
        main_page.click_basket()
        now = main_page.get_report()
    with allure.step(
        "Проверить,что количество кликов = количеству товаров в корзине"):
        assert was == now
    with allure.step("Закрыть браузер"):
        main_page.close_browser()

def test_empty_the_basket():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step("Развернуть окно"):
        main_page.maximize_browser()
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step("Ввести текст в поле поиска и кликнуть кнопку Найти"):
        main_page.search_product("Педагогическая поэма")
    with allure.step("Кликнуть на кнопку Купить"):
        main_page.add_product()
    with allure.step("Кликнуть на кнопку Корзина"):
        main_page.click_basket()
    with allure.step("Кликнуть на кнопку Очистить корзину"):
        main_page.empty_the_basket()
    with allure.step("Проверить текст"):
        assert()== "Корзина очищена"
    with allure.step("Закрыть браузер"):
        main_page.close_browser()

def test_auth():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step("Развернуть окно"):  
        main_page.maximize_browser()
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step("Кликнуть на кнопку авторизации"):
        main_page.button_auth()
        txt = main_page.get_field_name()
    with allure.step("Проверить текст"):
        assert(txt) == "Вход и регистрация"
    with allure.step("Закрыть браузер"):
        main_page.close_browser()

def test_chitai_gorod_logo():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step("Свернуть окно согласно заданным размерам"):
        main_page.resize_browser(100, 700)
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step("Закрыть всплывающее окно"):
        main_page.click_target_button()
    with allure.step("Проверить наличие логотипа"):
        assert main_page.logo() == True
    with allure.step("Закрыть браузер"):
        main_page.close_browser()
