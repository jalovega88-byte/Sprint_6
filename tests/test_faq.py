import allure
import pytest

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.feature("Главная страница")
@allure.story("Вопросы о важном")
class TestFAQ:

    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_answer",
        [
            (
                MainPageLocators.FAQ_QUESTION_0,
                MainPageLocators.FAQ_ANSWER_0,
                "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
            ),
            (
                MainPageLocators.FAQ_QUESTION_1,
                MainPageLocators.FAQ_ANSWER_1,
                "Пока что у нас так: один заказ — один самокат. "
                "Если хотите покататься с друзьями, можете просто "
                "сделать несколько заказов — один за другим.",
            ),
            (
                MainPageLocators.FAQ_QUESTION_2,
                MainPageLocators.FAQ_ANSWER_2,
                "Допустим, вы оформляете заказ на 8 мая. "
                "Мы привозим самокат 8 мая в течение дня. "
                "Отсчёт времени аренды начинается с момента, "
                "когда вы оплатите заказ курьеру. "
                "Если мы привезли самокат 8 мая в 20:30, "
                "суточная аренда закончится 9 мая в 20:30.",
            ),
            (
                MainPageLocators.FAQ_QUESTION_3,
                MainPageLocators.FAQ_ANSWER_3,
                "Только начиная с завтрашнего дня. "
                "Но скоро станем расторопнее.",
            ),
            (
                MainPageLocators.FAQ_QUESTION_4,
                MainPageLocators.FAQ_ANSWER_4,
                "Пока что нет! Но если что-то срочное — "
                "всегда можно позвонить в поддержку "
                "по красивому номеру 1010.",
            ),
            (
                MainPageLocators.FAQ_QUESTION_5,
                MainPageLocators.FAQ_ANSWER_5,
                "Самокат приезжает к вам с полной зарядкой. "
                "Этого хватает на восемь суток — даже если "
                "будете кататься без передышек и во сне. "
                "Зарядка не понадобится.",
            ),
            (
                MainPageLocators.FAQ_QUESTION_6,
                MainPageLocators.FAQ_ANSWER_6,
                "Да, пока самокат не привезли. Штрафа не будет, "
                "объяснительной записки тоже не попросим. "
                "Все же свои.",
            ),
            (
                MainPageLocators.FAQ_QUESTION_7,
                MainPageLocators.FAQ_ANSWER_7,
                "Да, обязательно. Всем самокатов! "
                "И Москве, и Московской области.",
            ),
        ],
        ids=[
            "question_0",
            "question_1",
            "question_2",
            "question_3",
            "question_4",
            "question_5",
            "question_6",
            "question_7",
        ]
    )
    @allure.title("Проверка ответа на вопрос №{question_locator}")
    def test_faq_question_opens_answer(
        self,
        driver,
        question_locator,
        answer_locator,
        expected_answer,
    ):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Открыть вопрос"):
            main_page.click_faq_question(
                question_locator
            )

        with allure.step("Получить текст ответа"):
            answer = main_page.get_faq_answer(
                answer_locator
            )

        with allure.step("Проверить текст ответа"):
            assert answer == expected_answer