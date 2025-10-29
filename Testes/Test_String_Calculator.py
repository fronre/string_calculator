import pytest
from src.String_Calculator import String_Calculator

@pytest.mark.parametrize("string_input, expected", [
    ("", 0),
    ("0", 0),
    ("1", 1),
    ("9", 9),
    ("0,1", 1),
    ("1,1", 2),
    ("1,2", 3),
    ("2,3", 5),
    ("5,5", 10),
    ("7,3", 10),
    ("0,5", 5),
    ("5,0", 5),
    ("9,1", 10),
    ("10,15", 25),
    ("99,1", 100),
    ("500,500", 1000),
    ("999,1", 1000),
])
def test_String_numbers(string_input, expected):
    actual_result = String_Calculator(string_input)
    assert actual_result == expected
