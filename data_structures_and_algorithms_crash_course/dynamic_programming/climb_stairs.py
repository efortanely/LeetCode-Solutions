from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 1:
                return 1
            if i == 2:
                return 2
            
            return dp(i-1) + dp(i-2)

        return dp(n)

def main():
    runner = Solution()
    n = 3
    ans = runner.climbStairs(n)
    print(ans)

if __name__ == "__main__":
    main()