from typing import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True
        
        adj_list = defaultdict(list)
        
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        def dfs(node):
            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        seen = set()
        dfs(source)

        return destination in seen

def main():
    runner = Solution()

    n = 1
    edges = []
    source = 0
    destination = 0
    ans = runner.validPath(n, edges, source, destination)
    print(ans)

if __name__ == "__main__":
    main()