import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.CalculatorPage import Calculator

spinner_time = 5


@pytest.mark.parametrize('num1, num2, operator, result', [
    (7, 8, '+', 15), (6, 1, '+', 7)])
def test_caculator_math_operation_with_numbers(num1, num2, operator, result):
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    calculator_page = Calculator(driver)
    calculator_page.set_timer(spinner_time)
    calculator_page.set_num(num1)
    calculator_page.set_operant(operator)
    calculator_page.set_num(num2)
    calculator_page.set_operant('=')
    to_be = result
    as_is = calculator_page.get_calculated_value(
        spinner_time, to_be)

    assert to_be == as_is
