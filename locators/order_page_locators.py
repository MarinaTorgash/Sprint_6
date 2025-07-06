from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Страница 1
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_DROPDOWN = (By.CLASS_NAME, 'select-search__input')
    METRO_STATION_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//button[contains(., '{}')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Страница "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")
    COLOR_BLACK_CHECKBOX = (By.ID, 'black')
    COLOR_GREY_CHECKBOX = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    # Модальное окно подтверждения
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(., 'Заказ оформлен')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Order_Text')]")

    ORDER_FORM_HEADER = (By.XPATH, '//div[text()="Для кого самокат"]')


    FAQ_SECTION = (By.CLASS_NAME, 'Home_FAQ__3uVm4')