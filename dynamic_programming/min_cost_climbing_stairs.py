from functools import cache
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            if 0 <= i <= 1:
                return 0

            return min(cost[i-1] + dp(i-1), cost[i-2] + dp(i-2))

        return dp(len(cost))

def main():
    runner = Solution()
    cost = [1,100,1,1,1,100,1,1,100,1]
    ans = runner.minCostClimbingStairs(cost)
    print(ans)

if __name__ == "__main__":
    main()