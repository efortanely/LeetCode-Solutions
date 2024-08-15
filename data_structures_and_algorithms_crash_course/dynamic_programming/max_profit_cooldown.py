from functools import cache
from typing import List

class Solution:    
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, holding, cooldown):
            if i == len(prices):
                return 0

            if cooldown:
                return dp(i+1, holding, 0)
            else:
                ans = dp(i+1, holding, cooldown)

                if holding:
                    ans = max(ans, prices[i] + dp(i+1, False, 1))
                else:
                    ans = max(ans, -prices[i] + dp(i+1, True, 0))

            return ans
        
        return dp(0, False, 0)

def main():
    runner = Solution()
    prices = [1,2,3,0,2]
    ans = runner.maxProfit(prices)
    print(ans)

if __name__ == "__main__":
    main()