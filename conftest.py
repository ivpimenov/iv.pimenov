from selene.support.shared import browser
import pytest
import selene



@pytest.fixture(scope='session', autouse=True)
def browser_size():
    browser.open('https://google.com').driver.set_window_size(1920, 1080)
