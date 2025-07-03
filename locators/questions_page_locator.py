from selenium.webdriver.common.by import By


class QuestionsPageLocators:

    FAQ_SECTION = (By.XPATH, "//div[@class='accordion']")
    QUESTION_ITEMS = (By.CSS_SELECTOR, "div.accordion__item")

    @staticmethod
    def question_button(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def answer_text(index):
        return (By.ID, f"accordion__panel-{index}")
