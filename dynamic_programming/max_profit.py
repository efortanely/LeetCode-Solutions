from functools import cache
from typing import List

class Solution:
    def maxProfitBottomUp(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(2):
                dp[i][j] = dp[i+1][j]

                if j:
                    dp[i][j] = max(dp[i][j], prices[i] + dp[i+1][0])
                else:
                    dp[i][j] = max(dp[i][j], -prices[i] - fee + dp[i+1][1])

        return dp[0][0]
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i, holding):
            if i == len(prices):
                return 0
            
            ans = dp(i+1, holding)

            if holding:
                ans = max(ans, prices[i] + dp(i+1, False))
            else:
                ans = max(ans, -prices[i] - fee + dp(i+1, True))

            return ans
        
        return dp(0, 0)

def main():
    runner = Solution()
    prices = [1,3,2,8,4,9]
    fee = 2
    ans = runner.maxProfitBottomUp(prices, fee)
    print(ans)

if __name__ == "__main__":
    main()