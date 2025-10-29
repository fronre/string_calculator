import pytest
from src.String_Calculator import String_Calculator

@pytest.mark.parametrize("input_str, expected", [
    ("", 0),
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
])
def test_String_numbers(string_input, expected):
    assert String_Calculator(string_input) == expected
