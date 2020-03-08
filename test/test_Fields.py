import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(
    os.path.join(
        os.getcwd(),
        os.path.expanduser(__file__)
    )))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Utils.Fields import *
import pytest


charfield = CharField("testfield", 15)
charfield2 = CharField("testfield", 15)


def test_maxlen_zero_error():
    with pytest.raises(AssertionError):
        charfield = CharField("testfield", 0)


def test_maxlen_negative_error():
    with pytest.raises(AssertionError):
        charfield = CharField("testfield", -1)


def test_maxlen_nan_error():
    with pytest.raises(TypeError):
        charfield = CharField("testfield", "-1")


def test_maxlen_overlength_error():
    with pytest.raises(AssertionError):
        charfield.value = "a" * 16


def test_cf_type_test():
    with pytest.raises(TypeError):
        charfield.value = 15


def test_cf_sum_ordinary_str():
    charfield.value = "Hola"
    assert str(charfield + " ") == "Hola "


def test_cf_str_mult():
    charfield.value = "1"
    assert str(charfield * 2) == "11"


def test_cf_sum_right_str():
    charfield.value = "Hola"
    assert str(" " + charfield) == " Hola"


def test_cf_equality_str():
    charfield.value = "1"
    assert charfield == "1"


def test_cf_r_equality_str():
    charfield.value = "1"
    assert "1" == charfield


def test_cf_greater_or_equal_0():
    charfield.value = "1"
    charfield2.value = "1"
    assert charfield >= charfield2

    charfield2.value = "11"
    assert not charfield >= charfield2
    assert charfield2 >= charfield


def test_cf_less_or_equal_0():
    charfield.value = "1"
    charfield2.value = "1"
    assert charfield <= charfield2

    charfield2.value = "11"
    assert charfield <= charfield2
    assert not charfield2 <= charfield


def test_cf_greater_test_0():
    charfield.value = "11"
    charfield2.value = "1"

    assert charfield > charfield2
    assert not charfield2 > charfield


def test_cf_less_test_0():
    charfield.value = "11"
    charfield2.value = "1"

    assert not charfield < charfield2
    assert charfield2 < charfield


def test_cf_greater_or_equal_1():
    charfield.value = "1"
    assert charfield >= "1"

    assert not charfield >= "11"
    assert "11" >= charfield


def test_cf_less_or_equal_1():
    charfield.value = "1"
    assert charfield <= "1"

    assert charfield <= "11"
    assert not "11" <= charfield


def test_cf_greater_test_1():
    charfield.value = "11"
    charfield2.value = "1"

    assert charfield > "1"
    assert not "1" > charfield


def test_cf_less_test_1():
    charfield.value = "11"
    charfield2.value = "1"

    assert not charfield < "1"
    assert "1" < charfield


def test_cf_len_field():
    charfield.value = "a"
    assert len(charfield) == 1


def test_cf_sub():
    charfield.value = "b"
    charfield2.value = "a"
    with pytest.raises(TypeError):
        charfield - charfield2


def test_cf_div():
    charfield.value = "b"
    charfield2.value = "a"
    with pytest.raises(TypeError):
        charfield / charfield2


def test_cf_divfloor():
    charfield.value = "b"
    charfield2.value = "a"
    with pytest.raises(TypeError):
        charfield // charfield2


def test_cf_mod():
    charfield.value = "b"
    charfield2.value = "a"
    with pytest.raises(TypeError):
        charfield % charfield2


def test_cf_pow():
    charfield.value = "b"
    charfield2.value = "a"
    with pytest.raises(TypeError):
        charfield ** charfield2
