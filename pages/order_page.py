from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage:

    def __init__(self, driver):
        self.page = BasePage(driver)

    # =========================
    # Первая часть формы
    # =========================

    def fill_name(self, name):
        self.page.find_element(
            OrderPageLocators.NAME_INPUT
        ).send_keys(name)

    def fill_surname(self, surname):
        self.page.find_element(
            OrderPageLocators.SURNAME_INPUT
        ).send_keys(surname)

    def fill_address(self, address):
        self.page.find_element(
            OrderPageLocators.ADDRESS_INPUT
        ).send_keys(address)

    def select_metro(self, station):
        metro_input = self.page.find_element(
            OrderPageLocators.METRO_INPUT
        )

        metro_input.click()
        metro_input.send_keys(station)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

    def fill_phone(self, phone):
        self.page.find_element(
            OrderPageLocators.PHONE_INPUT
        ).send_keys(phone)

    def click_next(self):
        self.page.click(
            OrderPageLocators.NEXT_BUTTON
        )

    # =========================
    # Вторая часть формы
    # =========================

    def fill_date(self, date):
        date_input = self.page.find_element(
            OrderPageLocators.DATE_INPUT
        )

        date_input.click()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    def select_rent_period(self, period):
        self.page.click(
            OrderPageLocators.RENT_PERIOD
        )

        locator = (
            OrderPageLocators.RENT_PERIOD_OPTION[0],
            OrderPageLocators.RENT_PERIOD_OPTION[1].format(
                period=period
            )
        )

        self.page.click(locator)

    def select_color(self, color):

        if color == "black":
            self.page.click(
                OrderPageLocators.BLACK_COLOR_CHECKBOX
            )

        elif color == "grey":
            self.page.click(
                OrderPageLocators.GREY_COLOR_CHECKBOX
            )

        else:
            raise ValueError(
                f"Неизвестный цвет: {color}"
            )

    def fill_comment(self, comment):
        self.page.find_element(
            OrderPageLocators.COMMENT_INPUT
        ).send_keys(comment)

    # =========================
    # Оформление заказа
    # =========================

    def click_order(self):
        self.page.click(
            OrderPageLocators.ORDER_BUTTON
        )

    def confirm_order(self):
        self.page.click(
            OrderPageLocators.CONFIRM_ORDER_BUTTON
        )

    def get_order_success_message(self):
        return self.page.get_text(
            OrderPageLocators.ORDER_SUCCESS_MESSAGE
        )