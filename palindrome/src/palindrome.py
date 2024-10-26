def is_palindrome(s):
  if s == "" or len(s) == 1:
    return True
  if s[0] == s[-1]:
    return is_palindrome(s[1:-1])
  return False
