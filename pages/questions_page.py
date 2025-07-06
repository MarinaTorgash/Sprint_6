from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure

from urls import Urls

class AccordionSection:
    def __init__(self, driver, index):
        self.driver = driver
        self.index = index
        self.header_locator = (By.XPATH, f'(//div[@class="accordion__button"])[{index + 1}]')
        self.panel_locator = (By.XPATH, f'(//div[@class="accordion__panel"])[{index + 1}]')

    @allure.step('Кликаем на вопрос')
    def click_header(self):
        header = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.header_locator)
        )
        header.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.panel_locator)
        )

    @allure.step('Получаем текст ответа на вопрос')
    def get_panel_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.panel_locator)
        ).text

    @allure.step('Скролим до блока "Вопросы о важном"')
    def scroll_to_accordion(self):
        accordion = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.header_locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'start', behavior: 'smooth'});",
            accordion
        )


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

        # Открытие страницы и ожидание загрузки
        self.open(Urls.MAIN_PAGE)
        self.wait_for_element(self.locators.FAQ_SECTION)

    def get_accordion_item(self, index):
        return AccordionSection(self.driver, index)

