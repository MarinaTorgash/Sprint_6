from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.questions_page_locator import QuestionsPageLocators

class QuestionsPage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = QuestionsPageLocators()

    def expand_question(self, index):
        button = self.driver.find_element(*self.locators.question_button(index))
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    def get_answer_text(self, index):
        answer_locator = self.locators.answer_text(index)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(answer_locator)
        )
        return self.driver.find_element(*answer_locator).text

    def is_answer_visible(self, index):
        try:
            return self.driver.find_element(*self.locators.answer_text(index)).is_displayed()
        except:
            return False