import pytest
from string_utils import StringUtils


str = StringUtils()

# Tests def capitilize(self, string: str) -> str


@pytest.mark.parametrize("input_str, result", [
    ("первый", "Первый"),
    ("rere", "Rere"),
    ("Первый", "Первый"),
    ("первый тест", "Первый тест"),
    ("в процессе форка создается копия всех файлов.\
    эта копия сохраняется.", "В процессе форка создается копия всех файлов.\
    эта копия сохраняется.")])
def test_input_tex_capitilize(input_str, result):
    # str = StringUtils()
    res = str.capitilize(input_str)
    assert res == result


@pytest.mark.parametrize("symbol, result", [("!", "!"), ("", ""), (" ", " ")])
def test_str_capitilize(symbol, result):
    res = str.capitilize(symbol)
    assert res == result


def test_int_capitilize():
    with pytest.raises(AttributeError):
        str.capitilize(0)


def test_none_capitilize():
    with pytest.raises(TypeError):
        str.capitilize()


def test_empty_str_capitilize():
    with pytest.raises(AttributeError):
        str.capitilize([])


# Test def trim(self, string: str) -> str


@pytest.mark.parametrize("input_str, result", [
    ("Without whitespace", "Without whitespace"),
    (" Grom", "Grom"), ("  Лето", "Лето"),
    ("     Spring tring", "Spring tring")])
def test_whitespaces_word_start_trim(input_str, result):
    res = str.trim(input_str)
    assert res == result


@pytest.mark.parametrize("input_str, result", [
    ("Without whitespace ", "Without whitespace "),
    ("Grom     ", "Grom     "), ("Лето      ", "Лето      "),
    ("маска                                                    ",
     "маска                                                    "),
    ("Frog     Green",
     "Frog     Green")])
def test_whitespaces_word_finish_trim(input_str, result):
    res = str.trim(input_str)
    assert res == result


# Test def to_list(self, string: str, delimeter=",") -> list[str]

@pytest.mark.parametrize("input_str, result", [
    # без пробелов перед символом латиница
    ("a,b,c,f", ["a", "b", "c", "f"]),
    # с пробелов перед символом латиница
    (" a, b, c, f", [" a", " b", " c", " f"]),
    # без пробелов перед символом кириллица
    ("а,б,в,г", ["а", "б", "в", "г"]),
    # с пробелов перед символом кириллица
    (" а, б, в, г", [" а", " б", " в", " г"]),
    # цифры
    ("1,2,3,4", ["1", "2", "3", "4"]),
    # больше 1 слова кириллица
    ("Онлайн регистрация,Личный кабинет,Приложение и интернет",
     ["Онлайн регистрация", "Личный кабинет", "Приложение и интернет"]),
    # больше 1 слова латиница
    ("Online Registration,Personal Office,App and Internet",
     ["Online Registration", "Personal Office", "App and Internet"]),
    # символы
    ("!!!,####,8888,~~~~,=", ["!!!", "####", "8888", "~~~~", "="])
     ])
def test_symbols_to_list(input_str, result):
    res = str.to_list(input_str)
    assert res == result


@pytest.mark.parametrize("input_str, delimeter, result", [
    ("a:b:c:d:f", ":", ["a", "b", "c", "d", "f"]),
    # разделитель : кириллица
    ("а:б:в:г", ":", ["а", "б", "в", "г"]),
    # разделитель ! латиница
    ("a!b!c!d!f", "!", ["a", "b", "c", "d", "f"]),
    # разделитель ! кириллица
    ("а!б!в!г", "!", ["а", "б", "в", "г"]),
    # разделитель ! латиница
    ("a.b.c.d.f", ".", ["a", "b", "c", "d", "f"]),
    # разделитель ! кириллица
    ("а.б.в.г", ".", ["а", "б", "в", "г"]),
    # разделитель ! латиница
    ("a b c d f", " ", ["a", "b", "c", "d", "f"]),
    # разделитель ! кириллица
    ("а б в г", " ", ["а", "б", "в", "г"])
])
def test_symbols_with_delimeter(input_str, delimeter, result):
    res = str.to_list(input_str, delimeter)
    assert res == result


# =======================================
# WARNING Вопрос - почему через print выводит ок, а при тесте дает ошибку????
# @pytest.mark.parametrize("input_str, result", [
#     ("12345", ["12345"])
#     # ("a b c d f", ["a b c d f"])
# ])
# def test_without_delimeter_to_list(input_str, delimeter, result):
#     res = str.to_list(input_str, delimeter, result)
#     assert res == result


# print(str.to_list("12345"))
# print(str.to_list("a b c d f"))
# =======================================

def test_none_argument_to_list():
    with pytest.raises(TypeError):
        str.to_list()


# Должна появлять ошибка, что передайте верный аргумент - лист
@pytest.mark.skip
def test_none_to_list():
    with pytest.raises(AttributeError):
        str.to_list("")


@pytest.mark.skip
def test_whitespace_to_list():
    with pytest.raises(AttributeError):
        str.to_list(" ")


# def contains(self, string: str, symbol: str) -> bool

@pytest.mark.parametrize("input_str, symbol, result", [
    ("Marmelad", "a", True),
    ("Marmelad", "y", False),
    ("Мармелад", "р", True),
    ("Мармелад", "ы", False),
    ("Marmasdef Llqzxcc", "z", True),
    ("Marmasdef Llqzxcc", "v", False),
    ("Marmasdef Llqzxcc", "qzx", True),
    ("Marmasdef Llqzxcc", "qzy", False)
])
def test_string_contains(input_str, symbol, result):
    res = str.contains(input_str, symbol)
    assert res == result


# почему метод не ищет символы внезависимости от upper/lower case???
@pytest.mark.skip(reason="реализовать поиск не чувствительный к регистру")
@pytest.mark.parametrize("input_str, symbol, result", [
    ("Marmelad", "E", True),
    ("Tarmelad", "t", True),
    ("Вишня", "Я", True),
    ("Вишня", "в", True),
    ("Marmasdef Llqzxcc", "llq", True)
])
def test_dependent_case_contains(input_str, symbol, result):
    res = str.contains(input_str, symbol)
    assert res == result


def test_empty_arguments_str_contains():
    with pytest.raises(TypeError):
        str.contains()


def test_empty_argument1_str_contains():
    with pytest.raises(TypeError):
        str.contains("gjdlfgjdfgjd")


# def test_empty_argument2_str_contains():
#     with pytest.raises(TypeError):
#         str.contains("")


# print(str.contains("Marmasdef Llqzxcc", "qzx"))
# print(str.contains("Marmasdef Llqzxcc", "llq"))
# print(str.contains())
