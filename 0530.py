# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        vals = self.tree_vals([], root)
        vals = sorted(vals)
        
        min_diff = float('inf')
        for i in range(len(vals) - 1):
            min_diff = min(min_diff, vals[i+1]-vals[i])
        return min_diff
    
    def tree_vals(self, arr, root: TreeNode):
        if root:
            arr.append(root.val)
            arr = self.tree_vals(arr, root.left)
            arr = self.tree_vals(arr, root.right)
        return arr
