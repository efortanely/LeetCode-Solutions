class Solution:
    '''
    #O(n^2)
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        if not prices:
            return profit
        
        min_val = sys.maxsize
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
                max_val = max(prices[i:])
                new_profit = max_val - min_val
                if new_profit > profit:
                    profit = max_val - min_val
        
        return profit
    '''
    
    #O(n)
    def maxProfit(self, prices: List[int]) -> int:
        max_val = 0
        profit = 0
        if not prices:
            return profit
        
        for i in range(len(prices) - 1, -1, -1):
            max_val = max(max_val, prices[i])
            new_profit = max_val - prices[i]
            if new_profit > profit:
                profit = new_profit
        return profit
