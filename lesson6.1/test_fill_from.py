from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


def test_color_of_form_elements():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                    .install()))
    driver.maximize_window()

    background_color_alert_danger = Color.from_string('rgba(248, 215, 218, 1)')
    background_color_alert_success = Color.from_string(
        'rgba(209, 231, 221, 1)')

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(
        By.CSS_SELECTOR, "button.btn-outline-primary").click()

    zip_code_check = Color.from_string(driver.find_element(
        By.ID, "zip-code")
        .value_of_css_property("background-color"))
    assert zip_code_check == background_color_alert_danger

    first_name_check = Color.from_string(driver.find_element(
        By.ID, "first-name")
        .value_of_css_property("background-color"))
    assert first_name_check == background_color_alert_success
    last_name_check = Color.from_string(driver.find_element(
        By.ID, "last-name")
        .value_of_css_property("background-color"))
    assert last_name_check == background_color_alert_success
    last_name_check = Color.from_string(driver.find_element(
        By.ID, "last-name")
        .value_of_css_property("background-color"))
    assert last_name_check == background_color_alert_success
    address_check = Color.from_string(driver.find_element(
        By.ID, "address")
        .value_of_css_property("background-color"))
    assert address_check == background_color_alert_success
    city_check = Color.from_string(driver.find_element(
        By.ID, "city")
        .value_of_css_property("background-color"))
    assert city_check == background_color_alert_success
    country_check = Color.from_string(driver.find_element(
        By.ID, "country")
        .value_of_css_property("background-color"))
    assert country_check == background_color_alert_success
    e_mail_check = Color.from_string(driver.find_element(
        By.ID, "e-mail")
        .value_of_css_property("background-color"))
    assert e_mail_check == background_color_alert_success
    phone_check = Color.from_string(driver.find_element(
        By.ID, "phone")
        .value_of_css_property("background-color"))
    assert phone_check == background_color_alert_success
    job_position_check = Color.from_string(driver.find_element(
        By.ID, "job-position")
        .value_of_css_property("background-color"))
    assert job_position_check == background_color_alert_success
    company_check = Color.from_string(driver.find_element(
        By.ID, "company")
        .value_of_css_property("background-color"))
    assert company_check == background_color_alert_success

    driver.quit()
