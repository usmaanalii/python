# test_capitalize.py
import pytest


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()


def test_capital_case():
    assert capital_case('sephamore') == 'Sephamore'


def test_raises_exception_on_non_string_arguments():
    # asserts that our function should raise a TypeError in case the argument
    # is not a string
    with pytest.raises(TypeError):
        capital_case(9)