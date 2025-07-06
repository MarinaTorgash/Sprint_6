from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_ITEMS = (By.CSS_SELECTOR, "div.accordion__item")

    @staticmethod
    def question_button(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def answer_text(index):
        return (By.ID, f"accordion__panel-{index}")

    ACCORDION_ITEM = (By.CSS_SELECTOR, '[data-accordion-component="AccordionItem"]')
    ACCORDION_HEADER = (By.CLASS_NAME, 'accordion__button')
    ACCORDION_PANEL = (By.CLASS_NAME, 'accordion__panel')
    COOKIE_BANNER = (By.ID, 'rcc-confirm-button')
    FAQ_SECTION = (By.CLASS_NAME, 'Home_FAQ__3uVm4')

    # Точки входа для заказа
    TOP_ORDER_BUTTON = (
    By.XPATH, "//button[contains(text(), 'Заказать') and ancestor::div[@class='Header_Nav__AGCXC']]")
    BOTTOM_ORDER_BUTTON = (
    By.XPATH, "//button[contains(text(), 'Заказать') and ancestor::div[contains(@class, 'Home_FinishButton__')]]")

    BUTTON_DESCRIPTIONS = {
        TOP_ORDER_BUTTON: "вверху страницы",
        BOTTOM_ORDER_BUTTON: "внизу страницы"
    }