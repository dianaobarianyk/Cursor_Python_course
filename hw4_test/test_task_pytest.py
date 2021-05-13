import pytest
from functions_to_test import Calculator


def test_py_add():
    assert Calculator.add(5, 4) == 9


def test_py_subtract():
    assert Calculator.subtract(13, 7) == 6


def test_py_multiply():
    assert Calculator.multiply(8, 9) == 72


def test_py_divide():
    assert Calculator.divide(14, 7) == 2
    with pytest.raises(ValueError, match=r".*Can not divide by zero!.*"):
        Calculator.divide(10, 0)
