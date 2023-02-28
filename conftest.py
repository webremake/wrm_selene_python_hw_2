# это файл для хранения fixture
from selene.support.shared import browser
import pytest


@pytest.fixture
def config_browser():
    browser.config.window_width = 1300
    browser.config.window_height = 700
    return browser
