from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from hw7_pages.FormFillPage import FormFill

full_id_list = {
        "first-name": "Иван", "last-name": "Петров",
        "address": "Ленина, 55-3", "zip-code": "",
        "city": "Москва", "country": "Россия",
        "e-mail": "test@skypro.com", "phone": "+7985899998787",
        "job-position": "QA", "company": "SkyPro"
        }
id_list = ["first-name", "last-name", "address", "city", "country",
           "e-mail", "phone", "job-position", "company"]

property = 'background-color'
not_fill_field = 'zip-code'

background_color_alert_danger = 'rgba(248, 215, 218, 1)'
background_color_alert_success = 'rgba(209, 231, 221, 1)'


def test_background_color_unfilled_field_in_form():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    fill_form = FormFill(driver)
    fill_form.fill_all_fields(full_id_list)
    result = fill_form.get_property_element(
        not_fill_field, property, background_color_alert_danger)

    assert result is True

    driver.quit()


def test_background_color_fill_field_in_form():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    fill_form = FormFill(driver)
    fill_form.fill_all_fields(full_id_list)
    result = fill_form.get_property_elements(
        id_list, property, background_color_alert_success)

    assert result is True

    driver.quit()
