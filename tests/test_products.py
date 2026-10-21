
BASE_URL = "https://automationexercise.com"


def test_products_page_is_displayed(driver):
    # Truy cập trang danh sách sản phẩm
    driver.get(f"{BASE_URL}/products")

    # Kiểm tra URL hiện tại có chứa đường dẫn products
    assert "/products" in driver.current_url

    # Kiểm tra trang có tiêu đề Products
    assert driver.find_element(
        "xpath", "//*[normalize-space()='All Products']"
    ).is_displayed()

def test_search_product_returns_results(driver):
    # Mở trang danh sách sản phẩm
    driver.get(f"{BASE_URL}/products")

    # Tìm ô nhập từ khóa
    search_input = driver.find_element("id", "search_product")

    # Nhập từ khóa cần tìm
    search_input.send_keys("Blue Top")

    # Nhấn nút tìm kiếm
    driver.find_element("id", "submit_search").click()

    # Kiểm tra kết quả tìm kiếm được hiển thị
    assert driver.find_element(
        "xpath", "//*[normalize-space()='Searched Products']"
    ).is_displayed()

    # Kiểm tra có ít nhất một sản phẩm được hiển thị
    products = driver.find_elements(
        "css selector", ".product-image-wrapper"
    )
    assert len(products) > 0


def test_search_product_returns_no_results(driver):
    # Mở trang danh sách sản phẩm
    driver.get(f"{BASE_URL}/products")

    # Nhập một từ khóa khó có thể trùng với sản phẩm
    search_input = driver.find_element("id", "search_product")
    search_input.send_keys("xyzproduct987654")

    # Thực hiện tìm kiếm
    driver.find_element("id", "submit_search").click()

    # Kiểm tra tiêu đề kết quả tìm kiếm xuất hiện
    assert driver.find_element(
        "xpath", "//*[normalize-space()='Searched Products']"
    ).is_displayed()

    # Kiểm tra không có sản phẩm nào được hiển thị
    products = driver.find_elements(
        "css selector", ".product-image-wrapper"
    )
    assert len(products) == 0


def test_product_details_page_is_displayed(driver):
    # Mở trang danh sách sản phẩm
    driver.get(f"{BASE_URL}/products")

    # Tìm nút View Product đầu tiên
    view_product_links = driver.find_elements(
        "xpath", "//a[contains(text(), 'View Product')]"
    )

    # Xác nhận có ít nhất một liên kết xem chi tiết
    assert len(view_product_links) > 0

    # Nhấn vào liên kết xem chi tiết đầu tiên
    view_product_links[0].click()

    # Kiểm tra đã chuyển sang trang chi tiết sản phẩm
    assert "product_details" in driver.current_url

    # Kiểm tra thông tin sản phẩm hiển thị
    assert driver.find_element(
        "xpath", "//*[normalize-space()='Availability:']"
    ).is_displayed()
