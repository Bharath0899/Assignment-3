import pytest
from myapp.mymodule.funcs import area_of_square

EXPECTED_LAST_TWO = 79


def test_area_of_square_with_id_digits():
    side = 1.0 * EXPECTED_LAST_TWO   
    expected_area = EXPECTED_LAST_TWO ** 2
    result = area_of_square(side)
    assert result == expected_area