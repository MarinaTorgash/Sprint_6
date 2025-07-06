import pytest
from selenium import webdriver
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from urls import Urls
import allure
from data import ORDER_DATA, EXPECTED_SUCCESS_MESSAGE, ERROR_MESSAGE_NO_SUCCESS_POPUP, ERROR_MESSAGE_WRONG_SUCCESS_TEXT

class TestQuestionsPage:

#Убираем setup_class и teardown_class, в обучении был пример с этими методами.

    @pytest.mark.parametrize('order_button_locator', [
        MainPageLocators.TOP_ORDER_BUTTON,
        MainPageLocators.BOTTOM_ORDER_BUTTON
    ])
    @pytest.mark.parametrize('order_data', ORDER_DATA)
    def test_order_scooter(self, driver, order_button_locator, order_data):

        order_data_index = ORDER_DATA.index(order_data)
        button_position = MainPageLocators.BUTTON_DESCRIPTIONS[order_button_locator]
        allure.dynamic.title(f'Проверка заказа самоката при нажатии на кнопку "Заказать" {button_position} с набором данных №{order_data_index + 1}')
        allure.dynamic.description(f' На странице нажимаем на кнопку "Заказать" {button_position} для оформления заказа. Оформляем заказ с набором данных: {list(order_data.values())}')

        with allure.step(f'Открываем страницу {Urls.MAIN_PAGE}'):
            order_page = OrderPage(driver)

        order_page.accept_cookies()

        with allure.step('Нажимаем кнопку "Заказать"'):
            if order_button_locator == MainPageLocators.TOP_ORDER_BUTTON:
                order_button = driver.find_element(*MainPageLocators.TOP_ORDER_BUTTON)
            else:
                # Прокручиваем к нижней кнопке
                bottom_button = driver.find_element(*MainPageLocators.BOTTOM_ORDER_BUTTON)
                driver.execute_script("arguments[0].scrollIntoView();", bottom_button)
                order_button = bottom_button

            order_button.click()

        order_page.fill_first_page(order_data)
        order_page.go_to_second_page()
        order_page.fill_second_page(order_data)
        order_page.submit_order()
        order_page.confirm_order()

        success_message = order_page.get_success_message()
        assert success_message is not None, ERROR_MESSAGE_NO_SUCCESS_POPUP
        assert EXPECTED_SUCCESS_MESSAGE in success_message, f"{ERROR_MESSAGE_WRONG_SUCCESS_TEXT}: {success_message}"

        order_number = order_page.get_order_number()
        assert order_number is not None, "Номер заказа не отображается"