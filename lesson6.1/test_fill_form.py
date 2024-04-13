from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_color_of_form_elements():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                    .install()))
    driver.maximize_window()

    background_color_alert_danger = 'rgba(248, 215, 218, 1)'
    background_color_alert_success = 'rgba(209, 231, 221, 1)'

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    full_id_list = {
        "first-name": "Иван", "last-name": "Петров",
        "address": "Ленина, 55-3", "zip-code": "",
        "city": "Москва", "country": "Россия",
        "e-mail": "test@skypro.com", "phone": "+7985899998787",
        "job-position": "QA", "company": "SkyPro"}

    for id, value in full_id_list.items():
        driver.find_element(By.NAME, id).send_keys(value)

    driver.find_element(
        By.CSS_SELECTOR, "button.btn-outline-primary").click()

    zip_code_check = driver.find_element(
        By.ID, "zip-code").value_of_css_property("background-color")
    assert zip_code_check == background_color_alert_danger

    id_list = ["first-name", "last-name", "address", "city", "country",
               "e-mail", "phone", "job-position", "company"]

    for i in id_list:
        i_check = driver.find_element(By.ID, i).value_of_css_property(
            "background-color")
        assert i_check == background_color_alert_success

    driver.quit()
