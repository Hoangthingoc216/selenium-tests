
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"


def test_test_cases_page_is_displayed(driver):
    # Mở trang Test Cases
    driver.get(f"{BASE_URL}/test_cases")

    # Chờ tiêu đề trang hiển thị
    heading = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(., 'Test Cases')]")
        )
    )

    # Xác nhận tiêu đề đang hiển thị
    assert heading.is_displayed()

    # Xác nhận URL đã điều hướng đến trang Test Cases
    assert "/test_cases" in driver.current_url
