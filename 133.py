"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def __init__(self):
        self.visited = dict() #int -> Node
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        elif node.val in self.visited:
            return self.visited[node.val]
        else:
            clone_node = Node(node.val, [])
            self.visited[node.val] = clone_node
            
            for neighbor in node.neighbors:
                clone_node.neighbors.append(self.cloneGraph(neighbor))
            
            return clone_node
            
