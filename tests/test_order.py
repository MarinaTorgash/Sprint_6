import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from pages.order_page import OrderPage
from data import ORDER_DATA
from urls import Urls


class TestQuestionsPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize('order_button_locator', [
        MainPageLocators.TOP_ORDER_BUTTON,
        MainPageLocators.BOTTOM_ORDER_BUTTON
    ])
    @pytest.mark.parametrize('order_data', ORDER_DATA)
    def test_order_scooter(self, order_button_locator, order_data):
        """Тест заказа самоката с двумя точками входа и двумя наборами данных"""
        # Инициализация страницы
        order_page = OrderPage(self.driver)

        try:
            #Открытие главной страницы
            self.driver.get(self.driver, Urls.MAIN_PAGE)

            #Принятие куки
            order_page.accept_cookies()

            #Нажатие кнопки заказа
            if order_button_locator == MainPageLocators.TOP_ORDER_BUTTON:
                order_button = self.driver.find_element(*MainPageLocators.TOP_ORDER_BUTTON)
            else:
                # Прокручиваем к нижней кнопке
                bottom_button = self.find_element(*MainPageLocators.BOTTOM_ORDER_BUTTON)
                self.driver.execute_script("arguments[0].scrollIntoView();", bottom_button)
                order_button = bottom_button

            order_button.click()

            #Заполнение первой страницы
            order_page.fill_first_page(order_data)

            #Переход на вторую страницу
            order_page.go_to_second_page()

            #Заполнение второй страницы
            order_page.fill_second_page(order_data)

            order_page.submit_order()

            #Подтверждение заказа
            order_page.confirm_order()

            #Проверка успешного заказа
            success_message = order_page.get_success_message()
            assert success_message is not None, "Сообщение об успешном заказе не появилось"
            assert "Заказ оформлен" in success_message, f"Неверное сообщение: {success_message}"

            # Дополнительно: получаем номер заказа
            order_number = order_page.get_order_number()
            assert order_number is not None, "Номер заказа не отображается"
            print(f"\nУспешный заказ! Номер: {order_number}")

        except Exception as e:
            pytest.fail(f"Тест с ошибкой: {str(e)}")