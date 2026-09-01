import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти видимый элемент: {locator}")
    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Нажать на элемент: {locator}")
    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Прокрутить страницу к элементу: {locator}")
    def scroll_to(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Получить атрибут '{attribute}' элемента: {locator}")
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    @allure.step("Получить URL текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить дескриптор текущего окна")
    def get_current_window(self):
        return self.driver.current_window_handle

    @allure.step("Получить список открытых окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключиться на окно")
    def switch_to_window(self, window):
        self.driver.switch_to.window(window)

    @allure.step("Дождаться открытия нового окна")
    def wait_for_new_window(self, old_windows):
        return self.wait.until(
            lambda driver: len(driver.window_handles) > len(old_windows)
        )

    @allure.step("Дождаться URL, содержащего '{url_part}'")
    def wait_for_url_contains(self, url_part):
        return self.wait.until(
            EC.url_contains(url_part)
        )