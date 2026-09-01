import allure

from pages.main_page import MainPage
from urls import DZEN_URL_PART, MAIN_PAGE_URL


@allure.feature("Навигация")
class TestNavigation:
    @allure.story("Навигация по сайту")
    @allure.title("Логотип Самоката возвращает на главную страницу")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_header_order_button()
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == MAIN_PAGE_URL

    @allure.story("Навигация по внешней ссылке")
    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)

        main_page.open()

        original_window = main_page.get_current_window()
        original_windows = main_page.get_window_handles()

        main_page.click_yandex_logo()
        main_page.wait_for_new_window(original_windows)

        new_window = next(
            window
            for window in main_page.get_window_handles()
            if window != original_window
        )
        main_page.switch_to_window(new_window)
        main_page.wait_for_url_contains(DZEN_URL_PART)

        assert DZEN_URL_PART in main_page.get_current_url()
