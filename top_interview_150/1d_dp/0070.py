from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(step):
            if step < 0:
                return 0
            if step == 0:
                return 1
            
            ans = dp(step-1) + dp(step-2)
            return ans
            
        return dp(n)

if __name__ == "__main__":
    runner = Solution()
    n = 3
    ans = runner.climbStairs(n)
    print(ans)