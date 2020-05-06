import pytest
from appium import webdriver

from .config import desired_caps
from .page_object.home_page_object import HomePage
from .page_object.message_page_object import MessagePage


@pytest.fixture
def setup():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()


@pytest.fixture
def home_page(setup):
    return HomePage(setup)


@pytest.fixture
def message_page(setup):
    return MessagePage(setup)
