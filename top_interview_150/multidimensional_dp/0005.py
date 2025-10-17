from functools import cache

class Solution:
    def longestPalindrome(self, s: str) -> str:
        @cache
        def dp(left, right):
            if left < 0 or right >= len(s) or s[left] != s[right]:
                return 0
            
            length = dp(left - 1, right + 1)

            if not length:
                return right - left + 1
            else:
                return length
            
        max_len = 0
        ans = ""

        for i in range(len(s)):
            length = dp(i, i)
            if length > max_len:
                max_len = length
                start = i - (length - 1) // 2
                ans = s[start:start + length]
            
            length = dp(i, i + 1)
            if length > max_len:
                max_len = length
                start = i - (length - 2) // 2
                ans = s[start:start + length]

        return ans

if __name__ == "__main__":
    s = "babad"
    ans = Solution().longestPalindrome(s)
    print(ans)