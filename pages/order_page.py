import allure

from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнить имя")
    def fill_name(self, name):
        self.find_element(OrderPageLocators.NAME_INPUT).send_keys(name)

    @allure.step("Заполнить фамилию")
    def fill_surname(self, surname):
        self.find_element(OrderPageLocators.SURNAME_INPUT).send_keys(surname)

    @allure.step("Заполнить адрес")
    def fill_address(self, address):
        self.find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step("Выбрать станцию метро: {station}")
    def select_metro(self, station):
        metro_input = self.find_element(OrderPageLocators.METRO_INPUT)
        metro_input.click()
        metro_input.send_keys(station)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

    @allure.step("Заполнить номер телефона")
    def fill_phone(self, phone):
        self.find_element(OrderPageLocators.PHONE_INPUT).send_keys(phone)

    @allure.step("Перейти ко второй части формы")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать дату доставки: {date}")
    def fill_date(self, date):
        date_input = self.find_element(OrderPageLocators.DATE_INPUT)
        date_input.click()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды: {period}")
    def select_rent_period(self, period):
        self.click(OrderPageLocators.RENT_PERIOD)
        locator = (
            OrderPageLocators.RENT_PERIOD_OPTION[0],
            OrderPageLocators.RENT_PERIOD_OPTION[1].format(period=period),
        )
        self.click(locator)

    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color):
        colors = {
            "black": OrderPageLocators.BLACK_COLOR_CHECKBOX,
            "grey": OrderPageLocators.GREY_COLOR_CHECKBOX,
        }
        if color not in colors:
            raise ValueError(f"Неизвестный цвет: {color}")
        self.click(colors[color])

    @allure.step("Заполнить комментарий")
    def fill_comment(self, comment):
        self.find_element(OrderPageLocators.COMMENT_INPUT).send_keys(comment)

    @allure.step("Нажать кнопку «Заказать»")
    def click_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Получить сообщение об успешном заказе")
    def get_order_success_message(self):
        return self.get_text(OrderPageLocators.ORDER_SUCCESS_MESSAGE)

    @allure.step("Проверить отображение формы заказа")
    def is_name_input_displayed(self):
        return self.find_element(OrderPageLocators.NAME_INPUT).is_displayed()
