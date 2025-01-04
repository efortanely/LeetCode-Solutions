class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_graph = {}
        
        for i in range(n):
            adj_graph[i] = set()
            
        for edge in edges:
            n1, n2 = edge
            adj_graph[n1].add(n2)
            adj_graph[n2].add(n1)
        
        stack = [list(adj_graph.keys())[0]]
        visited = set()
        
        while stack:
            node = stack.pop(0)
            
            if node in visited:
                return False
            visited.add(node)
            
            for nbr in adj_graph[node]:
                stack.append(nbr)
                adj_graph[nbr].remove(node)
            
            del adj_graph[node]
        
        return not adj_graph
