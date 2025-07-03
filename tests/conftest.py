import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture
def fDriver():
    options = FirefoxOptions()
    options.add_argument("--headless")  # Уберите, если хотите видеть браузер
    fDriver = webdriver.Firefox(options=options)

    # Открыть окно на весь экран
    fDriver.maximize_window()  # 🔥 Здесь ключевая строка

    yield fDriver
    fDriver.quit()


@pytest.fixture
def important_questions():
    questions_data = [
        {
            "question_index": 0,
            "question_text": "Сколько это стоит? И как оплатить?",
            "expected_answer": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        },
        {
            "question_index": 1,
            "question_text": "Хочу сразу несколько самокатов! Так можно?",
            "expected_answer": "Пока что у нас так: один заказ — один самокат."
        },
        {
            "question_index": 2,
            "question_text": "Как рассчитывается время аренды?",
            "expected_answer": "Допустим, вы оформляете заказ на 8 мая..."
        },
        {
            "question_index": 3,
            "question_text": "Можно ли заказать самокат прямо на сегодня?",
            "expected_answer": "Только начиная с завтрашнего дня."
        },
        {
            "question_index": 4,
            "question_text": "Можно ли продлить заказ или вернуть самокат раньше?",
            "expected_answer": "Пока что нет! Но если что-то срочное..."
        },
        {
            "question_index": 5,
            "question_text": "Вы привозите зарядку вместе с самокатом?",
            "expected_answer": "Самокат приезжает к вам с полной зарядкой."
        },
        {
            "question_index": 6,
            "question_text": "Можно ли отменить заказ?",
            "expected_answer": "Да, пока самокат не привезли."
        },
        {
            "question_index": 7,
            "question_text": "Я живу за МКАДом, привезёте?",
            "expected_answer": "Да, обязательно."
        }
    ]
    return questions_data