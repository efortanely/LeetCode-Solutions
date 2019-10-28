class Solution:
    def climbStairs(self, n: int) -> int:
        M = [0 for x in range(n+1)]
        M[0] = 1
        for stair in range(1, n+1):
            M[stair] = M[stair-2] + M[stair-1]
        
        return M[-1]
