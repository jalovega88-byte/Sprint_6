import allure
import pytest

from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий оформления заказа")
class TestOrder:
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, period, color, comment",
        ORDER_DATA,
        ids=["order_anna", "order_ivan"],
    )
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

        main_page.open()
        main_page.click_header_order_button()
        order_page.fill_name(name)
        order_page.fill_surname(surname)
        order_page.fill_address(address)
        order_page.select_metro(metro)
        order_page.fill_phone(phone)
        order_page.click_next()
        order_page.fill_date(date)
        order_page.select_rent_period(period)
        order_page.select_color(color)
        order_page.fill_comment(comment)
        order_page.click_order()
        order_page.confirm_order()

        assert "Заказ оформлен" in order_page.get_order_success_message()


@allure.story("Точки входа в оформление заказа")
class TestOrderButton:
    @allure.title("Нижняя кнопка «Заказать» открывает форму")
    def test_bottom_order_button_opens_order_form(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_bottom_order_button()

        assert order_page.is_name_input_displayed()
