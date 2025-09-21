from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)
            else:
                return max(dp(i+1, j), dp(i, j+1))

        return dp(0, 0)

if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    ans = Solution().longestCommonSubsequence(text1, text2)
    print(ans)
    assert ans == 3