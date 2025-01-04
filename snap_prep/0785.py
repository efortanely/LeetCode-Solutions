class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = dict()
        for node in range(len(graph)):
            if node not in colors:
                stack = [node]
                colors[node] = 0
                while stack:
                    node = stack.pop()
                    for nbr in graph[node]:
                        if nbr not in colors:
                            stack.append(nbr)
                            colors[nbr] = 1 if not colors[node] else 0
                        elif colors[nbr] == colors[node]:
                            return False
        return True
