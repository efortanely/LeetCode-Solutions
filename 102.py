# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.levelHelper(root, 0, [])
    
    def levelHelper(self, node: TreeNode, level: int, levels: List[List[int]]) -> List[List[int]]:
            if not node:
                return
            
            if level == len(levels):
                levels.append([])
            levels[level].append(node.val)
            
            self.levelHelper(node.left, level + 1, levels)
            self.levelHelper(node.right, level + 1, levels)
            
            return levels
