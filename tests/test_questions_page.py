import pytest
from selenium import webdriver
from pages.questions_page import MainPage
from urls import Urls
from data import QUESTIONS_DATA
import allure

class TestQuestionsPage:
    driver = None

    @classmethod
    def setup_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver = webdriver.Firefox()

    @allure.description('При нажатии на стрелочку открывается соответствующий текст')
    @pytest.mark.parametrize('index, expected_text', QUESTIONS_DATA)
    def test_accordion_item(self, index, expected_text):
        allure.dynamic.title(f'Проверка вопроса №{index+1} в разделе «Вопросы о важном»')

        with allure.step(f'1. Открываем страницу {Urls.MAIN_PAGE}'):
            page = MainPage(self.driver, Urls.MAIN_PAGE)
            page.open()

        with allure.step('2. Принимаем куки'):
            page.accept_cookies()

        with allure.step(f'3. Тестируем вопрос №{index+1}'):
            page.scroll_to_accordion()

            items = page.get_accordion_items()
            assert index < len(items), f"Недостаточно вопросов. Всего: {len(items)}"

            item = items[index]
            item.click_header()

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
        with allure.step('Закрываем браузер'):
            cls.driver.quit()