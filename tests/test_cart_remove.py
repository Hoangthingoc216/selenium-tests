
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"


def test_remove_product_from_cart(driver):
    # Mở trang danh sách sản phẩm
    driver.get(f"{BASE_URL}/products")

    wait = WebDriverWait(driver, 15)

    # Thêm sản phẩm đầu tiên vào giỏ hàng
    add_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.add-to-cart[data-product-id='1']")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        add_button
    )
    add_button.click()

    # Chờ thông báo và tiếp tục mua sắm
    continue_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
        )
    )
    continue_button.click()

    # Mở giỏ hàng
    driver.get(f"{BASE_URL}/view_cart")

    # Chờ sản phẩm xuất hiện
    product_row = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#cart_info_table tbody tr")
        )
    )

    # Tìm và nhấn nút xóa sản phẩm
    delete_button = product_row.find_element(
        By.CSS_SELECTOR, "a.cart_quantity_delete"
    )
    delete_button.click()

    # Chờ sản phẩm bị xóa khỏi giỏ hàng
    wait.until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, "#cart_info_table tbody tr")
        )
    )

    # Xác nhận giỏ hàng không còn sản phẩm
    remaining_products = driver.find_elements(
        By.CSS_SELECTOR, "#cart_info_table tbody tr"
    )

    assert len(remaining_products) == 0
