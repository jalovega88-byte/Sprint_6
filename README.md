Sprint 6 — автотесты сервиса «Яндекс Самокат»

Проект содержит UI-автотесты сервиса «Яндекс Самокат» на Python, Pytest, Selenium и Allure.

Что проверяется
ответы на вопросы в разделе FAQ;
оформление заказа по двум наборам тестовых данных;
открытие формы заказа по нижней кнопке «Заказать»;
возврат на главную страницу по логотипу Самоката;
открытие Дзена по логотипу Яндекса в новом окне.
Структура проекта
Sprint_6/
├── allure-report/          # готовый Allure-отчёт
├── locators/               # локаторы элементов страницы
├── pages/                  # Page Object
│   ├── __init__.py
│   ├── base_page.py        # базовые действия Selenium
│   ├── main_page.py        # главная страница
│   └── order_page.py       # страница заказа
├── tests/                  # автотесты
│   ├── __init__.py
│   ├── test_faq.py         # тесты FAQ
│   ├── test_navigation.py  # тесты навигации
│   └── test_order.py       # тесты оформления заказа
├── conftest.py             # фикстуры Pytest
├── data.py                 # тестовые данные
├── urls.py                 # URL и части URL
├── pytest.ini              # настройки Pytest
├── requirements.txt        # зависимости проекта
├── README.md
└── .gitignore
Технологии
Python
Pytest
Selenium WebDriver
Allure
Page Object Model
Установка

Клонировать репозиторий и перейти в директорию проекта:

git clone <URL_репозитория>
cd Sprint_6

Создать виртуальное окружение:

python -m venv venv

Активировать виртуальное окружение.

Windows PowerShell
venv\Scripts\Activate.ps1

Установить зависимости:

pip install -r requirements.txt

Для запуска тестов необходим установленный браузер Firefox и совместимый geckodriver.

Запуск тестов

Запустить все автотесты:

pytest

Запустить тесты с подробным выводом:

pytest -v
Allure

Для формирования результатов Allure:

pytest --alluredir=allure-results

Для просмотра отчёта локально:

allure serve allure-results

Готовый HTML-отчёт находится в директории:

allure-report/

Директория allure-report/ добавляется в репозиторий, чтобы готовый отчёт был доступен в GitHub.

Временные результаты тестов из allure-results/ в репозиторий не добавляются.

Архитектура

В проекте используется паттерн Page Object Model.

Page Object-классы наследуются от BasePage. Базовые действия с Selenium WebDriver инкапсулированы в BasePage, поэтому тесты не работают с driver напрямую.

URL вынесены в:

urls.py

Тестовые данные находятся в:

data.py

Фикстуры Pytest находятся в:

conftest.py

Публичные действия Page Object и базовые действия BasePage отмечены декоратором @allure.step, поэтому сценарии отображаются в Allure в виде последовательности шагов.

.gitignore

В репозиторий не добавляются:

виртуальное окружение venv/;
Python-кэш __pycache__/;
файлы .pyc;
.pytest_cache/;
временные результаты Allure allure-results/;
настройки IDE.

Готовый отчёт allure-report/, напротив, хранится в репозитории.