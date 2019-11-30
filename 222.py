# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left:
            return 1 + self.countNodes(root.right)
        elif not root.right:
            return 1 + self.countNodes(root.left)
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
