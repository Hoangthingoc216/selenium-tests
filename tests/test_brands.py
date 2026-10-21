
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"


def test_brands_are_displayed_on_products_page(driver):
    # Mở trang danh sách sản phẩm
    driver.get(f"{BASE_URL}/products")

    # Chờ khu vực thương hiệu hiển thị
    brands_heading = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[self::h2 or self::h4][contains(., 'Brands')]")
        )
    )

    assert brands_heading.is_displayed()

    # Kiểm tra có ít nhất một thương hiệu trong danh sách
    brand_links = driver.find_elements(
        By.CSS_SELECTOR, ".brands-name a"
    )

    assert len(brand_links) > 0, "Không tìm thấy thương hiệu sản phẩm"
