from palindrome import is_palindrome

def test_is_palindrome_empty():
  assert is_palindrome("")

def test_is_palindrome_one_digit():
  assert is_palindrome("1")

def test_is_not_palindrome_two_digits():
  assert not is_palindrome("12")

def test_is_palindrome_two_digits():
  assert is_palindrome("22")

def test_is_not_palindrome_when_its_negative():
  assert not is_palindrome("-22")

def test_is_palindrome_three_digits():
  assert is_palindrome("929")

def test_is_not_palindrome_three_digits():
  assert not is_palindrome("125")

def test_is_palindrome_many_digits():
  assert is_palindrome("1234567654321")

