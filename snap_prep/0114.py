# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flattenHelper(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if not root.left and not root.right:
            return root
        
        leftTail = self.flattenHelper(root.left)
        rightTail = self.flattenHelper(root.right)
        
        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            root.left = None
            
        return rightTail if rightTail else leftTail
    
    def flatten(self, root: TreeNode) -> None:
        self.flattenHelper(root)
