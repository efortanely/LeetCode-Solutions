from typing import List
from heapq import *
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for source, destination, cost in flights:
            graph[source].append((destination, cost))
        
        heap = [(0, 0, src)]
        visited = {}

        while heap:
            cost, nodes_visited, node = heappop(heap)
            
            if node == dst and nodes_visited - 1 <= k:
                return cost
            
            if node not in visited or visited[node] > nodes_visited:
                visited[node] = nodes_visited
                for neighbor, price in graph[node]:
                    heappush(heap, (cost + price, nodes_visited + 1, neighbor))

        return -1

def main():
    runner = Solution()
    n = 5
    flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
    src = 0
    dst = 2
    k = 2
    ans = runner.findCheapestPrice(n, flights, src, dst, k)
    print(ans)

if __name__ == "__main__":
    main()