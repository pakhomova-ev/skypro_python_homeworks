from selenium.webdriver.common.by import By


class FormFill:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def fill_all_fields(self, dict):
        for name, value in dict.items():
            self._driver.find_element(By.NAME, name).send_keys(value)

        self._driver.find_element(
            By.CSS_SELECTOR, "button.btn-outline-primary").click()

    def get_property_element(self, element, property, value):
        check_property = self._driver.find_element(
            By.ID, element).value_of_css_property(property)
        if (check_property != value):
            print(f'Error {id} property = {check_property} not {value}')
            return False
        return True

    def get_property_elements(self, list, property, value):
        for id in list:
            id_check = self._driver.find_element(
                By.ID, id).value_of_css_property(property)
            if (id_check != value):
                print(f'Error {id} property = {id_check} not {value}')
                return False
        return True
