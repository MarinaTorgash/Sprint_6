import pytest
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from pages.questions_page import MainPage
from urls import Urls
from data import QUESTIONS_DATA

class TestQuestionsPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('index, expected_text', QUESTIONS_DATA)
    def test_accordion_item(self, index, expected_text):
        page = MainPage(self.driver, Urls.MAIN_PAGE)

        page.open()
        page.accept_cookies()
        page.scroll_to_accordion()
        #page.close_all_accordion_items()

        items = page.get_accordion_items()
        assert index < len(items), f"Недостаточно вопросов. Всего: {len(items)}"

        item = items[index]

        initial_state = item.is_panel_open()

        # Кликаем на вопрос
        item.click_header()

        # Проверяем текст, если панель открылась
        if item.is_panel_open():
            actual_text = item.get_panel_text()
            assert actual_text == expected_text, (
                f"Неверный текст в элементе {index}:\n"
                f"Ожидалось: '{expected_text}'\n"
                f"Получено: '{actual_text}'"
            )
        else:
            pytest.fail(f"Панель не открылась после клика на элемент {index}")


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()