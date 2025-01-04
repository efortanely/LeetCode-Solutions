class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] is not s[r]:
                left = s[l:r]
                right = s[l+1:r+1]
                return left == left[::-1] or right == right[::-1]
            l += 1
            r -= 1
        return True
