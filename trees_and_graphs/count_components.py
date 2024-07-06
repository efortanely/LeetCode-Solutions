from typing import List
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
        ans = 0

        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)

        return ans

def main():
    runner = Solution()

    n = 5
    edges = [[0,1],[1,2],[3,4]]
    ans = runner.countComponents(n, edges)
    print(ans)

if __name__ == "__main__":
    main()