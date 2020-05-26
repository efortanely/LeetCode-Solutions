# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBSTHelper(self, root: TreeNode, low: int, high: int):
        if not root:
            return True
        
        if not low < root.val < high:
            return False
        
        return self.isValidBSTHelper(root.left, low, root.val) and self.isValidBSTHelper(root.right, root.val, high)
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))
