class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = 0

        for i in range(n):
            for j in range(n):
                match = True
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        match = False
                ans += match

        return ans