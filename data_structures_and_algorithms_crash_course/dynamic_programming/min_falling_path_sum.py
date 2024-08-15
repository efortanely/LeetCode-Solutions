from functools import cache
from typing import List

class Solution:    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n
        
        @cache
        def dp(i, j):
            if i == 0:
                return matrix[i][j]
            
            ans = float("inf")

            if valid(i-1, j-1):
                ans = min(ans, dp(i-1, j-1))
            if valid(i-1, j):
                ans = min(ans, dp(i-1, j))
            if valid(i-1, j+1):
                ans = min(ans, dp(i-1, j+1))
            
            ans += matrix[i][j]
            return ans
        
        m = len(matrix)
        n = len(matrix[0])
        return min([dp(m-1, j) for j in range(n)])

def main():
    runner = Solution()
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    ans = runner.minFallingPathSum(matrix)
    print(ans)

if __name__ == "__main__":
    main()