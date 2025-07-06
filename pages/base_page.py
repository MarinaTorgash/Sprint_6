from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу по URL")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ожидаем появления элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Ожидаем появления элемента")
    def wait_for_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Принимаем куки')
    def accept_cookies(self):
        try:
            # Ожидаем появления и кликаем на куки-баннер
            cookie_banner = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_BANNER)
            )
            cookie_banner.click()
        except:
            # Если баннер не найден, продолжаем
            pass