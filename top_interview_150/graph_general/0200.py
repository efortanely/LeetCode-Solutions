from collections import defaultdict
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # track x, y coordinates w/ mapping x: [y_1, y_2, ..., y_n]
        seen = defaultdict(list)
        num_islands = 0
        stack = []
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0" or j in seen[i]:
                    continue

                if grid[i][j] == "1" and j not in seen[i]:
                    num_islands += 1
                    seen[i].append(j)
                    stack.append((i, j))

                    while stack:
                        x, y = stack.pop()
                        for nbr_x, nbr_y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                            if nbr_x < 0 or nbr_x >= len(grid) or nbr_y < 0 or nbr_y >= len(grid[i]):
                                continue

                            if grid[nbr_x][nbr_y] == "1" and nbr_y not in seen[nbr_x]:
                                seen[nbr_x].append(nbr_y)
                                stack.append((nbr_x, nbr_y))

        return num_islands

if __name__ == "__main__":
    runner = Solution()
    grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
    ans = runner.numIslands(grid)
    print(ans)