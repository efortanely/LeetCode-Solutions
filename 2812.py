from typing import List
from collections import deque, defaultdict

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < n and 0 <= col < n

        def doesPathExist(safety_val):
            coord_map = {key: safety_map[key] for key in safety_map if key >= safety_val}
            valid_coords = set(val for sublist in coord_map.values() for val in sublist)

            if (0,0) not in valid_coords:
                return False

            stack = [(0,0)]
            seen = {(0,0)}

            while stack:
                row, col = stack.pop()

                if row == n - 1 and col == n - 1:
                    return True
                
                for dx, dy in directions:
                    next_row, next_col = row + dx, col + dy
                    if valid(next_row, next_col) and (next_row, next_col) in valid_coords and (next_row, next_col) not in seen:
                        seen.add((next_row, next_col))
                        stack.append((next_row, next_col))
                
            return False
        
        n = len(grid)
        thieves = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        queue = deque([(thief[0], thief[1], 0) for thief in thieves])
        seen = set(thieves)
        safety_grid = [[0 for j in range(n)] for i in range(n)]
        safety_map = defaultdict(list)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while queue:
            row, col, safety = queue.popleft()
            
            safety_grid[row][col] = safety
            safety_map[safety].append((row, col))

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, safety + 1))

        safety_vals = sorted(list(safety_map.keys()))
        left = 0
        right = len(safety_vals) - 1
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            safety_val = safety_vals[mid]

            if not doesPathExist(safety_val):
                right = mid - 1
            #there is a path and safety val can be larger
            else:
                left = mid + 1
                ans = safety_val

        return ans

def main():
    runner = Solution()
    grid = [[1,1,1],[0,1,1],[0,0,0]]
    ans = runner.maximumSafenessFactor(grid)
    print(ans)

if __name__ == "__main__":
    main()