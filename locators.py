from selenium.webdriver.common.by import By


class MainPageLocators:

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
    # Страница 1
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_DROPDOWN = (By.CLASS_NAME, 'select-search__input')
    METRO_STATION_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//button[contains(., '{}')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Страница 2
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")
    COLOR_BLACK_CHECKBOX = (By.ID, 'black')
    COLOR_GREY_CHECKBOX = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    # Модальное окно подтверждения
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да' and contains(@class, 'Button_Middle')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(., 'Заказ оформлен')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Order_Text')]")