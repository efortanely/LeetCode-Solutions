class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] is '1':
                    islands += 1
                    self.floodFill(grid, i, j)
        return islands
    
    #Thanks to Shane for telling me about flood fill
    def floodFill(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] is '1':
            grid[i][j] = '0'
            self.floodFill(grid, i+1, j)
            self.floodFill(grid, i-1, j)
            self.floodFill(grid, i, j+1)
            self.floodFill(grid, i, j-1)
