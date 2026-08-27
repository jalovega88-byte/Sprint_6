from selenium.webdriver.common.by import By


class MainPageLocators:

    # FAQ
    FAQ_QUESTION_0 = (
        By.ID,
        "accordion__heading-0"
    )

    FAQ_ANSWER_0 = (
        By.ID,
        "accordion__panel-0"
    )

    FAQ_QUESTION_1 = (
        By.ID,
        "accordion__heading-1"
    )

    FAQ_ANSWER_1 = (
        By.ID,
        "accordion__panel-1"
    )

    FAQ_QUESTION_2 = (
        By.ID,
        "accordion__heading-2"
    )

    FAQ_ANSWER_2 = (
        By.ID,
        "accordion__panel-2"
    )

    FAQ_QUESTION_3 = (
        By.ID,
        "accordion__heading-3"
    )

    FAQ_ANSWER_3 = (
        By.ID,
        "accordion__panel-3"
    )

    FAQ_QUESTION_4 = (
        By.ID,
        "accordion__heading-4"
    )

    FAQ_ANSWER_4 = (
        By.ID,
        "accordion__panel-4"
    )

    FAQ_QUESTION_5 = (
        By.ID,
        "accordion__heading-5"
    )

    FAQ_ANSWER_5 = (
        By.ID,
        "accordion__panel-5"
    )

    FAQ_QUESTION_6 = (
        By.ID,
        "accordion__heading-6"
    )

    FAQ_ANSWER_6 = (
        By.ID,
        "accordion__panel-6"
    )

    FAQ_QUESTION_7 = (
        By.ID,
        "accordion__heading-7"
    )

    FAQ_ANSWER_7 = (
        By.ID,
        "accordion__panel-7"
    )

    # Верхняя кнопка «Заказать»
    HEADER_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Заказать' and "
        "not(contains(@class, 'Button_Middle'))]"
    )

    # Нижняя кнопка «Заказать»
    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Заказать' and "
        "contains(@class, 'Button_Middle')]"
    )

    # Логотип Самоката
    SCOOTER_LOGO = (
        By.XPATH,
        "//a[contains(@class, 'Header_LogoScooter')]"
    )

    # Логотип Яндекса
    YANDEX_LOGO = (
        By.XPATH,
        "//a[contains(@class, 'Header_LogoYandex')]"
    )