import pytest


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res


print(factorial(0))


@pytest.mark.parametrize("input_num, result", [(5, 120), (0, 1)])
def test_possitive_num(input_num, result):
    res = factorial(input_num)
    assert res == result


