# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.helper(root, [])[k-1]
        
    def helper(self, node: TreeNode, nodes: List[TreeNode]) -> List[TreeNode]:
        if not node:
            return -1
        
        self.helper(node.left, nodes)
        nodes.append(node.val)
        self.helper(node.right, nodes)
        
        return nodes
