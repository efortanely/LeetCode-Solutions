from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i, (a, b) in enumerate(equations):
            value = values[i]
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited.add(start)
            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0

        results = []
        for query in queries:
            result = dfs(query[0], query[1], set())
            results.append(result)

        return results

if __name__ == "__main__":
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    ans = Solution().calcEquation(equations, values, queries)
    assert ans == [6.00000,0.50000,-1.00000,1.00000,-1.00000]