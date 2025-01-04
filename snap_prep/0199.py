# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        seen = [(root, 0)]
        levels = []
        
        while seen:
            node, level = seen.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append(node.val)
                else:
                    levels[level] = node.val
                seen.append((node.left, level + 1))
                seen.append((node.right, level + 1))
                
        return levels
