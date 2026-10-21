
BASE_URL = "https://automationexercise.com"


def test_chrome_opens(driver):
    driver.get(BASE_URL)

    assert "Automation Exercise" in driver.title
