# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            root_idx = inorder.index(postorder.pop(-1))
            root = TreeNode(inorder[root_idx])
            root.right = self.buildTree(inorder[root_idx+1:], postorder)
            root.left = self.buildTree(inorder[0:root_idx], postorder)
            return root
