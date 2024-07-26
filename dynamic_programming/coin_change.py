from functools import cache
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i):
            if i > amount:
                return float("inf")
            if i == amount:
                return 0
            
            min_amount = float("inf")
            for coin in coins:
                next = 1 + dp(i + coin)
                min_amount = min(min_amount, next)

            return min_amount
        
        return dp(0) if dp(0) != float("inf") else -1

def main():
    runner = Solution()
    coins = [2]
    amount = 3
    ans = runner.coinChange(coins, amount)
    print(ans)

if __name__ == "__main__":
    main()