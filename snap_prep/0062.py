class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        M = [[1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                M[i][j] = M[i-1][j] + M[i][j-1]
        
        return M[-1][-1]
