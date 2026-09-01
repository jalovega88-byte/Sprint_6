import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import MAIN_PAGE_URL


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open(self):
        super().open(MAIN_PAGE_URL)

    @allure.step("Открыть ответ FAQ")
    def click_faq_question(self, locator):
        self.scroll_to(locator)
        self.click(locator)

    @allure.step("Получить ответ FAQ")
    def get_faq_answer(self, locator):
        return self.get_text(locator)

    @allure.step("Нажать верхнюю кнопку «Заказать»")
    def click_header_order_button(self):
        self.click(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Нажать нижнюю кнопку «Заказать»")
    def click_bottom_order_button(self):
        self.scroll_to(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
