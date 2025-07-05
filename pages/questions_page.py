from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccordionSection:
    def __init__(self, driver, element):
        self.driver = driver
        self.root = element
        self.header = WebDriverWait(self.root, 10).until(
            EC.presence_of_element_located(MainPageLocators.ACCORDION_HEADER)
        )
        self.panel = self.root.find_element(*MainPageLocators.ACCORDION_PANEL)

    def click_header(self):
        # Прокручиваем к элементу с дополнительным смещением
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});"
            "window.scrollBy(0, -150);",  # Смещаем выше, чтобы избежать перекрытия
            self.header
        )
        # Явное ожидание кликабельности
        accordion = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.header)
        )
        accordion.click()
        # Ожидаем, пока раздел станет видимым
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(accordion)
        )

    def is_panel_open(self):
        # Проверяем состояние через атрибут hidden
        return self.panel.get_attribute("hidden") is None

    def get_panel_text(self):
        # Ожидаем появления текста внутри панели
        WebDriverWait(self.panel, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'p'))
        )
        return self.panel.find_element(By.TAG_NAME, 'p').text


class MainPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'Home_FAQ__3uVm4'))
        )

    def get_accordion_items(self):
        items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(MainPageLocators.ACCORDION_ITEM)
        )
        return [AccordionSection(self.driver, item) for item in items]

    def close_all_accordion_items(self):
        items = self.get_accordion_items()
        for item in items:
            if item.is_panel_open():
                item.click_header()
                WebDriverWait(self.driver, 3).until(
                    lambda d: not item.is_panel_open(),
                    message="Панель не закрылась"
                )

    def is_element_in_viewport(self, element):
        # Проверяем, находится ли элемент в области видимости
        return self.driver.execute_script(
            "var rect = arguments[0].getBoundingClientRect();"
            "return ("
            "rect.top >= 0 && "
            "rect.left >= 0 && "
            "rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && "
            "rect.right <= (window.innerWidth || document.documentElement.clientWidth)"
            ");",
            element
        )
    def scroll_to_accordion(self):
        # Находим раздел аккордеона
        accordion = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'Home_FourPart__1uthg'))
        )

        # Прокручиваем к разделу
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'start', behavior: 'smooth'});",
            accordion
        )

        # Ожидаем, пока раздел станет видимым
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(accordion)
        )

        WebDriverWait(self.driver, 10).until(
            lambda d: self.is_element_in_viewport(accordion)
        )

        # Дополнительное смещение для уверенности
        self.driver.execute_script("window.scrollBy(0, -150);")

    def accept_cookies(self):
        try:
            # Ожидаем появления баннера куки
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located(MainPageLocators.COOKIE_BANNER)
            ).click()

            # Ожидаем исчезновения баннера
            WebDriverWait(self.driver, 1).until(
                EC.invisibility_of_element_located(MainPageLocators.COOKIE_BANNER)
            )
            return True
        except:
            # Если баннер не появился, продолжаем работу
            return False

class QuestionsPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = MainPageLocators()

    def expand_question(self, index):
        button = self.driver.find_element(*self.locators.question_button(index))
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    def get_answer_text(self, index):
        answer_locator = self.locators.answer_text(index)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(answer_locator)
        )
        return self.driver.find_element(*answer_locator).text

    def is_answer_visible(self, index):
        try:
            return self.driver.find_element(*self.locators.answer_text(index)).is_displayed()
        except:
            return False