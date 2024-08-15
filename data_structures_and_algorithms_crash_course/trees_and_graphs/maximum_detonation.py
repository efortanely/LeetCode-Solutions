from typing import List
from collections import defaultdict, deque
from math import sqrt

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            x, y, radius = bombs[i]

            for j in range(i+1, len(bombs)):
                x_2, y_2, radius_2 = bombs[j]

                dist = sqrt((x_2 - x)**2 + (y_2 - y)**2)
                
                if dist <= radius:
                    graph[i].append(j)
                    
                if dist <= radius_2:
                    graph[j].append(i)

        max_bombs = 0

        for i in range(len(bombs)):
            queue = deque([i])
            seen = {i}

            while queue:
                idx = queue.popleft()

                for neighbor in graph[idx]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)

            max_bombs = max(max_bombs, len(seen))
        
        return max_bombs

def main():
    runner = Solution()

    bombs = [[2,1,3],[6,1,4]]
    ans = runner.maximumDetonation(bombs)
    print(ans)

if __name__ == "__main__":
    main()