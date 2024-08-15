from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        def isEdge(row, col) -> bool:
            if row == 0 or col == 0 or row == m-1 or col == n-1:
                return True
            
            return False
        
        def isValid(row, col) -> bool:
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."
                
        queue = deque([(entrance[0], entrance[1], 0)]) #row, col, steps
        seen = {(entrance[0], entrance[1])}
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        while queue:
            row, col, steps = queue.popleft()
            
            if isEdge(row, col) and not (row == entrance[0] and col == entrance[1]):
                return steps
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if isValid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
            
        return -1
    
def main():
    runner = Solution()

    maze = [[".","+"]]
    entrance = [0,0]
    ans = runner.nearestExit(maze, entrance)
    print(ans)

if __name__ == "__main__":
    main()