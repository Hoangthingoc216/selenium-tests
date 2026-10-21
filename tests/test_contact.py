
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"


def test_contact_us_page_is_displayed(driver):
    # Mở trang liên hệ
    driver.get(f"{BASE_URL}/contact_us")

    wait = WebDriverWait(driver, 15)

    # Kiểm tra tiêu đề Contact Us hiển thị
    heading = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(., 'Contact Us')]")
        )
    )
    assert heading.is_displayed()

    # Kiểm tra các trường nhập liệu của biểu mẫu
    name_field = driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='name']"
    )
    email_field = driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='email']"
    )
    subject_field = driver.find_element(
        By.CSS_SELECTOR, "input[data-qa='subject']"
    )
    message_field = driver.find_element(
        By.CSS_SELECTOR, "textarea[data-qa='message']"
    )

    assert name_field.is_displayed()
    assert email_field.is_displayed()
    assert subject_field.is_displayed()
    assert message_field.is_displayed()
