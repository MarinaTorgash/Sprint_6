from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OrderPageLocators
import time

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_BANNER)
            ).click()
        except:
            pass

    def fill_first_page(self, data):
        """Заполнение первой страницы заказа"""
        # Ожидаем появления формы
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.NAME_INPUT)
        )

        # Заполняем поля
        self.driver.find_element(*OrderPageLocators.NAME_INPUT).send_keys(data['name'])
        self.driver.find_element(*OrderPageLocators.LAST_NAME_INPUT).send_keys(data['last_name'])
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(data['address'])

        # Выбираем станцию метро
        self.driver.find_element(*OrderPageLocators.METRO_STATION_DROPDOWN).click()
        stations = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located(OrderPageLocators.METRO_STATION_OPTION)
        )
        for station in stations:
            if data['metro'] in station.text:
                station.click()
                break

        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(data['phone'])

    def go_to_second_page(self):
        """Переход на вторую страницу заказа"""
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def fill_second_page(self, data):
        """Заполнение второй страницы заказа"""
        # Ожидаем появления второй страницы
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT)
        )

        # Заполняем поля
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).send_keys(data['date'])

        # Выбираем срок аренды
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN).click()
        period_locator = (OrderPageLocators.RENTAL_PERIOD_OPTION[0],
                         OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(data['rental_period']))
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(period_locator)
        ).click()

        # Выбираем цвет
        color_locator = (OrderPageLocators.COLOR_CHECKBOX[0],
                        OrderPageLocators.COLOR_CHECKBOX[1].format(data['color']))
        self.driver.find_element(*color_locator).click()

        # Заполняем комментарий
        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(data['comment'])

    def submit_order(self):
        """Отправка заказа"""
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    def confirm_order(self):
        """Подтверждение заказа"""
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)
        ).click()

    def check_success_message(self):
        """Проверка сообщения об успешном заказе"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE)
        ).is_displayed()