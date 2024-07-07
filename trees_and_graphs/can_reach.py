from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:        
        def getNeighbors(idx):
            neighbors = []

            left_idx = idx - arr[idx]

            if left_idx >= 0:
                neighbors.append(left_idx)
            
            right_idx = idx + arr[idx]

            if right_idx < len(arr):
                neighbors.append(right_idx)

            return neighbors
        
        seen = {start}
        queue = deque([start])

        while queue:
            idx = queue.popleft()

            if arr[idx] == 0:
                return True
            
            for neighbor in getNeighbors(idx):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return False

def main():
    runner = Solution()

    arr = [0,3,0,6,3,3,4]
    start = 6
    ans = runner.canReach(arr, start)
    print(ans)

if __name__ == "__main__":
    main()