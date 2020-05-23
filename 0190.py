class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            if n & (1 << i):
                ans |= 1 << (32-i-1)
        return ans
