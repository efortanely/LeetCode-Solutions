from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def initialize_tree(cls, nodes):
        def build_tree(index):
            if index >= len(nodes) or nodes[index] is None:
                return None
            root = cls(nodes[index])
            root.left = build_tree(2 * index + 1)
            root.right = build_tree(2 * index + 2)
            return root
        
        if not nodes:
            return None
        
        return build_tree(0)

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.ans = 0
        
        def dfs(root, max_val, min_val):
            if not root:
                return
            
            self.ans = max(self.ans, abs(max_val-root.val), abs(min_val-root.val))

            max_val = max(max_val, root.val)
            min_val = min(min_val, root.val)
            
            dfs(root.left, max_val, min_val)
            dfs(root.right, max_val, min_val)
            
        dfs(root, root.val, root.val)
        return self.ans

def main():
    runner = Solution()

    root = TreeNode.initialize_tree([8,3,10,1,6,None,14,None,None,4,7,13])
    ans = runner.maxAncestorDiff(root)
    print(ans)

if __name__ == "__main__":
    main()