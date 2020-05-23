# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        lowestLevel = self.levelHelper(root, 0, [])[-1]
        if len(lowestLevel) == 1:
            return lowestLevel[0]
        elif len(lowestLevel) == 2:
            return self.lowestCommonAncestor(root, lowestLevel[0].val, lowestLevel[1].val)
        elif len(lowestLevel) == 3:
            left = self.lowestCommonAncestor(root, lowestLevel[0].val, lowestLevel[1].val)
            right = self.lowestCommonAncestor(root, lowestLevel[1].val, lowestLevel[2].val)
            return self.lowestCommonAncestor(root, left.val, right.val)
    
    def lowestCommonAncestor(self, root: TreeNode, n1: int, n2: int) -> TreeNode: 
        if not root: 
            return None
        if root.val == n1 or root.val == n2: 
            return root  
        
        left = self.lowestCommonAncestor(root.left, n1, n2)  
        right = self.lowestCommonAncestor(root.right, n1, n2) 
        
        if left and right: 
            return root  
        
        return left if left else right
    
    def levelHelper(self, node: TreeNode, level: int, levels: List[List[int]]) -> List[List[int]]:
            if not node:
                return
            
            if level == len(levels):
                levels.append([])
            levels[level].append(node)
            
            self.levelHelper(node.left, level + 1, levels)
            self.levelHelper(node.right, level + 1, levels)
            
            return levels
