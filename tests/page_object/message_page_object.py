from selenium.webdriver.support.wait import WebDriverWait

from tests.page_object.base_page_object import BasePage

# Selector
selector_message = "com.example.pierwszaapka:id/textView"


class MessagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_message_text(self):
        message = self.find_element(selector_message)
        return message

    def verify_message_text(self):
        message_text = self.find_message_text().text
        text = 'Enter a message'
        assert message_text == text
