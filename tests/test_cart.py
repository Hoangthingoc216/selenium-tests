
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"


def test_add_product_to_cart(driver):
    # Mở trang danh sách sản phẩm
    driver.get(f"{BASE_URL}/products")

    # Chờ nút thêm sản phẩm đầu tiên xuất hiện
    wait = WebDriverWait(driver, 15)

    add_button = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a.add-to-cart[data-product-id='1']")
        )
    )

    # Cuộn nút vào giữa màn hình để hạn chế bị quảng cáo che
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        add_button
    )

    # Chờ nút có thể nhấn
    add_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.add-to-cart[data-product-id='1']")
        )
    )

    # Nhấn thêm sản phẩm vào giỏ
    add_button.click()

    # Chờ nút Continue Shopping xuất hiện
    continue_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
        )
    )

    continue_button.click()

    # Mở trang giỏ hàng
    driver.get(f"{BASE_URL}/view_cart")

    # Chờ bảng giỏ hàng xuất hiện
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#cart_info_table")
        )
    )

    # Kiểm tra giỏ hàng có sản phẩm
    cart_products = driver.find_elements(
        By.CSS_SELECTOR, "#cart_info_table tbody tr"
    )

    assert len(cart_products) > 0, "Giỏ hàng chưa có sản phẩm"
