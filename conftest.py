
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Khởi tạo Chrome và đóng trình duyệt sau mỗi test."""
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    browser.quit()
