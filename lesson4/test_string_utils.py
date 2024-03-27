import pytest
from string_utils import StringUtils


str = StringUtils()


# Tests def capitilize(self, string: str) -> str
@pytest.mark.parametrize("input_str, result", [
    ("первый", "Первый"),
    ("rere", "Rere"),
    ("первый тест", "Первый тест"),
    ("в процессе форка создается копия всех файлов.\
    эта копия сохраняется.", "В процессе форка создается копия всех файлов.\
    эта копия сохраняется."),
    ("without whitespace", "Without whitespace")
    ])
def test_input_tex_capitilize(input_str, result):
    res = str.capitilize(input_str)
    assert res == result


@pytest.mark.parametrize("symbol, result", [
    ("!", "!"),
    ("", ""),
    (" ", " ")
    ])
def test_symbols_capitilize(symbol, result):
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
    ("a,b,c,f", ["a", "b", "c", "f"]),
    (" a, b, c, f", [" a", " b", " c", " f"]),
    ("а,б,в,г", ["а", "б", "в", "г"]),
    (" а, б, в, г", [" а", " б", " в", " г"]),
    ("1,2,3,4", ["1", "2", "3", "4"]),
    ("Онлайн регистрация,Личный кабинет,Приложение и интернет",
     ["Онлайн регистрация", "Личный кабинет", "Приложение и интернет"]),
    ("Online Registration,Personal Office,App and Internet",
     ["Online Registration", "Personal Office", "App and Internet"]),
    ("!!!,####,8888,~~~~,=", ["!!!", "####", "8888", "~~~~", "="])
     ])
def test_symbols_to_list(input_str, result):
    res = str.to_list(input_str)
    assert res == result


@pytest.mark.parametrize("input_str, delimeter, result", [
    ("a:b:c:d:f", ":", ["a", "b", "c", "d", "f"]),
    ("а:б:в:г", ":", ["а", "б", "в", "г"]),
    ("a!b!c!d!f", "!", ["a", "b", "c", "d", "f"]),
    ("а!б!в!г", "!", ["а", "б", "в", "г"]),
    ("a.b.c.d.f", ".", ["a", "b", "c", "d", "f"]),
    ("а.б.в.г", ".", ["а", "б", "в", "г"]),
    ("a b c d f", " ", ["a", "b", "c", "d", "f"]),
    ("а б в г", " ", ["а", "б", "в", "г"])
])
def test_symbols_with_delimeter(input_str, delimeter, result):
    res = str.to_list(input_str, delimeter)
    assert res == result


def test_string_without_delimeter_to_list():
    res = str.to_list("12345")
    assert res == ["12345"]


def test_string_without_delimeter_to_list2():
    res = str.to_list("a b c d f")
    assert res == ["a b c d f"]


def test_without_delimeter_to_list2():
    with pytest.raises(ValueError):
        str.to_list("12345", "")


def test_none_argument_to_list():
    with pytest.raises(TypeError):
        str.to_list()


@pytest.mark.skip(reason="должна быть ошибка - неверный аргумент")
def test_none_to_list():
    with pytest.raises(AttributeError):
        str.to_list("")


@pytest.mark.skip(reason="должна быть ошибка - неверный аргумент")
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
    ("Marmasdef Llqzxcc", "c", True),
    ("рлткыыат лпвпртрн", "ы", True),
    ("Marmasdef Llqzxcc", "v", False),
    ("Marmasdef Llqzxcc", "qzx", True),
    ("Marmasdef Llqzxcc", "qzy", False)
])
def test_string_contains(input_str, symbol, result):
    res = str.contains(input_str, symbol)
    assert res == result


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


# def delete_symbol(self, string: str, symbol: str) -> str
@pytest.mark.parametrize("input_str, symbol, result", [
    ("This", "s", "Thi"),
    ("This simple technique is used", "s", "Thi imple technique i ued"),
    ("This simple technique is used", "is", "Th simple technique  used"),
    ("This simple technique is used", "T", "his simple technique is used")
])
def test_delete_symbol(input_str, symbol, result):
    res = str.delete_symbol(input_str, symbol)
    assert res == result


@pytest.mark.parametrize("input_str, symbol, result", [
    ("", "", ""),
    (" ", " ", "")
])
def test_empty_arguments_delete_symbol(input_str, symbol, result):
    res = str.delete_symbol(input_str, symbol)
    assert res == result


def test_none_arguments_delete_symbol():
    with pytest.raises(TypeError):
        str.delete_symbol()


# def starts_with(self, string: str, symbol: str) -> bool
@pytest.mark.parametrize("input_str, symbol, result", [
    ("This", "T", True),
    ("This", "s", False),
    ("This", "t", False),
    ("simple technique is used", "s", True),
    ("simple technique is used", "t", False),
    ("Периметр", "П", True),
    ("сторона", "а", False),
    ("Как изменится периметр", "К", True),
    ("Как изменится периметр", "к", False)
])
def test_starts_with(input_str, symbol, result):
    res = str.starts_with(input_str, symbol)
    assert res == result


def test_none_arguments_starts_with():
    with pytest.raises(TypeError):
        str.starts_with()


def test_only_one_arguments_starts_with():
    with pytest.raises(TypeError):
        str.starts_with("")


#  def end_with(self, string: str, symbol: str) -> bool
@pytest.mark.parametrize("input_str, symbol, result", [
    ("This", "s", True),
    ("This", "T", False),
    ("This", "S", False),
    ("simple technique is used", "d", True),
    ("simple technique is used", "e", False),
    ("Периметр", "р", True),
    ("сторона", "с", False),
    ("Как изменится периметр", "р", True),
    ("Как изменится периметр", "к", False)
])
def test_end_with(input_str, symbol, result):
    res = str.end_with(input_str, symbol)
    assert res == result


def test_none_arguments_end_with():
    with pytest.raises(TypeError):
        str.starts_with()


def test_only_one_arguments_end_with():
    with pytest.raises(TypeError):
        str.starts_with("")


# def is_empty(self, string: str) -> bool
@pytest.mark.parametrize("input_str, result", [
    ("", True),
    ("    ", True),  # являет символ пробел не символом?
    ("This", False),
    ("simple technique is used", False)
])
def test_is_empty_with(input_str, result):
    res = str.is_empty(input_str)
    assert res == result


def test_none_arguments_is_empty():
    with pytest.raises(TypeError):
        str.is_empty()


# def list_to_string(self, lst: list, joiner=", ") -> str
@pytest.mark.parametrize("input_list, result", [
    (["a", "b", "c", "f"], "a, b, c, f"),
    ([" a", " b", " c", " f"], " a,  b,  c,  f"),
    (["а", "б", "в", "г"], "а, б, в, г"),
    ([" а", " б", " в", " г"], " а,  б,  в,  г"),
    (["1", "2", "3", "4"], "1, 2, 3, 4"),
    (["Онлайн регистрация", "Личный кабинет", "Приложение и интернет"],
     "Онлайн регистрация, Личный кабинет, Приложение и интернет"),
    (["Online Registration", "Personal Office", "App and Internet"],
     "Online Registration, Personal Office, App and Internet"),
    (["!!!", "####", "8888", "~~~~", "="], "!!!, ####, 8888, ~~~~, =")
     ])
def test_list_to_string(input_list, result):
    res = str.list_to_string(input_list)
    assert res == result


@pytest.mark.parametrize("input_str, delimeter, result", [
    (["a", "b", "c", "d", "f"], ":", "a:b:c:d:f"),
    (["а", "б", "в", "г"], ":", "а:б:в:г"),
    (["a", "b", "c", "d", "f"], "!", "a!b!c!d!f"),
    (["а", "б", "в", "г"], "!", "а!б!в!г"),
    (["a", "b", "c", "d", "f"], ".", "a.b.c.d.f"),
    (["а", "б", "в", "г"], ".", "а.б.в.г"),
    (["a", "b", "c", "d", "f"], " ", "a b c d f")
])
def test_list_to_string_with_delimeter(input_str, delimeter, result):
    res = str.list_to_string(input_str, delimeter)
    assert res == result


def test_none_argument_list_to_string():
    with pytest.raises(TypeError):
        str.list_to_string()


# Нет смысла возвращать пустую строку, должна быть ошибка
@pytest.mark.skip(reason="должна быть ошибка - неверный аргумент")
def test_empty_argument_list_to_string():
    with pytest.raises(AttributeError):
        str.list_to_string("")


@pytest.mark.skip(reason="должна быть ошибка - неверный аргумент")
def test_whitespace_list_to_string():
    with pytest.raises(AttributeError):
        str.list_to_string(" ")
