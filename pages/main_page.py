from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage:

    URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.page = BasePage(driver)

    def open(self):
        self.page.open(self.URL)

    # FAQ

    def click_faq_question(self, locator):
        self.page.scroll_to(locator)
        self.page.click(locator)

    def get_faq_answer(self, locator):
        return self.page.get_text(locator)

    # Кнопки заказа

    def click_header_order_button(self):
        self.page.click(
            MainPageLocators.HEADER_ORDER_BUTTON
        )

    def click_bottom_order_button(self):
        self.page.scroll_to(
            MainPageLocators.BOTTOM_ORDER_BUTTON
        )

        self.page.click(
            MainPageLocators.BOTTOM_ORDER_BUTTON
        )

    # Логотип Самоката

    def click_scooter_logo(self):
        self.page.click(
            MainPageLocators.SCOOTER_LOGO
        )

    # Логотип Яндекса

    def click_yandex_logo(self):
        self.page.click(
            MainPageLocators.YANDEX_LOGO
        )