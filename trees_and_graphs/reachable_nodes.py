from typing import List
from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        graph = defaultdict(list)
        
        for x, y in edges:
            if x not in restricted and y not in restricted:
                graph[x].append(y)
                graph[y].append(x)

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        seen = set([0])
        dfs(0)

        return len(seen)

def main():
    runner = Solution()

    n = 7
    edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
    restricted = [4,5]
    ans = runner.reachableNodes(n, edges, restricted)
    print(ans)

if __name__ == "__main__":
    main()