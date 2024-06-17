from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from configuration import *



background_color_alert_danger = 'rgba(248, 215, 218, 1)'
background_color_alert_success = 'rgba(209, 231, 221, 1)'

full_field_list = {
        "first-name": "Иван", "last-name": "Петров",
        "address": "Ленина, 55-3", "zip-code": "",
        "city": "Москва", "country": "Россия",
        "e-mail": "test@skypro.com", "phone": "+7985899998787",
        "job-position": "QA", "company": "SkyPro"}
field_list = ["first-name", "last-name", "address", "city", "country",
           "e-mail", "phone", "job-position", "company"]


def test_background_color_unfilled_elements_in_form(driver_chrome):
    driver_chrome.get(URL_FILL_FORM)

    for id, value in full_field_list.items():
        driver_chrome.find_element(By.NAME, id).send_keys(value)

    WebDriverWait(driver_chrome, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-outline-primary"))).click()
 
    zip_code_check = driver_chrome.find_element(
        By.ID, "zip-code").value_of_css_property("background-color")

    assert zip_code_check == background_color_alert_danger


def test_background_color_filled_elements_in_form(driver_chrome):
    driver_chrome.get(URL_FILL_FORM)

    for id, value in full_field_list.items():
        driver_chrome.find_element(By.NAME, id).send_keys(value)

    WebDriverWait(driver_chrome, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-outline-primary"))).click()

    for i in field_list:
        i_check = driver_chrome.find_element(By.ID, i).value_of_css_property(
            "background-color")

        assert i_check == background_color_alert_success
