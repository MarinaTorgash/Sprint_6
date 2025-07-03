import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.questions_page import QuestionsPage
from from urls import Urls



class TestQuestionsPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize("test_case", questions_data,
                             ids=[x["question_text"] for x in questions_data])
    def test_faq_question_expanding(self, test_case):

        faq_page = QuestionsPage(self.driver)
        self.driver.get(Urls.MAIN_PAGE)

        # Проверка начального состояния
        assert not faq_page.is_answer_visible(test_case["question_index"]), \
            f"Ответ изначально отображается для вопроса: {test_case['question_text']}"

        # Раскрытие вопроса
        faq_page.expand_question(test_case["question_index"])

        # Проверка отображения ответа
        assert faq_page.is_answer_visible(test_case["question_index"]), \
            f"Ответ не отобразился для вопроса: {test_case['question_text']}"

        # Проверка текста ответа
        answer_text = faq_page.get_answer_text(test_case["question_index"])
        assert test_case["expected_answer"] in answer_text, \
            f"Неверный текст ответа для вопроса: {test_case['question_text']}"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()