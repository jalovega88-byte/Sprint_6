import allure
import pytest

from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators


@allure.feature("Заказ самоката")
class TestOrder:

    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, period, color, comment",
        [
            (
                "Анна",
                "Иванова",
                "Москва, улица Тестовая, 1",
                "Черкизовская",
                "89991234567",
                "30.08.2026",
                "двое суток",
                "black",
                "Позвонить перед доставкой",
            ),
            (
                "Иван",
                "Петров",
                "Москва, улица Тестовая, 10",
                "Сокольники",
                "89991234568",
                "31.08.2026",
                "трое суток",
                "grey",
                "Позвонить за час",
            ),
        ],
        ids=[
            "order_anna",
            "order_ivan",
        ]
    )
    @allure.story("Позитивный сценарий оформления заказа")
    @allure.title("Успешное оформление заказа")
    def test_create_order(
        self,
        driver,
        name,
        surname,
        address,
        metro,
        phone,
        date,
        period,
        color,
        comment,
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Нажать верхнюю кнопку «Заказать»"):
            main_page.click_header_order_button()

        with allure.step("Заполнить имя"):
            order_page.fill_name(name)

        with allure.step("Заполнить фамилию"):
            order_page.fill_surname(surname)

        with allure.step("Заполнить адрес"):
            order_page.fill_address(address)

        with allure.step("Выбрать станцию метро"):
            order_page.select_metro(metro)

        with allure.step("Заполнить номер телефона"):
            order_page.fill_phone(phone)

        with allure.step("Перейти ко второй части формы"):
            order_page.click_next()

        with allure.step("Выбрать дату доставки"):
            order_page.fill_date(date)

        with allure.step("Выбрать срок аренды"):
            order_page.select_rent_period(period)

        with allure.step("Выбрать цвет самоката"):
            order_page.select_color(color)

        with allure.step("Заполнить комментарий"):
            order_page.fill_comment(comment)

        with allure.step("Нажать кнопку «Заказать»"):
            order_page.click_order()

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить успешное оформление"):
            success_message = (
                order_page.get_order_success_message()
            )

            assert "Заказ оформлен" in success_message

    @allure.story("Точки входа в оформление заказа")
    @allure.title("Нижняя кнопка «Заказать» открывает форму")
    def test_bottom_order_button_opens_order_form(
        self,
        driver
    ):
        main_page = MainPage(driver)

        main_page.open()

        main_page.click_bottom_order_button()

        order_page = OrderPage(driver)

        name_input = order_page.page.find_element(
            OrderPageLocators.NAME_INPUT
        )

        assert name_input.is_displayed()

    @allure.story("Навигация")
    @allure.title("Логотип Самоката возвращает на главную страницу")
    def test_scooter_logo_redirects_to_main_page(
        self,
        driver
    ):
        main_page = MainPage(driver)

        main_page.open()

        main_page.click_header_order_button()

        main_page.click_scooter_logo()

        assert driver.current_url == main_page.URL

    @allure.story("Навигация")
    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_redirects_to_dzen(
        self,
        driver
    ):
        main_page = MainPage(driver)

        main_page.open()

        original_window = driver.current_window_handle
        original_windows = driver.window_handles

        main_page.click_yandex_logo()

        WebDriverWait(driver, 10).until(
            lambda current_driver:
            len(current_driver.window_handles)
            > len(original_windows)
        )

        new_window = next(
            window
            for window in driver.window_handles
            if window != original_window
        )

        driver.switch_to.window(new_window)

        WebDriverWait(driver, 15).until(
            lambda current_driver:
            "dzen.ru" in current_driver.current_url
        )

        assert "dzen.ru" in driver.current_url