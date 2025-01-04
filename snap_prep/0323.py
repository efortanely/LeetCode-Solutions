class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = dict()
        for i in range(n):
            graph[i] = set()
        
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
            
        components = 0
        
        while len(graph) > 0:
            queue = [list(graph.keys())[0]]
            visited = set()

            while queue:
                node = queue.pop(0)

                if node in visited:
                    continue
                visited.add(node)

                for nbr in graph[node]:
                    queue.append(nbr)
                    graph[nbr].remove(node)

                del graph[node]
                
            components += 1
        
        return components
