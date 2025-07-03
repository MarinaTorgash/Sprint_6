from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import OrderPageLocators
from locators import MainPageLocators
import time


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def accept_cookies(self):
        try:
            # Ожидаем появления и кликаем на куки-баннер
            cookie_banner = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_BANNER)
            )
            cookie_banner.click()
            time.sleep(0.5)  # Даем время для исчезновения баннера
        except:
            # Если баннер не найден, продолжаем
            pass

    def fill_first_page(self, data):
        """Заполнение первой страницы заказа с надежными ожиданиями"""
        # Ожидаем появления формы
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.NAME_INPUT))

        # Заполняем поля с очисткой и явными ожиданиями
        self._fill_field(OrderPageLocators.NAME_INPUT, data['name'])
        self._fill_field(OrderPageLocators.LAST_NAME_INPUT, data['last_name'])
        self._fill_field(OrderPageLocators.ADDRESS_INPUT, data['address'])

        # Выбираем станцию метро
        self._select_metro_station(data['metro'])
        self._fill_field(OrderPageLocators.PHONE_INPUT, data['phone'])

    def _fill_field(self, locator, value):
        """Универсальный метод заполнения поля с очисткой и ожиданиями"""
        field = self.wait.until(EC.element_to_be_clickable(locator))
        field.click()
        field.clear()
        field.send_keys(value)
        time.sleep(0.2)  # Небольшая задержка для стабилизации

    def _select_metro_station(self, station_name):
        """Выбор станции метро с защитой от перекрытия"""
        dropdown = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_STATION_DROPDOWN))
        dropdown.click()

        # Формируем локатор для конкретной станции
        station_locator = (OrderPageLocators.METRO_STATION_OPTION[0],
                           OrderPageLocators.METRO_STATION_OPTION[1].format(station_name))

        # Прокручиваем к элементу и кликаем
        station = self.wait.until(EC.visibility_of_element_located(station_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", station)

        # Используем ActionChains для надежного клика
        ActionChains(self.driver).move_to_element(station).pause(0.5).click().perform()

    def go_to_second_page(self):
        """Переход на вторую страницу с проверкой"""
        next_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        next_button.click()

        # Ждем появления элементов второй страницы
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT))
        time.sleep(0.5)  # Дополнительная задержка для стабилизации

    def fill_second_page(self, data):
        """Заполнение второй страницы заказа"""
        # Заполняем дату
        self._fill_field(OrderPageLocators.DATE_INPUT, data['date'])

        # Выбираем срок аренды
        self._select_rental_period(data['rental_period'])

        # Выбираем цвет
        self._select_color(data['color'])

        # Заполняем комментарий
        self._fill_field(OrderPageLocators.COMMENT_INPUT, data['comment'])

    def _select_rental_period(self, period):
        """Выбор срока аренды"""
        dropdown = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))
        dropdown.click()

        # Формируем локатор для конкретного периода
        period_locator = (OrderPageLocators.RENTAL_PERIOD_OPTION[0],
                          OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(period))

        # Ждем и кликаем
        period_option = self.wait.until(EC.element_to_be_clickable(period_locator))
        period_option.click()

    def _select_color(self, color):
        """Выбор цвета самоката"""
        color_locator = OrderPageLocators.COLOR_BLACK_CHECKBOX if color == 'black' else OrderPageLocators.COLOR_GREY_CHECKBOX
        checkbox = self.wait.until(EC.element_to_be_clickable(color_locator))

        # Если чекбокс еще не выбран, кликаем
        if not checkbox.is_selected():
            checkbox.click()

    def submit_order(self):
        """Отправка заказа"""
        order_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))

        # Прокручиваем к кнопке для избежания перекрытия
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)
        order_button.click()

        # Ожидаем появления модального окна подтверждения
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.CONFIRM_BUTTON))

    def confirm_order(self):
        """Подтверждение заказа"""
        confirm_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON))
        confirm_button.click()

    def get_success_message(self):
        """Получение сообщения об успешном заказе"""
        try:
            return self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE)).text
        except:
            return None

    def get_order_number(self):
        """Получение номера заказа"""
        try:
            return self.wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_NUMBER)).text
        except:
            return None