"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        ptrs = self.treeToDoubleListHelper([], root)
        for i in range(len(ptrs)):
            node = ptrs[i]
            node.left = ptrs[i-1]
            node.right = ptrs[(i+1) % len(ptrs)]
        return ptrs[0]
    
    def treeToDoubleListHelper(self, pointers, root: 'Node'):
        if root:
            pointers = self.treeToDoubleListHelper(pointers, root.left)
            pointers.append(root)
            pointers = self.treeToDoubleListHelper(pointers, root.right)
        return pointers
