class Solution:
  def isPalindrome(self, x: int) -> bool:
    return is_palindrome(str(x))
    # if x < 0:
    #     return False
    # if x <= 9:
    #     return True

    # s = str(x)
    # if s[0] == s[-1]:
    #     substring = s[1:-1]
    #     if len(substring) > 0:
    #       return self.isPalindrome(int(substring))
    #     else:
    #       return True
    # return False

def is_palindrome(s):
  if s == "" or len(s) == 1:
    return True
  if s[0] == s[-1]:
    return is_palindrome(s[1:-1])
  return False

