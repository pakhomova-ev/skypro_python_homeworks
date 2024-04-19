from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from hw7_pages.PurchaseShopPage import PurchasePage

total_in_cart = '$58.29'

product_buttons = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]


def test_total_in_cart():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    purchase_page = PurchasePage(driver)
    purchase_page.login_shop()
    purchase_page.add_items_to_cart(product_buttons)
    purchase_page.open_cart()
    purchase_page.fill_info_form('Ippolit', 'Ip', 123567)

    as_is = purchase_page.get_total_amount_in_cart()

    driver.quit()

    assert total_in_cart == as_is
