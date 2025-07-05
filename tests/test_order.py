import pytest
from selenium import webdriver
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from data import ORDER_DATA
from urls import Urls
import allure


class TestQuestionsPage:
    driver = None

    @classmethod
    def setup_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        with allure.step('Закрываем браузер'):
            cls.driver.quit()


    @pytest.mark.parametrize('order_button_locator', [
        MainPageLocators.TOP_ORDER_BUTTON,
        MainPageLocators.BOTTOM_ORDER_BUTTON
    ])
    @pytest.mark.parametrize('order_data', ORDER_DATA)
    def test_order_scooter(self, order_button_locator, order_data):

        order_data_index = ORDER_DATA.index(order_data)
        button_position = MainPageLocators.BUTTON_DESCRIPTIONS[order_button_locator]
        allure.dynamic.title(f'Проверка заказа самоката при нажатии на кнопку "Заказать" {button_position} с набором данных №{order_data_index + 1}')
        allure.dynamic.description(f' На странице нажимаем на кнопку "Заказать" {button_position} для оформления заказа. Оформляем заказ с набором данных: {list(order_data.values())}')

        with allure.step(f'1. Открываем страницу {Urls.MAIN_PAGE}'):
            order_page = OrderPage(self.driver)
            self.driver.get(Urls.MAIN_PAGE)

        with allure.step('2. Принимаем куки'):
            order_page.accept_cookies()

        with allure.step('3. Нажимаем кнопку "Заказать"'):
            if order_button_locator == MainPageLocators.TOP_ORDER_BUTTON:
                order_button = self.driver.find_element(*MainPageLocators.TOP_ORDER_BUTTON)
            else:
                # Прокручиваем к нижней кнопке
                bottom_button = self.driver.find_element(*MainPageLocators.BOTTOM_ORDER_BUTTON)
                self.driver.execute_script("arguments[0].scrollIntoView();", bottom_button)
                order_button = bottom_button

            order_button.click()

        with allure.step('4. Заполняем страницу "Для кого самокат"'):
            order_page.fill_first_page(order_data)

        with allure.step('5. Нажимаем кнопку "Далее" и переходим на страницу "Про аренду" '):
            order_page.go_to_second_page()

        with allure.step('6. Заполняем страницу "Про аренду"'):
            order_page.fill_second_page(order_data)
            order_page.submit_order()

        with allure.step('7. Нажимаем кнопку "Заказать"'):#
            order_page.confirm_order()

        #Проверка успешного заказа
        success_message = order_page.get_success_message()
        assert success_message is not None, "Сообщение об успешном заказе не появилось"
        assert "Заказ оформлен" in success_message, f"Неверное сообщение: {success_message}"

        # Дополнительно: получаем номер заказа
        order_number = order_page.get_order_number()
        assert order_number is not None, "Номер заказа не отображается"
        print(f"\nУспешный заказ! Номер: {order_number}")
