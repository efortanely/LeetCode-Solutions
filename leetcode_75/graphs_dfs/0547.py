from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
            
        graph = [[] for _ in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected[i])):
                if i != j and isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()
        ans = 0

        for i in range(len(graph)):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)

        return ans

if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    ans = Solution().findCircleNum(isConnected)
    assert ans == 2