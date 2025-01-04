"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraphHelper(self, node: 'Node', visited) -> 'Node':
        if not node:
            return None
        elif node.val in visited:
            return visited[node.val]
        else:
            visited[node.val] = Node(node.val, [])
            for nbr in node.neighbors:
                visited[node.val].neighbors.append(self.cloneGraphHelper(nbr, visited))
            return visited[node.val]
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = dict()
        self.cloneGraphHelper(node, visited)
        return visited[node.val] if node else None
