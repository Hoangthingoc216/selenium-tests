
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"


def test_product_categories_are_displayed(driver):
    # Mở trang danh sách sản phẩm
    driver.get(f"{BASE_URL}/products")

    # Chờ danh mục sản phẩm xuất hiện
    category_panel = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".left-sidebar")
        )
    )

    # Lấy nội dung danh mục
    category_text = category_panel.text

    # Kiểm tra các nhóm danh mục chính
    assert "WOMEN" in category_text.upper()
    assert "MEN" in category_text.upper()
    assert "KIDS" in category_text.upper()
