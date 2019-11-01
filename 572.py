# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return s and (self.treeEquals(s, t) or self.isSubtree(s.left, t) \
                          or self.isSubtree(s.right, t))
    
    def treeEquals(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        elif not s or not t:
            return False
        else:
            return s.val == t.val and self.treeEquals(s.left, t.left) and \
                self.treeEquals(s.right, t.right)
