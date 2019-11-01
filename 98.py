# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidHelper(root, float('-inf'), float('inf'))
    
    def isValidHelper(self, node: TreeNode, lower, upper):
        if node is None:
            return True
        
        if node.val <= lower or node.val >= upper:
            return False
        
        if not self.isValidHelper(node.right, node.val, upper):
            return False
        if not self.isValidHelper(node.left, lower, node.val):
            return False

        return True
