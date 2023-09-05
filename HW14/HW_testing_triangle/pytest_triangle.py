import pytest
from HW14.HW_testing_triangle.triangle import get_triangle_side


def test_convert_string_to_float():
    with pytest.raises(ValueError):
        get_triangle_side('asd')


def test_work_with_float():
    assert get_triangle_side('2.25') == 2.25, 'Work with the float type'


def test_work_with_integer():
    assert get_triangle_side('2') == 2.0, 'Work with the integer type'


def test_negative_value_exception():
    with pytest.raises(ValueError):
        get_triangle_side('0')


if __name__ == '__main__':
    pytest.main()
