from src.String_Calculator import String_Calculator
def test_string_Calculator():

  def test_empty_string_returns_0():
        assert String_Calculator('') == 0

  def test_single_number_returns_same_value():
      assert String_Calculator("1") == 1


