class Solution(object):
    def hammingWeight(self, n):
        ans = 0
        for i in range(32):
           if n & (1 << i):
            ans += 1
        return ans
        
