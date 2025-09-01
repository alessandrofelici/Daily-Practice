class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(lambda x: x.isalnum(), s))
        length = len(s)
        for i in range(math.ceil(length/2)):
              if s[i].lower() != s[length-i-1].lower():
                  return False
        return True