from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        def dfs(node, depth):
            if not node:
                return depth
            
            return max(dfs(node.left, depth+1), dfs(node.right, depth+1))
            
        return dfs(root, 0)

if __name__ == "__main__":
    runner = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    ans = runner.maxDepth(root)
    print(ans)
    assert ans == 3