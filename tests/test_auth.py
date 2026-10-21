

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"


def test_login_with_invalid_credentials(driver):
    # Mở trang đăng nhập
    driver.get(f"{BASE_URL}/login")

    # Nhập email và mật khẩu sai
    driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='login-email']"
    ).send_keys("invalid_user_987654@example.com")

    driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='login-password']"
    ).send_keys("WrongPassword123")

    # Nhấn Login
    driver.find_element(
        By.CSS_SELECTOR, "button[data-qa='login-button']"
    ).click()

    # Chờ tối đa 10 giây để website phản hồi
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//*[contains(text(), 'Your email or password is incorrect!')]"
            ))
        )
        assert error_message.is_displayed()

    except Exception:
        # Lưu lại trạng thái thực tế để chẩn đoán
        print("\nURL hiện tại:", driver.current_url)
        print("Tiêu đề trang:", driver.title)
        print("Nội dung trang:", driver.find_element(
            By.TAG_NAME, "body"
        ).text[:3000])

        raise


def test_signup_with_existing_email(driver):
    # Mở trang đăng ký
    driver.get(f"{BASE_URL}/login")

    # Nhập tên người dùng
    driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='signup-name']"
    ).send_keys("Ngoc Test")

    # Nhập email thử nghiệm
    driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='signup-email']"
    ).send_keys("existing_user@example.com")

    # Nhấn nút Signup
    driver.find_element(
        By.CSS_SELECTOR, "button[data-qa='signup-button']"
    ).click()

    # Chờ thông báo email đã tồn tại
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//*[contains(text(), 'Email Address already exist!')]"
        ))
    )

    assert error_message.is_displayed()
