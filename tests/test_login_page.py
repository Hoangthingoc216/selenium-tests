
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"


def test_login_page_displays_login_and_signup_forms(driver):
    # Mở trang đăng nhập và đăng ký
    driver.get(f"{BASE_URL}/login")

    wait = WebDriverWait(driver, 15)

    # Kiểm tra tiêu đề phần đăng nhập
    login_heading = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(., 'Login to your account')]")
        )
    )
    assert login_heading.is_displayed()

    # Kiểm tra tiêu đề phần đăng ký
    signup_heading = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(., 'New User Signup!')]")
        )
    )
    assert signup_heading.is_displayed()

    # Kiểm tra các trường đăng nhập
    assert driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='login-email']"
    ).is_displayed()

    assert driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='login-password']"
    ).is_displayed()

    # Kiểm tra các trường đăng ký
    assert driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='signup-name']"
    ).is_displayed()

    assert driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='signup-email']"
    ).is_displayed()
