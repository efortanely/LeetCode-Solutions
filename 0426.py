"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        prev, head = None, None
        def inorderTraversal(node: 'Node') -> None:
            nonlocal prev, head
            if not node:
                return

            inorderTraversal(node.left)
            
            if not prev:
                head = node
            else:
                prev.right = node
                node.left = prev
            
            prev = node
            
            inorderTraversal(node.right)
        
        inorderTraversal(root)
        if head:
            head.left = prev
            prev.right = head
        return head
