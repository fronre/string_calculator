from src.String_Calculator import String_Calculator

def test_empty_string_returns_0():
    assert String_Calculator('') == 0

def test_single_number_returns_same_value():
    assert String_Calculator("1") == 1

def test_string_number2_returns_2():
    assert String_Calculator("2") == 2

def test_string_number3_returns_3():
    assert String_Calculator("3") == 3

def test_string_number4_returns_4():
    assert String_Calculator("4") == 4

def test_string_number5_returns_5():
    assert String_Calculator("5") == 5
