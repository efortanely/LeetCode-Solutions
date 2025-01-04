from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                if i > 0:
                    top = dp[i-1][j]
                else:
                    top = float("inf")

                if j > 0:
                    left = dp[i][j-1]
                else:
                    left = float("inf")

                dp[i][j] = min(top, left) + grid[i][j]

        return dp[m-1][n-1]
    
if __name__ == "__main__":
    runner = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    ans = runner.minPathSum(grid)
    print(ans)