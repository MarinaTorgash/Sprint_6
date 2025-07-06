import pytest
from pages.questions_page import MainPage
from data import QUESTIONS_DATA
import allure

class TestQuestionsPage:

    @allure.description('При нажатии на стрелочку открывается соответствующий текст')
    @pytest.mark.parametrize('index, expected_text', QUESTIONS_DATA)
    def test_accordion_item(self, driver, index, expected_text):

        allure.dynamic.title(f'Проверка вопроса №{index + 1} в разделе «Вопросы о важном»')
        page = MainPage(driver)
        page.accept_cookies()
        #page.scroll_to_accordion()

        item = page.get_accordion_item(index)
        item.scroll_to_accordion()
        item.click_header()

        actual_text = item.get_panel_text()
        assert actual_text == expected_text, (
            f"Неверный текст в элементе {index}:\n"
            f"Ожидалось: '{expected_text}'\n"
            f"Получено: '{actual_text}'"
        )
