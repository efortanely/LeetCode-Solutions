# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def lowestCommonAncestorHelper(node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
            nonlocal lca
            if not node:
                return False

            in_left = lowestCommonAncestorHelper(node.left, p, q)
            in_right = lowestCommonAncestorHelper(node.right, p, q)
            in_self = node.val == p.val or node.val == q.val

            if (in_left and in_right) or ((in_left or in_right) and in_self):
                lca = node
            
            return in_left or in_right or in_self
        
        lowestCommonAncestorHelper(root, p, q)
        return lca
