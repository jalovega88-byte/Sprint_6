import allure
import pytest

from data import FAQ_DATA
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


FAQ_LOCATORS = [
    (
        getattr(MainPageLocators, question),
        getattr(MainPageLocators, answer),
        expected_answer,
    )
    for question, answer, expected_answer in FAQ_DATA
]


@allure.feature("Главная страница")
@allure.story("Вопросы о важном")
class TestFAQ:
    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_answer",
        FAQ_LOCATORS,
        ids=[item[0] for item in FAQ_DATA],
    )
    @allure.title("Проверка ответа на вопрос")
    def test_faq_question_opens_answer(
        self,
        driver,
        question_locator,
        answer_locator,
        expected_answer,
    ):
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_faq_question(question_locator)
        answer = main_page.get_faq_answer(answer_locator)

        assert answer == expected_answer
