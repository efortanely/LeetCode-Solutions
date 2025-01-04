class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s[0:len(s)] == s[-1:-len(s)-1:-1]
