from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs_area(row, col, area) -> int:
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    area = dfs_area(next_row, next_col, area+1)
                
            return area
        
        seen = set()
        max_area = 0
        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    area = dfs_area(row, col, 1)
                    max_area = max(max_area, area)
        
        return max_area

def main():
    runner = Solution()

    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    ans = runner.maxAreaOfIsland(grid)
    print(ans)

if __name__ == "__main__":
    main()