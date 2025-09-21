from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return dp(i+1, j+1)

            insert = 1 + dp(i, j+1)
            delete = 1 + dp(i+1, j)
            replace = 1 + dp(i+1, j+1)

            return min(insert, delete, replace)

        return dp(0, 0)

if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    ans = Solution().minDistance(word1, word2)
    assert ans == 3