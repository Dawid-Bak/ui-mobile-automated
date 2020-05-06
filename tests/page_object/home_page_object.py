from selenium.webdriver.support.wait import WebDriverWait

from tests.page_object.base_page_object import BasePage

# Selector
selector_button = "com.example.pierwszaapka:id/button"


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_button(self):
        button = self.find_element(selector_button)
        button.click()
