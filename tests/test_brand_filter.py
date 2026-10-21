
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"


def test_filter_products_by_brand(driver):
    # Mở trang sản phẩm
    driver.get(f"{BASE_URL}/products")

    wait = WebDriverWait(driver, 15)

    # Chờ liên kết thương hiệu đầu tiên xuất hiện
    brand_link = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".brands-name a")
        )
    )

    # Lưu tên thương hiệu để đối chiếu sau khi nhấn
    brand_name = brand_link.text.split("\n")[-1].strip()
    assert brand_name, "Tên thương hiệu không được để trống"

    # Nhấn vào thương hiệu
    brand_link.click()

    # Chờ trang hiển thị tiêu đề thương hiệu
    heading = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".features_items h2.title")
        )
    )

    # Kiểm tra tiêu đề có chứa tên thương hiệu
    assert brand_name.lower() in heading.text.lower()
