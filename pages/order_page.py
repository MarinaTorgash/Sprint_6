from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure
from urls import Urls

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

        # Открытие страницы и ожидание загрузки
        self.open(Urls.MAIN_PAGE)
        self.wait_for_element(self.locators.FAQ_SECTION)


    @allure.step('Заполняем страницу "Для кого самокат"')
    def fill_first_page(self, data):
        # Ожидаем появления формы
        self.wait_for_element(OrderPageLocators.NAME_INPUT)

        # Заполняем поля с очисткой и явными ожиданиями
        self._fill_field(OrderPageLocators.NAME_INPUT, data['name'])
        self._fill_field(OrderPageLocators.LAST_NAME_INPUT, data['last_name'])
        self._fill_field(OrderPageLocators.ADDRESS_INPUT, data['address'])

        # Выбираем станцию метро
        self._select_metro_station(data['metro'])
        self._fill_field(OrderPageLocators.PHONE_INPUT, data['phone'])

    def _fill_field(self, locator, value):
        field = self.wait_for_clickable_element(locator)
        field.click()
        field.clear()
        field.send_keys(value)

    def _select_metro_station(self, station_name):
        dropdown = self.wait_for_clickable_element(OrderPageLocators.METRO_STATION_DROPDOWN)
        dropdown.click()

        # Формируем локатор для конкретной станции
        station_locator = (OrderPageLocators.METRO_STATION_OPTION[0],
                           OrderPageLocators.METRO_STATION_OPTION[1].format(station_name))

        # Прокручиваем к элементу и кликаем
        station = self.wait_for_element(station_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", station)

        # Используем ActionChains для надежного клика
        ActionChains(self.driver).move_to_element(station).pause(0.5).click().perform()

    @allure.step('Нажимаем кнопку "Далее" и переходим на страницу "Про аренду"')
    def go_to_second_page(self):
        next_button = self.wait_for_clickable_element(OrderPageLocators.NEXT_BUTTON)
        next_button.click()

        # Ждем появления элементов второй страницы
        self.wait_for_element(OrderPageLocators.DATE_INPUT)

    @allure.step('Заполняем страницу "Про аренду"')
    def fill_second_page(self, data):
        # Заполняем дату
        self._fill_field(OrderPageLocators.DATE_INPUT, data['date'])

        # Закрываем календарь даты, если он открыт
        self._close_date_picker()

        # Выбираем срок аренды
        self._select_rental_period(data['rental_period'])

        # Выбираем цвет
        self._select_color(data['color'])

        # Заполняем комментарий
        self._fill_field(OrderPageLocators.COMMENT_INPUT, data['comment'])

    def _close_date_picker(self):
        header = self.driver.find_element(By.TAG_NAME, 'body')
        header.click()

    def _select_rental_period(self, period):
        dropdown = self.wait_for_clickable_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        dropdown.click()

        # Формируем локатор для конкретного периода
        period_locator = (OrderPageLocators.RENTAL_PERIOD_OPTION[0],
                          OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(period))

        # Ждем и кликаем
        period_option = self.wait_for_clickable_element(period_locator)
        period_option.click()

    def _select_color(self, color):
        color_locator = OrderPageLocators.COLOR_BLACK_CHECKBOX if color == 'black' else OrderPageLocators.COLOR_GREY_CHECKBOX
        checkbox = self.wait_for_clickable_element(color_locator)

        # Если чекбокс еще не выбран, кликаем
        if not checkbox.is_selected():
            checkbox.click()

    @allure.step('Нажимаем кнопку "Заказать"')
    def submit_order(self):
        order_button = self.wait_for_clickable_element(OrderPageLocators.ORDER_BUTTON)

        # Прокручиваем к кнопке для избежания перекрытия
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)
        order_button.click()

        # Ожидаем появления модального окна подтверждения
        self.wait_for_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Нажимаем кнопку "Да" - подтверждение заказа')
    def confirm_order(self):
        confirm_button = self.wait_for_clickable_element(OrderPageLocators.CONFIRM_BUTTON)
        confirm_button.click()

    @allure.step('Проверка успешного заказа')
    def get_success_message(self):
        try:
            return self.wait_for_element(OrderPageLocators.SUCCESS_MESSAGE).text
        except:
            return None

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        try:
            return self.wait_for_element(OrderPageLocators.ORDER_NUMBER).text
        except:
            return None