from selenium.webdriver.common.by import By


class mainPageLocators:

    FAQ_SECTION = (By.XPATH, "//div[@class='accordion']")
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

    # Точки входа для заказа
    TOP_ORDER_BUTTON = (
    By.XPATH, "//button[contains(text(), 'Заказать') and ancestor::div[@class='Header_Nav__AGCXC']]")
    BOTTOM_ORDER_BUTTON = (
    By.XPATH, "//button[contains(text(), 'Заказать') and ancestor::div[contains(@class, 'Home_FinishButton__')]]")


class OrderPageLocators:
    # Форма заказа - страница 1
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_DROPDOWN = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//button")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Форма заказа - страница 2
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")
    COLOR_CHECKBOX = (By.ID, '{}')  # Будет форматироваться под конкретный цвет
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (
    By.XPATH, "//button[contains(text(), 'Заказать') and ancestor::div[contains(@class, 'Order_Buttons__')]]")

    # Подтверждение заказа
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")