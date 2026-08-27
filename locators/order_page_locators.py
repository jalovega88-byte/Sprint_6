from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Первая часть формы

    NAME_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Имя']"
    )

    SURNAME_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Фамилия']"
    )

    ADDRESS_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Адрес: куда привезти заказ']"
    )

    METRO_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Станция метро']"
    )

    PHONE_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[text()='Далее']"
    )

    # Вторая часть формы

    DATE_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Когда привезти самокат']"
    )

    RENT_PERIOD = (
        By.CSS_SELECTOR,
        ".Dropdown-placeholder"
    )

    RENT_PERIOD_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-option') "
        "and text()='{period}']"
    )

    BLACK_COLOR_CHECKBOX = (
        By.ID,
        "black"
    )

    GREY_COLOR_CHECKBOX = (
        By.ID,
        "grey"
    )

    COMMENT_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]"
        "//button[text()='Заказать']"
    )

    CONFIRM_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Да']"
    )

    ORDER_SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".Order_ModalHeader__3FDaJ"
    )

    BACK_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]"
        "//button[text()='Назад']"
    )