from functools import cache
from typing import List

class Solution:    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if i + j == 0:
                return 1 if not obstacleGrid[i][j] else 0

            ans = 0
            if not obstacleGrid[i][j]:
                if i > 0 and not obstacleGrid[i-1][j]:
                    ans += dp(i-1, j)
                if j > 0 and not obstacleGrid[i][j-1]:
                    ans += dp(i, j-1)

            return ans
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return dp(m-1, n-1)

def main():
    runner = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    ans = runner.uniquePathsWithObstacles(obstacleGrid)
    print(ans)

if __name__ == "__main__":
    main()