# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root_idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_idx])
            root.left = self.buildTree(preorder, inorder[0:root_idx])
            root.right = self.buildTree(preorder, inorder[root_idx+1:])
            return root
