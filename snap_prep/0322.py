class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        M = [amount+1 for a in range(amount+1)]
        M[0] = 0
        
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin >= 0: 
                    M[i] = min(M[i], M[i-coin] + 1)
        
        return -1 if M[amount] > amount else M[amount]
