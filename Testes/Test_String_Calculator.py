import pytest
from src.String_Calculator import String_Calculator

@pytest.mark.parametrize("string_input, expected", [
    ("", 0),
    ("1", 1),
    ("0,1", 1),
    ("1,1", 2),
    ("1,2", 3),
    ("1,3", 4),
    ("1,2\n3", 6),
])
def test_String_numbers(string_input, expected):
    actual_result = String_Calculator(string_input)
    assert actual_result == expected
